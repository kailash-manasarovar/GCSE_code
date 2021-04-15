number = 0

# open the file and set a variable name 'f' to represent the file
with open("file.txt") as f:
    # use the readLines() function to read the file contents
    content = f.readlines()

    # here is the 2D array loop to check for commas and increment the number
    for i in content:
        for j in i:
            if j == ',':
                number = number + 1

print(number)