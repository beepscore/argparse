#!/usr/bin/env python3

# References:
# http://docs.python.org/3.3/library/argparse.html?highlight=argparse#argparse
# http://bip.weizmann.ac.il/course/python/PyMOTW/PyMOTW/docs/argparse/index.html

import argparse

def main():
    '''
    For help, use argument -h
    $ ./arg-reader.py -h
    To specify an argument, prefix with -
    $ ./arg-reader.py -animalbig hippo -animalsmall fly
    To read arguments from a file, prefix file name with @
    $ ./arg-reader.py @args2.txt
    To specify arguments from command line and from a file
    $ ./arg-reader.py @args.txt -animalbig hippo
    '''

    parser = argparse.ArgumentParser(description='To read arguments from a file, prefix file name with @ e.g. $ ./arg-reader.py @args.txt -animalbig hippo',
                                    fromfile_prefix_chars='@',
                                    )

    parser.add_argument('-animalbig', action="store", dest="animalbig",
                        help = 'name of a big animal')
    parser.add_argument('-animalsmall', action="store", dest="animalsmall",
                        help = 'name of a small animal')

    arguments = parser.parse_args()
    print(arguments)
    print(arguments.animalbig)
    print(arguments.animalsmall)

if __name__ == "__main__": main()

