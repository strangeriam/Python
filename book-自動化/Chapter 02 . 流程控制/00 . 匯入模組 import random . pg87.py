# 一次匯入多個模組.
import random, sys, os, math

# 模組 random
# random.randint() , 功能是隨機求取傳給它的 2 個整數之間的一個整數值.
import random
for i in range(5):
  print(random.randint(1, 10))

# 輸出:
6
4
7
8
3
[Finished in 132ms]
