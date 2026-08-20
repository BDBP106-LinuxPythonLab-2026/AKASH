#!/bin/bash

name="Akash"
if [ -n "$name" ] ; then
	echo "String is not empty"
else 
	echo "String is Empty"
fi


if [ -z "$name" ] ; then
	echo "String is Empty"
else 
	echo "String is not empty"
fi
