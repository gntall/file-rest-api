#!/bin/bash

mkdir test_data

ROOT="$(pwd)/test_data"

echo "set root to $ROOT"

pytest --basetemp=$ROOT test.py
