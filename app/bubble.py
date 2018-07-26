import random

numbers = [random.randrange(1000) for i in range(40)]


def bubble_sort(list):
    l = len(list)
    for i in range(l - 1, 0, -1):
        for j in range(i):
            if list[j] > list[j + 1]:
                list[j + 1], list[j] = list[j], list[j + 1]
    return list


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


def fibonacci(index):
    if index < 2:
        return index
    return fibonacci(index - 1) + fibonacci(index - 2)


def fibonacci_non_recursive(index):  # 반복문으로 피보나치 수열을 구해보자
    if index < 2:
        return index

    value = 1
    prev1 = 1
    prev2 = 1

    for i in range(index - 2):
        value = prev1 + prev2
        prev2 = prev1
        prev1 = value

    return value


mem = [0] * 101  # index 번째 피보나치 수열 저장소


def fibonacci_dynamic(index):  # 다이나믹 프로그래밍으로
    if index < 2:
        return index

    # mem 리스트의 인덱스 : index - 2도 가능 - 1, 2번째 리스트는 그냥 리턴하기 때문에 저장안되기 때문에...

    if mem[index]:  # 피보나치 수열을 이미 계산했다면...
        return mem[index]
    else:  # 계산한 피보나치 수열이 아니에요...
        mem[index] = fibonacci_dynamic(index - 1) + fibonacci_dynamic(index - 2)  # 값 계산해서 리스트에 저장해놓고
        return mem[index]  # 리턴하기
