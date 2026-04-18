---------------------------------------------

-- Tabela contribuinte
CREATE TABLE nota_fiscal.contribuinte (
    cnpj_contribuinte VARCHAR2(20) PRIMARY KEY,
    nm_fantasia VARCHAR2(200) NOT NULL
);

GRANT SELECT, INSERT, UPDATE, DELETE ON nota_fiscal.contribuinte TO PUBLIC;

INSERT INTO nota_fiscal.contribuinte (cnpj_contribuinte, nm_fantasia) VALUES ('12345678000199', 'MACIEIRA MENEZES');
INSERT INTO nota_fiscal.contribuinte (cnpj_contribuinte, nm_fantasia) VALUES ('55443322000111', 'SUPERMERCADO PRUDENTE');
INSERT INTO nota_fiscal.contribuinte (cnpj_contribuinte, nm_fantasia) VALUES ('22334455000199', 'PADARIA DOCE PÃO');
INSERT INTO nota_fiscal.contribuinte (cnpj_contribuinte, nm_fantasia) VALUES ('99887766000133', 'AUTO PEÇAS CENTRAL');
INSERT INTO nota_fiscal.contribuinte (cnpj_contribuinte, nm_fantasia) VALUES ('11223344000155', 'MERCADINHO SÃO JORGE');
INSERT INTO nota_fiscal.contribuinte (cnpj_contribuinte, nm_fantasia) VALUES ('55667788000111', 'FRIGORÍFICO BOM CORTE');
INSERT INTO nota_fiscal.contribuinte (cnpj_contribuinte, nm_fantasia) VALUES ('66778899000100', 'OFICINA MECÂNICA SILVA');
INSERT INTO nota_fiscal.contribuinte (cnpj_contribuinte, nm_fantasia) VALUES ('77889900000144', 'DISTRIBUIDORA ALVORADA');
INSERT INTO nota_fiscal.contribuinte (cnpj_contribuinte, nm_fantasia) VALUES ('88990011000166', 'PAPELARIA LUZ E VIDA');
INSERT INTO nota_fiscal.contribuinte (cnpj_contribuinte, nm_fantasia) VALUES ('99001122000177', 'FARMÁCIA POPULAR');
INSERT INTO nota_fiscal.contribuinte (cnpj_contribuinte, nm_fantasia) VALUES ('10203040000150', 'LOJA DE CALÇADOS PASSOS');
INSERT INTO nota_fiscal.contribuinte (cnpj_contribuinte, nm_fantasia) VALUES ('20304050000161', 'AÇOUGUE CARNE NOBRE');
INSERT INTO nota_fiscal.contribuinte (cnpj_contribuinte, nm_fantasia) VALUES ('30405060000172', 'MATERIAIS DE CONSTRUÇÃO FORTE');
INSERT INTO nota_fiscal.contribuinte (cnpj_contribuinte, nm_fantasia) VALUES ('40506070000183', 'SALÃO DE BELEZA GLAMOUR');
INSERT INTO nota_fiscal.contribuinte (cnpj_contribuinte, nm_fantasia) VALUES ('50607080000194', 'HORTIFRUTI VERDE VIDA');
INSERT INTO nota_fiscal.contribuinte (cnpj_contribuinte, nm_fantasia) VALUES ('60708090000105', 'LIVRARIA CONHECIMENTO');
INSERT INTO nota_fiscal.contribuinte (cnpj_contribuinte, nm_fantasia) VALUES ('70809010000116', 'ÓTICA VISÃO CLARA');
INSERT INTO nota_fiscal.contribuinte (cnpj_contribuinte, nm_fantasia) VALUES ('80900120000127', 'PET SHOP AMIGO FIEL');
INSERT INTO nota_fiscal.contribuinte (cnpj_contribuinte, nm_fantasia) VALUES ('90010230000138', 'ELETRÔNICOS TECH PLUS');
INSERT INTO nota_fiscal.contribuinte (cnpj_contribuinte, nm_fantasia) VALUES ('10112340000149', 'RESTAURANTE SABOR NORDESTE');
INSERT INTO nota_fiscal.contribuinte (cnpj_contribuinte, nm_fantasia) VALUES ('11213141000150', 'CLÍNICA SAÚDE TOTAL');
INSERT INTO nota_fiscal.contribuinte (cnpj_contribuinte, nm_fantasia) VALUES ('21314151000161', 'ACADEMIA FITNESS POWER');
INSERT INTO nota_fiscal.contribuinte (cnpj_contribuinte, nm_fantasia) VALUES ('31415161000172', 'TRANSPORTADORA RÁPIDO SUL');
INSERT INTO nota_fiscal.contribuinte (cnpj_contribuinte, nm_fantasia) VALUES ('41516171000183', 'CONFEITARIA DOCE ARTE');
INSERT INTO nota_fiscal.contribuinte (cnpj_contribuinte, nm_fantasia) VALUES ('51617181000194', 'AGROPECUÁRIA CAMPO VERDE');
INSERT INTO nota_fiscal.contribuinte (cnpj_contribuinte, nm_fantasia) VALUES ('61718191000105', 'LOJA DE MÓVEIS CONFORTO');
INSERT INTO nota_fiscal.contribuinte (cnpj_contribuinte, nm_fantasia) VALUES ('71819201000116', 'HOTEL POUSADA DO SOL');
INSERT INTO nota_fiscal.contribuinte (cnpj_contribuinte, nm_fantasia) VALUES ('81920211000127', 'INFORMÁTICA BYTE CERTO');
INSERT INTO nota_fiscal.contribuinte (cnpj_contribuinte, nm_fantasia) VALUES ('91021221000138', 'POSTO COMBUSTÍVEL NORDESTE');
INSERT INTO nota_fiscal.contribuinte (cnpj_contribuinte, nm_fantasia) VALUES ('12132232000149', 'VIDRAÇARIA CRISTAL');
INSERT INTO nota_fiscal.contribuinte (cnpj_contribuinte, nm_fantasia) VALUES ('13233343000150', 'DROGARIA SAÚDE E BEM');
INSERT INTO nota_fiscal.contribuinte (cnpj_contribuinte, nm_fantasia) VALUES ('14334454000161', 'PEIXARIA MAR ABERTO');
INSERT INTO nota_fiscal.contribuinte (cnpj_contribuinte, nm_fantasia) VALUES ('15435565000172', 'FLORICULTURA JARDIM BOM');
INSERT INTO nota_fiscal.contribuinte (cnpj_contribuinte, nm_fantasia) VALUES ('16536676000183', 'ESCOLA DE IDIOMAS TALK');
INSERT INTO nota_fiscal.contribuinte (cnpj_contribuinte, nm_fantasia) VALUES ('17637787000194', 'BORRACHARIA EXPRESS');
INSERT INTO nota_fiscal.contribuinte (cnpj_contribuinte, nm_fantasia) VALUES ('18738898000105', 'MERCADO ATACADO PREÇO BOM');
INSERT INTO nota_fiscal.contribuinte (cnpj_contribuinte, nm_fantasia) VALUES ('19839909000116', 'LAVANDERIA ROUPA LIMPA');
INSERT INTO nota_fiscal.contribuinte (cnpj_contribuinte, nm_fantasia) VALUES ('20940010000127', 'SERRALHERIA FERRO FORTE');
INSERT INTO nota_fiscal.contribuinte (cnpj_contribuinte, nm_fantasia) VALUES ('21041121000138', 'CONSULTÓRIO DENTAL SORRIR');
INSERT INTO nota_fiscal.contribuinte (cnpj_contribuinte, nm_Fantasia) VALUES ('22142232000149', 'CASA DE FESTAS ALEGRIA');
INSERT INTO nota_fiscal.contribuinte (cnpj_contribuinte, nm_fantasia) VALUES ('23243343000150', 'LOJA DE ROUPAS ESTILO');
INSERT INTO nota_fiscal.contribuinte (cnpj_contribuinte, nm_fantasia) VALUES ('24344454000161', 'AGÊNCIA DE VIAGENS TURISMO SE');
INSERT INTO nota_fiscal.contribuinte (cnpj_contribuinte, nm_fantasia) VALUES ('25445565000172', 'PADARIA PÃO QUENTE');
INSERT INTO nota_fiscal.contribuinte (cnpj_contribuinte, nm_fantasia) VALUES ('26546676000183', 'DISTRIBUIDORA BEBIDAS GELADAS');
INSERT INTO nota_fiscal.contribuinte (cnpj_contribuinte, nm_fantasia) VALUES ('27647787000194', 'ELÉTRICA ILUMINA');
INSERT INTO nota_fiscal.contribuinte (cnpj_contribuinte, nm_fantasia) VALUES ('28748898000105', 'SUPERMERCADO COMPRE MAIS');
INSERT INTO nota_fiscal.contribuinte (cnpj_contribuinte, nm_fantasia) VALUES ('29849909000116', 'LOJA DE BRINQUEDOS SONHO');
INSERT INTO nota_fiscal.contribuinte (cnpj_contribuinte, nm_fantasia) VALUES ('30950010000127', 'IMOBILIÁRIA TETO PRÓPRIO');
INSERT INTO nota_fiscal.contribuinte (cnpj_contribuinte, nm_fantasia) VALUES ('31051121000138', 'AUTOESCOLA DIREÇÃO CERTA');
INSERT INTO nota_fiscal.contribuinte (cnpj_contribuinte, nm_fantasia) VALUES ('32152232000149', 'LANCHONETE SABOR RÁPIDO');

COMMIT;

---------------------------------------------

-- Tabela danfe
CREATE TABLE nota_fiscal.danfe (
    id_danfe NUMBER GENERATED BY DEFAULT ON NULL AS IDENTITY PRIMARY KEY,
    cnpj_contribuinte VARCHAR2(20) REFERENCES nota_fiscal.contribuinte(cnpj_contribuinte) NOT NULL,
    numero VARCHAR2(15) UNIQUE NOT NULL,
    valor_total NUMBER(12,2) NOT NULL,
    data_emissao DATE NOT NULL
);

