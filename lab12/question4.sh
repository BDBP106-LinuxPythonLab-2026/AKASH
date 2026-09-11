#!/bin/bash

read -ra numbers < nums.txt

echo "${numbers[@]}"


for i in ${numbers[@]}
do
	result=$(( i*2 ))
	echo "$result"
done
