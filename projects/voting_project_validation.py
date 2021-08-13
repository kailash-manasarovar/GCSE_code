## validate tutor group name function
def check_tutor_group_name(tutor_group_name):
    validated = True
    ## it has to have 2 or 3 characters
    if len(tutor_group_name) < 2 or len(tutor_group_name) > 3:
        validated = False
        print("The length of the tutor group name is incorrect.")
    ## it has to have a number between 7 and 11 in the beginning
    if len(tutor_group_name) == 3:
        # TESTING SPLITTING STRINGS IN PYTHON
        # my_string = "01234"
        # print(my_string[:2])
        if tutor_group_name[:2] not in ["10", "11"]:
            validated = False
            print("The year group should be 10 or 11.")
        if tutor_group_name[2:] not in ["A", "B", "C", "D", "E", "F"]:
            validated = False
            print("The tutor group for Year 10 or 11, should be A to F.")
    elif len(tutor_group_name) == 2:
        ### Debugging splitting the string
        # my_string = "7A"
        # print(my_string[:2])
        # print(my_string[:1])
        if tutor_group_name[:1] not in ["7", "8", "9"]:
            validated = False
            print("The year group should be 7, 8, or 9.")
        if tutor_group_name[1:] not in ["A", "B", "C", "D", "E", "F"]:
            validated = False
            print("The tutor group for years 7 to 9 should be A to F.")
    return validated
