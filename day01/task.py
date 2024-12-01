def task1(left_list, right_list):
    left_list.sort()
    right_list.sort()

    distances = 0
    for i, x in enumerate(left_list):
        dist = abs(x - right_list[i])
        distances += dist
    return distances


def task2(left_list, right_list):
    distances = 0
    for i, x in enumerate(left_list):
        dist = right_list.count(x)
        distances += (x * dist)
    return distances


def read_input():
    f = open("input.txt", "r").read()
    lines = f.split('\n')
    left_list = []
    right_list = []
    for l in lines:
        left, right = l.split()
        left_list.append(int(left))
        right_list.append(int(right))
    return left_list, right_list


def solution():
    left_list, right_list = read_input()
    res1 = task1(left_list, right_list)
    print(res1)
    res2 = task2(left_list, right_list)
    print(res2)

solution()
