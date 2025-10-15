---
allowed-tools: Read, Task, Bash(mem8:*), Bash(gh:*), Bash(git:*)
description: Conduct comprehensive codebase research by spawning parallel subagents
---

# Research Codebase

You are tasked with conducting comprehensive research across the codebase to answer user questions by spawning parallel subagents and synthesizing their findings.

## Initial Setup:

When this command is invoked, respond with:
```
I'm ready to research the codebase. Please provide your research question or area of interest, and I'll analyze it thoroughly by exploring relevant components and connections.
```

Then wait for the user's research query.

## Steps to follow after receiving the research query:

1. **Read any directly mentioned files first:**
   - If the user mentions specific files (tickets, docs, JSON), read them FULLY first
   - **IMPORTANT**: Use the Read tool WITHOUT limit/offset parameters to read entire files
   - **CRITICAL**: Read these files yourself in the main context before spawning any subagent tasks
   - This ensures you have full context before decomposing the research

2. **Analyze and decompose the research question:**
   - Break down the user's query into composable research areas
   - Take time to ultrathink about the underlying patterns, connections, and architectural implications the user might be seeking
   - Identify specific components, patterns, or concepts to investigate
   - Create a research plan using TodoWrite to track all subtasks
   - Consider which directories, files, or architectural patterns are relevant

3. **Spawn parallel subagent tasks for comprehensive research:**
   - Create multiple subagent tasks to research different aspects concurrently
   - We now have specialized agents that know how to do specific research tasks:

   **For codebase research:**
   - Use the **codebase-locator** agent to find WHERE files and components live
   - Use the **codebase-analyzer** agent to understand HOW specific code works
   - Use the **codebase-pattern-finder** agent if you need examples of similar implementations

   **For memory directory:**
   - Use the **memory-locator** agent to discover what documents exist about the topic
   - Use the **memory-analyzer** agent to extract key insights from specific documents (only the most relevant ones)

   **For web research (only if user explicitly asks):**
   - Use the **web-search-researcher** agent for external documentation and resources
   - IF you use web-research agents, instruct them to return LINKS with their findings, and please INCLUDE those links in your final report

   **For GitHub issues (if relevant):**
   - Use `gh issue view {number}` to get full details of a specific issue
   - Use `gh issue list --search "query"` to find related issues or historical context

   The key is to use these agents intelligently:
   - Start with locator agents to find what exists
   - Then use analyzer agents on the most promising findings
   - Run multiple agents in parallel when they're searching for different things
   - Each agent knows its job - just tell it what you're looking for
   - Don't write detailed prompts about HOW to search - the agents already know

4. **Wait for all subagents to complete and synthesize findings:**
   - IMPORTANT: Wait for ALL subagent tasks to complete before proceeding
   - Compile all subagent results (both codebase and memory findings)
   - Prioritize live codebase findings as primary source of truth
   - Use memory/ findings as supplementary historical context
   - Connect findings across different components
   - Include specific file paths and line numbers for reference
   - Verify all memory/ paths are correct using flat structure (memory/plans/, memory/research/, etc.)
   - Highlight patterns, connections, and architectural decisions
   - Answer the user's specific questions with concrete evidence

5. **Gather metadata for the research document:**
   - **IMPORTANT**: Use the mem8 CLI to generate proper metadata. DO NOT manually gather git information.
   - Run the command with the user's actual research question/topic:
     ```bash
     mem8 metadata research "the user's actual question here" --format json
     ```
   - **Example**: If user asks "How does auth work?", run: `mem8 metadata research "How does auth work?" --format json`
   - This will output JSON with all required fields including a **slug** field for the filename
   - Parse the JSON to extract the `slug` field for use in the filename
   - **Note**: The topic argument is optional and defaults to "research" if omitted, but it's better to use the actual user question
   - Store this output to use in the next step
   - **Filename format**: `memory/research/YYYY-MM-DD_HH-MM-SS_{slug}.md`
     - Extract timestamp from the `date` field: parse ISO format and convert to `YYYY-MM-DD_HH-MM-SS`
     - Use the `slug` field directly from the metadata JSON
     - Example: `2025-10-15_12-15-24_memory-directory-documentation.md`

