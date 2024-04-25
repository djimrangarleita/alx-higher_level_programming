#!/bin/bash
# Send http post request and print request body 
curl -sX POST -F 'email'='test@gmail.com' -F 'subject'='I will always be here for PLD' "$1"
