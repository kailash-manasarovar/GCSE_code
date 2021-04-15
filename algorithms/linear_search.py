list_of_values = [8, 6, 2, 5, 4, 6]
value_to_search_for = 6

found = False

for value in list_of_values:
    if value == value_to_search_for:
        found = True
        #break

print(found)




# LINEAR SEARCH WITH WHILE
# import time
#
# def linearSearch(myList, myItem):
#     found = False
#     position = 0
#     while position < len(myList) and not found:
#         if myList[position] == myItem:
#             found = True
#         position = position + 1
#     return found
#
#
#
# list_of_elements = [4, 2, 8, 9, 3, 7]
# number_to_search_for = int(input("Enter number to search: "))
#
# starttime = time.time()
# isFound = linearSearch(list_of_elements, number_to_search_for)
# endtime = time.time()
#
# time_it_took = endtime - starttime
# formatted_time = format(round(time_it_took,5))
#
# if isFound:
#     print("Your item is in the list.")
# else:
#     print("Your item is not in the list.")
#
# print("It took " + str(formatted_time) + "milliseconds to run Linear Search.")
#



# LINEAR SEARCH WITH FOR
found = False

for i in list_of_values:
    print(i)
    if i == value_to_search_for:
        found = True
        print("%d found at %dth position"%(value_to_search_for,i))
        break

if(found == False):
    print("%d is not in list"%value_to_search_for)



