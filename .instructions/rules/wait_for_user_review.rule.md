// WaitForUserReview Rule - Pseudocode

/*
Expected Output Template (Markdown):

# User Review

- User Approved: <true|false>
- Feedback: <feedback text>
- Next State: <execute|requirements>
*/

var user_approved = WaitForApproval()
var feedback = ""
var next_state

if user_approved == true:
    next_state = "execute"
else:
    feedback = GetUserFeedback()
    next_state = "requirements"

function RenderUserReviewMarkdown(user_approved, feedback, next_state) {
    var md = "# User Review\n\n"
    md += "- User Approved: " + user_approved + "\n"
    md += "- Feedback: " + feedback + "\n"
    md += "- Next State: " + next_state + "\n"
    return md
}

var output_file = "planning/documentation/user_review{YYYY-MM-dd-hh-mm-ss}.md"
var markdown = RenderUserReviewMarkdown(user_approved, feedback, next_state)

WriteFile(output_file, markdown)

return {
    "output_file": output_file,
    "user_approved": user_approved,
    "feedback": feedback,
    "next_state": next_state
}
