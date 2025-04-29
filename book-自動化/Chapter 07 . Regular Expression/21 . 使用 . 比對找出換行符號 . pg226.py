import re

noNewlineRegex = re.compile('.*')
a = noNewlineRegex.search('Serve the public trust.\nProtect the innocent.\nUpload the law.').group()
print(a) # Serve the public trust.

newlineRegex = re.compile('.*', re.DOTALL)
newlineRegex.search('Serve the public trust.\nProtect the innocent.\nUpload the law.').group() #
# OUTPUT:
'Serve the public trust.\nProtect the innocent.\nUpload the law.'

b = newlineRegex.search('Serve the public trust.\nProtect the innocent.\nUpload the law.').group()
print(b)
# OUTPUT:
Serve the public trust.
Protect the innocent.
Upload the law.
