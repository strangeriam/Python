regex1 = re.compile('Robocop')
regex2 = re.compile('ROBOCOP')
regex3 = re.compile('robOcop')
regex4 = re.compile('RobocOp')

# =================
import re

robocop = re.compile(r'robocop', re.I)
a = robocop.search('Robocop is part man, part machine, all cop.').group()
print(a) # Robocop

b = robocop.search('ROBOCOP protect the innocent.').group()
print(b) # ROBOCOP

c = robocop.search('Al, why does your programing boot talk about robocop so much?').group()
print(c) # robocop
