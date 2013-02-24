#!/usr/bin/env python3

# References:
# http://docs.python.org/3.3/library/argparse.html?highlight=argparse#argparse
# http://bip.weizmann.ac.il/course/python/PyMOTW/PyMOTW/docs/argparse/index.html

import argparse

def main():
    '''
    Read arguments from a file
    '''

    parser = argparse.ArgumentParser(description='Script reads arguments from a file. Type $ ./arg-reader.py @argsfilename e.g. $ ./arg-reader.py @args.txt',
                                    fromfile_prefix_chars='@',
                                    )

    parser.add_argument('-arga', action="store", dest="arga",
                        help = 'name of student')
    parser.add_argument('-argb', action="store", dest="argb",
                        help = 'name of teacher')

    arguments = parser.parse_args()
    print(arguments)
    print(arguments.arga)
    print(arguments.argb)

if __name__ == "__main__": main()

