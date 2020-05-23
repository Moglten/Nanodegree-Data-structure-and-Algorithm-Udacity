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
TASK 1:
How many different telephone numbers are there in the records? 
Print a message:
"There are <count> different telephone numbers in the records."
"""
#declare Variable
count = 0


#making List of All  Number

inComingTextNumbers =[ texts[x][0] for x in range(len(texts)) ]

answeringTextNumbers = [ texts[x][1] for x in range(len(texts)) ]

inComingCallNumbers = [ calls[x][0] for x in range(len(calls)) ]

answeringCallNumbers =[ calls[x][1] for x in range(len(calls)) ]


totalNumber = inComingTextNumbers + answeringTextNumbers + inComingCallNumbers + answeringCallNumbers

#calculation Length of Text Numbers

lengthNumber = len(totalNumber)


#convert List to  set

totalNumberAsSet = set(totalNumber)
lengthSetNumber = len(totalNumberAsSet)


count = lengthNumber - (lengthNumber-lengthSetNumber)


print("There are {} different telephone numbers in the records.".format(count))