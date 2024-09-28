#!/usr/bin/env bash

set -e
set -x

uv run --with coverage coverage run -m pytest