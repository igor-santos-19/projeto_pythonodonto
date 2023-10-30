create database odonto;

use odonto;


create table pessoa (
	cod int not null auto_increment,
    nome varchar(255),
    idade int,
    primary key(cod)
);

insert into pessoa (nome, idade) values('Giovana', 32);

select * from pessoa 