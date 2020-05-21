# TO-DO: complete the helper function below to merge 2 sorted arrays
def merge(arrA, arrB):
    elements = len(arrA) + len(arrB)
    merged_arr = [0] * elements

    i = 0
    j = 0
    k = 0

    while i < len(arrA) and j < len(arrB):
        if arrA[i] <= arrB[j]:
            merged_arr[k] = arrA[i]
            k = k + 1
            i = i + 1

        else:
            merged_arr[k] = arrB[j]
            k = k + 1
            j = j + 1
    
    while i < len(arrA):
        merged_arr[k] = arrA[i]
        k = k + 1
        i = i + 1
    while j < len(arrB):
        merged_arr[k] = arrB[j]
        k = k + 1
        j = j + 1


    return merged_arr


# TO-DO: implement the Merge Sort function below USING RECURSION
def merge_sort(arr):
    # Your code here
    if len(arr) < 2:
        # Base case arrays with 0 or 1 element are already "sorted"
        return arr
    else:
        # Recursive case
        pivot = arr[0]
        # Sub-array of all elements less than the pivot
        less = [i for i in arr[1:] if i <= pivot]
        # Sub-array of all elements greater than the pivot
        greater = [i for i in arr[1:] if i > pivot]
        return merge_sort(less) + [pivot] + merge_sort(greater)


# implement an in-place merge sort algorithm
def merge_in_place(arr, start, mid, end):
    # Your code here
    pass

    return arr


def merge_sort_in_place(arr, l, r):
    # Your code here
    pass

    return arr


# STRETCH: implement the Timsort function below
# hint: check out https://github.com/python/cpython/blob/master/Objects/listsort.txt
def timsort(arr):
    # Your code here
    pass
    return arr


