#!/usr/bin/python3
"""takes git hud credentials to display your id"""
import requests
import sys
from requests.auth import HTTPBasicAuth

if __name__ == '__main__':
    username = sys.argv[1]
    passwd = sys.argv[2]
    auth = HTTPBasicAuth(username, passwd)
    r = requests.get("https://api.github.com/user", auth=auth)

    if r.status_code == 200:
        try:
            body = r.json()
            if not body:
                print("None")
            else:
                print(body.get("id"))

        except ValueError:
            print("invalid json file")
    else:
        print("None")
