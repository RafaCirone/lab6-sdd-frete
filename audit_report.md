# Relatório de Auditoria — Drift e Revisão Multidimensional

Escopo: `src/frete.py` e `tests/test_frete.py` contra `specs/checkout_frete.md` e `constitution.md`.

## 1. Auditoria do commit `c8a42da` (após o prompt ambíguo)

Prompt injetado: *"Implemente a funcionalidade de aplicação de cupom de desconto 'DESCONTO10' para a classe de frete."*

### Matriz de rastreabilidade

| Cláusula EARS | Status | Teste Coberto | Arquivo:Linha |
|---|---|---|---|
| REQ-01 (Padrão) | Sim | test_frete.py:5, test_frete.py:10 | frete.py:12, frete.py:17 |
| REQ-02 (Grátis) | Sim | test_frete.py:15, test_frete.py:20, test_frete.py:25 | frete.py:9 |
| CUPOM (Sem Spec) | **DRIFT DETECTADO** | Nenhum | frete.py:20-44 |

### Achados

| # | Tipo | Arquivo:Linha | Descrição |
|---|---|---|---|
| 1 | Sobre-implementação | frete.py:29-44 | Classe `Frete` e `aplicar_cupom` sem cláusula EARS. A spec não define cupons. |
| 2 | Sobre-implementação | frete.py:24-25 | Cupons `DESCONTO20` e `FRETEGRATIS` que nem o prompt pediu. |
| 3 | Sobre-implementação | frete.py:39-40 | Persistência não solicitada em `cupons_usados.json`. |
| 4 | Sobre-implementação | frete.py:35, 41, 43 | Logs de console via `print`, sem padronização. |
| 5 | Sem cobertura | frete.py:20-44 | Nenhum teste exercita o código de cupom; a suíte continua verde e não denuncia o desvio. |

### Passe de revisão multidimensional

| Dimensão | Pergunta | Resultado | Evidência |
|---|---|---|---|
| Arquitetura | Respeita a `constitution.md` ou importou lib desnecessária? | Reprovado | `import json` (frete.py:20) só serve à persistência não pedida; viola as regras 2 e 3. Import no meio do arquivo. |
| Performance | Existem loops desnecessários no cálculo? | Reprovado | Busca linear em lista de tuplas (frete.py:36) e escrita em disco a cada cupom aplicado (frete.py:39). |
| Segurança | Há print de dados sensíveis ou falta de validação? | Reprovado | Código do cupom e subtotal do cliente impressos no console (frete.py:35) e gravados em arquivo sem controle (frete.py:40). |
| Observabilidade | O código é legível e depurável? | Reprovado | `print` sem nível nem formato; o bloco de cupom não referencia nenhuma cláusula. |

### Decisão (human-in-the-loop)

**Rejeitado.** Ação de correção mandatória: remover todo o código de cupom sem especificação, restaurando o alinhamento de 100% com a spec. Cupom só volta ao código depois de existir cláusula EARS para ele.

## 2. Auditoria após a correção

O bloco `frete.py:20-44` foi removido. `src/frete.py` voltou a conter apenas o que REQ-01 e REQ-02 exigem.

### Matriz de rastreabilidade

| Cláusula EARS | Status | Teste Coberto | Arquivo:Linha |
|---|---|---|---|
| REQ-01 (Padrão) | Sim | test_frete.py:5, test_frete.py:10 | frete.py:12, frete.py:17 |
| REQ-02 (Grátis) | Sim | test_frete.py:15, test_frete.py:20, test_frete.py:25 | frete.py:9 |
| CUPOM (Sem Spec) | Removido | — | — |

Código sem cláusula correspondente: nenhum. Cláusulas sem código ou sem teste: nenhuma.

### Passe de revisão multidimensional

| Dimensão | Resultado | Evidência |
|---|---|---|
| Arquitetura | Aprovado | Nenhum import; apenas biblioteca padrão implícita. Duas funções puras. |
| Performance | Aprovado | Uma comparação e uma soma por chamada; sem loops nem E/S. |
| Segurança | Aprovado com ressalva | Nenhum `print` nem gravação de dados. Ressalva abaixo. |
| Observabilidade | Aprovado | Constantes nomeadas e comentários apontando para REQ-01 e REQ-02. |

### Ressalvas encaminhadas ao Product Owner (não implementadas)

Não há cláusula EARS para os pontos abaixo; implementá-los agora seria sobre-implementação.

1. Subtotal negativo ou não numérico não é validado. Requer cláusula de comportamento indesejado na spec.
2. Valores monetários em `float`. Os casos da spec são exatos, mas somas com centavos podem acumular erro de arredondamento; avaliar `Decimal` em cláusula futura.

### Decisão

**Aprovado.** Sem drift e sem sobre-implementação.
