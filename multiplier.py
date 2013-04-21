#!/usr/bin/env python3


class Multiplier():
    '''
    Multiply two numbers
    '''

    def __init__(self):
        pass

    def multiply(a, b):
        return (a * b)


    def multiply_iterative(a, b):
        '''
        a and b must be integers
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


    def is_power_of_two(an_integer):
        '''
        a must be integer
        '''

        if an_integer = 0
            return False

        if an_integer < 0
            is_an_integer_positive = False
            abs_an_integer = -1 * an_integer
        else
            is_an_integer_positive = True
            abs_an_integer = an_integer

        current_power = 0
        while (2^current_power) <= abs_an_integer:
            if ((abs_an_integer == (2^current_power)):
                 return True

        return result

