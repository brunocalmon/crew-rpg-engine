// TodoList Rule - Pseudocode

/*
Expected Output Template (Markdown):

# Todo List - <Project or Goal Title>

**Descrição:**
<Descrição detalhada>

**Objetivo:**
<Objetivo claro e conciso>

## Checklist
- [ ] <Task 1>
- [ ] <Task 2>
...

**Observação:**
<Observações gerais>

**Obstáculos encontrados e solucionados:**
- <Obstáculo 1: solução>
- <Obstáculo 2: solução>
*/

var description = input.description
var objective = input.objective
var tasks = []
var observations = input.observations
var obstacles = input.obstacles

for action in input.actions:
    var task = {"task": action.step, "status": "pending"}
    tasks.append(task)

function RenderTodoMarkdown(description, objective, tasks, observations, obstacles) {
    var md = "# Todo List - " + input.title + "\n\n"
    md += "**Descrição:**\n" + description + "\n\n"
    md += "**Objetivo:**\n" + objective + "\n\n"
    md += "## Checklist\n"
    for t in tasks:
        if t.status == "done":
            md += "- [x] " + t.task + "\n"
        else:
            md += "- [ ] " + t.task + "\n"
    md += "\n**Observação:**\n" + observations + "\n\n"
    md += "**Obstáculos encontrados e solucionados:**\n"
    for o in obstacles:
        md += "- " + o + "\n"
    return md
}

var output_file = "planning/todolist/{YYYY-MM-dd}/todo{YYYY-MM-dd-hh-mm-ss}.md"
var markdown = RenderTodoMarkdown(description, objective, tasks, observations, obstacles)

WriteFile(output_file, markdown)

return {
    "output_file": output_file,
    "tasks": tasks
}
