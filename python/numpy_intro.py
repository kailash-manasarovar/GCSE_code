import numpy as np
# my_list = [1,2,3]
# x = np.array(my_list)
# print(x)


my_list = [[0, 1, 2, 3, 4, 5],
     [6, 7, 8, 9, 10, 11],
     [12, 13, 14, 15, 15, 17],
     [18, 19, 20, 21, 22, 23],
     [23, 25, 26, 27, 28, 29],
     [30, 31, 32, 33, 34, 35]]


r = np.array(my_list)

#print(r[0:6,::-7])
#print(r.reshape(36)[::7])
#print(r[:,::7])
#print(r.diagonal())
print(r[2:4,2:4])