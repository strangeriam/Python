# 建立圖檔放置目錄 result
# 新建位置 D:\Dropbox\12-Office-Sync-MTS\38_60GPythonPicReport\result\

from pathlib import Path
import os

os.chdir('D:\\Dropbox\\12-Office-Sync-MTS\\38_60GPythonPicReport\\')

worktmp = Path.cwd()
resultPath = 'result'
print(Path(worktmp, filename))
os.makedirs(Path(worktmp, filename))
