number = int(input("please enter a denary number between 0 and 255"))

digit1 = number // 16
print(hex(digit1))

digit2 = number - (digit1 * 16)
print(hex(digit2))


# i = 1
# j = -1
# k = -i
# print(k)
# l = +j
# print(l)
#
#

