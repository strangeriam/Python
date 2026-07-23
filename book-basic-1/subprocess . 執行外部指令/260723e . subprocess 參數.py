capture_output=True <-- 存成 預設屬性 byte
capture_output=True, text=True <-- 存成 屬性為 string
capture_output=True, encoding='utf-8' <-- 存成 特定編碼 encoding

cwd <-- 改變當前的工作目錄.
subprocess.run(['pwd'], cwd='/Users')



# 未知的使用
check :
希望在外部指令執行發生錯誤時, 讓 Python 也跟著拋出例外 (exception),
可設定 check 參數為 True, 讓 Python 檢查指令的回傳碼 (returncode), 只要不是 0, 就會拋出錯誤.
