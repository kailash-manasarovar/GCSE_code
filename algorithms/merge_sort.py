def merge(left, right):
    # check if lists are empty
    if not len(left) or not len(right):
        return left or right

    result = []
    i, j = 0, 0
    while (len(result) < len(left) + len(right)):
        if left[i] < right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1
        if i == len(left) or j == len(right):
            result.extend(left[i:] or right[j:])
            break
    print("Merging", result)
    return result


def mergesort(list):
    print("Splitting", list)
    if len(list) < 2:
        return list

    middle = len(list) // 2
    left = mergesort(list[:middle])
    right = mergesort(list[middle:])

    return merge(left, right)


an_unordered_list = [14, 46, 43, 27, 57, 41, 45, 21, 70]
print(mergesort(an_unordered_list))
#print(an_unordered_list)


# def merge(an_unordered_list):
#     print("Splitting ", an_unordered_list)
#     if len(an_unordered_list)>1:
#         mid = len(an_unordered_list) // 2 # floor it so no floats
#         left_half = an_unordered_list[:mid]
#         right_half = an_unordered_list[mid:]
#
#         # recursive call
#         merge(left_half)
#         merge(right_half)
#
#         # set loop indexes
#         i=j=k=0
#         while i < len(left_half) and j < len(right_half):
#             if left_half[i] < right_half[j]:
#                 an_unordered_list[k]=left_half[i]
#                 i=i+1
#             else:
#                 an_unordered_list[k]=right_half[j]
#                 j=j+1
#             k=k+1
#
#         while i < len(left_half):
#             an_unordered_list[k]=left_half[i]
#             i=i+1
#             k=k+1
#
#         while j < len(right_half):
#             an_unordered_list[k]=right_half[j]
#             j=j+1
#             k=k+1
#
#     print("Merging ", an_unordered_list)

