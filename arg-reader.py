#!/usr/bin/env python3

# References:
# http://docs.python.org/3.3/library/argparse.html?highlight=argparse#argparse
# http://bip.weizmann.ac.il/course/python/PyMOTW/PyMOTW/docs/argparse/index.html

import argparse

def main():
    ''' use file as argument to read other arguments'''

    parser = argparse.ArgumentParser(description='argfile.py reads a file to set variables',
                                    fromfile_prefix_chars='@',
                                    )

    parser.add_argument('-arga', action="store", dest="arga")
    parser.add_argument('-argb', action="store", dest="argb")

    arguments = parser.parse_args(['@args.txt'])
    print(arguments)
    print(arguments.arga)
    print(arguments.argb)

if __name__ == "__main__": main()