6. **Generate research document:**
   - **CRITICAL**: Use the metadata from step 5 to generate both frontmatter and filename
   - Get frontmatter by running: `mem8 metadata research "topic" --format frontmatter`
   - DO NOT manually run git commands or gather metadata yourself
   - Structure the document with the YAML frontmatter, followed by content:
     ```markdown
     ---
     date: [Current date and time with timezone in ISO format]
     researcher: [Researcher name from memory status]
     git_commit: [Current commit hash]
     branch: [Current branch name]
     repository: [Repository name]
     topic: "[User's Question/Topic]"
     slug: [URL-safe slug from metadata]
     tags: [research, codebase, relevant-component-names]
     status: complete
     last_updated: [Current date in YYYY-MM-DD format]
     last_updated_by: [Researcher name]
     ---

     # Research: [User's Question/Topic]

     **Date**: [Current date and time with timezone from step 4]
     **Researcher**: [Researcher name from memory status]
     **Git Commit**: [Current commit hash from step 4]
     **Branch**: [Current branch name from step 4]
     **Repository**: [Repository name]

     ## Research Question
     [Original user query]

     ## Summary
     [Hi#level findings answering the user's question]

     ## Detailed Findings

     ### [Component/Area 1]
     - Finding with reference ([file.ext:line](link))
     - Connection to other components
     - Implementation details

     ### [Component/Area 2]
     ...

     ## Code References
     - `path/to/file.py:123` - Description of what's there
     - `another/file.ts:45-67` - Description of the code block

     ## Architecture Insights
     [Patterns, conventions, and design decisions discovered]

     ## Historical Context (from memory/)
     [Relevant insights from memory/ directory with references]
     - `memory/decisions/something.md` - Historical decision about X
     - `memory/docs/notes.md` - Past exploration of Y
     Note: Paths exclude "searchable/" even if found there

     ## Related Research
     [Links to other research documents in memory/research/]

     ## Open Questions
     [Any areas that need further investigation]
     ```

7. **Add GitHub permalinks (if applicable):**
   - Check if on main branch or if commit is pushed: `git branch --show-current` and `git status`
   - If on main/master or pushed, generate GitHub permalinks:
     - Get repo info: `gh repo view --json owner,name`
     - Create permalinks: `https://github.com/{owner}/{repo}/blob/{commit}/{file}#L{line}`
   - Replace local file references with permalinks in the document

8. **Sync and present findings:**
   - Run `mem8 sync` to sync the memory directory (if configured with git sync)
   - Present a concise summary of findings to the user
   - Include key file references for easy navigation
   - Ask if they have follow-up questions or need clarification

9. **Handle follow-up questions:**
   - If the user has follow-up questions, append to the same research document
   - Update the frontmatter fields `last_updated` and `last_updated_by` to reflect the update
   - Add `last_updated_note: "Added follow-up research for [brief description]"` to frontmatter
   - Add a new section: `## Follow-up Research [timestamp]`
   - Spawn new subagents as needed for additional investigation
   - Continue updating the document and syncing

## Important notes:
- **ALWAYS use `mem8 metadata research` command** - NEVER manually gather git metadata
- **Use the slug from metadata JSON** - NEVER make up your own filename slug
- **Filename format**: `YYYY-MM-DD_HH-MM-SS_{slug}.md` where slug comes from `mem8 metadata research --format json`
- **Sorting**: Files use ISO date format (YYYY-MM-DD) which sorts chronologically
  - Ascending sort (A-Z, default): Oldest files first
  - Descending sort (Z-A): Newest files first ← **Recommended**
  - In VS Code: Click the column header to toggle sort order
  - Or sort by "Modified" date descending for most recent work
- Always use parallel subagent tasks to maximize efficiency and minimize context usage
- Always run fresh codebase research - never rely solely on existing research documents
- The memory/ directory provides historical context to supplement live findings
- Focus on finding concrete file paths and line numbers for developer reference
- Research documents should be self-contained with all necessary context
- Each subagent prompt should be specific and focused on read-only operations
- Consider cross-component connections and architectural patterns
- Include temporal context (when the research was conducted)
- Link to GitHub when possible for permanent references
- Keep the main agent focused on synthesis, not deep file reading
- Encourage subagents to find examples and usage patterns, not just definitions
- Explore all of memory/ directory, not just research subdirectory
- **File reading**: Always read mentioned files FULLY (no limit/offset) before spawning subagent tasks
- **Critical ordering**: Follow the numbered steps exactly
  - ALWAYS read mentioned files first before spawning subagent tasks (step 1)
  - ALWAYS wait for all subagents to complete before synthesizing (step 4)
  - ALWAYS gather metadata before writing the document (step 5 before step 6)
  - NEVER write the research document with placeholder values
- **Path handling**: The memory/searchable/ directory contains hard links for searching
  - Always document paths by removing ONLY "searchable/" - preserve all other subdirectories
  - Examples of correct transformations:
    - `memory/searchable/docs/notes.md` → `memory/docs/notes.md`
    - `memory/searchable/prs/123.md` → `memory/prs/123.md`
    - `memory/searchable/research/auth.md` → `memory/research/auth.md`
  - NEVER modify the subdirectory structure - preserve the exact paths found
  - This ensures paths are correct for editing and navigation
- **Frontmatter consistency**:
  - Always include frontmatter at the beginning of research documents
  - Keep frontmatter fields consistent across all research documents
  - Update frontmatter when adding follow-up research
  - Use snake_case for multi-word field names (e.g., `last_updated`, `git_commit`)
  - Tags should be relevant to the research topic and components studied
