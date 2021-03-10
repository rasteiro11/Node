SELECT * FROM tb_clientes LEFT JOIN tb_pedidos ON(tb_clientes.id_cliente = tb_pedidos.id_cliente);
SELECT * FROM tb_clientes RIGHT JOIN tb_pedidos ON(tb_clientes.id_cliente = tb_pedidos.id_cliente);