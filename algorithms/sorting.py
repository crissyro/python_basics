from time import time


def time_test(sort):
    def wrapper(*args, **kwargs):
        start_time = time()
        result = sort(*args, **kwargs)
        end_time = time()
        print(f"lead time {sort.__name__}: {end_time - start_time} seconds")
        return result

    return wrapper


# usage example

#  @algorithms.sorting.time_Test
#  def insertion_sorting_test(list):
#   return /../..insertion_Sort(list)


def selection_sort(lst: list):
    n = len(lst)
    for i in range(n - 1):
        m = i
        for j in range(i + 1, n):
            if lst[j] < lst[m]:
                m = j
        lst[i], lst[m] = lst[m], lst[i]

    return lst


def insertion_sort(lst: list):
    n = len(lst)
    for i in range(1, n):
        for j in range(i, 0, -1):
            if lst[j] < lst[j - 1]:
                lst[j], lst[j - 1] = lst[j - 1], lst[j]
            else:
                break

    return lst
