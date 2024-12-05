# with open('day1-input.txt', 'r+') as f:
#     left = []
#     right = []
#     for line in f:
#         # print(line)
#         tmp = line.split('   ')
#         left.append(int(tmp[0]))
#         right.append(int(tmp[1]))

#     left.sort()
#     right.sort()
#     diff = 0
#     for i in range(len(left)):
#         diff += (abs(left[i]-right[i]))
#     print(diff)

with open('day1-input.txt', 'r+') as f:
    left = []
    right = [0] * 99999
    for line in f:
        tmp = line.split('   ')
        left.append(int(tmp[0]))
        right[int(tmp[1])] += 1
    
    # print(right)
    similarity_score = 0
    for num in left:
        similarity_score += (right[num] * num)
    print(similarity_score)
