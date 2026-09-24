#!/usr/bin/env bash
# Works on macOS/Linux and Windows (Git Bash / WSL).
# Run with `source setup.sh` so the venv stays active in your shell.

MIN_VERSION="3.10"

# Find first interpreter that exists and is >= MIN_VERSION.
# `py -3` is the Windows launcher; `python3` on Windows may be a Store stub,
# so the version check filters it out.
PYTHON=""
for cmd in "python3" "python" "py -3"; do
    if $cmd -c 'import sys; sys.exit(sys.version_info < (3, 10))' >/dev/null 2>&1; then
        PYTHON="$cmd"
        break
    fi
done

if [ -z "$PYTHON" ]; then
    echo "Error: Python >= $MIN_VERSION not found (tried python3, python, py -3)." >&2
    echo "Install from https://www.python.org/downloads/" >&2
    return 1 2>/dev/null || exit 1
fi

echo "Using $($PYTHON --version) ($PYTHON)"

$PYTHON -m venv .venv || { return 1 2>/dev/null || exit 1; }

# Windows venvs put scripts in Scripts/, Unix in bin/
if [ -f .venv/Scripts/activate ]; then
    source .venv/Scripts/activate
else
    source .venv/bin/activate
fi || { return 1 2>/dev/null || exit 1; }

echo "✅ Setup complete. Virtual environment active: $VIRTUAL_ENV"
