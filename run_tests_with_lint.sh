#!/usr/bin/env bash


. ~/.virtualenvs/python2.7/bin/activate
set -e
set -x

rm -f pep8.log pyflakes.log

./test.py

pep8 pystache > pep8.log || true
pyflakes pystache > pyflakes.log || true
