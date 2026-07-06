import random

# 데이터 개수 쓰기
data_count = 100

# 무작위 데이터 생성
basic_list = []
for i in range(data_count):
    basic_list.append(random.randint(0, 1000))
print(f"무작위 데이터: {basic_list}")

# 정렬된 데이터 생성
sorted_list = [random.randint(0, 1000 // data_count)]
for i in range(data_count - 1):
    sorted_list.append(sorted_list[-1] + random.randint(0, 1000 // data_count))
print(f"정렬된 데이터: {sorted_list}")

# 거의 정렬된 데이터 생성
almost_sorted_list = [random.randint(0, 1000 // data_count)]
for i in range(data_count - 1):
    almost_sorted_list.append(almost_sorted_list[-1] + random.randint(-600 // data_count, 1000 // data_count))
print(f"거의 정렬된 데이터: {almost_sorted_list}")

# 역순 데이터 생성
reversed_list = sorted_list[::-1]
print(f"역순 데이터: {reversed_list}\n")

def bubble_sort(arr):
    compare = 0
    swap = 0
    n = len(arr)
    for i in range(n - 1):
        for j in range(n - 1 - i):
            compare += 1
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
                swap += 1
    return arr, compare, swap

def selection_sort(arr):
    compare = 0
    swap = 0
    n = len(arr)
    for i in range(n - 1):
        min_index = i
        for j in range(i + 1, n):
            compare += 1
            if arr[j] < arr[min_index]:
                min_index = j
        if min_index != i:
            arr[i], arr[min_index] = arr[min_index], arr[i]
            swap += 1
    return arr, compare, swap

def insertion_sort(arr):
    compare = 0
    move = 0
    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1
        while j >= 0:
            compare += 1
            if arr[j] > key:
                arr[j + 1] = arr[j]
                move += 1
                j -= 1
            else:
                break
        arr[j + 1] = key
        move += 1
    return arr, compare, move

def quick_sort(arr):
    compare = 0
    swap = 0
    def partition(low, high):
        nonlocal compare, swap
        pivot = arr[high]
        i = low - 1
        for j in range(low, high):
            compare += 1
            if arr[j] <= pivot:
                i += 1
                if i != j:
                    arr[i], arr[j] = arr[j], arr[i]
                    swap += 1
        if i + 1 != high:
            arr[i + 1], arr[high] = arr[high], arr[i + 1]
            swap += 1
        return i + 1
    def quick(low, high):
        if low < high:
            pi = partition(low, high)
            quick(low, pi - 1)
            quick(pi + 1, high)
    quick(0, len(arr) - 1)
    return arr, compare, swap

# 출력
for name, data in [
    ("무작위", basic_list),
    ("정렬된", sorted_list),
    ("거의 정렬된", almost_sorted_list),
    ("역순", reversed_list)
]:
    print(f"\n===== {name} 데이터 =====")
    _, compare, swap = bubble_sort(data.copy())
    print(f"Bubble sort   : 비교 {compare:4d}회, 교환 {swap:4d}회")
    _, compare, swap = selection_sort(data.copy())
    print(f"Selection sort: 비교 {compare:4d}회, 교환 {swap:4d}회")
    _, compare, move = insertion_sort(data.copy())
    print(f"Insertion sort: 비교 {compare:4d}회, 이동 {move:4d}회")
    _, compare, swap = quick_sort(data.copy())
    print(f"Quicksort     : 비교 {compare:4d}회, 교환 {swap:4d}회")
