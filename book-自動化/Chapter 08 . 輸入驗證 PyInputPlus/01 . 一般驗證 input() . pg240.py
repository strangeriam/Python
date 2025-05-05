# Lu-250505: 最後一行要加 等待, 不然看不到 'Your age is ' 被印出來.

import time

while True: 
	print('Enter your ago:')
	age = input()
	try:
		age = int(age)
	except:
		print('Please use numeric digits.')
		continue

	if age < 1:
		print('Please enter a positive number.')
		continue
	#break

print(f'Your age is {age}.')

time.sleep(3)
