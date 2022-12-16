#!/bin/bash

echo Please enter root directory
read -p 'Root:' root

if [ -z "$root" ]
then
    echo "user input is empty"
    export LOCAL_ROOT=$(pwd)
else
    echo "user entered $root"
    export LOCAL_ROOT=$root
fi

echo "set local root to $LOCAL_ROOT"

docker compose up --build