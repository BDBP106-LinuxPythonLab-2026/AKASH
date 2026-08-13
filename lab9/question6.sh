#!/bin/bash

echo $HOME

bc << EOF
scale=5
22934/44343
EOF


ls $HOME | grep "^D"

echo "The lines containing the username are: "
grep "$USER" /etc/passwd


