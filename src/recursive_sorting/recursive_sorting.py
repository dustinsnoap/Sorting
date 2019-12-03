# TO-DO: complete the helpe function below to merge 2 sorted arrays
def merge( arrA, arrB ):
    elements = len( arrA ) + len( arrB )
    merged_arr = [0] * elements
    # TO-DO
    #NOPE
    return merged_arr


# TO-DO: implement the Merge Sort function below USING RECURSION
def merge_sort(arr):
    print(arr)
    if len(arr) <= 1: return arr

    left_arr = merge_sort(arr[:len(arr)//2])
    right_arr = merge_sort(arr[len(arr)//2:])

    arr = []
    while left_arr and right_arr:
        if left_arr[0] < right_arr[0]:
            arr.append(left_arr.pop(0))
        else:
            arr.append(right_arr.pop(0))

    while left_arr:
        arr.append(left_arr.pop(0))
    while right_arr:
        arr.append(right_arr.pop(0))

    return arr


# STRETCH: implement an in-place merge sort algorithm
def merge_in_place(arr, start, mid, end):
    # TO-DO

    return arr

def merge_sort_in_place(arr, l, r): 
    # TO-DO

    return arr


# STRETCH: implement the Timsort function below
# hint: check out https://github.com/python/cpython/blob/master/Objects/listsort.txt
def timsort( arr ):

    return arr
