"""
    input: a list of student's scores
    output: the average score of the student
"""


def average_score(score_list):
    score_sum = 0
    for index in range(len(score_list)):
        score_sum += score_list[index]
    return round(score_sum / len(score_list), 2)


if __name__ == '__main__':
    n = int(input())
    student_marks = {}
    for _ in range(n):
        name, *line = input().split()
        scores = list(map(float, line))
        student_marks[name] = scores
    query_name = input()
    print("%.2f" % average_score(student_marks[query_name]))
