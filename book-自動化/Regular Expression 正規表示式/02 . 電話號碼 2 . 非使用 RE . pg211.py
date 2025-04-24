從一串文字找電話, 找出所有 電話號碼.

415-555-1011
415-555-9999
## ======================================================
def isPhoneNumber(text):
    if len(text) != 12: # 檢查是否剛好 12 個字元.
      return False

    for i in range(0, 3): # 檢查區碼 0 ~ 2 字串, 是否為數字.
      if not text[i].isdecimal():
        return False

    if text[3] != '-': # 第 3 個字, 是一個連字符號 '-'.
        return False

    for i in range(4, 7): # 檢查電話號碼 4 ~ 6 字串, 是否為數字.
        if not text[i].isdecimal():
            return False

    if text[7] != '-': # 第 7 個字, 是一個連字符號 '-'.
        return False

    for i in range(8, 12): # 檢查電話號碼 8 ~ 11 字串, 是否為數字.
        if not text[i].isdecimal():
              return False
    
    return True

# 從 message 變數取 12 個字元 到變數 chunk.
# 迴圈 1 (i == 0), chunk 的值是 message[0:12] --> 'Call me at 4'
# 迴圈 2 (i == 1), chunk 的值是 message[1:13] --> 'all me at 41'
# 迴圈 3 (i == 2), chunk 的值是 message[2:14] --> 'll me at 415'
# 迴圈 4 (i == 3), chunk 的值是 message[3:15] --> 'l me at 415-'
# ...
# 迴圈 12 (i == 11), chunk 的值是 message[11:23] --> '415-555-1011'
# ...
# 迴圈 35 (i == 34), chunk 的值是 message[34:24] --> '415-555-9999'
## ======================================================
message = 'Call me at 415-555-1011 tomorrow. 415-555-9999 is my office.'

for i in range(len(message)):
    chunk = message[i:i+12]

    if isPhoneNumber(chunk): # 每次迴圈將 chunk 傳入 isPhoneNumber(), 檢查是否符合電話號碼.
      print('Phone number found: ' + chunk) # 如果符合, 就印出這段文字.

    print('Done')

## 輸出
Phone number found: 415-555-1011
Phone number found: 415-555-9999
Done
>>> 
