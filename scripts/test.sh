#!/usr/bin/env bash

set -e
set -x

uv run coverage run -m pytest
uv run coverage report --skip-covered --skip-empty --include=./katty/**/*,./tests/**/*