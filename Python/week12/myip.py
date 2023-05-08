#!/usr/bin/env python3

import requests
import json


def get_myip():
    url = "http://jsonip.com"
    response = requests.get(url)
    data = json.loads(response.text)
    return data["ip"]


def main():
    print("Az IP címed:" +  get_myip())

   

if __name__ == "__main__":
    main()