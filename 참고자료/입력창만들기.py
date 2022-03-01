from tkinter import *

# 새로운 창 설정 
win1=Tk()
win1.title('정광규 tkinter')
win1.geometry('400x400')
win1.resizable(False, False)

# 문제 지시문 라벨 설정 

lab1 = Label(win1)

lab1['text']='다음 영어 단어의 뜻을 입력하세요'

lab1.pack()


# 문제 라벨 설정 

lab2 = Label(win1)

lab2['text']=' 영어 단어 next의 의미는?'

lab2.pack()

# 입력 결과를 받을 함수와 표현할 라벨을 설정 
lab3 = Label(win1)
def 결과(n):
    lab3.config(text="입력한 내용입니다. > "+ent1.get())
    
# 입력창 설정(입력한 결과를 받을 이벤트를 설정) 
ent1=Entry(win1)
ent1.bind("<Return>", 결과)     # 엔터를 치면 결과라는 함수를 실행하라.
ent1.pack()                     # 입력 결과를 입력창에 표시
lab3.pack()                     # 결과 함수를 표시
win1.mainloop()
