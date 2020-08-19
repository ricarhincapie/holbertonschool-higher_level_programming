#!/bin/bash
#Checks body response in bytes
curl -s --header | grep Length | cut -d " " -f2
