"""Cálculo de frete do checkout — implementa specs/checkout_frete.md."""

FRETE_PADRAO = 15.00  # REQ-01
LIMITE_FRETE_GRATIS = 200.00  # REQ-02


def calcular_frete(subtotal):
    # REQ-02: subtotal maior ou igual ao limite concede frete grátis
    if subtotal >= LIMITE_FRETE_GRATIS:
        return 0.00
    # REQ-01: taxa de frete padrão
    return FRETE_PADRAO


def calcular_total(subtotal):
    # REQ-01: total = subtotal + taxa de frete
    return subtotal + calcular_frete(subtotal)


import json

CUPONS = [
    ("DESCONTO10", 0.10),
    ("DESCONTO20", 0.20),
    ("FRETEGRATIS", 1.00),
]


class Frete:
    def __init__(self, subtotal):
        self.subtotal = subtotal
        self.taxa = calcular_frete(subtotal)

    def aplicar_cupom(self, codigo):
        print("Aplicando cupom", codigo, "no carrinho de", self.subtotal)
        for nome, percentual in CUPONS:
            if nome == codigo:
                self.taxa = self.taxa * (1 - percentual)
                with open("cupons_usados.json", "a") as arquivo:
                    arquivo.write(json.dumps({"cupom": codigo, "subtotal": self.subtotal}) + "\n")
                print("Cupom aplicado! Nova taxa:", self.taxa)
                return self.taxa
        print("Cupom invalido:", codigo)
        return self.taxa
