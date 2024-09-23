user_inputs = input("").split(' ', 6)
total_energy_consumption = 0
user_times = []
relative_starting_time = 0
inbetween_interval = 0
for i in range(int(user_inputs[0])):
    user_times += input("").split(' ', 2)
for i in range(len(user_times)//2):
    active_interval = int(user_times[1+2*i])-int(user_times[2*i])
    inbetween_interval = int(user_times[2*i])-relative_starting_time 
    total_energy_consumption += int(active_interval) * int(user_inputs[1])
    relative_starting_time = int(user_times[1+2*i])
    if i == 0:
        continue
    if inbetween_interval < int(user_inputs[4]):
        total_energy_consumption += (inbetween_interval)*int(user_inputs[1])
    elif int(user_inputs[5])+int(user_inputs[4]) > inbetween_interval >= int(user_inputs[4]):
        total_energy_consumption += int(user_inputs[4])*int(user_inputs[1]) + (inbetween_interval-int(user_inputs[4]))*int(user_inputs[2])
    else:
        total_energy_consumption += int(user_inputs[4])*int(user_inputs[1]) + int(user_inputs[5])*int(user_inputs[2]) + (inbetween_interval-int(user_inputs[4])-int(user_inputs[5]))*int(user_inputs[3])
print(total_energy_consumption)
