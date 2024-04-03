import time
import random


# decorator for check time complete
def time_test(sort):
    def wrapper(*args, **kwargs):
        start_time = time.time()
        result = sort(*args, **kwargs)
        end_time = time.time()
        print(f"lead time {sort.__name__}: {end_time - start_time} seconds")
        return result

    return wrapper


# usage example

#  @algorithms.sorting.time_Test
#  def insertion_sorting_test(list):
#   return /../..insertion_Sort(list)

# variant of selection sort
def selection_sort(lst: list) -> list:
    for i in range(len(lst) - 1):
        m = i

        for j in range(i + 1, len(lst)):
            if lst[j] < lst[m]:
                m = j

        lst[i], lst[m] = lst[m], lst[i]

    return lst


# variant of insertion sort
def insertion_sort(lst: list) -> list:
    for i in range(1, len(lst)):
        item_to_insert = lst[i]
        j = i - 1

        while j >= 0 and lst[j] > item_to_insert:
            lst[j + 1] = lst[j]
            j -= 1

        lst[j + 1] = item_to_insert

    return lst


# variant of bubble sort

def bubble_sort(lst: list) -> list:
    for i in range(len(lst) - 1):
        for j in range(i + 1, len(lst) - 1):
            if lst[i] > lst[j]:
                lst[i], lst[j] = lst[j], lst[i]

    return lst


# variant of merge sort
def merge_sort(lst: list) -> list:
    if len(lst) > 1:
        mid = len(lst) // 2
        left = lst[:mid]
        right = lst[mid:]

        merge_sort(left)
        merge_sort(right)

        i = j = k = 0
        while i < len(left) and j < len(right):
            if left[i] <= right[j]:
                lst[k] = left[i]
                i += 1
            else:
                lst[k] = right[j]
                j += 1
            k += 1

        while i < len(left):
            lst[k] = left[i]
            i += 1
            k += 1

        while j < len(right):
            lst[k] = right[j]
            j += 1
            k += 1

        return lst


# variant of quick sort
def quick_sort(lst: list) -> list:
    if len(lst) > 1:
        x = lst[random.randint(0, len(lst) - 1)]
        low = [u for u in lst if u < x]
        eq = [u for u in lst if u == x]
        hi = [u for u in lst if u > x]
        lst = quick_sort(low) + eq + quick_sort(hi)

    return lst


# variant of heap sort
def heapify(lst: list, n, i):
    largest = i
    l = 2 * i + 1
    r = 2 * i + 2
    if l < n and lst[i] < lst[l]:
        largest = l

    if r < n and lst[largest] < lst[r]:
        largest = r

    if largest != i:
        lst[i], lst[largest] = lst[largest], lst[i]

        heapify(lst, n, largest)


def heapSort(lst: list) -> list:
    n = len(lst)

    for i in range(n, -1, -1):
        heapify(lst, n, i)

    for i in range(n - 1, 0, -1):
        lst[i], lst[0] = lst[0], lst[i]
        heapify(lst, i, 0)

    return lst
