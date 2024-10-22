Learning A : 寫一個名為 isPhoneNumber() 的函式, 用來檢查字串在比對時是否符合此模式, 然後返回 True 或 False.
Learning B : 從一串文字找電話, 找出所有 電話號碼.

## ======================================================
## ======================================================
寫一個名為 isPhoneNumber() 的函式,
用來檢查字串在比對時是否符合此模式,
然後返回 True 或 False.

電話號碼: 415-555-4242
check 1: 檢查是否剛好 12 個字元.
check 2: 檢查區碼, text 的前 3 個字元是否為數字.
check 3: 號碼要在區碼後, 出現一個連字符號.
check 4: 再 3 個數字.
check 5: 另一個連字符號.
check 6: 最後是 4 個數字.
result: 如果都通過所有檢查, 則返回 True.

## Example Code

def isPhoneNumber(text):
  if len(text) != 12:
    return False
  for i in range(0, 3):
    if not text[i].isdecimal():
      return False

  if text[3] != '-':
    return False
  for i in range(4, 7):
    if not text[i].isdecimal():
      return False

  if text[7] != '-':
    return False
  for i in range(8, 12):
    if not text[i].isdecimal():
      return False
    return True

print('415-555-4242 is phone number:')
print(isPhoneNumber('415-555-4242'))
print('Moshi moshi is a phone number:')
print(isPhoneNumber('Moshi moshi'))

## 輸出
415-555-4242 is phone number:
True
Moshi moshi is a phone number:
False
>>> 


Learning B
## ======================================================
## ======================================================
從一串文字找電話, 找出所有 電話號碼.
415-555-1011
415-555-9999

## Example Code

def isPhoneNumber(text):
  if len(text) != 12:
    return False
  for i in range(0, 3):
    if not text[i].isdecimal():
      return False

  if text[3] != '-':
    return False
  for i in range(4, 7):
    if not text[i].isdecimal():
      return False

  if text[7] != '-':
    return False
  for i in range(8, 12):
    if not text[i].isdecimal():
      return False
    return True

## ========
message = 'Call me at 415-555-1011 tomorrow. 415-555-9999 is my office.'

# 從 message 變數取 12 個字元 到變數 chunk.
# 迴圈 1 (i == 0), chunk 的值是 message[0:12] --> 'Call me at 4'
# 迴圈 2 (i == 1), chunk 的值是 message[1:13] --> 'all me at 41'
# 迴圈 3 (i == 2), chunk 的值是 message[2:14] --> 'll me at 415'
# 迴圈 4 (i == 3), chunk 的值是 message[3:15] --> 'l me at 415-'
# ...
# 迴圈 12 (i == 11), chunk 的值是 message[11:23] --> '415-555-1011'
# ...
# 迴圈 35 (i == 34), chunk 的值是 message[34:24] --> '415-555-9999'

# 每次迴圈將 chunk 傳入 isPhoneNumber(), 檢查是否符合電話號碼.
# 如果符合, 就印出這段文字.
# 當迴圈巡完 message 所有字元, 會印出 Done.

for i in range(len(message)):
  chunk = message[i:i+12]
  if isPhoneNumber(chunk):
    print('Phone number found: ' + chunk)
print('Done')

## 輸出
Phone number found: 415-555-1011
Phone number found: 415-555-9999
Done
>>> 
