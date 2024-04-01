import time


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
