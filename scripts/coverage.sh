#!/usr/bin/env bash

set -e
set -x

uv run --with coverage coverage report --skip-covered --skip-empty --include=./katty/**/*,./tests/**/*