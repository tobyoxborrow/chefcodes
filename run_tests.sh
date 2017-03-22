#!/bin/bash

set -o errexit
set -o pipefail
set -o nounset

coverage run -m pytest -rw -s
coverage report -m
