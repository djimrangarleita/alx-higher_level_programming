#!/bin/bash
# Print the Content-Length of the requested url
curl -si "$1" | awk '/Content-Length/ {print $2}'