GRANT SELECT, INSERT, UPDATE, DELETE ON nota_fiscal.danfe TO PUBLIC;

INSERT INTO nota_fiscal.danfe (cnpj_contribuinte, numero, valor_total, data_emissao) VALUES ('12345678000199', '100001', 2580.50, TO_DATE('2025-10-31','YYYY-MM-DD'));
INSERT INTO nota_fiscal.danfe (cnpj_contribuinte, numero, valor_total, data_emissao) VALUES ('12345678000199', '100002', 180.00, TO_DATE('2025-10-30','YYYY-MM-DD'));
INSERT INTO nota_fiscal.danfe (cnpj_contribuinte, numero, valor_total, data_emissao) VALUES ('12345678000199', '100003', 950.75, TO_DATE('2025-10-25','YYYY-MM-DD'));
INSERT INTO nota_fiscal.danfe (cnpj_contribuinte, numero, valor_total, data_emissao) VALUES ('55443322000111', '200001', 990.90, TO_DATE('2025-10-31','YYYY-MM-DD'));
INSERT INTO nota_fiscal.danfe (cnpj_contribuinte, numero, valor_total, data_emissao) VALUES ('55443322000111', '200002', 1500.00, TO_DATE('2025-10-29','YYYY-MM-DD'));
INSERT INTO nota_fiscal.danfe (cnpj_contribuinte, numero, valor_total, data_emissao) VALUES ('55443322000111', '200003', 320.40, TO_DATE('2025-10-27','YYYY-MM-DD'));
INSERT INTO nota_fiscal.danfe (cnpj_contribuinte, numero, valor_total, data_emissao) VALUES ('22334455000199', '300001', 450.00, TO_DATE('2025-10-25','YYYY-MM-DD'));
INSERT INTO nota_fiscal.danfe (cnpj_contribuinte, numero, valor_total, data_emissao) VALUES ('22334455000199', '300002', 85.99, TO_DATE('2025-10-28','YYYY-MM-DD'));
INSERT INTO nota_fiscal.danfe (cnpj_contribuinte, numero, valor_total, data_emissao) VALUES ('22334455000199', '300003', 1200.00, TO_DATE('2025-10-30','YYYY-MM-DD'));
INSERT INTO nota_fiscal.danfe (cnpj_contribuinte, numero, valor_total, data_emissao) VALUES ('99887766000133', '400001', 980.25, TO_DATE('2025-10-29','YYYY-MM-DD'));
INSERT INTO nota_fiscal.danfe (cnpj_contribuinte, numero, valor_total, data_emissao) VALUES ('99887766000133', '400002', 760.10, TO_DATE('2025-10-27','YYYY-MM-DD'));
INSERT INTO nota_fiscal.danfe (cnpj_contribuinte, numero, valor_total, data_emissao) VALUES ('99887766000133', '400003', 230.00, TO_DATE('2025-10-26','YYYY-MM-DD'));
INSERT INTO nota_fiscal.danfe (cnpj_contribuinte, numero, valor_total, data_emissao) VALUES ('11223344000155', '500001', 670.00, TO_DATE('2025-10-23','YYYY-MM-DD'));
INSERT INTO nota_fiscal.danfe (cnpj_contribuinte, numero, valor_total, data_emissao) VALUES ('11223344000155', '500002', 1320.90, TO_DATE('2025-10-24','YYYY-MM-DD'));
INSERT INTO nota_fiscal.danfe (cnpj_contribuinte, numero, valor_total, data_emissao) VALUES ('11223344000155', '500003', 75.00, TO_DATE('2025-10-28','YYYY-MM-DD'));
INSERT INTO nota_fiscal.danfe (cnpj_contribuinte, numero, valor_total, data_emissao) VALUES ('55667788000111', '600001', 2050.00, TO_DATE('2025-10-22','YYYY-MM-DD'));
INSERT INTO nota_fiscal.danfe (cnpj_contribuinte, numero, valor_total, data_emissao) VALUES ('55667788000111', '600002', 880.40, TO_DATE('2025-10-30','YYYY-MM-DD'));
INSERT INTO nota_fiscal.danfe (cnpj_contribuinte, numero, valor_total, data_emissao) VALUES ('55667788000111', '600003', 129.99, TO_DATE('2025-10-31','YYYY-MM-DD'));
INSERT INTO nota_fiscal.danfe (cnpj_contribuinte, numero, valor_total, data_emissao) VALUES ('66778899000100', '700001', 430.75, TO_DATE('2025-10-28','YYYY-MM-DD'));
INSERT INTO nota_fiscal.danfe (cnpj_contribuinte, numero, valor_total, data_emissao) VALUES ('66778899000100', '700002', 1780.00, TO_DATE('2025-10-26','YYYY-MM-DD'));
INSERT INTO nota_fiscal.danfe (cnpj_contribuinte, numero, valor_total, data_emissao) VALUES ('66778899000100', '700003', 97.90, TO_DATE('2025-10-27','YYYY-MM-DD'));
INSERT INTO nota_fiscal.danfe (cnpj_contribuinte, numero, valor_total, data_emissao) VALUES ('77889900000144', '800001', 1560.00, TO_DATE('2025-10-20','YYYY-MM-DD'));
INSERT INTO nota_fiscal.danfe (cnpj_contribuinte, numero, valor_total, data_emissao) VALUES ('77889900000144', '800002', 640.50, TO_DATE('2025-10-22','YYYY-MM-DD'));
INSERT INTO nota_fiscal.danfe (cnpj_contribuinte, numero, valor_total, data_emissao) VALUES ('77889900000144', '800003', 230.00, TO_DATE('2025-10-24','YYYY-MM-DD'));
INSERT INTO nota_fiscal.danfe (cnpj_contribuinte, numero, valor_total, data_emissao) VALUES ('88990011000166', '900001', 250.00, TO_DATE('2025-10-25','YYYY-MM-DD'));
INSERT INTO nota_fiscal.danfe (cnpj_contribuinte, numero, valor_total, data_emissao) VALUES ('88990011000166', '900002', 820.30, TO_DATE('2025-10-26','YYYY-MM-DD'));
INSERT INTO nota_fiscal.danfe (cnpj_contribuinte, numero, valor_total, data_emissao) VALUES ('88990011000166', '900003', 1580.00, TO_DATE('2025-10-31','YYYY-MM-DD'));
INSERT INTO nota_fiscal.danfe (cnpj_contribuinte, numero, valor_total, data_emissao) VALUES ('99001122000177', '1000001', 980.90, TO_DATE('2025-10-29','YYYY-MM-DD'));
INSERT INTO nota_fiscal.danfe (cnpj_contribuinte, numero, valor_total, data_emissao) VALUES ('99001122000177', '1000002', 110.00, TO_DATE('2025-10-30','YYYY-MM-DD'));
INSERT INTO nota_fiscal.danfe (cnpj_contribuinte, numero, valor_total, data_emissao) VALUES ('99001122000177', '1000003', 220.45, TO_DATE('2025-10-31','YYYY-MM-DD'));
INSERT INTO nota_fiscal.danfe (cnpj_contribuinte, numero, valor_total, data_emissao) VALUES ('12345678000199', '100004', 730.00,  TO_DATE('2025-11-02','YYYY-MM-DD'));
INSERT INTO nota_fiscal.danfe (cnpj_contribuinte, numero, valor_total, data_emissao) VALUES ('12345678000199', '100005', 1890.40, TO_DATE('2025-11-05','YYYY-MM-DD'));
INSERT INTO nota_fiscal.danfe (cnpj_contribuinte, numero, valor_total, data_emissao) VALUES ('55443322000111', '200004', 415.60,  TO_DATE('2025-11-01','YYYY-MM-DD'));
INSERT INTO nota_fiscal.danfe (cnpj_contribuinte, numero, valor_total, data_emissao) VALUES ('55443322000111', '200005', 2300.00, TO_DATE('2025-11-04','YYYY-MM-DD'));
INSERT INTO nota_fiscal.danfe (cnpj_contribuinte, numero, valor_total, data_emissao) VALUES ('22334455000199', '300004', 99.90,   TO_DATE('2025-11-01','YYYY-MM-DD'));
INSERT INTO nota_fiscal.danfe (cnpj_contribuinte, numero, valor_total, data_emissao) VALUES ('22334455000199', '300005', 540.00,  TO_DATE('2025-11-03','YYYY-MM-DD'));
INSERT INTO nota_fiscal.danfe (cnpj_contribuinte, numero, valor_total, data_emissao) VALUES ('99887766000133', '400004', 1150.00, TO_DATE('2025-11-02','YYYY-MM-DD'));
INSERT INTO nota_fiscal.danfe (cnpj_contribuinte, numero, valor_total, data_emissao) VALUES ('99887766000133', '400005', 875.30,  TO_DATE('2025-11-06','YYYY-MM-DD'));
INSERT INTO nota_fiscal.danfe (cnpj_contribuinte, numero, valor_total, data_emissao) VALUES ('11223344000155', '500004', 640.00,  TO_DATE('2025-11-01','YYYY-MM-DD'));
INSERT INTO nota_fiscal.danfe (cnpj_contribuinte, numero, valor_total, data_emissao) VALUES ('11223344000155', '500005', 380.20,  TO_DATE('2025-11-05','YYYY-MM-DD'));
INSERT INTO nota_fiscal.danfe (cnpj_contribuinte, numero, valor_total, data_emissao) VALUES ('55667788000111', '600004', 1740.00, TO_DATE('2025-11-02','YYYY-MM-DD'));
INSERT INTO nota_fiscal.danfe (cnpj_contribuinte, numero, valor_total, data_emissao) VALUES ('55667788000111', '600005', 960.75,  TO_DATE('2025-11-04','YYYY-MM-DD'));
INSERT INTO nota_fiscal.danfe (cnpj_contribuinte, numero, valor_total, data_emissao) VALUES ('66778899000100', '700004', 510.00,  TO_DATE('2025-11-01','YYYY-MM-DD'));
INSERT INTO nota_fiscal.danfe (cnpj_contribuinte, numero, valor_total, data_emissao) VALUES ('66778899000100', '700005', 2100.90, TO_DATE('2025-11-06','YYYY-MM-DD'));
INSERT INTO nota_fiscal.danfe (cnpj_contribuinte, numero, valor_total, data_emissao) VALUES ('77889900000144', '800004', 325.50,  TO_DATE('2025-11-03','YYYY-MM-DD'));
INSERT INTO nota_fiscal.danfe (cnpj_contribuinte, numero, valor_total, data_emissao) VALUES ('77889900000144', '800005', 1985.00, TO_DATE('2025-11-07','YYYY-MM-DD'));
INSERT INTO nota_fiscal.danfe (cnpj_contribuinte, numero, valor_total, data_emissao) VALUES ('88990011000166', '900004', 445.00,  TO_DATE('2025-11-02','YYYY-MM-DD'));
INSERT INTO nota_fiscal.danfe (cnpj_contribuinte, numero, valor_total, data_emissao) VALUES ('88990011000166', '900005', 1120.60, TO_DATE('2025-11-05','YYYY-MM-DD'));
INSERT INTO nota_fiscal.danfe (cnpj_contribuinte, numero, valor_total, data_emissao) VALUES ('99001122000177', '1000004', 560.00, TO_DATE('2025-11-01','YYYY-MM-DD'));
INSERT INTO nota_fiscal.danfe (cnpj_contribuinte, numero, valor_total, data_emissao) VALUES ('99001122000177', '1000005', 890.30, TO_DATE('2025-11-04','YYYY-MM-DD'));
INSERT INTO nota_fiscal.danfe (cnpj_contribuinte, numero, valor_total, data_emissao) VALUES ('10203040000150', '1100001', 420.00,  TO_DATE('2025-10-01','YYYY-MM-DD'));
INSERT INTO nota_fiscal.danfe (cnpj_contribuinte, numero, valor_total, data_emissao) VALUES ('10203040000150', '1100002', 870.50,  TO_DATE('2025-10-05','YYYY-MM-DD'));
INSERT INTO nota_fiscal.danfe (cnpj_contribuinte, numero, valor_total, data_emissao) VALUES ('10203040000150', '1100003', 1350.00, TO_DATE('2025-10-10','YYYY-MM-DD'));
INSERT INTO nota_fiscal.danfe (cnpj_contribuinte, numero, valor_total, data_emissao) VALUES ('10203040000150', '1100004', 215.90,  TO_DATE('2025-10-15','YYYY-MM-DD'));
INSERT INTO nota_fiscal.danfe (cnpj_contribuinte, numero, valor_total, data_emissao) VALUES ('10203040000150', '1100005', 690.00,  TO_DATE('2025-10-20','YYYY-MM-DD'));
INSERT INTO nota_fiscal.danfe (cnpj_contribuinte, numero, valor_total, data_emissao) VALUES ('20304050000161', '1200001', 3200.00, TO_DATE('2025-10-01','YYYY-MM-DD'));
INSERT INTO nota_fiscal.danfe (cnpj_contribuinte, numero, valor_total, data_emissao) VALUES ('20304050000161', '1200002', 1540.75, TO_DATE('2025-10-06','YYYY-MM-DD'));
INSERT INTO nota_fiscal.danfe (cnpj_contribuinte, numero, valor_total, data_emissao) VALUES ('20304050000161', '1200003', 980.00,  TO_DATE('2025-10-11','YYYY-MM-DD'));
INSERT INTO nota_fiscal.danfe (cnpj_contribuinte, numero, valor_total, data_emissao) VALUES ('20304050000161', '1200004', 410.30,  TO_DATE('2025-10-16','YYYY-MM-DD'));
INSERT INTO nota_fiscal.danfe (cnpj_contribuinte, numero, valor_total, data_emissao) VALUES ('20304050000161', '1200005', 2670.40, TO_DATE('2025-10-21','YYYY-MM-DD'));
INSERT INTO nota_fiscal.danfe (cnpj_contribuinte, numero, valor_total, data_emissao) VALUES ('30405060000172', '1300001', 5800.00, TO_DATE('2025-10-02','YYYY-MM-DD'));
INSERT INTO nota_fiscal.danfe (cnpj_contribuinte, numero, valor_total, data_emissao) VALUES ('30405060000172', '1300002', 920.50,  TO_DATE('2025-10-07','YYYY-MM-DD'));
INSERT INTO nota_fiscal.danfe (cnpj_contribuinte, numero, valor_total, data_emissao) VALUES ('30405060000172', '1300003', 3410.00, TO_DATE('2025-10-12','YYYY-MM-DD'));
INSERT INTO nota_fiscal.danfe (cnpj_contribuinte, numero, valor_total, data_emissao) VALUES ('30405060000172', '1300004', 1750.80, TO_DATE('2025-10-17','YYYY-MM-DD'));
INSERT INTO nota_fiscal.danfe (cnpj_contribuinte, numero, valor_total, data_emissao) VALUES ('30405060000172', '1300005', 640.00,  TO_DATE('2025-10-22','YYYY-MM-DD'));
INSERT INTO nota_fiscal.danfe (cnpj_contribuinte, numero, valor_total, data_emissao) VALUES ('40506070000183', '1400001', 180.00,  TO_DATE('2025-10-02','YYYY-MM-DD'));
INSERT INTO nota_fiscal.danfe (cnpj_contribuinte, numero, valor_total, data_emissao) VALUES ('40506070000183', '1400002', 320.50,  TO_DATE('2025-10-07','YYYY-MM-DD'));
INSERT INTO nota_fiscal.danfe (cnpj_contribuinte, numero, valor_total, data_emissao) VALUES ('40506070000183', '1400003', 95.00,   TO_DATE('2025-10-12','YYYY-MM-DD'));
INSERT INTO nota_fiscal.danfe (cnpj_contribuinte, numero, valor_total, data_emissao) VALUES ('40506070000183', '1400004', 460.00,  TO_DATE('2025-10-17','YYYY-MM-DD'));
INSERT INTO nota_fiscal.danfe (cnpj_contribuinte, numero, valor_total, data_emissao) VALUES ('40506070000183', '1400005', 215.75,  TO_DATE('2025-10-22','YYYY-MM-DD'));
INSERT INTO nota_fiscal.danfe (cnpj_contribuinte, numero, valor_total, data_emissao) VALUES ('50607080000194', '1500001', 530.00,  TO_DATE('2025-10-03','YYYY-MM-DD'));
INSERT INTO nota_fiscal.danfe (cnpj_contribuinte, numero, valor_total, data_emissao) VALUES ('50607080000194', '1500002', 270.40,  TO_DATE('2025-10-08','YYYY-MM-DD'));
INSERT INTO nota_fiscal.danfe (cnpj_contribuinte, numero, valor_total, data_emissao) VALUES ('50607080000194', '1500003', 840.00,  TO_DATE('2025-10-13','YYYY-MM-DD'));
INSERT INTO nota_fiscal.danfe (cnpj_contribuinte, numero, valor_total, data_emissao) VALUES ('50607080000194', '1500004', 165.90,  TO_DATE('2025-10-18','YYYY-MM-DD'));
INSERT INTO nota_fiscal.danfe (cnpj_contribuinte, numero, valor_total, data_emissao) VALUES ('50607080000194', '1500005', 720.10,  TO_DATE('2025-10-23','YYYY-MM-DD'));
INSERT INTO nota_fiscal.danfe (cnpj_contribuinte, numero, valor_total, data_emissao) VALUES ('60708090000105', '1600001', 390.00,  TO_DATE('2025-10-03','YYYY-MM-DD'));
INSERT INTO nota_fiscal.danfe (cnpj_contribuinte, numero, valor_total, data_emissao) VALUES ('60708090000105', '1600002', 145.50,  TO_DATE('2025-10-08','YYYY-MM-DD'));
INSERT INTO nota_fiscal.danfe (cnpj_contribuinte, numero, valor_total, data_emissao) VALUES ('60708090000105', '1600003', 870.00,  TO_DATE('2025-10-13','YYYY-MM-DD'));
INSERT INTO nota_fiscal.danfe (cnpj_contribuinte, numero, valor_total, data_emissao) VALUES ('60708090000105', '1600004', 234.90,  TO_DATE('2025-10-18','YYYY-MM-DD'));
INSERT INTO nota_fiscal.danfe (cnpj_contribuinte, numero, valor_total, data_emissao) VALUES ('60708090000105', '1600005', 560.00,  TO_DATE('2025-10-23','YYYY-MM-DD'));
INSERT INTO nota_fiscal.danfe (cnpj_contribuinte, numero, valor_total, data_emissao) VALUES ('70809010000116', '1700001', 1200.00, TO_DATE('2025-10-04','YYYY-MM-DD'));
INSERT INTO nota_fiscal.danfe (cnpj_contribuinte, numero, valor_total, data_emissao) VALUES ('70809010000116', '1700002', 850.00,  TO_DATE('2025-10-09','YYYY-MM-DD'));
INSERT INTO nota_fiscal.danfe (cnpj_contribuinte, numero, valor_total, data_emissao) VALUES ('70809010000116', '1700003', 430.50,  TO_DATE('2025-10-14','YYYY-MM-DD'));
INSERT INTO nota_fiscal.danfe (cnpj_contribuinte, numero, valor_total, data_emissao) VALUES ('70809010000116', '1700004', 1680.00, TO_DATE('2025-10-19','YYYY-MM-DD'));
INSERT INTO nota_fiscal.danfe (cnpj_contribuinte, numero, valor_total, data_emissao) VALUES ('70809010000116', '1700005', 590.25,  TO_DATE('2025-10-24','YYYY-MM-DD'));
INSERT INTO nota_fiscal.danfe (cnpj_contribuinte, numero, valor_total, data_emissao) VALUES ('80900120000127', '1800001', 310.00,  TO_DATE('2025-10-04','YYYY-MM-DD'));
INSERT INTO nota_fiscal.danfe (cnpj_contribuinte, numero, valor_total, data_emissao) VALUES ('80900120000127', '1800002', 745.90,  TO_DATE('2025-10-09','YYYY-MM-DD'));
INSERT INTO nota_fiscal.danfe (cnpj_contribuinte, numero, valor_total, data_emissao) VALUES ('80900120000127', '1800003', 190.00,  TO_DATE('2025-10-14','YYYY-MM-DD'));
INSERT INTO nota_fiscal.danfe (cnpj_contribuinte, numero, valor_total, data_emissao) VALUES ('80900120000127', '1800004', 620.40,  TO_DATE('2025-10-19','YYYY-MM-DD'));
INSERT INTO nota_fiscal.danfe (cnpj_contribuinte, numero, valor_total, data_emissao) VALUES ('80900120000127', '1800005', 480.00,  TO_DATE('2025-10-24','YYYY-MM-DD'));
INSERT INTO nota_fiscal.danfe (cnpj_contribuinte, numero, valor_total, data_emissao) VALUES ('90010230000138', '1900001', 4500.00, TO_DATE('2025-10-05','YYYY-MM-DD'));
INSERT INTO nota_fiscal.danfe (cnpj_contribuinte, numero, valor_total, data_emissao) VALUES ('90010230000138', '1900002', 2300.99, TO_DATE('2025-10-10','YYYY-MM-DD'));
INSERT INTO nota_fiscal.danfe (cnpj_contribuinte, numero, valor_total, data_emissao) VALUES ('90010230000138', '1900003', 8750.00, TO_DATE('2025-10-15','YYYY-MM-DD'));
INSERT INTO nota_fiscal.danfe (cnpj_contribuinte, numero, valor_total, data_emissao) VALUES ('90010230000138', '1900004', 1200.50, TO_DATE('2025-10-20','YYYY-MM-DD'));
INSERT INTO nota_fiscal.danfe (cnpj_contribuinte, numero, valor_total, data_emissao) VALUES ('90010230000138', '1900005', 3670.00, TO_DATE('2025-10-25','YYYY-MM-DD'));
INSERT INTO nota_fiscal.danfe (cnpj_contribuinte, numero, valor_total, data_emissao) VALUES ('10112340000149', '2000001', 850.00,  TO_DATE('2025-10-05','YYYY-MM-DD'));
INSERT INTO nota_fiscal.danfe (cnpj_contribuinte, numero, valor_total, data_emissao) VALUES ('10112340000149', '2000002', 1240.50, TO_DATE('2025-10-10','YYYY-MM-DD'));
INSERT INTO nota_fiscal.danfe (cnpj_contribuinte, numero, valor_total, data_emissao) VALUES ('10112340000149', '2000003', 430.00,  TO_DATE('2025-10-15','YYYY-MM-DD'));
INSERT INTO nota_fiscal.danfe (cnpj_contribuinte, numero, valor_total, data_emissao) VALUES ('10112340000149', '2000004', 970.90,  TO_DATE('2025-10-20','YYYY-MM-DD'));
INSERT INTO nota_fiscal.danfe (cnpj_contribuinte, numero, valor_total, data_emissao) VALUES ('10112340000149', '2000005', 1580.00, TO_DATE('2025-10-25','YYYY-MM-DD'));
INSERT INTO nota_fiscal.danfe (cnpj_contribuinte, numero, valor_total, data_emissao) VALUES ('11213141000150', '2100001', 2800.00, TO_DATE('2025-10-06','YYYY-MM-DD'));
INSERT INTO nota_fiscal.danfe (cnpj_contribuinte, numero, valor_total, data_emissao) VALUES ('11213141000150', '2100002', 1450.00, TO_DATE('2025-10-11','YYYY-MM-DD'));
INSERT INTO nota_fiscal.danfe (cnpj_contribuinte, numero, valor_total, data_emissao) VALUES ('11213141000150', '2100003', 3100.75, TO_DATE('2025-10-16','YYYY-MM-DD'));
INSERT INTO nota_fiscal.danfe (cnpj_contribuinte, numero, valor_total, data_emissao) VALUES ('11213141000150', '2100004', 890.00,  TO_DATE('2025-10-21','YYYY-MM-DD'));
INSERT INTO nota_fiscal.danfe (cnpj_contribuinte, numero, valor_total, data_emissao) VALUES ('11213141000150', '2100005', 2200.40, TO_DATE('2025-10-26','YYYY-MM-DD'));
INSERT INTO nota_fiscal.danfe (cnpj_contribuinte, numero, valor_total, data_emissao) VALUES ('21314151000161', '2200001', 1500.00, TO_DATE('2025-10-06','YYYY-MM-DD'));
INSERT INTO nota_fiscal.danfe (cnpj_contribuinte, numero, valor_total, data_emissao) VALUES ('21314151000161', '2200002', 750.00,  TO_DATE('2025-10-11','YYYY-MM-DD'));
INSERT INTO nota_fiscal.danfe (cnpj_contribuinte, numero, valor_total, data_emissao) VALUES ('21314151000161', '2200003', 1200.00, TO_DATE('2025-10-16','YYYY-MM-DD'));
INSERT INTO nota_fiscal.danfe (cnpj_contribuinte, numero, valor_total, data_emissao) VALUES ('21314151000161', '2200004', 500.00,  TO_DATE('2025-10-21','YYYY-MM-DD'));
INSERT INTO nota_fiscal.danfe (cnpj_contribuinte, numero, valor_total, data_emissao) VALUES ('21314151000161', '2200005', 2100.00, TO_DATE('2025-10-26','YYYY-MM-DD'));
INSERT INTO nota_fiscal.danfe (cnpj_contribuinte, numero, valor_total, data_emissao) VALUES ('31415161000172', '2300001', 7800.00, TO_DATE('2025-10-07','YYYY-MM-DD'));
INSERT INTO nota_fiscal.danfe (cnpj_contribuinte, numero, valor_total, data_emissao) VALUES ('31415161000172', '2300002', 4200.00, TO_DATE('2025-10-12','YYYY-MM-DD'));
INSERT INTO nota_fiscal.danfe (cnpj_contribuinte, numero, valor_total, data_emissao) VALUES ('31415161000172', '2300003', 9500.50, TO_DATE('2025-10-17','YYYY-MM-DD'));
INSERT INTO nota_fiscal.danfe (cnpj_contribuinte, numero, valor_total, data_emissao) VALUES ('31415161000172', '2300004', 3100.75, TO_DATE('2025-10-22','YYYY-MM-DD'));
INSERT INTO nota_fiscal.danfe (cnpj_contribuinte, numero, valor_total, data_emissao) VALUES ('31415161000172', '2300005', 6450.00, TO_DATE('2025-10-27','YYYY-MM-DD'));
INSERT INTO nota_fiscal.danfe (cnpj_contribuinte, numero, valor_total, data_emissao) VALUES ('41516171000183', '2400001', 280.00,  TO_DATE('2025-10-07','YYYY-MM-DD'));
INSERT INTO nota_fiscal.danfe (cnpj_contribuinte, numero, valor_total, data_emissao) VALUES ('41516171000183', '2400002', 560.50,  TO_DATE('2025-10-12','YYYY-MM-DD'));
INSERT INTO nota_fiscal.danfe (cnpj_contribuinte, numero, valor_total, data_emissao) VALUES ('41516171000183', '2400003', 145.00,  TO_DATE('2025-10-17','YYYY-MM-DD'));
INSERT INTO nota_fiscal.danfe (cnpj_contribuinte, numero, valor_total, data_emissao) VALUES ('41516171000183', '2400004', 920.00,  TO_DATE('2025-10-22','YYYY-MM-DD'));
INSERT INTO nota_fiscal.danfe (cnpj_contribuinte, numero, valor_total, data_emissao) VALUES ('41516171000183', '2400005', 370.75,  TO_DATE('2025-10-27','YYYY-MM-DD'));
INSERT INTO nota_fiscal.danfe (cnpj_contribuinte, numero, valor_total, data_emissao) VALUES ('51617181000194', '2500001', 12000.00, TO_DATE('2025-10-08','YYYY-MM-DD'));
INSERT INTO nota_fiscal.danfe (cnpj_contribuinte, numero, valor_total, data_emissao) VALUES ('51617181000194', '2500002', 6700.50,  TO_DATE('2025-10-13','YYYY-MM-DD'));
INSERT INTO nota_fiscal.danfe (cnpj_contribuinte, numero, valor_total, data_emissao) VALUES ('51617181000194', '2500003', 3400.00,  TO_DATE('2025-10-18','YYYY-MM-DD'));
INSERT INTO nota_fiscal.danfe (cnpj_contribuinte, numero, valor_total, data_emissao) VALUES ('51617181000194', '2500004', 8900.80,  TO_DATE('2025-10-23','YYYY-MM-DD'));
INSERT INTO nota_fiscal.danfe (cnpj_contribuinte, numero, valor_total, data_emissao) VALUES ('51617181000194', '2500005', 5200.00,  TO_DATE('2025-10-28','YYYY-MM-DD'));
INSERT INTO nota_fiscal.danfe (cnpj_contribuinte, numero, valor_total, data_emissao) VALUES ('61718191000105', '2600001', 3200.00, TO_DATE('2025-10-08','YYYY-MM-DD'));
INSERT INTO nota_fiscal.danfe (cnpj_contribuinte, numero, valor_total, data_emissao) VALUES ('61718191000105', '2600002', 5800.50, TO_DATE('2025-10-13','YYYY-MM-DD'));
INSERT INTO nota_fiscal.danfe (cnpj_contribuinte, numero, valor_total, data_emissao) VALUES ('61718191000105', '2600003', 1400.00, TO_DATE('2025-10-18','YYYY-MM-DD'));
INSERT INTO nota_fiscal.danfe (cnpj_contribuinte, numero, valor_total, data_emissao) VALUES ('61718191000105', '2600004', 9200.00, TO_DATE('2025-10-23','YYYY-MM-DD'));
INSERT INTO nota_fiscal.danfe (cnpj_contribuinte, numero, valor_total, data_emissao) VALUES ('61718191000105', '2600005', 4600.75, TO_DATE('2025-10-28','YYYY-MM-DD'));
INSERT INTO nota_fiscal.danfe (cnpj_contribuinte, numero, valor_total, data_emissao) VALUES ('71819201000116', '2700001', 2400.00, TO_DATE('2025-10-09','YYYY-MM-DD'));
INSERT INTO nota_fiscal.danfe (cnpj_contribuinte, numero, valor_total, data_emissao) VALUES ('71819201000116', '2700002', 1800.00, TO_DATE('2025-10-14','YYYY-MM-DD'));
INSERT INTO nota_fiscal.danfe (cnpj_contribuinte, numero, valor_total, data_emissao) VALUES ('71819201000116', '2700003', 3600.00, TO_DATE('2025-10-19','YYYY-MM-DD'));
INSERT INTO nota_fiscal.danfe (cnpj_contribuinte, numero, valor_total, data_emissao) VALUES ('71819201000116', '2700004', 960.50,  TO_DATE('2025-10-24','YYYY-MM-DD'));
INSERT INTO nota_fiscal.danfe (cnpj_contribuinte, numero, valor_total, data_emissao) VALUES ('71819201000116', '2700005', 4800.00, TO_DATE('2025-10-29','YYYY-MM-DD'));
INSERT INTO nota_fiscal.danfe (cnpj_contribuinte, numero, valor_total, data_emissao) VALUES ('81920211000127', '2800001', 1800.00, TO_DATE('2025-10-09','YYYY-MM-DD'));
INSERT INTO nota_fiscal.danfe (cnpj_contribuinte, numero, valor_total, data_emissao) VALUES ('81920211000127', '2800002', 3200.50, TO_DATE('2025-10-14','YYYY-MM-DD'));
INSERT INTO nota_fiscal.danfe (cnpj_contribuinte, numero, valor_total, data_emissao) VALUES ('81920211000127', '2800003', 640.00,  TO_DATE('2025-10-19','YYYY-MM-DD'));
INSERT INTO nota_fiscal.danfe (cnpj_contribuinte, numero, valor_total, data_emissao) VALUES ('81920211000127', '2800004', 5100.75, TO_DATE('2025-10-24','YYYY-MM-DD'));
INSERT INTO nota_fiscal.danfe (cnpj_contribuinte, numero, valor_total, data_emissao) VALUES ('81920211000127', '2800005', 2250.00, TO_DATE('2025-10-29','YYYY-MM-DD'));
INSERT INTO nota_fiscal.danfe (cnpj_contribuinte, numero, valor_total, data_emissao) VALUES ('91021221000138', '2900001', 15000.00, TO_DATE('2025-10-10','YYYY-MM-DD'));
INSERT INTO nota_fiscal.danfe (cnpj_contribuinte, numero, valor_total, data_emissao) VALUES ('91021221000138', '2900002', 8700.00,  TO_DATE('2025-10-15','YYYY-MM-DD'));
INSERT INTO nota_fiscal.danfe (cnpj_contribuinte, numero, valor_total, data_emissao) VALUES ('91021221000138', '2900003', 22000.50, TO_DATE('2025-10-20','YYYY-MM-DD'));
INSERT INTO nota_fiscal.danfe (cnpj_contribuinte, numero, valor_total, data_emissao) VALUES ('91021221000138', '2900004', 11300.00, TO_DATE('2025-10-25','YYYY-MM-DD'));
INSERT INTO nota_fiscal.danfe (cnpj_contribuinte, numero, valor_total, data_emissao) VALUES ('91021221000138', '2900005', 6800.75,  TO_DATE('2025-10-30','YYYY-MM-DD'));
INSERT INTO nota_fiscal.danfe (cnpj_contribuinte, numero, valor_total, data_emissao) VALUES ('12132232000149', '3000001', 740.00,  TO_DATE('2025-10-10','YYYY-MM-DD'));
INSERT INTO nota_fiscal.danfe (cnpj_contribuinte, numero, valor_total, data_emissao) VALUES ('12132232000149', '3000002', 1650.50, TO_DATE('2025-10-15','YYYY-MM-DD'));
INSERT INTO nota_fiscal.danfe (cnpj_contribuinte, numero, valor_total, data_emissao) VALUES ('12132232000149', '3000003', 380.00,  TO_DATE('2025-10-20','YYYY-MM-DD'));
INSERT INTO nota_fiscal.danfe (cnpj_contribuinte, numero, valor_total, data_emissao) VALUES ('12132232000149', '3000004', 2100.00, TO_DATE('2025-10-25','YYYY-MM-DD'));
INSERT INTO nota_fiscal.danfe (cnpj_contribuinte, numero, valor_total, data_emissao) VALUES ('12132232000149', '3000005', 910.90,  TO_DATE('2025-10-30','YYYY-MM-DD'));
INSERT INTO nota_fiscal.danfe (cnpj_contribuinte, numero, valor_total, data_emissao) VALUES ('13233343000150', '3100001', 560.00,  TO_DATE('2025-10-11','YYYY-MM-DD'));
INSERT INTO nota_fiscal.danfe (cnpj_contribuinte, numero, valor_total, data_emissao) VALUES ('13233343000150', '3100002', 1290.75, TO_DATE('2025-10-16','YYYY-MM-DD'));
INSERT INTO nota_fiscal.danfe (cnpj_contribuinte, numero, valor_total, data_emissao) VALUES ('13233343000150', '3100003', 340.00,  TO_DATE('2025-10-21','YYYY-MM-DD'));
INSERT INTO nota_fiscal.danfe (cnpj_contribuinte, numero, valor_total, data_emissao) VALUES ('13233343000150', '3100004', 880.40,  TO_DATE('2025-10-26','YYYY-MM-DD'));
INSERT INTO nota_fiscal.danfe (cnpj_contribuinte, numero, valor_total, data_emissao) VALUES ('13233343000150', '3100005', 2050.00, TO_DATE('2025-10-31','YYYY-MM-DD'));
INSERT INTO nota_fiscal.danfe (cnpj_contribuinte, numero, valor_total, data_emissao) VALUES ('14334454000161', '3200001', 1100.00, TO_DATE('2025-10-11','YYYY-MM-DD'));
INSERT INTO nota_fiscal.danfe (cnpj_contribuinte, numero, valor_total, data_emissao) VALUES ('14334454000161', '3200002', 480.50,  TO_DATE('2025-10-16','YYYY-MM-DD'));
INSERT INTO nota_fiscal.danfe (cnpj_contribuinte, numero, valor_total, data_emissao) VALUES ('14334454000161', '3200003', 2300.00, TO_DATE('2025-10-21','YYYY-MM-DD'));
INSERT INTO nota_fiscal.danfe (cnpj_contribuinte, numero, valor_total, data_emissao) VALUES ('14334454000161', '3200004', 790.00,  TO_DATE('2025-10-26','YYYY-MM-DD'));
INSERT INTO nota_fiscal.danfe (cnpj_contribuinte, numero, valor_total, data_emissao) VALUES ('14334454000161', '3200005', 1540.30, TO_DATE('2025-10-31','YYYY-MM-DD'));
INSERT INTO nota_fiscal.danfe (cnpj_contribuinte, numero, valor_total, data_emissao) VALUES ('15435565000172', '3300001', 220.00,  TO_DATE('2025-10-12','YYYY-MM-DD'));
INSERT INTO nota_fiscal.danfe (cnpj_contribuinte, numero, valor_total, data_emissao) VALUES ('15435565000172', '3300002', 480.00,  TO_DATE('2025-10-17','YYYY-MM-DD'));
INSERT INTO nota_fiscal.danfe (cnpj_contribuinte, numero, valor_total, data_emissao) VALUES ('15435565000172', '3300003', 135.90,  TO_DATE('2025-10-22','YYYY-MM-DD'));
INSERT INTO nota_fiscal.danfe (cnpj_contribuinte, numero, valor_total, data_emissao) VALUES ('15435565000172', '3300004', 690.50,  TO_DATE('2025-10-27','YYYY-MM-DD'));
INSERT INTO nota_fiscal.danfe (cnpj_contribuinte, numero, valor_total, data_emissao) VALUES ('15435565000172', '3300005', 310.00,  TO_DATE('2025-10-31','YYYY-MM-DD'));
INSERT INTO nota_fiscal.danfe (cnpj_contribuinte, numero, valor_total, data_emissao) VALUES ('16536676000183', '3400001', 3500.00, TO_DATE('2025-10-12','YYYY-MM-DD'));
INSERT INTO nota_fiscal.danfe (cnpj_contribuinte, numero, valor_total, data_emissao) VALUES ('16536676000183', '3400002', 1800.00, TO_DATE('2025-10-17','YYYY-MM-DD'));
INSERT INTO nota_fiscal.danfe (cnpj_contribuinte, numero, valor_total, data_emissao) VALUES ('16536676000183', '3400003', 4200.00, TO_DATE('2025-10-22','YYYY-MM-DD'));
INSERT INTO nota_fiscal.danfe (cnpj_contribuinte, numero, valor_total, data_emissao) VALUES ('16536676000183', '3400004', 700.50,  TO_DATE('2025-10-27','YYYY-MM-DD'));
INSERT INTO nota_fiscal.danfe (cnpj_contribuinte, numero, valor_total, data_emissao) VALUES ('16536676000183', '3400005', 2600.00, TO_DATE('2025-10-31','YYYY-MM-DD'));
INSERT INTO nota_fiscal.danfe (cnpj_contribuinte, numero, valor_total, data_emissao) VALUES ('17637787000194', '3500001', 320.00,  TO_DATE('2025-10-13','YYYY-MM-DD'));
INSERT INTO nota_fiscal.danfe (cnpj_contribuinte, numero, valor_total, data_emissao) VALUES ('17637787000194', '3500002', 870.50,  TO_DATE('2025-10-18','YYYY-MM-DD'));
INSERT INTO nota_fiscal.danfe (cnpj_contribuinte, numero, valor_total, data_emissao) VALUES ('17637787000194', '3500003', 150.00,  TO_DATE('2025-10-23','YYYY-MM-DD'));
INSERT INTO nota_fiscal.danfe (cnpj_contribuinte, numero, valor_total, data_emissao) VALUES ('17637787000194', '3500004', 630.75,  TO_DATE('2025-10-28','YYYY-MM-DD'));
INSERT INTO nota_fiscal.danfe (cnpj_contribuinte, numero, valor_total, data_emissao) VALUES ('17637787000194', '3500005', 420.00,  TO_DATE('2025-10-31','YYYY-MM-DD'));
INSERT INTO nota_fiscal.danfe (cnpj_contribuinte, numero, valor_total, data_emissao) VALUES ('18738898000105', '3600001', 18500.00, TO_DATE('2025-10-13','YYYY-MM-DD'));
INSERT INTO nota_fiscal.danfe (cnpj_contribuinte, numero, valor_total, data_emissao) VALUES ('18738898000105', '3600002', 9200.50,  TO_DATE('2025-10-18','YYYY-MM-DD'));
INSERT INTO nota_fiscal.danfe (cnpj_contribuinte, numero, valor_total, data_emissao) VALUES ('18738898000105', '3600003', 14700.00, TO_DATE('2025-10-23','YYYY-MM-DD'));
INSERT INTO nota_fiscal.danfe (cnpj_contribuinte, numero, valor_total, data_emissao) VALUES ('18738898000105', '3600004', 6300.75,  TO_DATE('2025-10-28','YYYY-MM-DD'));
INSERT INTO nota_fiscal.danfe (cnpj_contribuinte, numero, valor_total, data_emissao) VALUES ('18738898000105', '3600005', 21000.00, TO_DATE('2025-10-31','YYYY-MM-DD'));
INSERT INTO nota_fiscal.danfe (cnpj_contribuinte, numero, valor_total, data_emissao) VALUES ('19839909000116', '3700001', 210.00,  TO_DATE('2025-10-14','YYYY-MM-DD'));
INSERT INTO nota_fiscal.danfe (cnpj_contribuinte, numero, valor_total, data_emissao) VALUES ('19839909000116', '3700002', 480.90,  TO_DATE('2025-10-19','YYYY-MM-DD'));
INSERT INTO nota_fiscal.danfe (cnpj_contribuinte, numero, valor_total, data_emissao) VALUES ('19839909000116', '3700003', 135.00,  TO_DATE('2025-10-24','YYYY-MM-DD'));
INSERT INTO nota_fiscal.danfe (cnpj_contribuinte, numero, valor_total, data_emissao) VALUES ('19839909000116', '3700004', 390.50,  TO_DATE('2025-10-29','YYYY-MM-DD'));
INSERT INTO nota_fiscal.danfe (cnpj_contribuinte, numero, valor_total, data_emissao) VALUES ('19839909000116', '3700005', 720.00,  TO_DATE('2025-10-31','YYYY-MM-DD'));
INSERT INTO nota_fiscal.danfe (cnpj_contribuinte, numero, valor_total, data_emissao) VALUES ('20940010000127', '3800001', 1800.00, TO_DATE('2025-10-14','YYYY-MM-DD'));
INSERT INTO nota_fiscal.danfe (cnpj_contribuinte, numero, valor_total, data_emissao) VALUES ('20940010000127', '3800002', 4200.50, TO_DATE('2025-10-19','YYYY-MM-DD'));
INSERT INTO nota_fiscal.danfe (cnpj_contribuinte, numero, valor_total, data_emissao) VALUES ('20940010000127', '3800003', 960.00,  TO_DATE('2025-10-24','YYYY-MM-DD'));
INSERT INTO nota_fiscal.danfe (cnpj_contribuinte, numero, valor_total, data_emissao) VALUES ('20940010000127', '3800004', 3500.75, TO_DATE('2025-10-29','YYYY-MM-DD'));
INSERT INTO nota_fiscal.danfe (cnpj_contribuinte, numero, valor_total, data_emissao) VALUES ('20940010000127', '3800005', 2100.00, TO_DATE('2025-10-31','YYYY-MM-DD'));
INSERT INTO nota_fiscal.danfe (cnpj_contribuinte, numero, valor_total, data_emissao) VALUES ('21041121000138', '3900001', 1200.00, TO_DATE('2025-10-15','YYYY-MM-DD'));
INSERT INTO nota_fiscal.danfe (cnpj_contribuinte, numero, valor_total, data_emissao) VALUES ('21041121000138', '3900002', 850.00,  TO_DATE('2025-10-20','YYYY-MM-DD'));
INSERT INTO nota_fiscal.danfe (cnpj_contribuinte, numero, valor_total, data_emissao) VALUES ('21041121000138', '3900003', 2400.50, TO_DATE('2025-10-25','YYYY-MM-DD'));
INSERT INTO nota_fiscal.danfe (cnpj_contribuinte, numero, valor_total, data_emissao) VALUES ('21041121000138', '3900004', 560.00,  TO_DATE('2025-10-29','YYYY-MM-DD'));
INSERT INTO nota_fiscal.danfe (cnpj_contribuinte, numero, valor_total, data_emissao) VALUES ('21041121000138', '3900005', 1900.75, TO_DATE('2025-10-31','YYYY-MM-DD'));
INSERT INTO nota_fiscal.danfe (cnpj_contribuinte, numero, valor_total, data_emissao) VALUES ('22142232000149', '4000001', 4500.00, TO_DATE('2025-10-15','YYYY-MM-DD'));
INSERT INTO nota_fiscal.danfe (cnpj_contribuinte, numero, valor_total, data_emissao) VALUES ('22142232000149', '4000002', 2800.00, TO_DATE('2025-10-20','YYYY-MM-DD'));
INSERT INTO nota_fiscal.danfe (cnpj_contribuinte, numero, valor_total, data_emissao) VALUES ('22142232000149', '4000003', 7200.50, TO_DATE('2025-10-25','YYYY-MM-DD'));
INSERT INTO nota_fiscal.danfe (cnpj_contribuinte, numero, valor_total, data_emissao) VALUES ('22142232000149', '4000004', 1900.00, TO_DATE('2025-10-29','YYYY-MM-DD'));
INSERT INTO nota_fiscal.danfe (cnpj_contribuinte, numero, valor_total, data_emissao) VALUES ('22142232000149', '4000005', 5600.00, TO_DATE('2025-10-31','YYYY-MM-DD'));
INSERT INTO nota_fiscal.danfe (cnpj_contribuinte, numero, valor_total, data_emissao) VALUES ('23243343000150', '4100001', 890.00,  TO_DATE('2025-10-16','YYYY-MM-DD'));
INSERT INTO nota_fiscal.danfe (cnpj_contribuinte, numero, valor_total, data_emissao) VALUES ('23243343000150', '4100002', 1450.50, TO_DATE('2025-10-21','YYYY-MM-DD'));
INSERT INTO nota_fiscal.danfe (cnpj_contribuinte, numero, valor_total, data_emissao) VALUES ('23243343000150', '4100003', 620.00,  TO_DATE('2025-10-26','YYYY-MM-DD'));
INSERT INTO nota_fiscal.danfe (cnpj_contribuinte, numero, valor_total, data_emissao) VALUES ('23243343000150', '4100004', 2100.75, TO_DATE('2025-10-29','YYYY-MM-DD'));
INSERT INTO nota_fiscal.danfe (cnpj_contribuinte, numero, valor_total, data_emissao) VALUES ('23243343000150', '4100005', 380.00,  TO_DATE('2025-10-31','YYYY-MM-DD'));
INSERT INTO nota_fiscal.danfe (cnpj_contribuinte, numero, valor_total, data_emissao) VALUES ('24344454000161', '4200001', 8500.00, TO_DATE('2025-10-16','YYYY-MM-DD'));
INSERT INTO nota_fiscal.danfe (cnpj_contribuinte, numero, valor_total, data_emissao) VALUES ('24344454000161', '4200002', 4200.00, TO_DATE('2025-10-21','YYYY-MM-DD'));
INSERT INTO nota_fiscal.danfe (cnpj_contribuinte, numero, valor_total, data_emissao) VALUES ('24344454000161', '4200003', 12700.50, TO_DATE('2025-10-26','YYYY-MM-DD'));
INSERT INTO nota_fiscal.danfe (cnpj_contribuinte, numero, valor_total, data_emissao) VALUES ('24344454000161', '4200004', 3100.00, TO_DATE('2025-10-29','YYYY-MM-DD'));
INSERT INTO nota_fiscal.danfe (cnpj_contribuinte, numero, valor_total, data_emissao) VALUES ('24344454000161', '4200005', 6800.75, TO_DATE('2025-10-31','YYYY-MM-DD'));
INSERT INTO nota_fiscal.danfe (cnpj_contribuinte, numero, valor_total, data_emissao) VALUES ('25445565000172', '4300001', 340.00,  TO_DATE('2025-10-17','YYYY-MM-DD'));
INSERT INTO nota_fiscal.danfe (cnpj_contribuinte, numero, valor_total, data_emissao) VALUES ('25445565000172', '4300002', 820.50,  TO_DATE('2025-10-22','YYYY-MM-DD'));
INSERT INTO nota_fiscal.danfe (cnpj_contribuinte, numero, valor_total, data_emissao) VALUES ('25445565000172', '4300003', 190.00,  TO_DATE('2025-10-27','YYYY-MM-DD'));
INSERT INTO nota_fiscal.danfe (cnpj_contribuinte, numero, valor_total, data_emissao) VALUES ('25445565000172', '4300004', 1100.75, TO_DATE('2025-10-29','YYYY-MM-DD'));
INSERT INTO nota_fiscal.danfe (cnpj_contribuinte, numero, valor_total, data_emissao) VALUES ('25445565000172', '4300005', 470.00,  TO_DATE('2025-10-31','YYYY-MM-DD'));
INSERT INTO nota_fiscal.danfe (cnpj_contribuinte, numero, valor_total, data_emissao) VALUES ('26546676000183', '4400001', 7200.00, TO_DATE('2025-10-17','YYYY-MM-DD'));
INSERT INTO nota_fiscal.danfe (cnpj_contribuinte, numero, valor_total, data_emissao) VALUES ('26546676000183', '4400002', 3800.50, TO_DATE('2025-10-22','YYYY-MM-DD'));
INSERT INTO nota_fiscal.danfe (cnpj_contribuinte, numero, valor_total, data_emissao) VALUES ('26546676000183', '4400003', 10500.00, TO_DATE('2025-10-27','YYYY-MM-DD'));
INSERT INTO nota_fiscal.danfe (cnpj_contribuinte, numero, valor_total, data_emissao) VALUES ('26546676000183', '4400004', 4600.75, TO_DATE('2025-10-29','YYYY-MM-DD'));
INSERT INTO nota_fiscal.danfe (cnpj_contribuinte, numero, valor_total, data_emissao) VALUES ('26546676000183', '4400005', 8900.00, TO_DATE('2025-10-31','YYYY-MM-DD'));
INSERT INTO nota_fiscal.danfe (cnpj_contribuinte, numero, valor_total, data_emissao) VALUES ('27647787000194', '4500001', 2400.00, TO_DATE('2025-10-18','YYYY-MM-DD'));
INSERT INTO nota_fiscal.danfe (cnpj_contribuinte, numero, valor_total, data_emissao) VALUES ('27647787000194', '4500002', 1100.50, TO_DATE('2025-10-23','YYYY-MM-DD'));
INSERT INTO nota_fiscal.danfe (cnpj_contribuinte, numero, valor_total, data_emissao) VALUES ('27647787000194', '4500003', 3700.00, TO_DATE('2025-10-27','YYYY-MM-DD'));
INSERT INTO nota_fiscal.danfe (cnpj_contribuinte, numero, valor_total, data_emissao) VALUES ('27647787000194', '4500004', 850.75,  TO_DATE('2025-10-29','YYYY-MM-DD'));
INSERT INTO nota_fiscal.danfe (cnpj_contribuinte, numero, valor_total, data_emissao) VALUES ('27647787000194', '4500005', 2900.00, TO_DATE('2025-10-31','YYYY-MM-DD'));
INSERT INTO nota_fiscal.danfe (cnpj_contribuinte, numero, valor_total, data_emissao) VALUES ('28748898000105', '4600001', 5600.00, TO_DATE('2025-10-18','YYYY-MM-DD'));
INSERT INTO nota_fiscal.danfe (cnpj_contribuinte, numero, valor_total, data_emissao) VALUES ('28748898000105', '4600002', 3200.90, TO_DATE('2025-10-23','YYYY-MM-DD'));
INSERT INTO nota_fiscal.danfe (cnpj_contribuinte, numero, valor_total, data_emissao) VALUES ('28748898000105', '4600003', 8900.50, TO_DATE('2025-10-27','YYYY-MM-DD'));
INSERT INTO nota_fiscal.danfe (cnpj_contribuinte, numero, valor_total, data_emissao) VALUES ('28748898000105', '4600004', 4100.00, TO_DATE('2025-10-29','YYYY-MM-DD'));
INSERT INTO nota_fiscal.danfe (cnpj_contribuinte, numero, valor_total, data_emissao) VALUES ('28748898000105', '4600005', 7300.75, TO_DATE('2025-10-31','YYYY-MM-DD'));
INSERT INTO nota_fiscal.danfe (cnpj_contribuinte, numero, valor_total, data_emissao) VALUES ('29849909000116', '4700001', 980.00,  TO_DATE('2025-10-19','YYYY-MM-DD'));
INSERT INTO nota_fiscal.danfe (cnpj_contribuinte, numero, valor_total, data_emissao) VALUES ('29849909000116', '4700002', 1560.50, TO_DATE('2025-10-24','YYYY-MM-DD'));
INSERT INTO nota_fiscal.danfe (cnpj_contribuinte, numero, valor_total, data_emissao) VALUES ('29849909000116', '4700003', 420.00,  TO_DATE('2025-10-27','YYYY-MM-DD'));
INSERT INTO nota_fiscal.danfe (cnpj_contribuinte, numero, valor_total, data_emissao) VALUES ('29849909000116', '4700004', 2300.75, TO_DATE('2025-10-29','YYYY-MM-DD'));
INSERT INTO nota_fiscal.danfe (cnpj_contribuinte, numero, valor_total, data_emissao) VALUES ('29849909000116', '4700005', 870.00,  TO_DATE('2025-10-31','YYYY-MM-DD'));
INSERT INTO nota_fiscal.danfe (cnpj_contribuinte, numero, valor_total, data_emissao) VALUES ('30950010000127', '4800001', 15000.00, TO_DATE('2025-10-19','YYYY-MM-DD'));
INSERT INTO nota_fiscal.danfe (cnpj_contribuinte, numero, valor_total, data_emissao) VALUES ('30950010000127', '4800002', 8500.00,  TO_DATE('2025-10-24','YYYY-MM-DD'));
INSERT INTO nota_fiscal.danfe (cnpj_contribuinte, numero, valor_total, data_emissao) VALUES ('30950010000127', '4800003', 22000.50, TO_DATE('2025-10-27','YYYY-MM-DD'));
INSERT INTO nota_fiscal.danfe (cnpj_contribuinte, numero, valor_total, data_emissao) VALUES ('30950010000127', '4800004', 6000.00,  TO_DATE('2025-10-29','YYYY-MM-DD'));
INSERT INTO nota_fiscal.danfe (cnpj_contribuinte, numero, valor_total, data_emissao) VALUES ('30950010000127', '4800005', 11200.75, TO_DATE('2025-10-31','YYYY-MM-DD'));
INSERT INTO nota_fiscal.danfe (cnpj_contribuinte, numero, valor_total, data_emissao) VALUES ('31051121000138', '4900001', 1800.00, TO_DATE('2025-10-20','YYYY-MM-DD'));
INSERT INTO nota_fiscal.danfe (cnpj_contribuinte, numero, valor_total, data_emissao) VALUES ('31051121000138', '4900002', 900.00,  TO_DATE('2025-10-24','YYYY-MM-DD'));
INSERT INTO nota_fiscal.danfe (cnpj_contribuinte, numero, valor_total, data_emissao) VALUES ('31051121000138', '4900003', 2700.50, TO_DATE('2025-10-27','YYYY-MM-DD'));
INSERT INTO nota_fiscal.danfe (cnpj_contribuinte, numero, valor_total, data_emissao) VALUES ('31051121000138', '4900004', 450.00,  TO_DATE('2025-10-29','YYYY-MM-DD'));
INSERT INTO nota_fiscal.danfe (cnpj_contribuinte, numero, valor_total, data_emissao) VALUES ('31051121000138', '4900005', 3600.00, TO_DATE('2025-10-31','YYYY-MM-DD'));
INSERT INTO nota_fiscal.danfe (cnpj_contribuinte, numero, valor_total, data_emissao) VALUES ('32152232000149', '5000001', 650.00,  TO_DATE('2025-10-20','YYYY-MM-DD'));
INSERT INTO nota_fiscal.danfe (cnpj_contribuinte, numero, valor_total, data_emissao) VALUES ('32152232000149', '5000002', 1280.50, TO_DATE('2025-10-24','YYYY-MM-DD'));
INSERT INTO nota_fiscal.danfe (cnpj_contribuinte, numero, valor_total, data_emissao) VALUES ('32152232000149', '5000003', 430.00,  TO_DATE('2025-10-27','YYYY-MM-DD'));
INSERT INTO nota_fiscal.danfe (cnpj_contribuinte, numero, valor_total, data_emissao) VALUES ('32152232000149', '5000004', 970.75,  TO_DATE('2025-10-29','YYYY-MM-DD'));
INSERT INTO nota_fiscal.danfe (cnpj_contribuinte, numero, valor_total, data_emissao) VALUES ('32152232000149', '5000005', 1800.00, TO_DATE('2025-10-31','YYYY-MM-DD'));

