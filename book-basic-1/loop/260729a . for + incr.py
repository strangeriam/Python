
count = 0

for num in range(10):
	if count >= 3:
		print('Debug: BREAK ..')
		break

	count = count + num
	print('count:', count)
