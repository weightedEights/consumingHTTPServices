#!/usr/bin/python
# -*- coding: utf-8 -*-

"""  Some Description """


import requests, json


def main():
    # user = mikeckennedy
    # repo = consuming_services_python_demos
    user, repo = get_repo_info()

    url = 'https://api.github.com/repos/{}/{}'.format(user, repo)
    resp = requests.get(url)

    if resp.status_code != 200:
        print("Error accessing repo: {}".format(resp.status_code))
        return

    print(json.dumps(json.loads(resp.text), indent = True))


def get_repo_info():

    user = input("What is the username?")
    repo = input("What is the repo?")

    return user, repo


if __name__ == '__main__':
    main()
