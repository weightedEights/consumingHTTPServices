#!/usr/bin/python
# -*- coding: utf-8 -*-

"""  Some Description """


import requests, json


def main():

    url = 'https://api.github.com/repos/mikeckennedy/consuming_services_python_demos'
    resp = requests.get(url)

    print(json.dumps(json.loads(resp.text), indent = True))


if __name__ == '__main__':
    main()
