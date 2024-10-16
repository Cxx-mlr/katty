#!/usr/bin/env bash

set -e
set -x

mypy katty
ruff check .
ruff format --check .