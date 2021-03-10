SELECT *, COUNT(*) FROM `tb_alunos` GROUP BY interesse 
SELECT *, COUNT(*) FROM `tb_alunos` GROUP BY interesse
SELECT *, COUNT(*) AS total_por_interesse FROM `tb_alunos` GROUP BY interesse
SELECT estado, COUNT(*) AS total_por_estado FROM `tb_alunos` GROUP BY estado