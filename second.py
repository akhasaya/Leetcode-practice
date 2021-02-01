# bitonic array
# 1 2 3 4 5 7 8 9 12 15 17 18 20 23
# 3 2 1

def bit_index(array, left, right):
    l = right - left + 1
    if l < 1:
        return -1

    mid = left + l/2
    if array[mid] > array[mid+1] and array[mid] > array[mid -1]:
        return mid

    elif array[mid]> array[mid+1] and array[mid] < array[mid -1]:
        return bit_index(array[0:mid-1])

    elif array[mid] < array[mid+1] and array[mid] > array[mid -1]:
        return mid + 1 + bit_index(array[mid+1:])