#!/usr/bin/python3
"""sends a request to the URL and
displays the value of
the variable X-Request-Id
"""

import requests
import sys

if __name__ == '__main__':
    url = sys.argv[1]
    r = requests.get(url)
    d = r.headers
    print(d.get("X-Request-Id"))
