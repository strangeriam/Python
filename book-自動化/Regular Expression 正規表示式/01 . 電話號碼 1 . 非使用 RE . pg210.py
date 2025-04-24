寫一個名為 isPhoneNumber() 的函式, 用來檢查字串在比對時是否符合此模式, 然後返回 True 或 False.

電話號碼: 415-555-4242
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

print('415-555-4242 is phone number:') # 415-555-4242 is phone number:
print(isPhoneNumber('415-555-4242')) # True
print('Moshi moshi is a phone number:') # Moshi moshi is a phone number:
print(isPhoneNumber('Moshi moshi')) # False
