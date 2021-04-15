# SET binary_key TO [128,64,32,16,8,4,2,1]
# OUTPUT = "Please enter 8 bit binary number"
# binary_number = INPUT
# result = 0
# FOR i = 0 TO LENGTH(binary_key)-1
# if binary_number[i] = '1'
# result = result + binary_key[i]
# RETURN result



def convert(binary_number):
    binary_list = [128, 64, 32, 16, 8, 4, 2, 1]
    result = 0

    for i in range(0, 8):
        if binary_number[i] == '1':
            result += binary_list[i]
            #print(result)

    return result


binary_number = input("Please enter an 8 bit binary number.")
print(convert(binary_number))