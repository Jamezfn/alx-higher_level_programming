#!/bin/bash
# takes url sends POST request to a passed url en displays body of respo
curl -s X POST -d "email=test@gmail.com&subject=I will always be here for PLD" "$1"
