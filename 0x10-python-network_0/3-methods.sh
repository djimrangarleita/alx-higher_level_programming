#!/bin/bash
# Print the list of allowed methods 
curl -sIL "$1" | sed -n 's/^Allow: //p' 
