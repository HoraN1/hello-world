# -*- coding: utf-8 -*-

"""
Author: zhanxin
Email: horacesunhe@gmail.com
date: 2019/7/4 13:54
"""
"""
    a function to swap cases
    input: a string
    output: a string whose case is swapped, lower to upper and vise versa
"""


def swap_case(a_str):
    a_list = list(a_str)
    for index in range(len(a_list)):
        if a_str[index] == a_list[index].lower():
            a_list[index] = a_str[index].upper()
        else:
            a_list[index] = a_str[index].lower()
    return ''.join(a_list)


if __name__ == '__main__':
    s = input()
    result = swap_case(s)
    print(result)
