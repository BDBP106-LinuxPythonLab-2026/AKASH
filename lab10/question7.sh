#!/bin/bash
#Getting the username of the logged-in user

logged_in_user=$(whoami)

#checking if the user is logged in 
# spelling og logged, change) to ] ,then in the same line
if [ -n "$logged_in_user" ]; then
 echo "The logged_in_user is: $logged_in_user"

else
 echo "user is not logged in"
fi
