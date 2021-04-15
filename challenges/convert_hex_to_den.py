# def convert(hex_number):
#
#     result = int(hex_number, 16)
#
#     return result
#
#
# hex_number1 = input("Please enter a hex number.")
# hex_number2 = input("Please enter a hex number.")
# #print(convert(hex_number))
# print(convert(hex_number1) + convert(hex_number2))


# score = 10
# answer = 9
# if answer == 10:
#     score = score + 1
# else:
#     score = score + 5
# print(score)


def decimal(hex_number):

    # STEP ONE: take the first digit
    first_digit = hex_number[0]
    if first_digit == 'A':
        first_digit = 10
    elif first_digit == 'B':
        first_digit = 11
    elif first_digit == 'C':
        first_digit = 12
    #etc

    first_digit = int(first_digit)
    #print(first_digit)

    # STEP TWO: times by 16
    total = first_digit * 16
    #print(total)

    # STEP THREE: add the second digit
    second_digit = hex_number[1]
    if second_digit == 'A':
        second_digit = 10
    elif second_digit == 'B':
        second_digit = 11
    elif second_digit == 'C':
        second_digit = 12
    # etc

    second_digit = int(second_digit)

    total = total + second_digit
    print(total)

decimal('3A')