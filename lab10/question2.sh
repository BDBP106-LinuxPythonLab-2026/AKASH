#!/bin/bash
#

filename=$1

if [ -f $1 ] ; then
       echo "file Exists"
    if [ -x $1 ] ; then
	 echo "File Executible"
         echo "file exists and executible"
    else
      echo "File non-Executible"  
      echo "file exits but not executible"
    fi
 
else
   echo "No File Exists"
   echo "No file exists nor executible" 

fi

