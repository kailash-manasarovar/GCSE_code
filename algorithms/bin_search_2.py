my_list = [1, 2, 3, 5, 8, 9, 11, 23, 24, 25, 27, 31, 32, 333, 444, 555]
n = int(input("please enter number that you are looking for"))
counter = 0
start = 0
end = len(my_list)-1
found = False
while counter < len(my_list) and found == False:
    #print(my_list[start:end])
    mid = (start + end)//2
    if n == my_list[mid]:
        found = True
    else:
        if n>my_list[mid]:
            start = mid+1
            counter = counter+1
        else:
            end = mid-1
            counter = counter +1
print(found)