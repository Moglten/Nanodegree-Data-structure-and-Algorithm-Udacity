def sqrt(number):

    if number > 1 :
        while True:
            root = number
            precision = .5
            while abs( number - root * root ) > precision:
                root = (root + number / root) / 2
            return int(root)

    elif number == 1 :
        return 1

    elif number == 0:
        return 0

    else:
        return None


print ("Pass" if  (3 == sqrt(9)) else "Fail")
print ("Pass" if  (0 == sqrt(0)) else "Fail")
print ("Pass" if  (4 == sqrt(16)) else "Fail")
print ("Pass" if  (1 == sqrt(1)) else "Fail")
print ("Pass" if  (6 == sqrt(36)) else "Fail")
print ("Pass" if  (5 == sqrt(30.006)) else "Fail") #Trying Float
print ("Pass" if  (None == sqrt(-30)) else "Fail") #Trying negative should return None
print ("Pass" if  (31 == sqrt(1000)) else "Fail")
