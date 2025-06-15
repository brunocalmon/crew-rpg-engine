// RequirementsIdentification Rule - Pseudocode

/*
Expected Output Template (Markdown):

# Requirements Identification

## Requirements
- <Requirement 1>
- <Requirement 2>
...

## Open Questions
- <Question 1>
- <Question 2>
...
*/

var requirements = []
var questions = []

for item in context.project_structure:
    if IsRequirement(item):
        requirements.append(item)
for request in context.user_requests:
    if IsRequirement(request):
        requirements.append(request)
for item in context:
    if IsOpenQuestion(item):
        questions.append(item)

function RenderRequirementsMarkdown(requirements, questions) {
    var md = "# Requirements Identification\n\n"
    md += "## Requirements\n"
    for r in requirements:
        md += "- " + r + "\n"
    md += "\n## Open Questions\n"
    for q in questions:
        md += "- " + q + "\n"
    return md
}

var output_file = "planning/documentation/requirements{YYYY-MM-dd-hh-mm-ss}.md"
var markdown = RenderRequirementsMarkdown(requirements, questions)

WriteFile(output_file, markdown)

return {
    "output_file": output_file,
    "requirements": requirements,
    "questions": questions
}
