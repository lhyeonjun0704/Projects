from tkinter import *

top = Tk() # 윈도우 창 만들기
#top = Label(top, text = 'Hi!')
#top = Button(top, text = "버튼이다.")

# 여러개의 버튼 삽입하기
b = [0 for i in range(3)]
b[0] = Button(top, text = "B1")
b[1] = Button(top, text = "B2")
b[2] = Button(top, text = "B3")
for k in b:
    #k.pack(side = RIGHT) # 오른쪽으로 정렬
    k.pack(fill = X) # X축 폭에 맞추기
    #k.pack(fill = Y)

# 여백조정(위젯들 사이 여백)
# k.pack(fill = X, padx = 10, pady = 10)

# 여백조정(위젯 내부 사이 여백)
# k.pack(fill = X, ipadx = 10, ipady = 10)

#top.title('Test') # 윈도우 창 이름 넣기
#top.geometry('350x550+100+0') # 윈도우 창 크기 설정, +는 창 나타날 위치
#top.resizable(False, False) # 윈도우 창 크기 조절 허용 불가.

top.mainloop()
#top.destroy() # 위 실행들이 끝나고 윈도우를 파괴한다.