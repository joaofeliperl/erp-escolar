from flask import Blueprint, flash, jsonify, render_template, redirect, url_for, request
from db import mysql  # Importe a instância do MySQL
from flask import jsonify
import MySQLdb

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

        return clientes  # Agora, retorna diretamente a lista de clientes

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
        permissoes = request.form.get('permissoes')
        funcoes = request.form.get('funcoes')
        contato = request.form.get('contato')

        try:
            cur = mysql.connection.cursor()
            cur.execute(
                "INSERT INTO clientes (cpf, nome_completo, cep, rua, bairro, numero, complemento, empresa, permissoes, funcoes, contato) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)",
                (cpf, nome_completo, cep, rua, bairro, numero, complemento, empresa_nome, permissoes, funcoes, contato)
            )
            mysql.connection.commit()
            cur.close()

            flash('Usuário adicionado com sucesso', 'success')
            return redirect(url_for('main_routes.adicionar_usuario'))  # Redireciona para a rota adicionar_usuario

        except Exception as e:
            flash(f'Erro ao adicionar usuário: {str(e)}', 'error')

    return render_template('adicionar_usuario.html')


@main_routes.route('/deletar_usuario/<cpf>', methods=['POST'])
def deletar_usuario(cpf):
    try:
        # Adicione o código para deletar o usuário do banco de dados usando o CPF
        # ...
        
        flash('Usuário deletado com sucesso', 'success')
    except Exception as e:
        flash(f'Erro ao deletar usuário: {str(e)}', 'error')

    return redirect(url_for('main_routes.painel_admin'))