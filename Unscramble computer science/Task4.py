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
TASK 4:
The telephone company want to identify numbers that might be doing
telephone marketing. Create a set of possible telemarketers:
these are numbers that make outgoing calls but never send texts,
receive texts or receive incoming calls.

Print a message:
"These numbers could be telemarketers: "
<list of numbers>
The list of numbers should be print out one per line in lexicographic order with no duplicates.
"""

telemarketersNumbers = []
abondonList = []


outGoingCalls = list(set([ calls[x][0] for x in range(len(calls)) ]))
answeringCalls = list(set([ calls[x][1] for x in range(len(calls)) ]))

goingText =[ texts[x][0] for x in range(len(texts)) ]
receivingText = [ texts[x][1] for x in range(len(texts)) ]

totalText = list(set(goingText+receivingText))

#iterate over all Number And take what is TeleMarket Of it

for i in range(len(outGoingCalls)):

    for j in range(len(answeringCalls)):

        if outGoingCalls[i] == answeringCalls[j]:
            abondonList.append(outGoingCalls[i])

    for y in range(len(totalText)):

        if outGoingCalls[i] == totalText[y] :
            abondonList.append(outGoingCalls[i])


telemarketersNumbers = sorted([x for x in outGoingCalls if x not in abondonList])

#Printing

print("These numbers could be telemarketers: ")
for i in range(len(telemarketersNumbers)):
    print(telemarketersNumbers[i] )

