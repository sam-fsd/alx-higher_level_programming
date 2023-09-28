#!/bin/bash
# script that takes in a URL, sends a GET request to the URL, and displays the body of the response
curl -s -o /dev/null -f -I "$1" && curl -s "$1"
