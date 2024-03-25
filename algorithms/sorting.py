import time


def selection_sort(list:list):
    n = len(list)
    for i in range(n-1):
        m = i
        for j in range(i+1, n):
            if list[j] < list[m]:
                m = j
        list[i], list[m] = list[m], list[i]