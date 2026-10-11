from frete import calcular_frete, calcular_total


# REQ-01: taxa de frete padrão de R$ 15,00
def test_req01_taxa_padrao_abaixo_do_limite():
    assert calcular_frete(249.99) == 15.00


# REQ-01: total = subtotal + taxa de frete padrão
def test_req01_total_soma_frete_padrao_ao_subtotal():
    assert calcular_total(100.00) == 115.00


# REQ-02: subtotal igual ao limite concede frete grátis
def test_req02_frete_gratis_no_limite():
    assert calcular_frete(250.00) == 0.00


# REQ-02: subtotal acima do limite concede frete grátis
def test_req02_frete_gratis_acima_do_limite():
    assert calcular_frete(350.00) == 0.00


# REQ-02: com frete grátis o total é o próprio subtotal
def test_req02_total_sem_taxa_com_frete_gratis():
    assert calcular_total(250.00) == 250.00


# REQ-02: o limite antigo (R$ 200,00) deixa de conceder frete grátis
def test_req02_subtotal_200_paga_frete_padrao():
    assert calcular_frete(200.00) == 15.00
