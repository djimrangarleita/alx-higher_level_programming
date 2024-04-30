#!/bin/bash
# Send http request and print status code
curl -sL --output /dev/null --write-out "%{http_code}" "$1"
