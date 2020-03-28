# -*- coding: utf-8 -*-

"""
Author: horacesun
Email: horacesunhe@gmail.com
date: 2019/7/4 14:08
"""

"""
    a function to split strings and join them with some symbol
    input: a string
    output: split and rejoined string 
"""


def split_and_join(a_str):
    a_list = a_str.split(" ")
    return '-'.join(a_list)


if __name__ == '__main__':
    test_str = input()
    print(split_and_join(test_str))
