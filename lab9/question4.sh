#!/bin/bash

echo $0
name=$1
age=$2

echo 'The first argument is: ',$1
echo 'The second argument is: ',$2
echo 'The third argument is: ',$3

echo 'The number of arguments passed to this script: '$#
echo 'The array/list of arguements passed to this script: '$@

# We can store the arguements in an array by enclosing $@ within ()
listofarg=($@)
#Recall elements like any othe array
echo ${listofarg[2]}


