keypress = input("Enter a letter")
sentence = ""

while keypress != "." and keypress != "?" and keypress != '!':
    sentence = sentence + keypress
    keypress = input("Enter a letter")

print(sentence)
