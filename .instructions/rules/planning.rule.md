// Planning Rule - Pseudocode

/*
Expected Output Template (Markdown):

# Project Planning

## Plan Steps
- <Step 1>
- <Step 2>
...
*/

var plan = []

for req in input.requirements:
    step = DefineStepForRequirement(req)
    plan.append(step)

function RenderPlanningMarkdown(plan) {
    var md = "# Project Planning\n\n"
    md += "## Plan Steps\n"
    for s in plan:
        md += "- " + s + "\n"
    return md
}

var output_file = "planning/documentation/plan{YYYY-MM-dd-hh-mm-ss}.md"
var markdown = RenderPlanningMarkdown(plan)

WriteFile(output_file, markdown)

return {
    "output_file": output_file,
    "plan": plan
}
