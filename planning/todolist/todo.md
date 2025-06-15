# Todo List - Reestruturação e Modernização do Projeto Crew

**Descrição:**
Checklist para reestruturação e modernização do projeto Crew, visando alinhamento com as melhores práticas Python 2025, clareza de planejamento e facilidade de manutenção.

**Objetivo:**
Deixar o projeto organizado, moderno, fácil de rodar, testar e contribuir, com documentação e planejamento claros.

## Checklist

- [x] Mover `src/main` para `src/crew/` (adotando o nome do pacote principal como `crew`)
- [x] Atualizar todos os imports de `main` para `crew`
- [x] Ajustar `[project.scripts]` no `pyproject.toml` para `crew.main:main`
- [x] Atualizar `[tool.hatch.build.targets.wheel]` para `packages = ["src/crew"]`
- [x] Criar `planning/`, `planning/documentation/` e `planning/todolist/` (já realizado)
- [x] Documentar a estrutura e decisões em `planning/documentation/estrutura.md`
- [x] Criar checklist em `planning/todolist/todo.md` (já realizado)
- [x] Garantir que o projeto instala e executa com `uv pip install -e .` e `uv run crew-main` (agora funcionando com Python 3.12)
- [x] Criar novos testes mínimos em `tests/` (ignorando quaisquer existentes)
- [x] Atualizar `README.md` com instruções modernas
- [x] Organizar o código em packages bem definidos, seguindo padrões comuns de arquitetura em camadas

**Observação:**

- Todos os itens principais do checklist foram concluídos.
- O projeto está rodando com Python 3.12, ambiente isolado via uv, e dependências nativas resolvidas.
- README.md, estrutura, testes e documentação física estão atualizados e alinhados com as melhores práticas Python 2025.

**Obstáculos encontrados e solucionados:**
- Incompatibilidade do pacote regex (e dependências nativas) com Python 3.13: solucionado ao restringir o projeto para Python 3.12 no pyproject.toml e ambiente uv.
- Falha de build por falta do compilador Rust: solucionado com instalação do Rust via winget e ajuste do PATH.
- Ambiente virtual bloqueado (erro de permissão ao remover .venv): solucionado ao garantir que nenhum terminal estivesse usando o ambiente antes de recriar.
- Necessidade de alinhar toda a estrutura do projeto, documentação e scripts para práticas modernas: solucionado com reestruturação, checklist e atualização do README.
