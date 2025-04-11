# absolute 絕對

from pathlib import Path

Path.cwd() # WindowsPath('C:/Users/Rlulu/AppData/Local/Programs/Python/Python311')

Path.cwd().is_absolute() # True

Path.cwd('spam/bacon/eggs').is_absolute() # False
