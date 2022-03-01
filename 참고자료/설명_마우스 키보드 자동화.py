from tkinter import Button
import pyautogui
import time


for i in range(0,10):
  i=pyautogui.position()

  time.sleep(1)
  print(i)





        

# pyautogui.moveTo(0,0) #moveTo(x,y,time)

# pyautogui.click(click=2, interval=2) #첫 클릭 후 2초 후 두번째 클릭

# pyautogui.click(click=2)  #더블클릭
# pyautogui.doubleClick()   #더블클릭

# time.sleep(1)

# pyautogui.typewrite('hello') #헬로우 글자 입력

# pyautogui.typewrite(['enter']) #엔터키 입력

# pyautogui.typewrite(['a','b','c','enter']) #a,b,c 엔터키 순차적으로 입력
