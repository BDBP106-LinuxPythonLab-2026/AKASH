#!/bin/bash


read n
i=1

until [ $i -gt 15 ]
do
	result=$(($n * $i ))
    echo " $n * $i = $result"
    i=$[ $i + 1 ]
done

