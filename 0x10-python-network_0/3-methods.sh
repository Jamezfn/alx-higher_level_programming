#!/bin/bash
# displays all http methods the server can accept 
curl -s -I -X OPTIONS "$1" | grep -i '^Allow:' | cut -d ' ' -f 2-
