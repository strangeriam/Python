from pathlib import Path

homeFolder = Path('D:\BeeStation\02_python\coding')
subFolder = Path('spam')
homeFolder / subFolder # WindowsPath('D:/BeeStation\x02_python/coding/spam')

str(homeFolder / subFolder) # 'D:\\BeeStation\x02_python\\coding\\spam'
