from pathlib import Path
my_file = Path('D:\\BeeStation\\02_python\\250402_mouseMove4\\hello.txt')

if my_file.exists():
  print('path exists')
else:
  print('no path')
