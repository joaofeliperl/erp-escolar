create database erp_escolar;

use erp_escolar;

create table admin(
id_admin int primary key auto_increment not null,
usuario varchar(100) not null,
senha varchar (100) not null
);