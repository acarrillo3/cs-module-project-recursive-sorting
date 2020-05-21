# step one UNDERSTAND
# [ 5 9 3 7 2 8 1 6]

# spilt things apart and then put them back together
# [ 5 9 3 7 ] [2 8 1 6]

# [5 9] [3 7] [2 8] [1 6]

# [5] [9] [3] [7] [2] [8] [1] [6] this are individually are all sorted

# i
# [9]
# [5 9]
# [5]
# j

# i
# [3]

# [7]
# j

# [5 9] [3 7] [2 8] [1 6] #these subarrays are individually sorted

#     i
# [5 9]
# [3 5 7 9]
# [3 7]
#     j

#     i
# [2 8]
# [1 2 6 8]
# [1 6]
#     j

# [3 5 7 9] [1 2 6 8]

#         i
# [3 5 7 9]

#                 k
# [1 2 3 5 6 7 8 9]

# [1 2 6 8]
#         j


# TO-DO: complete the helper function below to merge 2 sorted arrays
def merge(arrA, arrB):
    elements = len(arrA) + len(arrB)
    merged_arr = [0] * elements

    # Your code here
    # put back together here
    # sorting happens here
    a = 0
    b = 0

    k = 0

    for k in range(0, elements):
        # What do we do in here?
        # compare a and b
        #if a is out of range, push b and iterate 
        if a >=len(arrA): # done with a, push b
            merged_arr[k] = arrB[b]
            b += 1
        # if b is out of range, push a and iterate 
        elif b >= len(arrB):
            merged_arr[k] = arrA[a]
            a += 1
        # if a is smaller, put it in an array iterate both
        elif arrA[a] < arrB[b]:
            merged_arr[k] = arrA[a]
            a += 1
        # if b is smaller put it in an array and iterate both
        else:
            merged_arr[k] = arrB[b]
            b += 1

    return merged_arr


# TO-DO: implement the Merge Sort function below USING RECURSION
def merge_sort(arr):
    # Your code here
    # spilt here
    # if array size > 1

        # find the middle arr
        # sort stuff in left and put stuff to the left in left
        # sort stuff in right and put stuff to the right in right

        # merge left and right 
    # if array size <= 1 return the array
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
	# start2 is the first element in the right
	# half of the list
    start2 = mid + 1

    # If the two halves we're merging are already
	# sorted, no need to do anything
    if arr[mid] <= arr[start2]:
        return

    # Two pointers to maintain start
    # of both arrays to merge
    while start <= mid and start2 <= end:

        # If element 1 is in right place
        if arr[start] <= arr[start2]:
            start += 1

        else:
            value = arr[start2]
            index = start2

            # Shift all the elements between element 1
            # element 2, right by 1.
            while index != start:
                arr[index] = arr[index - 1]
                index -= 1

            arr[start] = value

            # Update all the pointers
            start += 1
            mid += 1
            start2 += 1
			
	# we don't return anything in in-place functions
	# since we're directly mutating the input array

def merge_sort_in_place(arr, l, r):
    if l < r:
        # Same as (l + r) / 2, but avoids overflow
        # for large l and r
        m = l + (r - l) // 2

        # Sort first and second halves
        merge_sort_in_place(arr, l, m)
        merge_sort_in_place(arr, m + 1, r)

        merge_in_place(arr, l, m, r)

    return arr