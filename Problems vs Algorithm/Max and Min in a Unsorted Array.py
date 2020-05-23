def get_min_max(ints):
    if len(ints) == 0 :
        return None
    min = ints[0]
    max = ints[0]
    for num in ints :
        if num > max :
            max = num
        if num < min:
            min = num
    return min,max

## Example Test Case of Ten Integers
import random

l = [i for i in range(0, 10)]  # a list containing 0 - 9
random.shuffle(l)

print ("Pass" if ((0, 9) == get_min_max(l)) else "Fail")
print(get_min_max([]))
print(get_min_max([0,0,0,0,0,0,0,0,0,0]))

