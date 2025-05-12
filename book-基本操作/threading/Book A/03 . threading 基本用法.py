thread = threading.Thread(target=function, args)
# function 要在執行緒裡執行的函式
# args 函式所需的引數，使用 tuple 格式，如果只有一個參數，格式 (參數,)

建立 threading 之後，就可以使用下列常用的方法：

方法	說明
start()	啟用執行緒。
join()	等待執行緒，直到該執行緒完成才會進行後續動作。
ident	取得該執行緒的標識符。
native_id	取得該執行緒的 id。
is_alive()	執行緒是否啟用，啟用 True，否則 False。
