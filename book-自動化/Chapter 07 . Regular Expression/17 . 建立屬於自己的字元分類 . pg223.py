import re

vowelRegex = re.compile(r'[aeiouAEIOU]')
a = vowelRegex.findall('Robocop eats baby food. BABY FOOD.')
print(a) # ['o', 'o', 'o', 'e', 'a', 'a', 'o', 'o', 'A', 'O', 'O']

# ================
import re
consonantRegex = re.compile(r'[^aeiouAEIOU]')
b = consonantRegex.findall('Robocop eats baby food. BABY FOOD.')
print(b) # ['R', 'b', 'c', 'p', ' ', 't', 's', ' ', 'b', 'b', 'y', ' ', 'f', 'd', '.', ' ', 'B', 'B', 'Y', ' ', 'F', 'D', '.']
