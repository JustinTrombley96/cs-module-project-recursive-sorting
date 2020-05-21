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
    start2 = mid + 1
    # If the direct merge is already sorted 
    if (arr[mid] <= arr[start2]):
        return
    # Two pointers to maintain start 
    # of both arrays to merge 
    while (start <= mid and start2 <= end):
        # If element 1 is in right place 
        if (arr[start] <= arr[start2]):
            start += 1
        else:
            value = arr[start2]
            index = start2

            # Shift all the elements between element 1 
            # element 2, right by 1. 
            while (index != start):
                arr[index] = arr[index - 1]
                index -= 1
            arr[start] = value
            # Update all the pointers 
            start += 1
            mid += 1 
            start2 += 1

 

    return arr

# l is for left index and r is right index of the sub-array of arr to be sorted 
def merge_sort_in_place(arr, l, r):
    # Your code here
    if (l < r):
        # Same as (l + r) / 2, but avoids overflow 
        # for large l and r 
        m = l + (r - 1) 
        # Sort first and second halves 
        merge_sort_in_place(arr, l, m)
        merge_sort_in_place(arr, m + 1, r)
        merge_in_place(arr, l, m, r)

    return arr


# STRETCH: implement the Timsort function below
# hint: check out https://github.com/python/cpython/blob/master/Objects/listsort.txt
def timsort(arr):
    # Your code here
    pass
    return arr


