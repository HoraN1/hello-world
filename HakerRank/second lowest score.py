# -*- coding: utf-8 -*-

"""
Author: zhanxin
Email: horacesunhe@gmail.com
date: 2019/7/3 16:03
"""

'''
if __name__ == '__main__':
    second_name = []
    name_list = []
    score_list = []
    for _ in range(int(input())):
        name = input()
        score = float(input())
        name_list += [name]
        score_list += [score]
    print(name_list)
    print(score_list)
    lowest = min(score_list)
    while min(score_list) == lowest:
        score_list.remove(lowest)

    second_low = min(score_list)
    for index in range(len(score_list)):
        if score_list[index] == second_low:
            second_name += [name_list[index]]
    print(sorted(second_name))
'''

if __name__ == '__main__':
    score_sheet = []
    second_name = []
    for _ in range(int(input())):
        score_sheet += [[input(), float(input())]]
    ordered_score = [score_sheet[index][1] for index in range(len(score_sheet))]
    lowest = min(ordered_score)
    while min(ordered_score) == lowest:
        ordered_score.remove(lowest)
    for index in range(len(score_sheet)):
        if score_sheet[index][1] == min(ordered_score):
            second_name += [score_sheet[index][0]]
    for number in range(len(second_name)):
        print(sorted(second_name)[number])







