
# ================
import re
phoneNumRegex = re.compile(r'\d\d\d-\d\d\d-\d\d\d\d')
mo = phoneNumRegex.search('Cell: 415-555-9999 Work: 212-555-0000')
a = mo.group()
print(a) # 415-555-9999

# ================
import re
phoneNumRegex = re.compile(r'\d\d\d-\d\d\d-\d\d\d\d') #--> has no groups
b = phoneNumRegex.findall('Cell: 415-555-9999 Work: 212-555-0000')
print(b) # ['415-555-9999', '212-555-0000']

# ================
import re
phoneNumRegex = re.compile(r'(\d\d\d)-(\d\d\d)-(\d\d\d\d)')
c = phoneNumRegex.findall('Cell: 415-555-9999 Work: 212-555-0000') #--> has groupss
print(c) # [('415', '555', '9999'), ('212', '555', '0000')]
