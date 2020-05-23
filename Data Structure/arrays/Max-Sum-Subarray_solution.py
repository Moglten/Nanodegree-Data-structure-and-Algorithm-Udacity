
def max_sum_subarray(arr):
    '''
    :param arr: list of integers
    :return: interger of biggest sum of subarray
    '''
    max_sum = arr[0]
    current_sum = arr[0]

    for num in arr[1:]:
        current_sum = max(current_sum + num, num)
        max_sum = max(current_sum, max_sum)
    return max_sum

