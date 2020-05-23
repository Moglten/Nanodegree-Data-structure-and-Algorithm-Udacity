def merge_sort(lista):
    if len(lista)<= 1:
         return lista
    mid = len(lista)//2
    left = merge_sort(lista[:mid])
    right = merge_sort(lista[mid:])

    return merged(left,right)

def merged(l,r):
    sorted_list = []
    x = 0
    y= 0
    while x<len(l) and y<len(r):
        if l[x] < r[y]:
            sorted_list.append(l[x])
            x+=1
        elif l[x] > r[y]:
            sorted_list.append(r[y])
            y+=1
    sorted_list+= l[x:]
    sorted_list+= r[y:]
    return sorted_list



def rearrange_digits(input_list):
    """
        Find the index by searching in a rotated sorted array

        Args:
           input_list(array), number(int): Input array to search and the target
        Returns:
           int: Index or -1
        """

    if len(input_list) == 0 :
        return []

    elif len(input_list) == 1:
        return input_list

    input_list = merge_sort(input_list)
    num1 = ""
    num2 = ""
    x = len(input_list)-1
    while x>0:
        num1 += str(input_list[x])
        num2 += str(input_list[x-1])
        x-=2
        if x == 0 :
            num1 += str(input_list[x])

    return [int(num1),int(num2)]


def test_function(test_case):
    output = rearrange_digits(test_case[0])
    solution = test_case[1]
    if sum(output) == sum(solution):
        print("Pass")
    else:
        print("Fail")

test_case = [[4, 6, 2, 5, 9, 8], [964, 852]]
test_function(test_case)

test_case1 = ([[1, 2, 3, 4, 5], [542, 31]])
test_function(test_case1)

test_case2 = [[ 2, 5, 9, 8], [95, 82]]
test_function(test_case2)

test_case3 = [[ 2], [2]]
test_function(test_case3)

test_case4 = [[], []]
test_function(test_case4)

test_case5 = [[3,2], [3,2]]
test_function(test_case5)






