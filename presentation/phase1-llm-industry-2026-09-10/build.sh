#!/usr/bin/env bash
set -euo pipefail
DECK_WORKSPACE="$(cd -- "$(dirname -- "${BASH_SOURCE[0]}")" && pwd)"
DECK_RUNTIME_NODE=/Users/sthmax/.cache/codex-runtimes/codex-primary-runtime/dependencies/node/bin/node
DECK_RUNTIME_MODULES=/Users/sthmax/.cache/codex-runtimes/codex-primary-runtime/dependencies/node/node_modules
if [[ $# -ne 1 ]]; then
  echo 'Usage: ./build.sh a-new-output-filename.pptx' >&2
  exit 1
fi
export DECK_FILENAME="$1"
mkdir -p "$DECK_WORKSPACE/.build" "$DECK_WORKSPACE/output"
if [[ ! -e "$DECK_WORKSPACE/.build/node_modules" ]]; then
  ln -s "$DECK_RUNTIME_MODULES" "$DECK_WORKSPACE/.build/node_modules"
fi
cp "$DECK_WORKSPACE/src/build.mjs" "$DECK_WORKSPACE/.build/build.mjs"
"$DECK_RUNTIME_NODE" "$DECK_WORKSPACE/.build/build.mjs"
