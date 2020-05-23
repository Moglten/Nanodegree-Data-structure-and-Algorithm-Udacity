def pair_sum_to_zero(input_list, target):
    """
    Given a List to see if have two values is equal to target

    Args:
       input_list : List to search in it
       targert : integer
    Returns:
      list : list of two index its elements equal to target
    """
    index_dict = dict()
    for index, element in enumerate(input_list):
        if target - element in index_dict:
            return [index_dict[target - element], index]
        index_dict[element] = index
        
