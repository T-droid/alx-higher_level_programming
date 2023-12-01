#!/usr/bin/python3
"""sends a request to the URL and displays the body of the response"""

import urllib.request
from urllib.error import HTTPError
import sys

if __name__ == '__main__':
    url = sys.argv[1]
    request = urllib.request.Request(url)

    try:
        with urllib.request.urlopen(request) as body:
            print(body.read().decode('utf-8'))
    except HTTPError as e:
        print("Error code: {}".format(e))
