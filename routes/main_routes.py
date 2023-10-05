from flask import Blueprint, abort, current_app, flash, jsonify, render_template, redirect, url_for, request
from db import mysql  # Importe a instância do MySQL
from flask import jsonify
import MySQLdb
from werkzeug.security import check_password_hash, generate_password_hash


main_routes = Blueprint('main_routes', __name__)

def minha_funcao(mysql):
    # Código que utiliza mysql.connection.cursor()
    pass

@main_routes.route('/')
def index():
    return render_template('index.html')

@main_routes.route('/login', methods=['POST', 'GET'])
def admin_login():
    if request.method == 'POST':
        username = request.form.get('username')
        password = request.form.get('password')

        cur = mysql.connection.cursor()
        cur.execute("SELECT * FROM admin WHERE usuario = %s AND senha = %s", (username, password))
        user = cur.fetchone()
        cur.close()

        if user:
            # Ajuste a rota de redirecionamento para 'main_routes.painel_admin'
            return redirect(url_for('main_routes.painel_admin'))
        else:
            return redirect(url_for('main_routes.unauthorized'))

    return render_template('login_admin.html')


def obter_dados_da_tabela_clientes(conexao):
    try:
        # Cria um cursor a partir da conexão
        cursor = conexao.cursor()

        # Consulta SQL para obter dados da tabela clientes
        consulta = "SELECT cpf, nome_completo, empresa, funcoes FROM clientes"
        cursor.execute(consulta)

        # Obtém todos os resultados
        clientes = cursor.fetchall()

        # Fecha o cursor
        cursor.close()

        return clientes  # Retorna diretamente a lista de clientes

    except Exception as e:
        print(f"Erro ao obter dados da tabela clientes: {str(e)}")
        # Trate o erro conforme necessário
        raise


@main_routes.route('/painel_admin')
def painel_admin():
    try:
        # Obtém a conexão do MySQL a partir do aplicativo Flask
        conexao = mysql.connection

        # Chama a função para obter dados da tabela clientes
        clientes = obter_dados_da_tabela_clientes(conexao)

        print(f"Clientes recebidos: {clientes}")  # Adicione esta linha para depuração

        # Renderiza a página HTML com os dados obtidos
        return render_template('painel_admin.html', clientes=clientes)

    except Exception as e:
        print(f"Erro ao obter dados da tabela clientes: {str(e)}")
        # Trate o erro conforme necessário, por exemplo, exibindo uma página de erro
        return render_template('erro.html', mensagem="Erro ao obter dados da tabela clientes")


@main_routes.route('/colaboradores')
def colaboradores():
    # Lógica para a rota colaboradores, se aplicável
    pass

@main_routes.route('/unauthorized')
def unauthorized():
    return render_template ('unauthorized.html')

@main_routes.route('/cadastrar_empresa', methods=['GET', 'POST'])
def cadastrar_empresa():
    if request.method == 'POST':
        cnpj = request.form.get('cnpj')
        nome = request.form.get('nome')
        contato = request.form.get('contato')
        cep = request.form.get('cep')
        rua = request.form.get('rua')
        bairro = request.form.get('bairro')
        numero = request.form.get('numero')
        complemento = request.form.get('complemento')

        cur = mysql.connection.cursor()

        # Verifique se o CNPJ já está cadastrado
        cur.execute("SELECT * FROM empresa WHERE cnpj = %s", (cnpj,))
        existing_empresa = cur.fetchone()

        if existing_empresa:
            flash('Empresa já cadastrada', 'error')
        else:
            # Se não estiver cadastrada, faça a inserção
            cur.execute(
                "INSERT INTO empresa (cnpj, nome, contato, cep, rua, bairro, numero, complemento) VALUES (%s, %s, %s, %s, %s, %s, %s, %s)",
                (cnpj, nome, contato, cep, rua, bairro, numero, complemento)
            )
            mysql.connection.commit()
            flash('Empresa cadastrada com sucesso', 'success')

        cur.close()

    return render_template('cadastrar_empresa.html')



@main_routes.route('/adicionar_usuario', methods=['GET', 'POST'])
def adicionar_usuario():
    if request.method == 'GET':
        # Consulta ao banco de dados para obter as empresas
        cur = mysql.connection.cursor()
        cur.execute("SELECT cnpj, nome FROM empresa")
        empresas = cur.fetchall()
        cur.close()

        return render_template('adicionar_usuario.html', empresas=empresas)

    elif request.method == 'POST':
        cpf = request.form.get('cpf')
        nome_completo = request.form.get('nome_completo')
        cep = request.form.get('cep')
        rua = request.form.get('rua')
        bairro = request.form.get('bairro')
        numero = request.form.get('numero')
        complemento = request.form.get('complemento')
        empresa_nome = request.form.get('empresa')  # Use diretamente o nome da empresa
        funcoes = request.form.get('funcoes')
        contato = request.form.get('contato')

        try:
            cur = mysql.connection.cursor()
            cur.execute(
                "INSERT INTO clientes (cpf, nome_completo, cep, rua, bairro, numero, complemento, empresa, funcoes, contato) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s)",
                (cpf, nome_completo, cep, rua, bairro, numero, complemento, empresa_nome, funcoes, contato)
            )
            mysql.connection.commit()
            cur.close()

            flash('Usuário adicionado com sucesso', 'success')
            return redirect(url_for('main_routes.adicionar_usuario'))  # Redireciona para a rota adicionar_usuario

        except Exception as e:
            flash(f'Erro ao adicionar usuário: {str(e)}', 'error')

    return render_template('adicionar_usuario.html')


