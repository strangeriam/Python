import re

phoneNumberRegex = re.compile(r'(\(\d\d\d\)) (\d\d\d-\d\d\d\d)')
mo = phoneNumberRegex.search('My phone number is (415) 555-4242.')
a = mo.group(1)
print(a) # (415)

b = mo.group(2)
print(b) # 555-4242
