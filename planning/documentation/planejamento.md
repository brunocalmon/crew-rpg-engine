# Planejamento

- Refatorar a estrutura do projeto para:
  - Mover `src/main` para `src/crew/`
  - Atualizar todos os imports de `main` para `crew`
  - Ajustar `pyproject.toml` para refletir o novo caminho do pacote
- Criar a pasta `planning/` com subpastas `documentation/` e `todolist/`
- Documentar o racional da estrutura e as decisões tomadas em `planning/documentation/estrutura.md`
- Criar um checklist claro e objetivo em `planning/todolist/todo.md`
- Garantir que o projeto seja instalável e executável via `uv` e scripts definidos
- Atualizar ou criar testes mínimos em `tests/`
- Instruir sobre como rodar, testar e contribuir com o projeto
