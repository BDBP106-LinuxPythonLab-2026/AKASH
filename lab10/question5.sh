#!/bin/bash

echo -n "Your score:"
read score

if [ $score -gt 90 ] && [ $score -lt 100 ]; then
	echo "A+"
fi

if [ $score -ge 80 ] && [ $score -le 89 ]; then
	echo "B"
fi

if [ $score -ge 70 ] && [ $score -le 79 ]; then
	echo "C"
fi

if [ $score -lt 70 ]; then
	echo "FAIL"
fi

if [ $score -gt 100 ]; then
	echo "Maximum score is 100"
fi
