#!/bin/bash


function divide {

	local a=$1
	local b=$2
if [ $b -eq 0 ]; then
   echo "Cannot Divide by ZERO"
   return
fi
        local quotient=$(echo " scale=2; $a/$b" | bc)
	local remainder=$(( $1%$2 ))

echo " quotient is :"$quotient
echo " remainder is :"$remainder

}

divide 20 5 
