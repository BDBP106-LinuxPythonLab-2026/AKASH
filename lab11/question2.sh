#!/bin/bash
#
#checking if a file/directory or symbolic link exists or not [-e]
if [ -e timepass ] ; then
       echo "Exists"	

else
	echo "Doesnt exits"
fi

#checking if the file exits and has data in it [-s]
if [ -s timepass ] ; then 
	echo "file exits and has data"
else 
	echo "File either doesnt exits or doesnt haver any data "
fi

#Checking if just the File exists or not [-f]
if [ -f fall ] ; then
	echo "File exists"
else
	echo "File doesnt exists"
fi


