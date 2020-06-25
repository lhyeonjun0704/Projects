from tkinter import *

win = Tk()

lbl = Label(win, text= "이름")
txt = Entry(win)
btn = Button(win, text = "OK", width = 15)

# 격자 배치하기(1행 배치)
lbl.grid(row = 0, column = 0)
txt.grid(row = 0, column = 1)
btn.grid(row = 0, column = 2)

# 절대위치 배치하기
#lbl.place(x = 100, y = 0)

# fg = 글자색, bg = 배경색
#lbl = Label(fg = 'blue', bg = "yellow")

# font는 글씨체, 크기, 옵션
Label(font = ('현대하모니L', 16, 'bold'))

#cursor : 커서 스타일

#justify : 정렬(L / C / R)
Label(justify = CENTER)

# command : 이벤트 처리함수
Button(command = callback)

# borderwidth = 숫자(픽셀) : 경계선 두께
Label(borderwidth = 숫자(픽셀))

# relief : 경계선 모양(FLAT, RAISED, SUNKEN, FLAT, RIDGE, GROOVE, SOLID)
Label(root, relief = GROOVE)

# 위젯 속성 변경
# 위젯 객체 생성시 parameter값 지정.
widget = tkinter.Frame(root, background = 'red')

# 객체 생성후 configure()메서드로 변경하기
widget.configure(background = 'red')
widget.config(background = 'red')

# 사전형식을 이용하여 parameter값 변경
widget['background'] = 'red'

win.mainloop()
