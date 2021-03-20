nums = [2, 6 ,88, 45, 3, 8, 0, 1, 0 ,3 ,4, 2 ,34, 789, 43, 12 ,1]

def swap(arr, index_1, index_2):
    temp = arr[index_1]
    arr[index_1] = arr[index_2]
    arr[index_2] = temp

def bubble_sort(arr):
    for index in arr:
        for index in range(len(arr) - 1):
            if arr[index] > arr[index+1]:
                swap(arr, index, index+1)
    return arr

print(bubble_sort(nums))