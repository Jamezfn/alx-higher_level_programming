#!/bin/bash
# displays all http methods the server can accept
curl -Is "$1" | grep Allow | cut -c 8-
