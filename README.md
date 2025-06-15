# Crew

A narrative-driven interactive AI system inspired by Dungeons & Dragons. This project simulates dynamic conversations between a vampire-led crew of agents and user-defined visitors using Gemini LLM, structured agent sheets, and a detailed logging system in Markdown.

## Project Structure

```

Crew/
├── src/crew/                      # Main application logic
│   ├── main.py                    # Entry point for execution
│   └── gemini\_llm.py              # Gemini LLM integration
├── src/resources/
│   ├── agents/agent\_sheets.json   # Agent character sheets (D\&D style)
│   └── users/user\_sheet.json      # Visitor/user character sheet
├── verbose/                       # Full conversation logs in Markdown
├── results/                       # Final outcome of each interaction
├── tests/                         # Unit tests
├── README.md
└── pyproject.toml

````

## Requirements

- Python 3.12+
- [uv](https://github.com/astral-sh/uv) installed
- Environment variables:
  - `GEMINI_API_KEY`
  - `SERPER_API_KEY`

## Installation

```bash
uv venv --python=3.12 .venv
.venv/Scripts/activate  # or source .venv/bin/activate
uv pip install -e .
````

## Running

```bash
uv run crew-main
```

This will:

* Load detailed agent sheets from `agent_sheets.json`
* Load a visitor sheet from `user_sheet.json`
* Simulate dialogue between the agents and the visitor
* Save:

  * Full dialogue log in Markdown: `verbose/<timestamp>.md`
  * Final result/decision by Alaric in `results/<timestamp>.md`

## Logging Output

| Type       | Format | Description                                    |
| ---------- | ------ | ---------------------------------------------- |
| `verbose/` | `.md`  | Full interaction log (all agents and messages) |
| `results/` | `.md`  | Final result (Alaric's ruling/decision)        |

Both logs are timestamped and versioned automatically.

## Narrative Engine

* Agents are defined like D\&D characters:

  * Attributes (STR, DEX, etc.)
  * Skills and Equipment
  * Traits, goals, and backstories
* Users (visitors) are defined through `user_sheet.json`
* Interactions are governed by logic such as:

  * Attribute checks (e.g., charisma vs. wisdom)
  * Possible outcomes: alliance, tension, challenge, or threat
* Alaric, the drunken vampire, is always the crew’s leader and final voice

## Adding Characters

* Add new crew members to: `src/resources/agents/agent_sheets.json`
* Add new visitors to: `src/resources/users/user_sheet.json`

## Testing

```bash
uv pip install pytest
pytest
```

## License

MIT