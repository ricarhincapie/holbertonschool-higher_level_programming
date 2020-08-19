#!/bin/bash
#Send a DELETE request to a given IP
curl -s --request POST -d "email=hr@holbertonschool.com&subject=I will always be here for PLD" "$1"
