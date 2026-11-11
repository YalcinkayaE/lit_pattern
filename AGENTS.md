# Repository Instructions

Codex communication principles:

1. No overselling: state what exists without exaggeration.
2. No confabulation.
3. No embellishment: keep descriptions accurate and plain.
4. Stick to facts: report actual state, errors, and results.
5. Be constructive: investigate issues, provide insights, and suggest practical solutions.
6. Avoid superlatives: no "revolutionary", "world's first", or "breakthrough" claims.
7. Skip metrics without context: no improvement or confidence claims without baseline data.
8. Question assumptions: verify claims before repeating them.
9. Focus on what works: test and confirm functionality rather than trusting documentation.
10. Minimise ceremony: no unnecessary emojis, formatting, or section headers.
11. Be skeptical of counts: arbitrary numbers add no technical value.
12. Prefer showing over telling: demonstrate with code or commands rather than descriptions.

Production system principles:

13. No hardcoded values: all configuration must be external and validated.
14. No fake data fallbacks: systems must fail explicitly when real data is unavailable.
15. No silent dependency failures: missing imports or APIs must cause clear startup failures.
16. Validate before claiming "production ready": verify all external systems actually work.
17. Use real error messages: tell users exactly what is broken and how to fix it.

Repository-specific rules:

- Read `REPO_CONTRACT.md` before acting.
- Treat the repository contract as the control document for identity, status,
  authoritative sources, runtime, verification, open items, vocabulary, and
  update discipline.
- Do not silently change repository identity, scope, source ordering, runtime
  path, milestone claims, vocabulary, or contract surfaces.
- Do not describe a proposed pattern definition as validated, operational, or
  accepted until evidence from an actual pilot is recorded.
- Do not add copyrighted corpus content, private annotation data, credentials,
  or downloaded dependencies to version control.
- Preserve the original workbook export and its checksum when normalising data.

Project document control:

This repository uses `repo_contract.global.skill`.

Always read `REPO_CONTRACT.md` first.

If another document disagrees with the repository contract, follow the
authority order declared in `REPO_CONTRACT.md`.

If `REPO_CONTRACT.md` is missing, create it using the standard repository
contract schema before making further changes.

