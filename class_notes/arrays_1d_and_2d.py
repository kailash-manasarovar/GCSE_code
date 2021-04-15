# normally a list is OK
# arrays better for large amounts of data and when doing mathematical calculations on the data



# list
# l = [1.0, 2.0, 3.0]
# print(type(l))
# #
# print(l)
# a = array(l)
# print(a)
# print(a.shape)
# print(a.dtype)

#
# from numpy import empty
# a = empty([3,3])
# print(a)
# print(a.shape)
# print(a.dtype)
# #
# #
# # create zero array
# from numpy import zeros
# a = zeros([3,5])
# print(a)
# # #
# # #


# from numpy import array
#
# filled_array = [[0, 1, 2, 3],
#                [4, 5, 6, 7],
#                 [8, 9, 10, 11]]
# # # #
# fa = array(filled_array)
# print(fa)
# print(fa[2][0])
#
# # array_name[row, col]
#
# colour_array = ['red', 'green', 'blue', 'pink', 'brown']
# print(len(colour_array))
# for i in range(0, len(colour_array)):
#     print(colour_array[i])
#
#
# resting_pulse = [[65, 73, 70],
#                 [69, 75, 68],
#                 [70, 80, 65],
#                 [68, 79, 69]]
#
# rp = array(resting_pulse)
# #print(rp)
#
# print(rp[0][1])
# print(rp[2][2])
#
# for day in range(0, 4):
#     total = 0
#     for time in range(0, 3):
#         total = total + rp[day][time]
#     print('Average =', total/3)
#

# Sequence - step by step instructions, 72, 73, 76, 78
# Selection - if else
# Iteration - loops

# cupcakes = ["Vanilla", "Banana", "Strawberry", "Cherry", "Caramel"]
# user_input = input("What flavour would you like")
# result = False
#
# for i in cupcakes: # for i=0 TO LENGTH(cupcakes)
#     if user_input == i:
#         result = True
#     #else:
#         #print("We don't have this flavour")
#
# if result == True:
#     print("Flavour is there")
# else:
#     print("Not there")

#name = "Dulmin"
#print(type(name))

# distanceRun = [[9, 10, 8, 12, 0, 6, 9],
#               [10, 12, 15, 15, 0, 0, 10],
#               [15, 14, 13, 16, 0, 8, 9],
#               [6, 8, 9, 10, 12, 12, 0]]
#
#
# runner = 0
#
# print(distanceRun[runner])
#
# total_miles = 0
#
# for i in distanceRun[runner]:
#     total_miles = total_miles + i
#
# j=0
# print(len(distanceRun[j]))
#
# for i in range(0, len(distanceRun[runner])):
#     total_miles = total_miles + distanceRun[runner][i]
#     print(distanceRun[runner][i])
#
# print(total_miles)
#
#
# for row in range(0, len(distanceRun)):
#     #print("row = ", row)
#     for column in range(0, len(distanceRun[row])):
#         #print("column = ", column)
#         miles = distanceRun[row][column]
#         kilometre = miles * 1.6
#         #print("Miles = ", str(miles) + " : Kilometre = ", str(kilometre))
#
#
rows=4
columns=6
myArray=[[86 for column in range(columns)] for row in range(rows)]
print(myArray)

# print out a row at a time
#for row in range(rowLength):
#    print(myArray[row])

# print every element one by one
for row in range (0, rows):
    for col in range(0, columns):
        #print("Row = ", row, "Col = ", col)
        print(myArray[row][col])