@main_routes.route('/deletar_usuario/<cpf>', methods=['POST'])
def delete_usuario(cpf):
    if request.method == 'POST':
        try:
            with mysql.connection.cursor() as cursor:
                cursor.execute("DELETE FROM clientes WHERE cpf=%s", (cpf,))
                mysql.connection.commit()
            flash("Usuário excluído com sucesso")
        except Exception as e:
            flash("Não foi possível excluir o usuário")
        return redirect(url_for('main_routes.painel_admin'))
    else:
        return redirect(url_for('main_routes.painel_admin'))

@main_routes.route('/permissao/<cpf>', methods=['GET', 'POST'])
def permissao_individual(cpf):
    cursor = mysql.connection.cursor()

    if request.method == 'POST':
        try:
            # Atualizar informações pessoais
            cursor.execute("SELECT * FROM clientes WHERE cpf=%s", (cpf,))
            user = cursor.fetchone()

            if user:
                nome_completo = request.form.get('nome_completo')
                contato = request.form.get('contato')
                cep = request.form.get('cep')
                bairro = request.form.get('bairro')
                rua = request.form.get('rua')
                numero = request.form.get('numero')
                complemento = request.form.get('complemento')
                empresa = request.form.get('empresa')

                # Verificar se os valores foram alterados
                if nome_completo != user['nome_completo']:
                    user['nome_completo'] = nome_completo
                if contato != user['contato']:
                    user['contato'] = contato
                if cep != user['cep']:
                    user['cep'] = cep
                if bairro != user['bairro']:
                    user['bairro'] = bairro
                if rua != user['rua']:
                    user['rua'] = rua
                if numero != user['numero']:
                    user['numero'] = numero
                if complemento != user['complemento']:
                    user['complemento'] = complemento
                if empresa != user['empresa']:
                    user['empresa'] = empresa

                # Atualizar as informações pessoais na tabela de clientes
                cursor.execute(
                    "UPDATE clientes SET nome_completo=%s, contato=%s, cep=%s, bairro=%s, rua=%s, numero=%s, complemento=%s, empresa=%s WHERE cpf=%s",
                    (user['nome_completo'], user['contato'], user['cep'], user['bairro'], user['rua'], user['numero'], user['complemento'], user['empresa'], cpf)
                )
                mysql.connection.commit()

                # Cadastro de permissões
                matricula = request.form.get('matricula') == '1'
                cadastro = request.form.get('cadastro') == '1'
                secretaria = request.form.get('secretaria') == '1'
                financeiro = request.form.get('financeiro') == '1'

                # Verificar se as permissões existem
                cursor.execute("SELECT * FROM permissao WHERE cpf_cliente=%s", (cpf,))
                permissoes = cursor.fetchone()

                if permissoes:
                    # Atualizar as permissões na tabela de permissao
                    cursor.execute(
                        "UPDATE permissao SET matricula=%s, cadastro=%s, secretaria=%s, financeiro=%s WHERE cpf_cliente=%s",
                        (matricula, cadastro, secretaria, financeiro, cpf)
                    )
                else:
                    # Se não houver permissões, crie um novo registro
                    cursor.execute(
                        "INSERT INTO permissao (matricula, cadastro, secretaria, financeiro, cpf_cliente) VALUES (%s, %s, %s, %s, %s)",
                        (matricula, cadastro, secretaria, financeiro, cpf)
                    )

                mysql.connection.commit()
                flash("Informações atualizadas com sucesso!", "success")
            else:
                flash("Cliente não encontrado.", "error")
        except Exception as e:
            flash(f"Erro ao atualizar informações: {str(e)}", "error")

    # Buscar as informações do cliente após a atualização
    cursor.execute("SELECT * FROM clientes WHERE cpf=%s", (cpf,))
    user = cursor.fetchone()

    # Buscar as informações sobre empresas
    cursor.execute("SELECT * FROM empresa")
    empresas = cursor.fetchall()

    # Buscar as informações de permissões
    cursor.execute("SELECT * FROM permissao WHERE cpf_cliente=%s", (cpf,))
    permissoes = cursor.fetchone()

    cursor.close()

    if user:
        return render_template('permissao.html', user=user, empresas=empresas, permissoes=permissoes)
    else:
        abort(404)


