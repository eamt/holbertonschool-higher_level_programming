#!/usr/bin/python3
"""Take in a URL and send a request to the URL
and display the value of X-Request-Id
"""

from sys import argv
import requests


if __name__ == "__main__":
    req = requests.get(argv[1])

    print(req.headers.get('X-Request-Id'))
