# Example
stage 1:
    定義 calcProd() 函式.
    以迴圈巡遍 1 到 99999 的整數.
    返回他們相乘的積.
stage 2:
    呼叫 time.time(), 將結果存放 startTime.
    呼叫 calcProd()
    呼叫 time.time(), 將結果存放 endTime.
stage 3:
    印出 calcProd(), 返回乘積的長度.
stage 4:
    印出 執行 calcProd() 所花費的時間.

# Example code 
import time

def calcProd():
    # Calculate the product of the first 100,000 numbers.
    product = 1
    for i in range(1, 100000):
        product = product * i
    return product

startTime = time.time()
prod = calcProd()
endTime = time.time()
print('The result is %s digits long.' % (len(str(prod))))
print('Took %s seconds to calculate.' % (endTime - startTime))

# 輸出
The result is 456569 digits long.
Took 2.7750282287597656 seconds to calculate.
>>> 
