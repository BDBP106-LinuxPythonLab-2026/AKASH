#!/bin/bash
#Age condition if Adult or Minor


echo "Enter your age: "
read age

if [ $age -ge 18 ] ; then
	echo "You are an Adult"
     else
     echo "You are a Minor"	
fi     

