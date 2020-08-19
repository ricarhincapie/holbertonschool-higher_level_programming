#!/bin/bash
#Checks body response in bytes
curl -s --head | grep Length | cut -d " " -f2
