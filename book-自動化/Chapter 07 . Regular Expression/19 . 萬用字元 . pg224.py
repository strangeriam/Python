import re

atRegex = re.compile(r'.at')
a = atRegex.findall('The cat in the hat sat on the flat mat.')
print(a) # ['cat', 'hat', 'sat', 'lat', 'mat']

