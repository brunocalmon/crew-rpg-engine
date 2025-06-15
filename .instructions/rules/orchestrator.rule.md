// Orchestrator Rule - Pseudocode

var current_state = input.current_state
var context = input.context
var next_state
var actions = []

switch (current_state) {
    case "init":
        next_state = "requirements"
        actions.append(RunRule("RequirementsIdentification"))
        goto END
    case "requirements":
        next_state = "documentation"
        actions.append(RunRule("Documentation"))
        goto END
    case "documentation":
        next_state = "planning"
        actions.append(RunRule("Planning"))
        goto END
    case "planning":
        next_state = "action_plan"
        actions.append(RunRule("ActionPlan"))
        goto END
    case "action_plan":
        next_state = "todolist"
        actions.append(RunRule("TodoList"))
        goto END
    case "todolist":
        next_state = "review"
        actions.append(WaitForUserReview())
        goto END
    case "review":
        if (UserApproved()) {
            next_state = "execute"
            actions.append(RunRule("ExecuteTodoList"))
        } else {
            next_state = "requirements"
            actions.append(RunRule("RequirementsIdentification"))
        }
        goto END
    case "execute":
        if (AllTasksCompleted()) {
            next_state = "done"
            actions.append(NotifyCompletion())
        } else {
            next_state = "error"
            actions.append(LogError("Tasks not completed"))
        }
        goto END
    default:
        next_state = "error"
        actions.append(LogError("Invalid state"))
}

END:
return {
    "current_state": current_state,
    "next_state": next_state,
    "actions": actions,
    "notes": ""
}
