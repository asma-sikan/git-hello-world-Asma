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
        if left[i] <= right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1
    result.extend(left[i:])
    result.extend(right[j:])
    return result

input_str = input("Enter numbers, separated by ',': ")
input_list = input_str.split(',')
try:
    value_list = [int(x.strip()) for x in input_list]
    array = merge_sort(value_list)
    print("input_list:", input_list)
    print("value_list:", value_list)
    print("array:", array)
except ValueError:
    print("Please enter integers separated by commas.")
