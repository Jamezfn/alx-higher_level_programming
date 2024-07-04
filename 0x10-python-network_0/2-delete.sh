#!/bin/bash
# deltes request passed as first arg and displays body of response
curl -sX DELETE "$1"
