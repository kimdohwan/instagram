import random

numbers = [random.randrange(1000) for i in range(40)]


def bubble_sort(list):
    l = len(list)
    for i in range(l - 1, 0, -1):
        for j in range(i):
            if list[j] > list[j + 1]:
                list[j + 1], list[j] = list[j], list[j + 1]


def selection_sort(list):
    l = len(list)
    for i in range(l - 1):
        min_index = i
        for j in range(i + 1, l):
            if list[min_index] > list[j]:
                min_index = j
        if min_index != i:
            list[i], list[min_index] = list[min_index], list[i]
    return list


def insertion_sort(list):
    l = len(list)
    for i in range(1, l):
        curr_value = list[i]
        index = i
        while index > 0 and list[index - 1] > curr_value:
            list[index] = list[index - 1]
            index -= 1
        list[index] = curr_value

    return list


print(selection_sort(numbers.copy()))
