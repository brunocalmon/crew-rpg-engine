# Plano de Ação

1. Refatoração da Estrutura
   - Renomear/mover `src/main` para `src/crew/`
   - Atualizar todos os imports de `main` para `crew`
   - Ajustar `pyproject.toml` para refletir o novo caminho do pacote
2. Configuração de Planejamento
   - Criar `planning/`, `planning/documentation/` e `planning/todolist/`
   - Documentar a estrutura e decisões em `planning/documentation/estrutura.md`
   - Criar checklist em `planning/todolist/todo.md`
3. Ajustes de Execução
   - Garantir que `[project.scripts]` aponte para `crew.main:main`
   - Testar execução com `uv run crew-main`
4. Testes
   - Criar ou mover testes para `tests/`
   - Garantir que `pytest` rode corretamente
5. Documentação
   - Atualizar `README.md` com instruções de uso, instalação e contribuição
