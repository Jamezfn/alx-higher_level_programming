#!/bin/bash
# Sents a delete request to the URL passed as the first argument
curl -s -X DELETE "$1"
