testCaseNum = int(input(""))
for i in range(int(testCaseNum)):
    sum = 0
    sequence_len = int(input(""))
    user_input_nums = input("").split(" ", sequence_len)
    for i in range(len(user_input_nums)): 
        sum = sum + ((-1)**i)*int(user_input_nums[i])
    print(sum)


