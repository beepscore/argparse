#!/usr/bin/env python3

# References:
# http://docs.python.org/3.3/library/argparse.html?highlight=argparse#argparse
# http://bip.weizmann.ac.il/course/python/PyMOTW/PyMOTW/docs/argparse/index.html
# http://stackoverflow.com/questions/3853722/python-argparse-how-to-insert-newline-the-help-text

import argparse
from argparse import RawTextHelpFormatter

def main():
    '''
    Multiply two integers. Read arguments from command line or from a file.
    '''

    parser = argparse.ArgumentParser(description='''    For help, use argument -h
    $ ./multiplier.py -h
    To specify an argument, prefix with -
    $ ./multiplier.py -multiplicand 5 -multiplier 3
    To read arguments from a file, prefix file name with @
    $ ./multiplier.py @args-multiply.txt
    To specify arguments from command line and from a file
    $ ./multiplier.py @args-multiply.txt -multiplier 17''',
                                    fromfile_prefix_chars='@',
                                    formatter_class=RawTextHelpFormatter,
                                    )

    parser.add_argument('-multiplicand', type=int, action="store", dest="multiplicand",
                        help = 'integer to be multiplied')
    parser.add_argument('-multiplier', type=int, action="store", dest="multiplier",
                        help = 'integer to multiply by')

    arguments = parser.parse_args()

    multiply_result = multiply(arguments.multiplicand, arguments.multiplier)
    print('multiply({}, {}) = {}'.format(arguments.multiplicand, arguments.multiplier, multiply_result))

    multiply_iterative_result = multiply_iterative(arguments.multiplicand, arguments.multiplier)
    print('multiply_iterative({}, {}) = {}'.format(arguments.multiplicand, arguments.multiplier, multiply_iterative_result))


def multiply(a, b):
    return (a * b)

def multiply_iterative(a, b):
    '''
    http://stackoverflow.com/questions/14638078/russian-peasant-multiplication-python-3-3?rq=1
    '''

    result = 0
    multiplicand_iterative = a
    multiplier_iterative = b

    while multiplier_iterative > 1:
        if ((multiplier_iterative % 2) == 1):
            result += multiplicand_iterative
        multiplicand_iterative *= 2
        # use integer division //
        multiplier_iterative //= 2
        #print('multiplicand_iterative:{} multiplier_iterative:{} result:{}'.format(multiplicand_iterative, multiplier_iterative, result))

    if (multiplier_iterative == 1):
        result += multiplicand_iterative

    return result

if __name__ == "__main__": main()

