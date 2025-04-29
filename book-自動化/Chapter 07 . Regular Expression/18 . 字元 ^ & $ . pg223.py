import re

beginsWithHello = re.compile(r'^Hello')
a = beginsWithHello.search('Hello world!')
print(a) # <re.Match object; span=(0, 5), match='Hello'>

b = beginsWithHello.search('He said hello.') == None
print(b) # True

# ===============
import re

endsWithNumber = re.compile(r'^\d+$')
c = endsWithNumber.search('Your number is 42')
print(c) # <re.Match object; span=(16, 17), match='2'>

d = endsWithNumber.search('Your number is forty two.') == None
print(d) # True

# ===============
import re

wholeStringIsNum = re.compile(r'^\d+$')
e = wholeStringIsNum.search('1234567890')
print(e) # <re.Match object; span=(0, 10), match='1234567890'>

f = wholeStringIsNum.search('12345xyz67890') == None
print(f) # True

g = wholeStringIsNum.search('12 34567890') == None
print(g) # True
