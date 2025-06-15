# Use Instructions

To execute the workflow, use the `orchestrator.rule.md` file as the entry point.

## How to Use

1. **Start with the Orchestrator Rule:**
   - Open `.instructions/rules/orchestrator.rule.md`.
   - The orchestrator pseudocode will determine the current state, next state, and which rule to execute next.

2. **Follow the State Machine:**
   - For each state, open the corresponding rule file (e.g., `requirements_identification.rule.md`, `documentation.rule.md`, etc.).
   - Execute the actions as described in the pseudocode.
   - Update the outputs and files as specified by each rule's template.

3. **State Tracking:**
   - Always record the current state and outputs in a log or state file if automating.
   - After each rule execution, return to the orchestrator to determine the next step.

4. **Special Integration:**
   - If the state requires, use `repo_to_text_import.rule.md` to supplement or migrate legacy artifacts.

## Example Flow

- Start: `init` → Orchestrator → `requirements` → RequirementsIdentification Rule
- Continue: `documentation` → Documentation Rule
- ...
- At each step, the orchestrator tells you which rule to open and execute next.

## Automation

- For full automation, implement a script or agent that reads the orchestrator pseudocode, tracks state, and calls each rule in sequence, updating files as per the templates.

---

**Summary:**
- The orchestrator is the single source of truth for workflow state and next actions.
- Always return to the orchestrator after executing a rule.
- All rule files are in `.instructions/rules/` and are referenced by the orchestrator.
