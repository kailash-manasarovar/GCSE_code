#decimal = int(input("please enter a number"))

decimal = 64

hex_result = ""

# decimal DIV 16
digit1 = decimal // 16
print(digit1)

# decimal MOD 16
digit2 = decimal % 16
print(digit2)

##
digit2 = hex(digit2)

hex_result = str(digit1) + str(digit2[2:])
print(hex_result)



#if digit1 >= 10:
#    digit1 = hex(digit1)
#print(digit1)
#digit2 = decimal % 16
#if digit2 >= 10:
#    digit2 = hex(digit2)
#print(digit2)





