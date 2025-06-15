// RepoToTextImport Rule - Pseudocode

/*
If the folder dir-to-text/repo-to-text-output/ exists, always attempt to read the most recent file (by timestamp or filename order).
Assume the file is in YAML format, even if the extension is .dttc.
Parse the YAML content and extract all documentation, code, and artifact references.
Use this data to:
- Supplement or update the current documentation, requirements, planning, or action plan.
- Detect legacy or non-standard artifacts and suggest migration/merge to the new standard.
- Always log which file was read and what was imported.

Expected Output Template (Markdown):

# Repo-to-Text Import

- File read: <filename>
- Artifacts imported: <list>
- Actions taken: <list>
- Issues found: <list>
*/

if FolderExists("dir-to-text/repo-to-text-output/"):
    var files = ListFilesByTimestamp("dir-to-text/repo-to-text-output/")
    var latest_file = files[-1]
    var yaml_content = ParseYamlFile(latest_file)
    var artifacts = ExtractArtifacts(yaml_content)
    var actions_taken = []
    var issues = []
    // Supplement documentation, requirements, planning, etc.
    for artifact in artifacts:
        if IsLegacyOrNonStandard(artifact):
            issues.append("Legacy or non-standard artifact: " + artifact)
            actions_taken.append("Suggest migration/merge for " + artifact)
        else:
            actions_taken.append("Imported " + artifact)
    var output_file = "planning/documentation/repo_to_text_import{YYYY-MM-dd-hh-mm-ss}.md"
    var md = "# Repo-to-Text Import\n\n"
    md += "- File read: " + latest_file + "\n"
    md += "- Artifacts imported: " + artifacts.join(", ") + "\n"
    md += "- Actions taken: " + actions_taken.join(", ") + "\n"
    md += "- Issues found: " + issues.join(", ") + "\n"
    WriteFile(output_file, md)
    return {
        "output_file": output_file,
        "file_read": latest_file,
        "artifacts": artifacts,
        "actions_taken": actions_taken,
        "issues": issues
    }
else:
    return {
        "output_file": null,
        "file_read": null,
        "artifacts": [],
        "actions_taken": [],
        "issues": ["dir-to-text/repo-to-text-output/ folder not found"]
    }
