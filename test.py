#!/usr/bin/env python
# coding: utf-8

import unittest
import xmlrunner

def runner(output='python_tests_xml'):
    return xmlrunner.XMLTestRunner(
        output=output
    )

def find_tests():
    return unittest.TestLoader().discover('pystache')

if __name__ == '__main__':
    lister = self.find_tests()
    for x in lister:
        print x
    runner().run(find_tests())
