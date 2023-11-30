#!/bin/bash
#sends a json post request with the contents
curl -s -X POST -H "Content-type: application/json" -d "@$2" "$1"
