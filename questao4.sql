create database processos;
use processos;

create table cliente (
id_cliente int,
nome varchar (45),
estado varchar(2),
primary key(id_cliente)
);

create table processos(
id_processo int,
id_cliente int,
assunto varchar(90),
data_abertura date,
primary key(id_processo),
foreign key (id_cliente) references cliente(id_cliente)
);

#Query pedida na questão
select c.nome
from cliente c left join processos p
on c.id_cliente = p.id_cliente
where year(p.data_abertura) = 2023 and c.estado = "SP" 
group by c.id_cliente;
