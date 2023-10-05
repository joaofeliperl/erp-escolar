create database erp_escolar;

use erp_escolar;

create table admin(
id_admin int primary key auto_increment not null,
usuario varchar(100) not null,
senha varchar (100) not null
);

CREATE TABLE empresa (
    cnpj VARCHAR(18) PRIMARY KEY,
    nome VARCHAR(255),
    contato VARCHAR(20),
    cep VARCHAR(15),
    rua VARCHAR(255),
    bairro VARCHAR(255),
    numero INT,
    complemento VARCHAR(255)
);

CREATE TABLE clientes (
    cpf VARCHAR(14) PRIMARY KEY,
    nome_completo VARCHAR(255) NOT NULL,
    contato VARCHAR(255),
    cep VARCHAR(11),
    rua VARCHAR(255),
    bairro VARCHAR(255),
    numero VARCHAR(10),
    complemento VARCHAR(255),
    empresa VARCHAR(255),
    funcoes VARCHAR(255)
);


Create table permissao(
id_permissao int primary key,
matricula boolean,
cadastro boolean,
secretaria boolean,
financeiro boolean
);

ALTER TABLE permissao
ADD COLUMN cpf_cliente VARCHAR(14),
ADD CONSTRAINT fk_permissao_clientes FOREIGN KEY (cpf_cliente) REFERENCES clientes(cpf);


create table login_cliente(
id_login_cliente int primary key auto_increment not null,
usuario_cliente varchar(100) unique ,
senha_cliente varchar (100) 
);

ALTER TABLE login_cliente
ADD COLUMN cpf_cliente VARCHAR(14),
ADD CONSTRAINT fk_login_clientes FOREIGN KEY (cpf_cliente) REFERENCES clientes(cpf);