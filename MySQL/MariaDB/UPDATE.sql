UPDATE tb_alunos SET nome = 'Joao' WHERE id_aluno = 13
SELECT * FROM `tb_alunos` WHERE idade >= 80
UPDATE tb_alunos SET interesse = 'Saude' WHERE idade >= 80
UPDATE tb_alunos SET nome='Jose', idade=25, email='jose@gmail.com' WHERE id_aluno = 18
SELECT * FROM `tb_alunos` WHERE idade BETWEEN 18 AND 25 estado = 'PA'
UPDATE tb_alunos SET nome = 'Maria' WHERE idade BETWEEN 18 AND estado = 'PA'