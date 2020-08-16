# To Do

- Sorting is automatic in all the categories, and in the index. It should be specified.
- The karma is computed using the reactions only. The number of comments, and probably the reactions to the comments should be considered too.
- Unlike `created_at`, `updated_at` is read in the Python script, but not used in the markdown file (yet).
- CI is triggered after any `issues` or `issue_comment` event, which rebuilds the whole site after retrieving the full list of issues. Instead, it would be desirable to update the corresponding markdown file only (in some staging branch), and have the site itself updated periodically.
- Reactions do not trigger automatic updates.
- The body of the submissions (first comment in the issue) is currently unused in the site, only the metadata (first code block) is used. Ideally, the body would be shown as an expandable/collapsible `div`, without requiring JavaScript.
- materialdesignicons are currently loaded through a `script` tag. Instead, it would be desirable to add it as an npm dependency, and have it bundled.
