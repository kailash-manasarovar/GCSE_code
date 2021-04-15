# MAJOR REQUIREMENT is that the list is SORTED

def binary_search(list_of_items, search_item):

    # beginning_of_list points to the beginning_of_list item in the list
    beginning_of_list = 0
    # end_of_list points to the end_of_list item in the list
    end_of_list = len(list_of_items) - 1
    # we assume we have not yet found the item
    found = False

    # we use an iteration structure to examine the list until we find the item or there are no more items left
    # while continues to run when the list has more than 1 element AND the search_item is not yet found
    while beginning_of_list <= end_of_list and not found:

        # TEST: print trace of algorithm
        # print(list_of_items[beginning_of_list:end_of_list + 1])

        # we find the median value of the list
        middle_of_list = (beginning_of_list + end_of_list) // 2

        # we check if middle_of_list is equal to the search item
        if list_of_items[middle_of_list] == search_item:
            found = True

        # if it is unequal, we check if search_item is smaller than the item at the middle
        # here is where we chop the list in half each time
        else:
            if search_item < list_of_items[middle_of_list]:
                # we bring the end of the list to the middle
                end_of_list = middle_of_list - 1
            # if the item isn't smaller, it must be larger
            else:
                # we bring the beginning of the list to the middle
                beginning_of_list = middle_of_list + 1

    # we return whether we find the item or not
    return found


#print(binary_search(['Ahmed', 'Ann'...], 'Stephen'))
#print(binary_search([1, 6, 9, 13, 15, 21, 28, 36, 42, 69, 76, 85, 94], 9))
print(binary_search([1, 2, 5, 6, 8, 9, 11, 21], 7))
#print(binary_search([1,2,3,5,8], 5))
#print(binary_search(['a','c','d','e','f'],'c'))


import random

size_of_list = int(input("Please enter the size of the random list. "))

my_list = random.sample(range(0,1000000),size_of_list)
#print(my_list)
my_list.sort()
#print(my_list)

print('Let\'s search the list! And see how long it takes!')

import time

# take a start time
start_time = time.time()
# run the algorithm
print(binary_search(my_list, 5))
# take a finish time
finish_time = time.time() - start_time
rounded_time = (round(finish_time,5))

print("It took in seconds: {:0.5f} ".format(rounded_time))