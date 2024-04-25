#!/bin/bash
# Print the body of the requested path
curl -siL "$1" | grep -q "HTTP/1.1 200 OK" && curl -sL "$1"
