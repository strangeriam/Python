import pyinputplus as pyip

response = input('Enter a number: ')
Enter a number: # --> 輸入 42
response # 42

response = pyip.inputInt(prompt='Enter a number: ')
Enter a number: # --> 輸入 cat --> 'cat' is not an integer.
Enter a number: # --> 輸入 42
response # 42
