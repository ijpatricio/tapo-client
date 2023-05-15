#!/usr/bin/env bash

function help {
    echo "$0 <task> <args>"
    echo "Tasks:"
    compgen -A function | cat -n
}

function default {
    help
}

function install {
    pip3 install -r requirements.txt
}

function main {
    python3 main.py "$1" "$2"
}

TIMEFORMAT="Task completed in %3lR"
time "${@:-default}"
