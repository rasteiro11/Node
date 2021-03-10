insert into pessoas
(id, nome ,nascimento, sexo, peso, altura, nacionalidade)
values
(default, 'creauza', '1930-12-30', 'F', '55.2', '1.56', default),
('godofredo','1984-01-02','M','78.50','1.83','Brasil'),
('maria','1999-12-30','F','55.20','1.56','Franca');
select * from pessoas; 

insert into pessoas values
(default, 'adalgiza', '1930-11-2', 'F', '63.2','1.75', 'irlanda');
select * from pessoas;

insert into pessoas
(id, nome, nascimento, sexo, peso, altura, nacionalidade)
values
(default, 'ana', '1975-12-22', 'F', '52.3', '1.45', 'EUA'),
(default, 'Pedro', '2000-07-15', 'M', '52.3', '1.45', default),
(default, 'Maria', '1999-05-30', 'F', '75.9', '1.70', 'Portugal');
select * from pessoas;