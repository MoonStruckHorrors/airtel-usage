#! /bin/bash

# Simple script to add the airtel-usage.py to crontab. Runs every 30 minutes.

chmod +x airtel-usage.py

read -p "This script will REPLACE your crontab. Are you sure you want to continue? <y/N> " prompt
if [[ $prompt == "y" || $prompt == "Y" || $prompt == "yes" || $prompt == "Yes" ]]
then
	echo "*/30 * * * * "$PWD"/airtel-usage.py" | crontab
	echo "Successfully added the job."
else
	echo "Exiting without any changes."
    exit 0
fi