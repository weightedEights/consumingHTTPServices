#!usr/bin/python
# -*- coding: utf-8 -*-

"""  Some Description """


import os
from xml.etree import ElementTree


def main():

    folder = os.path.dirname(__file__)
    file = os.path.join(folder, 'xml_data', 'reed.xml')

    with open(file) as fin:
        xml_text = fin.read()

    dom = ElementTree.fromstring(xml_text)

    print(dom)

if __name__ == '__main__':
    main()
