# Levantamento de Requisitos e Questionamentos

## Requisitos Encontrados
- Estrutura do projeto deve seguir o padrão moderno `src/crew/` para código de produção.
- Notebooks devem ficar em `notebooks/`.
- Testes automatizados devem ficar em `tests/`.
- Adicionar uma pasta `planning/` contendo `documentation/` e `todolist/`.
- O projeto deve ser configurado para rodar scripts via `[project.scripts]` no `pyproject.toml`.
- Utilizar ferramentas modernas como `uv` e `hatchling`.
- O código deve ser facilmente executável e testável via comandos modernos.
- Documentação e planejamento devem ser claros e versionados.

## Questionamentos
1. O nome do pacote principal pode ser alterado para `crew` (em vez de `main`)?
    - sim
2. Há arquivos de documentação já existentes que devem ser movidos para `planning/documentation/`? Se sim, quais?
    - não
3. Algum conteúdo específico deve ser iniciado em `planning/documentation/` ou ficará vazio por ora?
    - isso é dinamico e você acabou de fazer.
4. Os testes já existentes devem ser migrados para `tests/` ou devem ser criados exemplos mínimos?
    ignore os tests existentes (acho que não há), crie novos minimos.
5. Alguma convenção específica para nomes de arquivos ou scripts além do padrão sugerido?
    Use os padrões comuns em arquiteturas de camadas, já será o suficiente, separe em packages bem definidos.