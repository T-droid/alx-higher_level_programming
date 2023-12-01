#!/usr/bin/python3
""" sends a POST request to the passed URL with the email as a parameter"""
import sys
import requests

if __name__ == '__main__':
    url = sys.argv[1]
    email = sys.argv[2]
    data = {'email': email}
    r = requests.post(url, data=data)
    content = r.json()
    print(content.get("email"))