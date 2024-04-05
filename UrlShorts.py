'''ⓒ 2024. (CodeWasabi) all rights reserved.'''

from pyshorteners import *
import tkinter as tk
import clipboard
import textwrap
import webbrowser

window = tk.Tk()
window.title("URL_Shorts")
window.geometry("640x400+100+100")
window.resizable(False, False)

url_title = "URL"

def short_url_ex():
    entry_1_text = entry_1.get()
    short_url = Shortener().tinyurl.short(entry_1_text)
    label_4.config(text=short_url)                       #Short url display text
    clipboard.copy(short_url)                            #Auto copy clipboard text (Ctrl+c)

#label
label_0 = tk.Label(window, text="[ URL 변환기 ]", font=("맑은 고딕", 30))
label_1 = tk.Label(window, text=url_title, font=("맑은 고딕", 20))
label_3 = tk.Label(window, text="↓ Click ↓", font=("맑은 고딕", 20))
label_4 = tk.Label(window, text='', font=("맑은 고딕", 20))
label_0.pack()
label_1.pack()
label_3.pack()
label_4.pack()

#entry
entry_1 = tk.Entry(window,  text=textwrap.fill('', 50), width=50)
entry_1.pack()

#button
button_1 = tk.Button(window, text="URL 변환", font=("맑은 고딕", 20), command=short_url_ex)
button_1.pack()

window.mainloop()


