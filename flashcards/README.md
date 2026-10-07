# flashcards

A tiny flashcard app built on the standard library. Cards live in `cards.json`.

```
python -m flashcards serve                 # http://127.0.0.1:8765
python -m flashcards list [-c caching]
python -m flashcards add -c graphs -q "question" -a "answer" [-s source]
python -m flashcards add --json new.json   # or --json - to read from stdin
```

Click the card (or press space) to reveal the answer. Use ←/→ to move between cards.
Refresh the page to pick up newly added cards.

Each card has `question`, `answer`, `category`, `source`, `id` and `created`.
Answers support a small subset of markdown: ```` ``` ```` code blocks, `` `inline code` `` and `**bold**`.

## Brainstorming new cards with Claude

Ask something like "let's brainstorm flashcards about X" or "make cards from today's commits".
Claude drafts the cards and you edit or approve them. Claude then pipes the approved cards in as JSON:

```
python -m flashcards add --json - <<'EOF'
[{"category": "graphs", "question": "...", "answer": "...", "source": "..."}]
EOF
```

Duplicate questions are skipped.
