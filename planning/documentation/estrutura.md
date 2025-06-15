# Estrutura e Decisões do Projeto Crew

## Estrutura Atual

- Código principal: `src/crew/`
- Notebooks: `notebooks/`
- Testes: `tests/`
- Planejamento: `planning/` (com `documentation/` e `todolist/`)
- Configuração: `pyproject.toml`, `.env`, `README.md`

## Decisões Tomadas

- Adotado padrão moderno `src/crew/` para evitar conflitos de importação e facilitar manutenção.
- Nome do pacote principal definido como `crew`.
- Testes existentes ignorados, criados novos testes mínimos.
- Organização do código em packages bem definidos, seguindo arquitetura em camadas.
- Uso de ferramentas modernas: `uv`, `hatchling`, scripts via `[project.scripts]`.
- Documentação e planejamento versionados em `planning/`.
