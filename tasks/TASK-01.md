# TASK-01 — Cálculo de frete padrão e frete grátis por valor

## Contexto fornecido ao agente (isolamento estrito)

Apenas estes três arquivos; nunca o projeto inteiro:

- `tasks/TASK-01.md`
- `specs/checkout_frete.md`
- `constitution.md`

## Escopo (tamanho mínimo)

- Calcular a taxa de frete padrão e o valor total do carrinho (REQ-01).
- Conceder frete grátis por valor do subtotal (REQ-02).

Fora do escopo: cupons, regiões, persistência, logs, validações não descritas na spec.

## Entregáveis

- `tests/test_frete.py` — suíte pytest cobrindo REQ-01 e REQ-02 (escrita antes do código).
- `src/frete.py` — implementação mínima para a suíte passar.

## Rastreabilidade

Cada teste e cada trecho de código deve referenciar a cláusula que atende (`REQ-01`, `REQ-02`).

## Critério de aceite

`pytest` com 100% de aprovação e nenhuma linha de código sem cláusula EARS correspondente.
