#!/bin/bash

if [ -z "$1" ] ; then
    echo "No application name supplied."
    exit 1
fi

find . -type f -name "*.py" -print0 | xargs -0 sed -i '' -e "s/flaskapp/$1/g"
mv flaskapp $1

rm rename_project.sh

echo "Application renamed successfully"
