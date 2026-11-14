# Evaluating the skills

The scenarios in [scenarios.json](scenarios.json) are behavioral prompts and acceptance criteria. They are not automated model evaluations, and their presence does not mean they passed.

## Run a focused evaluation

Use an isolated synthetic Appmost project and the exact candidate skill files. Record the skill commit, host/tool availability, app source, renderer/context and the user's brief. Do not give an evaluating agent the expected answer or a suspected fix before it attempts the task.

Run the relevant scenarios, inspect actual tool calls and final artifacts, and grade the observable outcome. For design, inspect the complete app page at readable size and compare measurements where available. For release safety, use synthetic read/prepare/error transcripts or a supported isolated environment; never start a real build, upload or release just to test a skill.

Compare the same task with and without the skill when practical. Measure MCP calls, invalid edits, unnecessary catalog/document reads, correction rounds and the final useful result. Fewer calls alone do not outweigh worse visuals, lost work or missing checks.

## Grade outcomes

Score each relevant dimension 0 (fails), 1 (partly meets) or 2 (meets): task completion, tool selection, source/concurrency handling, native behavior, composition/readability, geometry, adaptation and evidence honesty. A lost edit, unauthorized external action, exposed private material or falsely claimed verification is a blocking failure regardless of the average.

Keep actual results and raw project evidence private when they contain account/customer material. A shareable result should use synthetic data and state exactly which tests ran. Unavailable rendering or provider access must remain unverified.

## Improve from feedback

Capture a concrete observation and its artifact before writing a new rule. Classify the cause: missing skill guidance, wrong activation, a confusing reference, a tool gap, an ignored instruction, or a runtime defect. Fix the appropriate layer.

Add a reusable instruction only when it changes a future decision. Put nuanced examples and component-specific details in a focused reference; keep SKILL.md as the short workflow. Preserve useful exceptions. Retest the original case and one nearby case so that a fix does not make every app look the same.

Do not turn every personal preference into a universal platform rule. Identify package preferences, verified Appmost contracts and external platform guidance clearly. External Apple skills can supplement a task when available; these skills must remain usable without those optional dependencies.
