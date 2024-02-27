import timeit
import random

from insertionSort import insertion_sort
from mergeSort import merge_sort
from timSort import tim_sort


if __name__ == '__main__':
    data_small = [random.randint(0, 1_000) for _ in range(100)]
    data_medium = [random.randint(0, 10_000) for _ in range(1_000)]
    data_large = [random.randint(0, 100_000) for _ in range(10_000)]


    ts_insertion = timeit.timeit(lambda: insertion_sort(data_small), number=10)
    ts_merge = timeit.timeit(lambda: merge_sort(data_small), number=10)
    ts_tim = timeit.timeit(lambda: tim_sort(data_small[:]), number=10)

    tm_insertion = timeit.timeit(lambda: insertion_sort(data_medium), number=10)
    tm_merge = timeit.timeit(lambda: merge_sort(data_medium), number=10)
    tm_tim = timeit.timeit(lambda: tim_sort(data_medium[:]), number=10)
    
    tl_insertion = timeit.timeit(lambda: insertion_sort(data_large), number=10)
    tl_merge = timeit.timeit(lambda: merge_sort(data_large), number=10)
    tl_tim = timeit.timeit(lambda: tim_sort(data_large[:]), number=10)


    print(f"| {'Algorithm':<15} | {'Small':<15} | {'Medium':<15} | {'Large':<15} |")
    print(f"| {'-'*15} | {'-'*15} | {'-'*15} | {'-'*15} |")
    print(f"| {'Insertion Sort':<15} | {ts_insertion:15f} | {tm_insertion:15f} | {tl_insertion:15f} |")
    print(f"| {'Merge Sort':<15} | {ts_merge:15f} | {tm_merge:15f} | {tl_merge:15f} |")
    print(f"| {'Tim Sort':<15} | {ts_tim:15f} | {tm_tim:15f} | {tl_tim:15f} |")