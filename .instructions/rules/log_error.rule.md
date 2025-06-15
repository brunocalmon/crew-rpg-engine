// LogError Rule - Pseudocode

/*
Expected Output Template (Markdown):

# Error Log

- Error Message: <error>
- Log File: <file>
- Notified: <true|false>
*/

var error_message = input.error
var log_file = LogErrorToFile(error_message)
NotifyUser(error_message)
var notified = true

function RenderErrorLogMarkdown(error_message, log_file, notified) {
    var md = "# Error Log\n\n"
    md += "- Error Message: " + error_message + "\n"
    md += "- Log File: " + log_file + "\n"
    md += "- Notified: " + notified + "\n"
    return md
}

var output_file = "planning/logs/errors{YYYY-MM-dd-hh-mm-ss}.md"
var markdown = RenderErrorLogMarkdown(error_message, log_file, notified)

WriteFile(output_file, markdown)

return {
    "output_file": output_file,
    "error_message": error_message,
    "log_file": log_file,
    "notified": notified
}
