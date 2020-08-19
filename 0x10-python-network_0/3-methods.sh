#!/bin/bash
#Send a DELETE request to a given IP
curl -sI "$1" | grep Allow: | cut -c8-
