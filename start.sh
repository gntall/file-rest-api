#!/bin/bash

echo Please enter root directory
read -p 'Root:' root
echo $root

export ROOT=$root

flask --debug run --port=8000