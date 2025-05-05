import time
import pyinputplus as pyip

def addsUpToTen(numbers):
	numbersList = list(numbers)

	for i, digit in enumerate(numbersList):
		numbersList[i] = int(digit)
	if sum(numbersList) != 10:
		raise Exception('The digits must add up to 10, not %s.' %(sum(numbersList)))
	return int(numbers) #Return an int form of numbers.

response = pyip.inputCustom(addsUpToTen) # No parentheses after addsUptoTen here.

# 輸入 Enter --> Blank values are not allowed.
# 輸入 123 --> The digits must add up to 10, not 6.
# 輸入 1235 --> The digits must add up to 10, not 11.
# 輸入  1234 --> 

print('response: ', response) # response:  1234
time.sleep(3)
