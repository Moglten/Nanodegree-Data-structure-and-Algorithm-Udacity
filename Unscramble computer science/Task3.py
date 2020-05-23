"""
Read file into texts and calls.
It's ok if you don't understand how to read files.
"""
import csv

with open('texts.csv', 'r') as f:
    reader = csv.reader(f)
    texts = list(reader)

with open('calls.csv', 'r') as f:
    reader = csv.reader(f)
    calls = list(reader)

"""
TASK 3:
(080) is the area code for fixed line telephones in Bangalore.
Fixed line numbers include parentheses, so Bangalore numbers
have the form (080)xxxxxxx.)

Part A: Find all of the area codes and mobile prefixes called by people
in Bangalore.
 - Fixed lines start with an area code enclosed in brackets. The area
   codes vary in length but always begin with 0.
 - Mobile numbers have no parentheses, but have a space in the middle
   of the number to help readability. The prefix of a mobile number
   is its first four digits, and they always start with 7, 8 or 9.
 - Telemarketers' numbers have no parentheses or space, but they start
   with the area code 140.

Print the answer as part of a message:
"The numbers called by people in Bangalore have codes:"
 <list of codes>
The list of codes should be print out one per line in lexicographic order with no duplicates.

Part B: What percentage of calls from fixed lines in Bangalore are made
to fixed lines also in Bangalore? In other words, of all the calls made
from a number starting with "(080)", what percentage of these calls
were made to a number also starting with "(080)"?

Print the answer as a part of a message::
"<percentage> percent of calls from fixed lines in Bangalore are calls
to other fixed lines in Bangalore."
The percentage should have 2 decimal digits
"""

calledByBangalore =[]
count = 0

for i in range(len(calls)):
    number1 = str(calls[i][0])
    number2 = str(calls[i][1])
    if (number1[1]=="0")and(number1[2]=="8")and(number1[3]=="0"):

        if number2[0] == "(":
            x=1
            code=""
            while number2[x] !=  ")":
                code += number2[x]
                x+=1

            if code == "080":
                count += 1

            calledByBangalore.append(code)

        elif ( number2[0]=="9" ) or ( number2[0]=="8" ) or ( number2[0]=="7" ):

            calledByBangalore.append("{}".format(number2[0:4]))

        else :

            calledByBangalore.append("140")

#using set to earse duplicates
            
calledByBangaloreAsSet = sorted(list(set(calledByBangalore)))

print("The numbers called by people in Bangalore have codes:")
for x in range(len(calledByBangaloreAsSet)):
    print(calledByBangaloreAsSet[x])

percent = "%.2f" % ((count/len(calledByBangalore))*100)

print(percent+" percent of calls from fixed lines in Bangalore are call to other fixed lines in Bangalore.")


