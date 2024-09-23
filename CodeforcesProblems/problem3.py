import math
user_input = input().split(' ', 2)
user_input = [int(i) for i in user_input]
user_sequence = input().split()
user_sequence = [int(i) for i in user_sequence]
count = 0
for i in range(0,len(user_sequence)):
    if i == len(user_sequence)-1:
        continue
    diff = user_sequence[i]-user_sequence[i+1]
    if diff ==0:
        count += 1
        user_sequence[i+1] += user_input[1]
    elif diff > 0:
        count += math.ceil(diff/user_input[1])
        user_sequence[i+1] += math.ceil(diff/user_input[1])*user_input[1]
    if user_sequence[i] == user_sequence[i+1]:
        user_sequence[i+1] += user_input[1]
        count += 1
print(count)
