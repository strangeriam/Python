import re

nameRegex = re.compile(r'First Name: (.*) Last Name: (.*)')
mo = nameRegex.search('First Name: Al Last Name: Sweigart')
a = mo.group(1)
print(a) # Al

b = mo.group(2)
print(b) # Sweigart

# ============
import re
nongreedyRegex = re.compile(r'<.*?>')
mo = nongreedyRegex.search('<To serve man> for dinner.>')
c = mo.group()
print(c) # <To serve man>

# ============
import re
greedyRegex = re.compile(r'<.*>')
mo = greedyRegex.search('<To serve man> for dinner.>')
d = mo.group()
print(d) # <To serve man> for dinner.>
