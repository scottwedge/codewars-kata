#!/usr/bin/env

#There is a queue for the self-checkout tills at the supermarket. Your task is write a function to calculate the total time required for all the customers to check out!
#input

#    customers: an array of positive integers representing the queue. Each integer represents a customer, and its value is the amount of time they require to check out.
#    n: a positive integer, the number of checkout tills.

#output

#The function should return an integer, the total time required.
#Important
#
#Please look at the examples and clarifications below, to ensure you understand the task correctly :)
#Examples

#queue_time([5,3,4], 1)
# should return 12
# because when n=1, the total time is just the sum of the times

#queue_time([10,2,3,3], 2)
# should return 10
# because here n=2 and the 2nd, 3rd, and 4th people in the 
# queue finish before the 1st person has finished.

#queue_time([2,3,10], 2)
# should return 12

#Clarifications

#    There is only ONE queue serving many tills, and
#    The order of the queue NEVER changes, and
#    The front person in the queue (i.e. the first element in the array/list) proceeds to a till as soon as it becomes free.

#N.B. You should assume that all the test input will be valid, as specified above.

#P.S. The situation in this kata can be likened to the more-computer-science-related idea of a thread pool, with relation to running multiple processes at the same time: https://en.wikipedia.org/wiki/Thread_pool

def q(lst, num):
    # Start with empty queues 
    # First n list values go into different queues represented by a different list
    # Subtract the minimum of all values from all and create a new list of non-zero values
    # replace the zero-sized queue(s) with the next value(s) in list and repeat until end of list
    
    count = 0

    l = []  # Initialize list
    for j in range(num):
        l.append(0)

    # Replace any 0's in list with next value from queue

    index = 0
    while index < len(lst) + 1: # Cycle through all values in list
        # If any of the queues are zero, fill it with next value in list
        for j in l:
            if j == 0: 
                new_list.append(lst[index])  # Replace zero value with next value in queue
                index += 1
            else:
                new_list.append(j)  # Re-use existing value
     
        m = min(new_list)  # Determine smallest value in all queues

        l = []  # Init new list
        for j in new_list:
            l.append(j - m)  # Shortest queue becomes zero and will be replaced with next element in list
        count = count + m  # Update counter with time that has passed

def queue_time(lst, num):
    result = 0
    if num == 1:
        for j in lst: result = result + j
    else:
         result = q(list, num)