COMMIT;

---------------------------------------------

-- Tabela endereco
CREATE TABLE nota_fiscal.endereco (
    id_endereco NUMBER GENERATED BY DEFAULT ON NULL AS IDENTITY PRIMARY KEY,
    cnpj_contribuinte VARCHAR2(20) REFERENCES nota_fiscal.contribuinte(cnpj_contribuinte) NOT NULL,
    logradouro VARCHAR2(200) NOT NULL,
    municipio VARCHAR2(100) NOT NULL,
    uf CHAR(2) NOT NULL
);

GRANT SELECT, INSERT, UPDATE, DELETE ON nota_fiscal.endereco TO PUBLIC;

INSERT INTO nota_fiscal.endereco (cnpj_contribuinte, logradouro, municipio, uf) VALUES ('12345678000199', 'Av. Beira Mar, 100', 'Aracaju', 'SE');
INSERT INTO nota_fiscal.endereco (cnpj_contribuinte, logradouro, municipio, uf) VALUES ('55443322000111', 'Rua das Flores, 45', 'Estância', 'SE');
INSERT INTO nota_fiscal.endereco (cnpj_contribuinte, logradouro, municipio, uf) VALUES ('22334455000199', 'Rua do Comércio, 200', 'Lagarto', 'SE');
INSERT INTO nota_fiscal.endereco (cnpj_contribuinte, logradouro, municipio, uf) VALUES ('99887766000133', 'Av. Principal, 321', 'Itabaiana', 'SE');
INSERT INTO nota_fiscal.endereco (cnpj_contribuinte, logradouro, municipio, uf) VALUES ('11223344000155', 'Rua São João, 89', 'Propriá', 'SE');
INSERT INTO nota_fiscal.endereco (cnpj_contribuinte, logradouro, municipio, uf) VALUES ('55667788000111', 'Rua das Oliveiras, 55', 'Tobias Barreto', 'SE');
INSERT INTO nota_fiscal.endereco (cnpj_contribuinte, logradouro, municipio, uf) VALUES ('66778899000100', 'Av. Tancredo Neves, 900', 'Aracaju', 'SE');
INSERT INTO nota_fiscal.endereco (cnpj_contribuinte, logradouro, municipio, uf) VALUES ('77889900000144', 'Rua da Liberdade, 12', 'Simão Dias', 'SE');
INSERT INTO nota_fiscal.endereco (cnpj_contribuinte, logradouro, municipio, uf) VALUES ('88990011000166', 'Rua José Bonifácio, 210', 'Neópolis', 'SE');
INSERT INTO nota_fiscal.endereco (cnpj_contribuinte, logradouro, municipio, uf) VALUES ('99001122000177', 'Av. Hermes Fontes, 501', 'Aracaju', 'SE');
INSERT INTO nota_fiscal.endereco (cnpj_contribuinte, logradouro, municipio, uf) VALUES ('10203040000150', 'Rua dos Calçadistas, 88', 'Aracaju', 'SE');
INSERT INTO nota_fiscal.endereco (cnpj_contribuinte, logradouro, municipio, uf) VALUES ('20304050000161', 'Av. do Gado, 201', 'Itabaiana', 'SE');
INSERT INTO nota_fiscal.endereco (cnpj_contribuinte, logradouro, municipio, uf) VALUES ('30405060000172', 'Rod. SE-170, km 3', 'Lagarto', 'SE');
INSERT INTO nota_fiscal.endereco (cnpj_contribuinte, logradouro, municipio, uf) VALUES ('40506070000183', 'Rua do Lazer, 15', 'Aracaju', 'SE');
INSERT INTO nota_fiscal.endereco (cnpj_contribuinte, logradouro, municipio, uf) VALUES ('50607080000194', 'Rua da Feira, 73', 'Estância', 'SE');
INSERT INTO nota_fiscal.endereco (cnpj_contribuinte, logradouro, municipio, uf) VALUES ('60708090000105', 'Praça da Cultura, 10', 'Aracaju', 'SE');
INSERT INTO nota_fiscal.endereco (cnpj_contribuinte, logradouro, municipio, uf) VALUES ('70809010000116', 'Av. Barão de Maruim, 320', 'Aracaju', 'SE');
INSERT INTO nota_fiscal.endereco (cnpj_contribuinte, logradouro, municipio, uf) VALUES ('80900120000127', 'Rua Animal, 44', 'São Cristóvão', 'SE');
INSERT INTO nota_fiscal.endereco (cnpj_contribuinte, logradouro, municipio, uf) VALUES ('90010230000138', 'Shopping Riomar, loja 215', 'Aracaju', 'SE');
INSERT INTO nota_fiscal.endereco (cnpj_contribuinte, logradouro, municipio, uf) VALUES ('10112340000149', 'Av. Ivo do Prado, 600', 'Aracaju', 'SE');
INSERT INTO nota_fiscal.endereco (cnpj_contribuinte, logradouro, municipio, uf) VALUES ('11213141000150', 'Rua Itabaianinha, 52', 'Aracaju', 'SE');
INSERT INTO nota_fiscal.endereco (cnpj_contribuinte, logradouro, municipio, uf) VALUES ('21314151000161', 'Av. Francisco Porto, 900', 'Aracaju', 'SE');
INSERT INTO nota_fiscal.endereco (cnpj_contribuinte, logradouro, municipio, uf) VALUES ('31415161000172', 'Distrito Industrial, Galpão 8', 'Nossa S. Socorro', 'SE');
INSERT INTO nota_fiscal.endereco (cnpj_contribuinte, logradouro, municipio, uf) VALUES ('41516171000183', 'Rua das Flores, 120', 'Lagarto', 'SE');
INSERT INTO nota_fiscal.endereco (cnpj_contribuinte, logradouro, municipio, uf) VALUES ('51617181000194', 'Rod. BR-235, km 15', 'Itabaiana', 'SE');
INSERT INTO nota_fiscal.endereco (cnpj_contribuinte, logradouro, municipio, uf) VALUES ('61718191000105', 'Av. Augusto Franco, 1500', 'Aracaju', 'SE');
INSERT INTO nota_fiscal.endereco (cnpj_contribuinte, logradouro, municipio, uf) VALUES ('71819201000116', 'Praia de Atalaia, s/n', 'Aracaju', 'SE');
INSERT INTO nota_fiscal.endereco (cnpj_contribuinte, logradouro, municipio, uf) VALUES ('81920211000127', 'Rua Laranjeiras, 33', 'Aracaju', 'SE');
INSERT INTO nota_fiscal.endereco (cnpj_contribuinte, logradouro, municipio, uf) VALUES ('91021221000138', 'BR-101 Norte, km 98', 'Nossa S. Socorro', 'SE');
INSERT INTO nota_fiscal.endereco (cnpj_contribuinte, logradouro, municipio, uf) VALUES ('12132232000149', 'Rua Itaporanga, 77', 'Propriá', 'SE');
INSERT INTO nota_fiscal.endereco (cnpj_contribuinte, logradouro, municipio, uf) VALUES ('13233343000150', 'Av. Coelho e Campos, 400', 'Aracaju', 'SE');
INSERT INTO nota_fiscal.endereco (cnpj_contribuinte, logradouro, municipio, uf) VALUES ('14334454000161', 'Rua do Porto, 8', 'Neópolis', 'SE');
INSERT INTO nota_fiscal.endereco (cnpj_contribuinte, logradouro, municipio, uf) VALUES ('15435565000172', 'Rua das Rosas, 30', 'São Cristóvão', 'SE');
INSERT INTO nota_fiscal.endereco (cnpj_contribuinte, logradouro, municipio, uf) VALUES ('16536676000183', 'Av. Tancredo Neves, 200', 'Aracaju', 'SE');
INSERT INTO nota_fiscal.endereco (cnpj_contribuinte, logradouro, municipio, uf) VALUES ('17637787000194', 'Rod. SE-290, km 2', 'Tobias Barreto', 'SE');
INSERT INTO nota_fiscal.endereco (cnpj_contribuinte, logradouro, municipio, uf) VALUES ('18738898000105', 'Av. Industrial, 1100', 'Itabaiana', 'SE');
INSERT INTO nota_fiscal.endereco (cnpj_contribuinte, logradouro, municipio, uf) VALUES ('19839909000116', 'Rua Pacatuba, 55', 'Aracaju', 'SE');
INSERT INTO nota_fiscal.endereco (cnpj_contribuinte, logradouro, municipio, uf) VALUES ('20940010000127', 'Av. Gonçalo Rollemberg, 780', 'Aracaju', 'SE');
INSERT INTO nota_fiscal.endereco (cnpj_contribuinte, logradouro, municipio, uf) VALUES ('21041121000138', 'Rua Sergipe, 99', 'Lagarto', 'SE');
INSERT INTO nota_fiscal.endereco (cnpj_contribuinte, logradouro, municipio, uf) VALUES ('22142232000149', 'Rua dos Eventos, 500', 'Aracaju', 'SE');
INSERT INTO nota_fiscal.endereco (cnpj_contribuinte, logradouro, municipio, uf) VALUES ('23243343000150', 'Rua João Pessoa, 145', 'Estância', 'SE');
INSERT INTO nota_fiscal.endereco (cnpj_contribuinte, logradouro, municipio, uf) VALUES ('24344454000161', 'Av. Beira Mar, 890', 'Aracaju', 'SE');
INSERT INTO nota_fiscal.endereco (cnpj_contribuinte, logradouro, municipio, uf) VALUES ('25445565000172', 'Rua Marechal Deodoro, 22', 'Simão Dias', 'SE');
INSERT INTO nota_fiscal.endereco (cnpj_contribuinte, logradouro, municipio, uf) VALUES ('26546676000183', 'Av. Coletora, 3000', 'Itabaiana', 'SE');
INSERT INTO nota_fiscal.endereco (cnpj_contribuinte, logradouro, municipio, uf) VALUES ('27647787000194', 'Rua da Eletricidade, 67', 'Aracaju', 'SE');
INSERT INTO nota_fiscal.endereco (cnpj_contribuinte, logradouro, municipio, uf) VALUES ('28748898000105', 'Av. Pedro Valadares, 2200', 'Aracaju', 'SE');
INSERT INTO nota_fiscal.endereco (cnpj_contribuinte, logradouro, municipio, uf) VALUES ('29849909000116', 'Rua das Crianças, 18', 'Nossa S. Socorro', 'SE');
INSERT INTO nota_fiscal.endereco (cnpj_contribuinte, logradouro, municipio, uf) VALUES ('30950010000127', 'Av. Santos Dumont, 1400', 'Aracaju', 'SE');
INSERT INTO nota_fiscal.endereco (cnpj_contribuinte, logradouro, municipio, uf) VALUES ('31051121000138', 'Rua da Habilitação, 300', 'Itabaiana', 'SE');
INSERT INTO nota_fiscal.endereco (cnpj_contribuinte, logradouro, municipio, uf) VALUES ('32152232000149', 'Rua da Alimentação, 7', 'Propriá', 'SE');

COMMIT;

---------------------------------------------

/*
ALTER USER nota_fiscal QUOTA UNLIMITED ON USERS;

DROP TABLE nota_fiscal.endereco;
DROP TABLE nota_fiscal.danfe;
DROP TABLE nota_fiscal.contribuinte;
*/

---------------------------------------------

