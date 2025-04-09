# 事前準備: 在 D:\\BeeStation\\02_python\\250402_mouseMove4 已存在子目路 hi.

from pathlib import Path
dirname = Path('D:\\BeeStation\\02_python\\250402_mouseMove4\\hi')

if dirname.is_dir():
  print('directory exists')
else:
  print('no directory')
