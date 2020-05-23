#here i get the pivot point where i flipped the list

def find_pivot(alist,start,last):
    mid = (last+start)//2
    if mid > start and alist[mid]>alist[mid+1]:
        return mid
    if mid<last and alist[mid] < alist[mid-1]:
        return mid-1
    elif alist[start] > alist[last]:
        return find_pivot(alist,mid+1,last)
    return find_pivot(alist,start,mid-1)

#here i making a Binary search on each part after pivot and before pivot

def rotated_array_search(input_list, number):
    """
       Find the index by searching in a rotated sorted array

       Args:
          input_list(array), number(int): Input array to search and the target
       Returns:
          int: Index or -1
    """

    if len(input_list) == 0 or not(type(number) is int):
        return None

    pivot_value = find_pivot(input_list,0,len(input_list)-1)

    if number == input_list[pivot_value]:
        return pivot_value
    if number < input_list[0]:
        return binary_search(input_list, (pivot_value + 1), len(input_list)-1, number)

    return binary_search(input_list, 0, (pivot_value -1), number)

#i making binary seach here

def binary_search(lista,start,last,target):
    while last>start:
        mid = (start+last)//2
        if lista[mid] == target:
            return mid
        elif lista[mid]>target:
            last=mid
        else:
            start = mid
    return -1

#-------------------------------------------------------------

def linear_search(input_list, number):
    for index, element in enumerate(input_list):
        if element == number:
            return index
    return -1

def test_function(test_case):
    input_list = test_case[0]
    number = test_case[1]
    if linear_search(input_list, number) == rotated_array_search(input_list, number):
        print("Pass")
    elif rotated_array_search(input_list,number) == None:
        print("None")
    else:
        print("Fail")

test_function([[6, 7, 8, 9, 10, 1, 2, 3, 4], 6])
test_function([[6, 7, 8, 9, 10, 1, 2, 3, 4], 1])
test_function([[6, 7, 8, 1, 2, 3, 4], 8])
test_function([[6, 7, 8, 1, 2, 3, 4], ""])
test_function([[], 10])