@main_routes.route('/empresas_cadastradas')
def visualizar_empresas():
    # Aqui você pode adicionar a lógica necessária para obter dados sobre as empresas, se necessário
    # Por exemplo, pode fazer consultas no banco de dados para obter informações sobre as empresas

    # Renderiza a página 'empresas_cadastradas.html'
    return render_template('empresas_cadastradas.html')

@main_routes.route('/usuario_cadastrado')
def usuario_cadastrado():
    cpf_cliente = request.args.get('cpf_cliente')
    cursor = mysql.connection.cursor()

    try:
        # Consulta no banco de dados para obter informações de login do usuário
        cursor.execute("SELECT * FROM login_cliente WHERE cpf_cliente=%s", (cpf_cliente,))
        login_info = cursor.fetchone()

        if login_info:
            # Obtendo informações do cliente associado ao login
            cursor.execute("SELECT nome_completo FROM clientes WHERE cpf=%s", (cpf_cliente,))
            cliente_info = cursor.fetchone()

            if cliente_info:
                nome_do_usuario = cliente_info['nome_completo']
                login_cadastrado = login_info['usuario_cliente']

                # Se houver informações de login, você pode passá-las para o template
                return render_template('usuario_cadastrado.html', nome_do_usuario=nome_do_usuario, login_cadastrado=login_cadastrado)
            else:
                flash(f'Informações do cliente para CPF {cpf_cliente} não encontradas.', 'error')
                return redirect(url_for('main_routes.criacao_login', cpf_cliente=cpf_cliente))
        else:
            # Se não houver informações de login, você pode lidar com isso de acordo com sua lógica
            flash(f'Login para CPF {cpf_cliente} não encontrado.', 'error')
            return redirect(url_for('main_routes.criacao_login', cpf_cliente=cpf_cliente))
    except Exception as e:
        flash(f'Erro ao obter informações de login: {str(e)}', 'error')
        return redirect(url_for('main_routes.criacao_login', cpf_cliente=cpf_cliente))
    finally:
        cursor.close()


@main_routes.route('/criacao_login/<cpf_cliente>', methods=['GET', 'POST'])
def criacao_login(cpf_cliente):
    cursor = mysql.connection.cursor()

    # Verificar se já existe um usuario_cliente cadastrado para o cpf_cliente
    cursor.execute("SELECT * FROM login_cliente WHERE cpf_cliente=%s", (cpf_cliente,))
    existing_user = cursor.fetchone()

    if existing_user:
        # Se já existir, redirecione para a página de usuário cadastrado
        return redirect(url_for('main_routes.usuario_cadastrado', cpf_cliente=cpf_cliente))

    if request.method == 'POST':
        # Obtenha o nome de usuário do formulário
        username = request.form.get('username')

        if username is not None:
            # Verifique se o cliente com o CPF existe
            cursor.execute("SELECT * FROM clientes WHERE cpf=%s", (cpf_cliente,))
            user = cursor.fetchone()

            try:
                if user:
                    # Insira o novo login para o cliente
                    cur = mysql.connection.cursor()
                    cur.execute(
                        "INSERT INTO login_cliente (usuario_cliente, cpf_cliente) VALUES (%s, %s)",
                        (username, cpf_cliente)
                    )
                    mysql.connection.commit()
                    cur.close()

                    flash('Login criado com sucesso!', 'success')
                    # Após criar o login, redirecione para a página de usuário cadastrado
                    return redirect(url_for('main_routes.usuario_cadastrado', cpf_cliente=cpf_cliente))
                else:
                    flash(f'Cliente com CPF {cpf_cliente} não encontrado.', 'error')
            except Exception as e:
                flash(f'Erro ao adicionar login: {str(e)}', 'error')

    # Aqui você pode usar o valor de 'cpf_cliente' como quiser
    return render_template('criacao_login.html', cpf_cliente=cpf_cliente)

@main_routes.route('/bloquear_cliente/<cpf>', methods=['POST'])
def bloquear_cliente(cpf):
    try:
        # Lógica para deletar o atributo senha_cliente do cliente com o CPF fornecido
        cursor = mysql.connection.cursor()

        # Defina a senha_cliente como NULL (ou remova o atributo completamente)
        # Substitua 'SUA_TABELA' pelo nome real da tabela no seu banco de dados
        # Substitua 'SUA_COLUNA' pelo nome real da coluna que armazena a senha
        sql_query = f"UPDATE login_cliente SET senha_cliente = NULL WHERE cpf_cliente = '{cpf}'"
        cursor.execute(sql_query)

        # Commit da transação
        mysql.connection.commit()

        # Feche o cursor
        cursor.close()

        # Redireciona de volta à página de painel_admin ou alguma outra página apropriada
        return redirect(url_for('main_routes.painel_admin'))

    except Exception as e:
        print(f"Erro ao bloquear cliente: {str(e)}")
        # Trate o erro conforme necessário
        return render_template('erro.html', mensagem="Erro ao bloquear cliente")