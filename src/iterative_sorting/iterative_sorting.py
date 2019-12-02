# TO-DO: Complete the selection_sort() function below 
def selection_sort(arr):
    # loop through n-1 elements
    for i in range(0, len(arr) - 1):
        smallest_index = i
        # TO-DO: find next smallest element
        # (hint, can do in 3 loc)
        for e in range(i + 1, len(arr)):
            if arr[e] < arr[smallest_index]:
                smallest_index = e
        # TO-DO: swap
        arr[i], arr[smallest_index] = arr[smallest_index], arr[i]
    return arr

# TO-DO:  implement the Bubble Sort function below
def bubble_sort(arr):
    swap_flag = True
    for i in range(len(arr)-1):
        for j in range(0, len(arr)-i-1):
            if arr[j+1] < arr[j]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
                swap_flag = True
        if not swap_flag:
            break
    return arr

# STRETCH: implement the Count Sort function below
def count_sort(arr):
    if len(arr) == 0: return arr
    min_value = max_value = arr[0]

    #find min and max variables
    for v in range(len(arr)):
        if arr[v] < 0: return 'Error, negative numbers not allowed in Count Sort'
        elif arr[v] < min_value: min_value = arr[v]
        elif arr[v] > max_value: max_value = arr[v]
    
    #create empty list of n size
    count_array = [0] * (max_value-min_value+1)

    #do the counting
    for n in range(len(arr)):
        count_array[arr[n]-min_value] += 1

    #sort array
    arr = []
    for i in range(len(count_array)):
        for n in range(count_array[i]):
            arr.append(i+min_value)

    return arr