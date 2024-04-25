#!/bin/bash
# Send http header and print request body 
curl -sX GET -H 'X-School-User-Id: 98' "$1"
