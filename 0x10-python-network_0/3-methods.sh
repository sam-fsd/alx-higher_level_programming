#!/bin/bash
# Sends an HTTP OPTIONS request to a URL and displays the allowed methods
curl -s -X OPTIONS -I "$1" | grep -i "Allow:" | cut -d ' ' -f 2-
