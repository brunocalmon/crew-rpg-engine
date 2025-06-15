// NotifyCompletion Rule - Pseudocode

/*
Expected Output Template (Markdown):

# Completion Notification

- Completed: <true|false>
- Archived Files:
  - <file1>
  - <file2>
...
- Notification: <message>
*/

if AllTasksDone():
    var archived_files = ArchiveDocumentation()
    var notification = "Project workflow complete."
    var completed = true
else:
    var archived_files = []
    var notification = "Tasks incomplete."
    var completed = false

function RenderCompletionMarkdown(completed, archived_files, notification) {
    var md = "# Completion Notification\n\n"
    md += "- Completed: " + completed + "\n"
    md += "- Archived Files:\n"
    for f in archived_files:
        md += "  - " + f + "\n"
    md += "- Notification: " + notification + "\n"
    return md
}

var output_file = "planning/documentation/completion{YYYY-MM-dd-hh-mm-ss}.md"
var markdown = RenderCompletionMarkdown(completed, archived_files, notification)

WriteFile(output_file, markdown)

return {
    "output_file": output_file,
    "completed": completed,
    "archived_files": archived_files,
    "notification": notification
}
