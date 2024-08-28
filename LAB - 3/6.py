def bubble_sort(arr):
    n = len(arr)
    for i in range(n):
        for j in range(0, n - i - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
    return arr

def merge_sort(arr):
    if len(arr) <= 1:
        return arr
    
    mid = len(arr) // 2
    left_half = merge_sort(arr[:mid])
    right_half = merge_sort(arr[mid:])
    
    return merge(left_half, right_half)

def merge(left, right):
    sorted_list = []
    left_index = 0
    right_index = 0
    
    while left_index < len(left) and right_index < len(right):
        if left[left_index] < right[right_index]:
            sorted_list.append(left[left_index])
            left_index += 1
        else:
            sorted_list.append(right[right_index])
            right_index += 1
    
    sorted_list.extend(left[left_index:])
    sorted_list.extend(right[right_index:])
    
    return sorted_list

def selection_sort(arr):
    n = len(arr)
    for i in range(n):
        min_index = i
        for j in range(i + 1, n):
            if arr[j] < arr[min_index]:
                min_index = j
        arr[i], arr[min_index] = arr[min_index], arr[i]
    return arr

def insertion_sort(arr):
    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1
        while j >= 0 and key < arr[j]:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key
    return arr

def execute_sort(choice, arr):
    if choice == 1:
        return bubble_sort(arr)
    elif choice == 2:
        return merge_sort(arr)
    elif choice == 3:
        return selection_sort(arr)
    elif choice == 4:
        return insertion_sort(arr)
    else:
        return "Invalid choice!"


numbers = list(map(int, input("Enter the numbers : ").split()))
print("Select sorting algorithm:")
print("1. Bubble Sort")
print("2. Merge Sort")
print("3. Selection Sort")
print("4. Insertion Sort")

choice = int(input("Enter your choice : "))


sorted_numbers = execute_sort(choice, numbers)

if isinstance(sorted_numbers, list):
    print("Sorted array is:", sorted_numbers)
else:
    print(sorted_numbers)
