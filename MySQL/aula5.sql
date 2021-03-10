select * from gafanhotos;
select * from cursos;

insert into cursos values 
('1','html','curso de html','40','37','2014'),
('2','algoritimos','logica de programacao','20','15','2014'),
('3','photoshop','dicas de photoshop','10','8','2010'),
('4','pgp','cursod e php para iniciantes','40','20','2010'),
('5','jarva','introducao ao java','10','29','2016'),
('6','mysql','bancos de dados mysql','30','15','2016'),
('7','world','curso completo de world','40','30','2018'),
('8','sapateado','dancas ritimicas','40','30','2018'),
('9','cozinha','aprenda a fazer kibe','40','30','2018'),
('10','youtuber','gerar polemica e ganhar inscritos','5','2','2018');

select * from cursos;

update cursos 
set nome = 'HTML5'
where idcursos = '1';

update cursos 
set nome = 'PHP', ano = '2015'
where idcursos = '4';

update cursos
set nome = 'java', carga = '40', ano = '2015'
where idcursos = '5'
limit 1; 

update cursos 
set ano = '2018', carga = '0'
where ano = '2050'
limit 1;

delete from cursos
where idcursos = '8';

delete from cursos
where ano = '2050'
limit 2;

truncate table cursos;
truncate cursos;


