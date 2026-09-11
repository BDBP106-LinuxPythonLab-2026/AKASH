#!/bin/bash


function check {
	directory=$1
if [ -d $directory ]; then
	echo " $directory exixts "
	ls "$directory"
 else
	 echo "$directory doesnot exists"
	 mkdir "$directory"
	 echo "Directory Created"

fi 

}
	
check tocheck




