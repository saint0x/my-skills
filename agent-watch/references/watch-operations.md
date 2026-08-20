# Agent Watch Operations

## Contents

- Upstream Provenance
- Runtime Layout
- Setup
- First Watch Run
- Focused Re-runs
- Detail Modes
- Transcript-Cue Frames
- Failure Handling
- Cleanup

## Upstream Provenance

This skill vendors the working watch runtime from:

- repo: `https://github.com/bradautomates/claude-video`
- commit: `83da59fa78c3eee9e20f515fe75c438bb5166efd`

The imported runtime is the upstream `skills/watch/scripts/` payload, preserved so the video-analysis behavior stays real instead of being re-described from scratch.

## Runtime Layout

Use the bundled scripts under this skill directory:

- `scripts/setup.py`
- `scripts/watch.py`
- `scripts/download.py`
- `scripts/frames.py`
- `scripts/transcribe.py`
- `scripts/whisper.py`
- `scripts/config.py`

The runtime uses `yt-dlp`, `ffmpeg`, and optionally Groq or OpenAI Whisper for transcription fallback.

Configuration lives in:

- `~/.config/watch/.env`

That location remains upstream-compatible on purpose.

## Setup

Run preflight before first use:

```bash
python3 "<skill-dir>/scripts/setup.py" --json
```

Silent success check for later runs:

```bash
python3 "<skill-dir>/scripts/setup.py" --check
```

Installer:

```bash
python3 "<skill-dir>/scripts/setup.py"
```

Operational expectations:

- macOS can auto-install `ffmpeg` and `yt-dlp` via Homebrew
- Linux and Windows print exact install commands
- Whisper keys are optional but strongly preferred
- native captions are used first whenever available

## First Watch Run

Basic invocation:

```bash
python3 "<skill-dir>/scripts/watch.py" "<video-url-or-path>"
```

Examples:

```bash
python3 "<skill-dir>/scripts/watch.py" "https://youtu.be/abc123"
python3 "<skill-dir>/scripts/watch.py" "/Users/deepsaint/Movies/bug-repro.mov"
```

After the run:

1. Inspect the transcript emitted by the script.
2. Read every returned frame path.
3. Answer from combined evidence.

Do not answer from transcript only when frames were available and relevant.

## Focused Re-runs

Use a narrow time window when the question is about a specific moment or when the full-video scan is sparse.

```bash
python3 "<skill-dir>/scripts/watch.py" "<source>" --start 2:15 --end 2:45
python3 "<skill-dir>/scripts/watch.py" "<source>" --start 50 --end 60
```

Focused runs are denser and usually more useful than burning tokens across the entire video.

## Detail Modes

Use `--detail` to control fidelity and token cost:

- `transcript`
  No frames. Best when spoken content is enough.
- `efficient`
  Fast keyframe pass, capped around 50 frames.
- `balanced`
  Scene-aware default, capped around 100 frames.
- `token-burner`
  Scene-aware and uncapped. Use only when the user truly needs full coverage.

Useful flags:

- `--max-frames N`
- `--resolution 1024`
- `--fps F`
- `--whisper groq|openai`
- `--no-whisper`
- `--no-dedup`

## Transcript-Cue Frames

If the speaker says things like:

- "look here"
- "as you can see"
- "notice this"
- "watch what happens"

then do a second run with exact cue timestamps:

```bash
python3 "<skill-dir>/scripts/watch.py" "<source>" --timestamps 4:32,7:10,9:55
```

Use this when visual emphasis matters more than scene changes.

## Failure Handling

Common cases:

- missing `ffmpeg` or `yt-dlp`
  Run the installer first
- no captions and no Whisper key
  proceed frames-only or ask the user whether to set a key
- download failure on login-required or region-locked content
  explain the limitation plainly
- long video sparse-scan warning
  propose a focused re-run

Do not keep retrying the same failing download blindly.

## Cleanup

The script prints a temporary working directory.

- Keep it if the user is likely to ask follow-ups about the same video.
- Remove it when the watch session is complete.
