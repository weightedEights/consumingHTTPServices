#!usr/bin/python
# -*- coding: utf-8 -*-

"""  Some Description """


import os
from xml.etree import ElementTree
import collections

# named tuple.. a class with fields only, no functions. better data container
Course = collections.namedtuple('Course', 'title room building')


def main():

    folder = os.path.dirname(__file__)
    file = os.path.join(folder, 'xml_data', 'reed.xml')

    with open(file) as fin:
        xml_text = fin.read()

    # data object model
    dom = ElementTree.fromstring(xml_text)

    # findall is a xpath query
    course_nodes = dom.findall('course')

    # sub-queries inside the findall query
    courses = [
        Course(n.find('title').text, n.find('place/room').text, n.find('place/building').text)
        for n in course_nodes
    ]

    building = input("What building are you in? ")
    room = input("What room are you near? ")

    room_courses = [
        c.title
        for c in courses
        if c.building == building and c.room == room
    ]

    for c in room_courses:
        print('*' + c)


if __name__ == '__main__':
    main()
