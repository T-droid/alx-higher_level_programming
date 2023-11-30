#!/bin/bash
#script to trake url and display its size
echo $(curl -s -w "%{size_download}\n" -o /dev/null "$1")
