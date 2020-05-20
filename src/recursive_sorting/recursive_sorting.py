# TO-DO: complete the helper function below to merge 2 sorted arrays
def merge(arrA, arrB):
    elements = len(arrA) + len(arrB)
    merged_arr = [0] * elements

    # Your code here
    a = 0
    b = 0

    for k in range(0, elements):
        # What do we do in here?
        # compare a and b
        #if a is out of range, push b and iterate
        if a >=len(arrA): #done with a, push b
            merged_arr[k] = arrB[b]
            b += 1
        # if b is out of range, push a and iterate
        elif b >= len(arrB):
            merged_arr[k] = arrA[a]
            a += 1
        # if a is smaller, put it in an array iterate 
        elif arrA[a] < arrB[b]:
            merged_arr[k] = arrA[a]
            a += 1
        # if b is smaller put it in an array and iterate 
        else:
            merged_arr[k] = arrB[b]
            b += 1

    return merged_arr


# TO-DO: implement the Merge Sort function below USING RECURSION
def merge_sort(arr):
    # Your code here
    if len(arr) > 1:
        # get midpoint
        mid = len(arr) // 2
        # recursively call merge_sort on LHS
        left = merge_sort(arr[:mid])
        # recursively call merge_sort on RHS
        right = merge_sort(arr[mid:])
        # merge left and right
        arr = merge(left, right)


    return arr


print(merge_sort([3, 4, 6, 1, 2, 5]))


# implement an in-place merge sort algorithm
def merge_in_place(arr, start, mid, end):
    # Your code here


    return arr


def merge_sort_in_place(arr, l, r):
    # Your code here


    return arr


# STRETCH: implement the Timsort function below
# hint: check out https://github.com/python/cpython/blob/master/Objects/listsort.txt
def timsort(arr):
    # Your code here

    return arr
