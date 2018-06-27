import random

numbers = [random.randrange(1000) for i in range(40)]


def bubble_sort(list):
    length = len(list)
    for i in range(length - 1, 0, -1):
        for j in range(i):
            if list[j] > list[j + 1]:
                list[j], list[i] = list[i], list[j]
    return list


def bubble_sort(list):
    length = len(list)
    for i in range(length - 1, 0, -1):
        for j in range(i):
            if list[j] > list[j + 1]:
                list[j], list[i] = list[i], list[j]
    return list
