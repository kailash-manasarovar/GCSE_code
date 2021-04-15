# numbers = [9, 5, 4, 15, 3, 8, 11, 2]
# number_of_items = len(numbers)
#
# for i in range(0, number_of_items-2):
#     for j in range(0, number_of_items - i - 2):
#         if numbers[j] > numbers[j + 1]:
#             temp = numbers[j]
#             numbers[j] = numbers[j + 1]
#             numbers[j + 1] = temp
#     print(numbers)

def bubble_sort(list_of_elements):
    more_swaps = True
    while more_swaps:
        more_swaps = False
        for element in range(len(list_of_elements) - 1):
            if (list_of_elements[element] > list_of_elements[element + 1]):
                more_swaps = True
                temp = list_of_elements[element]
                list_of_elements[element] = list_of_elements[element + 1]
                list_of_elements[element + 1] = temp
        print(list_of_elements)
    return list_of_elements


#a_list = [54,26,93,17,77,31,44,55,20]
#an_ordered_list = [1, 2, 3, 4, 5, 6, 7, 8, 9]
#another_list = ['cat','dog','lion','tiger','elephant','ant','giraffe']
#bubble_sort(an_ordered_list)
#print(an_ordered_list)

#time it
#get a random list




# bubblesort descending
# numbers = [9, 5, 4, 15, 3, 8, 11, 2]
# number_of_items = len(numbers)
# for i in range(number_of_items-1, 0, -1):
#     for j in range(i):
#         #print(i, " ", j)
#         if numbers[j] < numbers[j + 1]:
#             temp = numbers[j]
#             numbers[j] = numbers[j + 1]
#             numbers[j + 1] = temp
#     print(numbers)