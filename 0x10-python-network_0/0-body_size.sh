#!/bin/bash
#Checks body response in bytes
curl -s --head "$1" | grep Length | cut -d " " -f2
