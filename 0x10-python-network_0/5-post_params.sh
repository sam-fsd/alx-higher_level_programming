#!/bin/bash
# Sends POST request to server with data: A variable email must be sent with the value test@gmail.com A variable subject must be sent with the value I will always be here for PLD
curl -s -X POST --data "email=test@gmail.com" --data "subject=I will always be here for PLD" "$1"
