# Lu-260729: No work under SHELL

count = 0

while True:
	if count >= 3:
		print('Debug: BREAK ..')
		break

	# Add 1 to count every time the loop runs
	count += 1
	print('count:', count)
