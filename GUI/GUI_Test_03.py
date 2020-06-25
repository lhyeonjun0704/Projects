from tkinter import *

win = Tk()

win.geometry("320x200+100+100") # 창크기(h, v), 스크린 상 위치(x,y)
lbl = Label(win, text = 'Hello')
txt = Entry(win)
btn = Button(win, text = "이름")

# 절대위치 배치하기
lbl.place(x = 0, y = 0)
txt.place(x = 100, y = 50)
btn.place(x = 200, y = 100)

win.mainloop()