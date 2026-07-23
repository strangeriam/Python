import subprocess

# ==========================
r = subprocess.run(['ping', '127.0.0.1'], capture_output=True)
print(r.stdout)

輸出:
# stdout 屬性預設是存 bytes
>>> r = subprocess.run(['ping', '127.0.0.1'], capture_output=True)
>>> print(r.stdout)
b'\r\nPing 127.0.0.1 (\xa8\xcf\xa5\xce 32 \xa6\xec\xa4\xb8\xb2\xd5\xaa\xba\xb8\xea\xae\xc6):\r\n\xa6^\xc2\xd0\xa6\xdb 127.0.0.1: \xa6\xec\xa4\xb8\xb2\xd5=32 \xae\xc9\xb6\xa1<1ms TTL=128\r\n\xa6^\xc2\xd0\xa6\xdb 127.0.0.1: \xa6\xec\xa4\xb8\xb2\xd5=32 \xae\xc9\xb6\xa1<1ms TTL=128\r\n\xa6^\xc2\xd0\xa6\xdb 127.0.0.1: \xa6\xec\xa4\xb8\xb2\xd5=32 \xae\xc9\xb6\xa1<1ms TTL=128\r\n\xa6^\xc2\xd0\xa6\xdb 127.0.0.1: \xa6\xec\xa4\xb8\xb2\xd5=32 \xae\xc9\xb6\xa1<1ms TTL=128\r\n\r\n127.0.0.1 \xaa\xba Ping \xb2\xce\xadp\xb8\xea\xae\xc6:\r\n    \xab\xca\xa5]: \xa4w\xb6\xc7\xb0e = 4\xa1A\xa4w\xa6\xac\xa8\xec = 4, \xa4w\xbf\xf2\xa5\xa2 = 0 (0% \xbf\xf2\xa5\xa2)\xa1A\r\n\xa4j\xac\xf9\xaa\xba\xa8\xd3\xa6^\xae\xc9\xb6\xa1 (\xb2@\xac\xed):\r\n    \xb3\xcc\xa4p\xad\xc8 = 0ms\xa1A\xb3\xcc\xa4j\xad\xc8 = 0ms\xa1A\xa5\xad\xa7\xa1 = 0ms\r\n'
>>>


# ==========================
# 輸出成字串.
r = subprocess.run(['ping', '127.0.0.1'], capture_output=True, text=True)
print(r.stdout)

輸出:
>>> r = subprocess.run(['ping', '127.0.0.1'], capture_output=True, text=True)
>>> print(r.stdout)

Ping 127.0.0.1 (使用 32 位元組的資料):
回覆自 127.0.0.1: 位元組=32 時間<1ms TTL=128
回覆自 127.0.0.1: 位元組=32 時間<1ms TTL=128
回覆自 127.0.0.1: 位元組=32 時間<1ms TTL=128
回覆自 127.0.0.1: 位元組=32 時間<1ms TTL=128

127.0.0.1 的 Ping 統計資料:
    封包: 已傳送 = 4，已收到 = 4, 已遺失 = 0 (0% 遺失)，
大約的來回時間 (毫秒):
    最小值 = 0ms，最大值 = 0ms，平均 = 0ms

>>>
