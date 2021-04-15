# # REVERSE a string
# str_input = input('Please enter a string to reverse: ')
# reverse_str = str_input[::-1]
# print(reverse_str)
#
#
# # REVERSE every word in a sentence
# str_input = input('Enter a sentence: ')
# l=str_input.split()
# l1=[]
# for word in l:
#     l1.append(word[::-1])
#     output=' '.join(l1)
# print(output)
#
#
# # REVERSE every second word
# count = 0
# l2 = []
# while count < len(l):
#     if count % 2 == 0:
#         l2.append(l[count])
#     else:
#         l2.append(l[count][::-1])
#     count = count + 1
# output = ' '.join(l2)
# print(output)
#
#
# # ODD AND EVEN indexing
# s = input('Enter a sentence:')
# print('Characters present at Even Index:')
# i = 0
# while i < len(s):
#     print(s[i])
#     i=i+2
# print('Characters present at Odd Index:')
# i = 1
# while i < len(s):
#     print(s[i])
#     i=i+2
#
# # OR
# s = input('Enter a sentence:')
# print('Characters present at Even Index:',s[0::2])
# print('Characters present at Even Index:',s[::2])
# print('Characters present at Odd Index:',s[1::2])
#
#
# # MERGE characters from 2 strings into a single string
# # 1. when strings are same length
# s1 = 'aaaaaa'
# s2 = 'bbbbbb'
# output=''
# i,j=0,0
# while i < len(s1) or j < len(s2):
#     output = output + s1[i] + s2[j]
#     i=i+1
#     j=j+1
# print(output)
# # OR
# s3 ='cccccc'
# s4 = 'dddddd'
# l =list(map(lambda x,y : x+y, s3, s4))
# print(''.join(l))
# # 2. when strings have different length
# s5 = input('Enter first string:')
# s6 = input('Enter second string:')
# output=''
# i,j=0,0
# while i < len(s5) or j < len(s6):
#     if i < len(s5):
#         output=output+s5[i]
#         i=i+1
#     if j < len(s6):
#         output=output+s6[j]
#         j=j+1
# print(output)
#
#
#
# SORT characters of string input
#input:B4A1D3
#output:ABD134
# s='B4A1D3'
# alphabets=[]
# digits=[]
# for ch in s:
#     if ch.isalpha():
#         alphabets.append(ch)
#     else:
#         digits.append(ch)
# output = ''.join(sorted(alphabets) + sorted(digits))
# print(output)
#
#
#
# REVERSE RLE
# input:a4b3c2
# output:aaaabbbcc
# s=input('Enter some string where alphabet symbol should be followed by digit:')
# output=''
# for ch in s:
#     if ch.isalpha():
#         x=ch
#     else:
#         d=int(ch)
#         output=output+x*d
# print(output)
#
#
#
#
# RLE
# input:aaaabbbccz
# output:4a3b2c1z
s='aaaabbbcczzzz'
output=''
previous = s[0]
c=1
i=1
while i < len(s):
    if s[i] == previous:
        c=c+1
    else:
        output=output+str(c)+previous
        previous=s[i] # update letter
        c=1 # reset count
    if i == len(s)-1: # deal with the final case where there is no way to get to above else
        output=output+str(c)+previous
    i=i+1
print(output)
#
#
#
#
# Input: a4k3b2
# Output: aeknbd
s='a4k3b2'
output=''
for ch in s:
    if ch.isalpha():
        x=ch
        output=output+ch
    else:
        d=int(ch)
        newc = chr(ord(x)+d)
        output=output+newc
print(output)