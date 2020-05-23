In Greedy Algorithm 

- U taking that choice give u max benefit neverless after that u take ducsion just for now .


-Examlple Code1-
------------------------------------------------------------------
Given arrival and departure times of trains on a single day in a railway platform, find out the minimum number of platforms 
required so that no train has to wait for the other(s) to leave.

You will be given arrival and departure times in the form of a list.

Note: Time hh:mm would be written as integer hhmm for e.g. 9:30 would be written as 930. Similarly, 13:45 would be given as 1345
-----------------------------------------------------------------------------------------------------------
Solution:-

from queue import PriorityQueue
def min_platforms(arrival, departure):
    #departure

    platforms =PriorityQueue()
    if platforms.qsize() == 0:
        platforms.put_nowait(departure[0])

    for i in range(1,len(arrival)):
        if arrival[i]>=platforms.queue[0]:
            platforms.get_nowait()
            platforms.put_nowait(departure[i])
        else :
            platforms.put_nowait(departure[i])

    return platforms.qsize()


-Examlple Code1-
------------------------------------------------------------------
Given arrival and departure times of trains on a single day in a railway platform, find out the minimum number of platforms 
required so that no train has to wait for the other(s) to leave.

You will be given arrival and departure times in the form of a list.

Note: Time hh:mm would be written as integer hhmm for e.g. 9:30 would be written as 930. Similarly, 13:45 would be given as 1345
-----------------------------------------------------------------------------------------------------------
Solution:-

from queue import PriorityQueue
def min_platforms(arrival, departure):
    #departure

    platforms =PriorityQueue()
    if platforms.qsize() == 0:
        platforms.put_nowait(departure[0])

    for i in range(1,len(arrival)):
        if arrival[i]>=platforms.queue[0]:
            platforms.get_nowait()
            platforms.put_nowait(departure[i])
        else :
            platforms.put_nowait(departure[i])

    return platforms.qsize()



-Examlple Code(1)-
------------------------------------------------------------------
Given arrival and departure times of trains on a single day in a railway platform, find out the minimum number of platforms 
required so that no train has to wait for the other(s) to leave.

You will be given arrival and departure times in the form of a list.

Note: Time hh:mm would be written as integer hhmm for e.g. 9:30 would be written as 930. Similarly, 13:45 would be given as 1345
-----------------------------------------------------------------------------------------------------------
Solution:-

from queue import PriorityQueue
def min_platforms(arrival, departure):

    platforms =PriorityQueue()

    if platforms.qsize() == 0:
        platforms.put_nowait(departure[0])

    for i in range(1,len(arrival)):

        if arrival[i]>=platforms.queue[0]:
            platforms.get_nowait()
            platforms.put_nowait(departure[i])
        else :
            platforms.put_nowait(departure[i])

    return platforms.qsize()


-Examlple Code(2)-
------------------------------------------------------------------
Starting from the number 0, find the minimum number of operations required to reach a given positive target number. You can only use the following two operations:

1. Add 1
2. Double the number
-----------------------------------------------------------------------------------------------------------
Solution:-


def min_operations(number):
    steps = 0
    while number > 0:
        if number % 2 == 0 :
            number /= 2
            steps += 1
        else :
            number -=1
            steps += 1
    return steps











