import random
import time

#сортування злиттям
def merge_sort(arr):
    if len(arr) <= 1:
        return arr

    mid = len(arr) // 2
    left = merge_sort(arr[:mid])
    right = merge_sort(arr[mid:])

    return merge(left, right)

def merge(left, right):
    result = []
    i = j = 0

    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1

    result += left[i:]
    result += right[j:]
    return result


#сортування вставкою
def insertion_sort(arr):
    a = arr.copy()
    for i in range(1, len(a)):
        key = a[i]
        j = i - 1

        while j >= 0 and a[j] > key:
            a[j + 1] = a[j]
            j -= 1

        a[j + 1] = key
    return a


#Timsort
def timsort(arr):
    return sorted(arr)

#замір часу
def measure_time(sort_function, data):
    start = time.perf_counter()
    sort_function(data)
    return time.perf_counter() - start


#перевірка
sizes = [500, 1000, 2000]

for n in sizes:
    print(f"\n Розмір масиву: {n} ")

    data_random = [random.randint(0, 10000) for _ in range(n)]

    print("Merge Sort: ", measure_time(merge_sort, data_random))
    print("Insertion Sort: ", measure_time(insertion_sort, data_random))
    print("Timsort: ", measure_time(timsort, data_random))