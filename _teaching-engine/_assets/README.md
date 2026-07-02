# `_assets/` — the shared lesson component library

Reusable components for rendered lessons (`LLL_Lesson`; see `../05-LESSONS.md`). **Optional** — lessons live as markdown first; these only matter when you render the beautiful HTML artifact.

- **`lesson.css`** — the shared stylesheet every rendered lesson links, so a cartridge's lessons look like one consistent course rather than a pile of one-offs. Tufte-ish, print-friendly, self-contained (no web fonts, no external requests).

## Discipline

**Reuse is the default, not the exception.** Before authoring a rendered lesson, read this folder and build from what's here. When a lesson needs something new and reusable (a quiz widget, a diagram helper, a simulator), add it here as a component and link it — never inline code a future lesson would duplicate. The shared stylesheet is the first component every workspace earns; as the library grows, so should the consistency and the speed of authoring the next lesson.

Ships with the OV (like `_scripts/`). No build step, no dependencies — a rendered lesson is a single self-contained HTML file that links `lesson.css` by relative path (or inlines it for full portability).
