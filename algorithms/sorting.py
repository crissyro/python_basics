import time


def time_Test(sort):
    def wrapper(*args, **kwargs):
        start_time = time.time()
        result = sort(*args, **kwargs)
        end_time = time.time()
        print(f"lead time {sort.__name__}: {end_time - start_time} seconds")
        return result
    return wrapper


#usage example

#  @algorithms.sorting.time_Test
#  def insertion_sorting_test(list):
   #   return /../..insertion_Sort(list)


def selection_Sort(list:list):
    n = len(list)
    for i in range(n-1):
        m = i
        for j in range(i+1, n):
            if list[j] < list[m]:
                m = j
        list[i], list[m] = list[m], list[i]

    return list


def insertion_Sort(list:list):
    n = len(list)
    for i in range(1, n):
        for j in range(i, 0, -1):
            if list[j] < list[j - 1]:
                list[j], list[j - 1] = list[j - 1], list[j]
            else:
                break

    return list