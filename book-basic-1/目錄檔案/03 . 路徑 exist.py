from pathlib import Path
my_file = Path('D:\\BeeStation\\02_python\\250402_mouseMove4\\hello.txt')

# Way 1
if my_file.exists():
  print('path exists')
else:
  print('no path')

# Way 2
try:
    my_abs_path = my_file.resolve(strict=True)
except FileNotFoundError:
    print('no path')
else:
    print('path exists')
