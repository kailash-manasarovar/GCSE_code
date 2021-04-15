file = open("MyFile.txt", "w")
file.write("hello")
file = open("MyFile.txt", "a+")
file.append("hello")
print(file.read())
file.close()


# 24 a)
# string pixels = ""
# for square in bitmap image:
# if square is black:
#   pixels = pixels + "1"
# else:
#   pixels = pixels + "0"
pixels = "1110011001001111"
file = open("shape.txt", "w")
for character in pixels:
    file.write(character)
file.close()


# 24 b)
matrix = [[0, 0, 0, 0],
          [0, 0, 0, 0],
          [0, 0, 0, 0],
          [0, 0, 0, 0]]


file = open("shape.txt", "r")
for i in range(0, len(matrix)):
    for j in range(0, len(matrix[i])):
        matrix[i][j] = file.read(1)
print(matrix)
file.close()

