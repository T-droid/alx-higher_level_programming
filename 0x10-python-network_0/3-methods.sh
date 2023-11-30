#!/bin/bash
#displays all http methods a server will accept
curl -X OPTIONS "$1"
