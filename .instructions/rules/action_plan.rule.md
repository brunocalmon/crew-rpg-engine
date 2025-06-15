// ActionPlan Rule - Pseudocode

/*
Expected Output Template (Markdown):

# Action Plan

| Step | Responsible | Expected Result |
|------|-------------|----------------|
| <Step 1> | <Agent> | <Result> |
| <Step 2> | <Agent> | <Result> |
...
*/

var actions = []

for step in input.plan:
    var action = {
        "step": step,
        "responsible": AssignAgent(step),
        "expected_result": DefineExpectedResult(step)
    }
    actions.append(action)

function RenderActionPlanMarkdown(actions) {
    var md = "# Action Plan\n\n"
    md += "| Step | Responsible | Expected Result |\n"
    md += "|------|-------------|----------------|\n"
    for a in actions:
        md += "| " + a.step + " | " + a.responsible + " | " + a.expected_result + " |\n"
    return md
}

var output_file = "planning/documentation/action_plan{YYYY-MM-dd-hh-mm-ss}.md"
var markdown = RenderActionPlanMarkdown(actions)

WriteFile(output_file, markdown)

return {
    "output_file": output_file,
    "actions": actions
}
