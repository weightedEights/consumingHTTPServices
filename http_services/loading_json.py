#!/usr/bin/python
# -*- coding: utf-8 -*-

"""  Some Description """

import json


def main():

    text_json = '''{
        "demo": "Processing JSON in Python",
        "instructor": "Michael",
        "duration": 5.0    
        }'''

    data = json.loads(text_json)

    print(type(data), data)

    # instructor = data['instructor']
    instructor = data.get('instructor', 'Substitute')
    print("Your instructor is {}.".format(instructor))

    data['instructor'] = "Jeff"

    new_json = json.dumps(data)

    print(type(new_json), new_json)


if __name__ == '__main__':
    main()
