capture_output=True <-- 存成 預設屬性 byte
capture_output=True, text=True <-- 存成 屬性為 string
capture_output=True, encoding='utf-8' <-- 存成 特定編碼 encoding


# 未知如何使用
cwd <-- 改變當前的工作目錄.
subprocess.run(['pwd'], cwd='/Users')

env <-- 執行時的環境變數, 該參數接受字典型別的值.
>>> subprocess.run(['env'], env={'MY_ENV': 'Hello'})
MY_ENV=Hello

shell <-- 指令會交給 shell 執行（預設為 /bin/sh, 如此一來就不再需要將指令換成 list 形式.
>>> subprocess.run('ls -alh', shell=True)
total 1248
drwxr-xr-x   14 usr  staff   448B Jun 16 14:34 .
drwxr-xr-x   21 usr  staff   672B Jun 16 10:09 ..
drwxr-xr-x   15 usr  staff   480B Jun 16 14:33 .git
-rw-r--r--    1 usr  staff    19B Jan  6 14:22 .gitignore
CompletedProcess(args='ls -alh', returncode=0)

input 參數 <-- input 預設只接受 bytes 作為輸入

check :
希望在外部指令執行發生錯誤時, 讓 Python 也跟著拋出例外 (exception),
可設定 check 參數為 True, 讓 Python 檢查指令的回傳碼 (returncode), 只要不是 0, 就會拋出錯誤.
