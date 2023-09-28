#!/bin/bash
# Sends a GET request to a URL and displays the body of the response (200 status code only)
[ "$(curl -s -w '%{http_code}' "$1")" -eq 200 ] && curl -s "$1"
