describe pessoas; #desc pessoas
describe gafanhotos;

alter table pessoas
rename to gafanhotos;

alter table pessoas
add column profissao varchar(10) after nome;

select * from pessoas;

alter table pessoas
add column codigo int first;

alter table pessoas
drop column profissao;

select * from pessoas;

alter table pessoas 
modify column profissao varchar(20) not null default '';

alter table pessoas
change column profissao prof varchar(20) not null default'';

create table if not exists cursos(
nome varchar(30) not null unique,
descricao text,
carga int unsigned,
totaulas int unsigned,
ano year default '2016'
) default charset = utf8;

alter table cursos
add column idcursos int first;

alter table cursos 
add primary key (idcursos);

drop table cursos;

desc cursos;

create table if not exists teste(
id int,
nome varchar(10),
idade int
);

insert into teste value
('1','Pedro','22'),
('2','Maria','12'),
('3','Lucio','32');

describe teste;

drop table if exists teste;


