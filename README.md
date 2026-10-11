# Lab 6 — Implementação Dirigida por Agente (SDD) e Revisão Multidimensional

Modelagem de Sistemas — cálculo de frete do checkout, guiado por especificação EARS e TDD.

| Arquivo | Papel |
|---|---|
| `constitution.md` | Princípios invioláveis do projeto |
| `specs/checkout_frete.md` | Especificação EARS (fonte única da verdade) |
| `tasks/TASK-01.md` | Task atômica executada pelo agente |
| `tests/test_frete.py` | Suíte pytest |
| `src/frete.py` | Implementação |
| `audit_report.md` | Matriz de rastreabilidade e passe multidimensional |

## Como rodar

```
pip install pytest
pytest
```

## Histórico (um commit por etapa)

1. Setup: constituição, spec e task.
2. Exercício 1 — testes primeiro (Red), depois implementação mínima (Green).
3. Exercício 2 — prompt ambíguo de cupom, auditoria de drift e remoção do código sem spec.
4. Exercício 3 — REQ-02 passa a R$ 250,00: spec, testes e código no mesmo commit.
