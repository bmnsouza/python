---------------------------------------------

SELECT * FROM nota_fiscal.contribuinte c ORDER BY c.nm_fantasia;
SELECT * FROM nota_fiscal.danfe d ORDER BY d.cnpj_contribuinte, d.data_emissao;
SELECT * FROM nota_fiscal.endereco e ORDER BY e.uf, e.municipio, e.logradouro;

---------------------------------------------
