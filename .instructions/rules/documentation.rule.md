// Documentation Rule - Pseudocode

/*
Expected Output Template (Markdown):

# Project Documentation

## Summary
<summary>

## Legacy Documentation Analysis
- Legacy files detected: <list>
- Issues found: <list>
- Migration/merge suggestions: <list>
*/

// Step 1: Detect legacy or non-standard documentation
var legacy_files = DetectLegacyDocumentationFiles()
var issues = []
var migration_suggestions = []

for file in legacy_files:
    if NotInStandardFormat(file):
        issues.append("Non-standard format: " + file)
        migration_suggestions.append("Migrate or merge " + file + " to standard documentation.")
    if IsOutdated(file):
        issues.append("Outdated documentation: " + file)
        migration_suggestions.append("Update or archive " + file)

// Step 2: Generate summary as usual
var summary = input.summary

function RenderDocumentationMarkdown(summary, legacy_files, issues, migration_suggestions) {
    var md = "# Project Documentation\n\n"
    md += "## Summary\n"
    md += summary + "\n\n"
    md += "## Legacy Documentation Analysis\n"
    md += "- Legacy files detected: " + legacy_files.join(", ") + "\n"
    md += "- Issues found: " + issues.join(", ") + "\n"
    md += "- Migration/merge suggestions: " + migration_suggestions.join(", ") + "\n"
    return md
}

var output_file = "planning/documentation/structure{YYYY-MM-dd-hh-mm-ss}.md"
var markdown = RenderDocumentationMarkdown(summary, legacy_files, issues, migration_suggestions)

WriteFile(output_file, markdown)

return {
    "output_file": output_file,
    "summary": summary,
    "legacy_files": legacy_files,
    "issues": issues,
    "migration_suggestions": migration_suggestions
}
