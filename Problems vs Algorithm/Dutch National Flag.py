def sort_012(input_list):
    """
     Given an input array consisting on only 0, 1, and 2, sort the array in a single traversal.

     Args:
        input_list(list): List to be sorted
     """
    if len(input_list) == 0 :
        return None

    first_index = 0
    start = 0
    last_index = len(input_list)-1
    while start <= last_index :

        if input_list[start]==0:
            input_list[start] = input_list[first_index]
            input_list[first_index] = 0
            first_index+=1
            start += 1

        elif input_list[start]==2:
            input_list[start] = input_list[last_index]
            input_list[last_index] = 2
            last_index -=1

        else:
            start+=1

    return input_list

def test_function(test_case):
    sorted_array = sort_012( test_case )
    if sorted_array == sorted( test_case ):
        print( "Pass" )
        print( sorted_array )
    elif sorted_array == None :
        print(sorted_array)
    else:
        print( "Fail" )


test_function( [0, 0, 2, 2, 2, 1, 1, 1, 2, 0, 2] )
test_function( [2, 1, 2, 0, 0, 2, 1, 0, 1, 0, 0, 2, 2, 2, 1, 2, 0, 0, 0, 2, 1, 0, 2, 0, 0, 1] )
test_function( [0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 2, 2, 2, 2, 2, 2, 2] )
test_function([])
