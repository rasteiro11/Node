SELECT * FROM tb_produtos LEFT JOIN tb_descricoes_tecnicas ON (tb_produtos.id_produto = tb_descricoes_tecnicas.id_produto);


SELECT * FROM tb_produtos AS p LEFT JOIN tb_descricoes_tecnicas AS dt ON (p.id_produto = dt.id_produto);

SELECT p.id_produto, p.produto, p.valor, dt.descricao_tecnica FROM tb_produtos AS p LEFT JOIN tb_descricoes_tecnicas AS dt ON (p.id_produto = dt.id_produto);

SELECT p.id_produto, p.produto, p.valor, dt.descricao_tecnica FROM tb_produtos AS p LEFT JOIN tb_descricoes_tecnicas AS dt ON (p.id_produto = dt.id_produto) WHERE p.valor >= 500;

SELECT p.id_produto, p.produto, p.valor, dt.descricao_tecnica FROM tb_produtos AS p LEFT JOIN tb_descricoes_tecnicas AS dt ON (p.id_produto = dt.id_produto) WHERE p.valor >= 500 ORDER BY p.valor ASC;

