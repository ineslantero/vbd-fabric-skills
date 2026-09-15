# components/transcript-loader

Normalises a scoping-call transcript from any of three sources into `.vbd/transcript.md` so downstream skills see a single shape.

## Sources

### 1. Paste in chat
CSA pastes raw text, or drops a `.docx`, `.txt`, or `.vtt` file into chat.
- `.docx` → parse with python-docx, strip formatting.
- `.vtt` → strip WEBVTT headers, timestamps; keep speaker + line.
- Text → passthrough.

### 2. WorkIQ meeting lookup
CSA provides a customer or meeting name. Skill:
1. `workiq_list_events` with `search` = subject keyword and/or `attendees` filter for customer domain.
2. Present matches to CSA (m_ask_user) — never guess.
3. `workiq_get_event` for `onlineMeeting.joinUrl` and meeting id.
4. Fetch the Teams meeting transcript (Graph `/me/onlineMeetings/{id}/transcripts`) or the SharePoint-hosted transcript file linked from the event.
5. Fall back to `workiq_search_files` if the transcript is stored separately (e.g. Copilot for M365 output).

### 3. Email thread fallback
Used when there's no formal scoping call.
1. `workiq_search_emails` with subject/participant filter.
2. Fetch full thread via `workiq_get_email` (include quoted history).
3. Concatenate in chronological order as `transcript.md`.

## Output

```
.vbd/
├── transcript.md          ← normalised, downstream reads this
├── transcript.source.yaml ← provenance (source, ids, timestamps)
└── transcript.raw/        ← original files/JSON for audit
```

## Privacy

- Everything under `.vbd/` is CSA-only. `/vbd-repo-build` explicitly drops this folder before shipping.
- Never send transcript content to any 3rd party or external service — freshness verifier only sees the extracted objectives, not raw transcript.
