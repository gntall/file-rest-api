#!/bin/bash

echo Please enter root directory
read -p 'Root:' LOCAL_ROOT

if [ -z "$LOCAL_ROOT" ]
then
    echo "user input is empty"
    export LOCAL_ROOT=$(pwd)
fi

echo "set local root to $LOCAL_ROOT"

docker compose up --build