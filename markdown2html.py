#!/usr/bin/python3
'''
A script that codes markdown to HTML
'''
import sys
import os
import re

if __name__ == '__main__':

    # Test that the number of arguments passed is 2
    if len(sys.argv[1:]) != 2:
        print('Usage: ./markdown2html.py README.md README.html',
              file=sys.stderr)
        sys.exit(1)
