
# 呈現說明
# Tkinter 的 Text 元件通常用來輸入或編輯多行文字,
# 如果要複製部分或全部內容, 可以用滑鼠選取後按 CTRL+C 或按滑鼠右鍵選複製,
# 這樣便會被複製到作業系統的剪貼簿裡, 方便於其他軟體中貼上.

# 這種透過剪貼簿複製貼上的功能也可以用 Python Tkinter 程式碼控制.
# 視窗頂層物件 (即呼叫 tk.Tk() 建立之物件) 可利用  clipboard_append() 與 clipboard_get() 方法存取作業系統的剪貼簿以便實作複製與貼上功能.  

# 在下面的簡化範例中, 視窗中放置了一個 Text 元件, 以及四個按鈕,
# 分別是貼上, 清除, 選取複製, 與全部複製, 按下複製鈕會將選取內容存入剪貼簿,
# 按下貼上則是從剪貼簿取得暫存之內容 :

# 程式內容摘要說明如下 : 
# 呼叫視窗物件的 clipboard_append(selection) 方法可將選取內容複製到剪貼簿
# 呼叫視窗物件的 clipboard_get() 方法可取得剪貼簿內容
# 呼叫視窗物件的 clipboard_clear() 方法可清除剪貼簿
# 呼叫 Text 物件的 delete(1.0, "end") 方法可刪除 Text 物件全部內容
# 呼叫 Text 物件的 get(tk.SEL_FIRST, tk.SEL_LAST) 方法可取得被選取內容, 但未選取時會出現 _tkinter.TclError: text doesn't contain any characters tagged with "sel" 例外, 故須放在 try~except 中捕捉例外. 

import tkinter as tk
from tkinter import ttk
from tkinter import messagebox as msgbox

root=tk.Tk()  
root.title('剪貼簿複製貼上測試') 
root.geometry('500x300') 

def paste():  # 從剪貼簿貼到編輯區
    editor_text.delete(1.0, "end")   # 清除編輯區內容
    editor_text.insert(tk.INSERT, root.clipboard_get())  # 插入內容

def clear():  # 清除編輯區
    editor_text.delete(1.0, "end")   # 清除編輯區

def copy_all():
    selection=editor_text.get(1.0, tk.END) # 取得 Text 全部內容
    root.clipboard_clear()  # 清除剪貼簿
    root.clipboard_append(selection)  # 複製到剪貼簿
    msgbox.showinfo('通知訊息', '編輯區內容已全部複製到剪貼簿')

def copy_select():
    try: # 未選取會出現例外
        selection=editor_text.get(tk.SEL_FIRST, tk.SEL_LAST) # 取得被選取內容
        root.clipboard_clear()  # 清除剪貼簿
        root.clipboard_append(selection)  # 複製到剪貼簿
        msgbox.showinfo('通知訊息', '選取內容已複製到剪貼簿')
    except Exception as e:
        msgbox.showinfo('通知訊息', '未選取內容') 

editor_text=tk.Text(root, width=70, height=12)
editor_text.pack(fill=tk.X, expand=True)
paste_btn=ttk.Button(root, text='貼上', command=paste)
paste_btn.pack(side=tk.LEFT)
clear_btn=ttk.Button(root, text='清除', command=clear)
clear_btn.pack(side=tk.LEFT)
copy_select_btn=ttk.Button(root, text='選取複製', command=copy_select)
copy_select_btn.pack(side=tk.LEFT)
copy_all_btn=ttk.Button(root, text='全部複製', command=copy_all)
copy_all_btn.pack(side=tk.LEFT)

root.mainloop()
