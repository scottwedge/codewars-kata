#!/usr/bin/env python3

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

# Tests:
def test_1(): assert queue_time([], 1) == 0

def test_2(): assert queue_time([5], 1) == 5

def test_3(): assert queue_time([2], 5) == 2

def test_4(): assert queue_time([1,2,3,4,5], 1) == 15

def test_5(): assert queue_time([1,2,3,4,5], 100) == 5

def test_6(): assert queue_time([2,2,3,3,4,4], 2) == 9

def test_7(): assert queue_time([2,2,3,3,4,4,5], 2) == 14


def queue_time(customers, num):
    # Start with empty queues 
    # First customer values go into different queues represented by a list
    # Subtract the minimum of all values from all and create a new list of non-zero values
    # replace the zero-sized queue(s) with the next value(s) in list and repeat until end of list
    
    if customers == []: 
        return 0  # Handle corner case
    if len(customers) < num: 
        num = len(customers)

    count = 0

    old_list = []  # Initialize list
    for j in range(num):  # Initialize each queue to empty
        old_list.append(0)

    # Replace any 0's in list with next value from queue

    index = 0
    while index < len(customers): # Cycle through all values in list
        # If any of the queues are zero, fill it with next value in list
        new_list = []
        zero_count = 0  # Init counter
        for j in old_list:
            if j == 0: 
                if len(customers) > index:  # This is after the last customer
                    pass  # So do nothing
                else:
                    new_list.append(customers[index])  # Replace zero value with next value in queue
                    print("DEBUG_____ added customer: ", customers[index])
                    index += 1
                    if index == len(customers):
                        not_done = False  # Exit loop
            else:
                new_list.append(j)  # Re-use existing value
                print("DEBUG_____ reuse customer: ", j)
     
        m = min(new_list)  # Determine smallest value in all queues
        print("DEBUG_____ smallest value is: ", m)

        old_list = []  # Init list
        for j in new_list:
            old_list.append(j - m)  # Shortest queue becomes zero and will be replaced with next element in list
            print("DEBUG_____ reduced value is: {}-{}={}".format(j, m, j-m))

        count = count + m  # Update counter with time that has passed
        print("DEBUG_____  current count is: ", count)
       

    count = count + max(old_list)  # add longest of remaining queue 
    print("DEBUG_____  final count is: ", count)

    return count

