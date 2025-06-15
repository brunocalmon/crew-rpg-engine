import os
import json
import warnings
from datetime import datetime
from pathlib import Path
from dotenv import load_dotenv, find_dotenv

from crewai import Agent, Task, Crew, Process
from crew.gemini_llm import GeminiLLM
from crewai_tools import SerperDevTool

# === Load environment variables ===
load_dotenv(find_dotenv())
api_key = os.getenv("GEMINI_API_KEY")
serper_api_key = os.getenv("SERPER_API_KEY")
model_name = os.getenv("MODEL")

if not api_key or not serper_api_key:
    raise EnvironmentError("Missing GEMINI_API_KEY or SERPER_API_KEY in .env")

# === LLM Configuration ===
llm = GeminiLLM(
    model=model_name or "gemini-2.0-pro",
    api_key=api_key,
    temperature=0.7
)

# === Paths ===
base_path = Path("src/resources")
agent_sheet_path = base_path / "agents" / "agent_sheets.json"
user_sheet_path = base_path / "users" / "user_sheets.json"

# === Load agent and user sheets ===
with open(agent_sheet_path, "r", encoding="utf-8") as f:
    agent_sheets = json.load(f)

with open(user_sheet_path, "r", encoding="utf-8") as f:
    user_input = json.load(f)

# === Build Agents ===
def build_agent(key, goal, tools=None, allow_delegation=True):
    sheet = agent_sheets[key]
    backstory = (
        f"{sheet['background']}\n\n{sheet['motive']}\n\n"
        f"Physical Description: {json.dumps(sheet['physical_description'], indent=2)}\n"
        f"Attributes: {sheet['attributes']}\n"
        f"Skills: {sheet['skills']}\n"
        f"Equipment: {sheet['equipment']}\n"
        f"Traits: {sheet['features_and_traits']}"
    )
    return Agent(
        role=sheet["name"],
        goal=goal,
        backstory=backstory,
        tools=tools or [],
        allow_delegation=allow_delegation,
        verbose=True,
        llm=llm
    )

# === Tools ===
search_tool = SerperDevTool()

# === Context for all tasks ===
context_info = f"""
Visitor Name: {user_input['name']}
Race/Class/Level: {user_input['race']} / {user_input['class']} / Level {user_input['level']}
Appearance: {user_input['physical_features']}
Equipment: {user_input['equipment']}
Skills: {user_input['skills']}
Attributes: {user_input['attributes']}
Topic: {user_input['topic']}
"""

# === Agents ===
drunk_vampire = build_agent("Alaric", "Drink endlessly, avoid his past, and lead the crew in chaotic brilliance.")
ghoul = build_agent("Stitch", "Serve Alaric, de-escalate chaos, and protect the crew.", allow_delegation=False)
ravella = build_agent("Ravella", "Turn mysteries into melodies and spread truths via poetry.")
arkwin = build_agent("Arkwin", "Uncover the hidden history of blood magic and vampire legacy.", tools=[search_tool])
bellatrix = build_agent("Bellatrix", "Confirm the mystic authenticity of stories using forbidden arcana.")

# === Tasks ===
vampire_response = Task(
    name="drunken_response",
    description=f"Respond to Seraphine's statement about crimson sigils in a chaotic, emotional or humorous way.\n\n{context_info}",
    expected_output="Drunken rant or hidden truth blurted out emotionally.",
    agent=drunk_vampire,
    markdown=True
)

ghoul_intervention = Task(
    name="ghoul_response",
    description=f"Politely cover for Alaric if he becomes too aggressive or incoherent. Keep tension down.\n\n{context_info}",
    expected_output="Calm or sarcastic response.",
    agent=ghoul,
    context=[vampire_response],
    markdown=True
)

bard_poem = Task(
    name="bard_poem",
    description=f"Turn the visitor’s experience into a gothic or tragic melody.\n\n{context_info}",
    expected_output="A haunting stanza or poem.",
    agent=ravella,
    markdown=True
)

arkwin_search = Task(
    name="arkwin_lookup",
    description=f"Use internet lore to investigate the sigils seen by the visitor.\n\n{context_info}",
    expected_output="A historical note or mention of the Crimson Cathedral.",
    agent=arkwin,
    tools=[search_tool],
    markdown=True
)

bellatrix_check = Task(
    name="bellatrix_check",
    description=f"Magically confirm Arkwin’s finding. Interpret the mystical nature.\n\n{context_info}",
    expected_output="Arcane interpretation, whether prophetic or false memory.",
    agent=bellatrix,
    context=[arkwin_search],
    markdown=True
)

# === Interaction mechanics ===
def simulate_interaction_outcome(visitor_attr, vampire_attr):
    diff = visitor_attr["charisma"] - vampire_attr["wisdom"]
    if diff >= 5:
        return "peace_offer"
    elif diff >= 2:
        return "tense_truce"
    elif diff >= -2:
        return "power_struggle"
    else:
        return "threat_detected"

interaction_outcome = simulate_interaction_outcome(
    user_input["attributes"],
    agent_sheets["Alaric"]["attributes"]
)

interaction_descriptions = {
    "peace_offer": "Visitor shows clear respect and diplomacy. Alaric may embrace this alliance.",
    "tense_truce": "An uneasy peace settles, with suspicions.",
    "power_struggle": "A verbal or emotional challenge is felt. Decision needed.",
    "threat_detected": "Alaric senses dominance and reacts with defiance. Conflict may erupt."
}

resolve_or_escalate = Task(
    name="resolve_or_escalate",
    description=f"{interaction_descriptions[interaction_outcome]}\n\nAlaric must decide the crew's response.\n\n{context_info}",
    expected_output="A final ruling by Alaric: ally, dismiss, challenge or threaten the visitor.",
    agent=drunk_vampire,
    context=[vampire_response, ghoul_intervention, bard_poem, bellatrix_check],
    markdown=True
)

# === Crew Assembly ===
crew = Crew(
    agents=[ghoul, ravella, arkwin, bellatrix],
    tasks=[
        vampire_response,
        ghoul_intervention,
        bard_poem,
        arkwin_search,
        bellatrix_check,
        resolve_or_escalate
    ],
    process=Process.hierarchical,
    manager_agent=drunk_vampire,
    name="The Crimson Revelry",
    description="A vampire and his cursed companions confront visitors who awaken memories and danger."
)

# === File logging setup ===
timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
file_prefix = f"crimson_revelry_session_{timestamp}"
verbose_path = Path("outputs/verbose")
results_path = Path("outputs/results")
verbose_path.mkdir(parents=True, exist_ok=True)
results_path.mkdir(parents=True, exist_ok=True)

# === Main execution ===
def main():
    warnings.filterwarnings("ignore")

    crew_result = crew.kickoff(inputs={"user": user_input["name"], "topic": user_input["topic"]})

    # === Save verbose (each task raw output concatenated)
    verbose_file = verbose_path / f"{file_prefix}.md"
    with open(verbose_file, "w", encoding="utf-8") as f:
        for task_output in crew_result.tasks_output:
            f.write(f"## Task: {task_output.name}\n")
            f.write(task_output.raw.strip())
            f.write("\n\n---\n\n")

    # === Save only final decision/result
    result_file = results_path / f"{file_prefix}.md"
    with open(result_file, "w", encoding="utf-8") as f:
        f.write(f"# Final Decision by Alaric\n\n{crew_result.raw.strip()}")

    print("\n=== FINAL RESULT ===\n")
    print(crew_result.raw)
    print(f"\nSaved logs to:\n- {verbose_file}\n- {result_file}")


if __name__ == "__main__":
    main()
