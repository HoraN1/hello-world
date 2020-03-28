# -*- coding: utf-8 -*-

"""
Author: horacesun
Email: horacesunhe@gmail.com
date: 2019/7/4 14:14
"""


"""
    a function to print full name using "...{0}...".format(str_a + str_b+ ... + str_n)
    input: a string
    output: a string with .format()
"""


def print_full_name(first, last):
    return print("Hello {0}! You just delved into python.".format(first + " " + last))


if __name__ == '__main__':
    first_name = input()
    second_name = input()
    print_full_name(first_name, second_name)
