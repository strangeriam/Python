import re

namesRegex = re.compile(r'Agent \w+')
a = namesRegex.sub('CENSORED', 'Agent Alice gave the secret document to Agent Bob.')
print(a) # CENSORED gave the secret document to CENSORED.

# ==============
import

agentNamesRegex = re.compile(r'Agent (\w)\w*')
b = agentNamesRegex.sub(r'\1****', 'Agent Alice told Agent Carol that Agent Eve knew Agent Bob was a double agent.')
print(b) # A**** told C**** that E**** knew B**** was a double agent.
