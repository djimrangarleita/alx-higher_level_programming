#!/bin/bash
# Send http request and print status code
curl -sL -X POST -H "Content-Type: application/json" -d @"$2" "$1"
