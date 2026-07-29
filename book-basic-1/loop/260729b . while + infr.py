# This loop will run forever until it hits a 'break'

count = 0

while True:
	if count >= 3:
		print('Debug: BREAK ..')
		break

	# Add 1 to count every time the loop runs
	count += 1
	print('count:', count)
