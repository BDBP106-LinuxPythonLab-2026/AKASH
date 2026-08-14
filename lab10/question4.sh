#!/bin/bash

 echo "Enter a number"
 read number
 
if [ $number -ge 0 ] ; then
	echo "Number is positive"
      if [ $number -eq 0 ] ; then
	      echo " Number is equal to ZERO"
      fi
    else 
      echo "Number is negative"	    
fi    

