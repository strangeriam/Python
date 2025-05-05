num1 = 48
num2 = 8

num_start = int(-num1)
num_end = int(num1) + int(num2)

num_list = []
for i in range(num_start, num_end, num2):
	num_list.append(i)


print('num_list: ', num_list) # num_list:  [-48, -40, -32, -24, -16, -8, 0, 8, 16, 24, 32, 40, 48]
