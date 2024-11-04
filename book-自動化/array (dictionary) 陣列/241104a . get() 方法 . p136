picnicItem = {'apples': 5, 'cups': 2}
'I am bringing ' + str(picnicItem.get('cups', 0)) + ' cups.'
輸出:
'I am bringing 2 cups.'
>>>

## picnicItem 裡沒有 key 'eggs', get() 返回的預設值為 0.
'I am bringing ' + str(picnicItem.get('eggs', 0)) + ' eggs.'
輸出:
'I am bringing 0 eggs.'
>>>

## 若不使用 get() 會產生錯誤.
'I am bringing ' + str(picnicItem['eggs']) + ' eggs.'
輸出:
'I am bringing 0 eggs.'
>>> 'I am bringing ' + str(picnicItem['eggs']) + ' eggs.'
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
KeyError: 'eggs'
>>>
