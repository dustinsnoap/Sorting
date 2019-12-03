# TO-DO: complete the helpe function below to merge 2 sorted arrays
def merge( arrA, arrB ):
    elements = len( arrA ) + len( arrB )
    merged_arr = [0] * elements
    # TO-DO
    #NOPE
    return merged_arr


# TO-DO: implement the Merge Sort function below USING RECURSION
def merge_sort(arr):
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
    #NOPE
    return arr

def merge_sort_in_place(array, left_start=None, right_end=None): 
    #if there are no elements in this section of the array
    if right_end - left_start == 0: return
    
    #set up pointers
    if left_start == None: left_start = 0
    if right_end == None: right_end = len(array) - 1
    left_end = left_start + (right_end - left_start) // 2
    right_start = left_end + 1

    #sort left half of array section
    merge_sort_in_place(array, left_start, left_end)
    #sort right half of array section
    merge_sort_in_place(array, right_start, right_end)

    #while both array sections contain elements
    while left_start <= left_end and right_start <= right_end:
        #if left_start value is greater than right_start value
        if array[left_start] > array[right_start]:
            #remove right_start value then insert it at left_start
            array.insert(left_start,array.pop(right_start))
            #left section has a new element
            #so push left_end and right_start ahead 1 index
            right_start += 1
            left_end += 1
        left_start += 1

    return array

# STRETCH: implement the Timsort function below
# hint: check out https://github.com/python/cpython/blob/master/Objects/listsort.txt
def timsort( arr ):

    return arr
