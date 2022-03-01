import pyautogui
import time

#터미널에서 CMD 탭에 가서 'pip install opencv-python' 를 입력하면 opencv 모듈을 설치한다.
#설치만 하고 opencv를 import 안하네? 모듈이 아닌가보다

'''
#방법 1
i=pyautogui.locateOnScreen('7.png')
print(i)
#위 내용을 출력하면 (x좌표값, y좌표값, x픽셀너비, y픽셀너비)

pyautogui.click(i)
#이렇게 쓰면 i안에 값이 4개이므로 클릭이 안 된다

q=pyautogui.center(i)
#로 i의 중앙 좌표 값을 가져온 후

pyautogui.click(q)

'''


#방법 2
i=pyautogui.locateCenterOnScreen('7.png')
#방법1'locateOnScreen'과  방법2'locateCenterOnScreen'에는 Center 유무 차이가 있다. (즉 이미지 좌표값을 4개 가져오냐 2개 가져오냐)2개만 가져오면 방법1에서 쓴 q=pyautogui.center(i)을 안써도 된다.

print(i)
pyautogui.click(i)

'''

#방법 3
num7=pyautogui.locateCenterOnScreen('7.png')
pyautogui.click(num7)

print(pyautogui.position())

pyautogui.screenshot('1.png', region=(1324,789,30,30))

num7 = pyautogui.locateCenterOnScreen('7.png')
pyautogui.click(num7)
'''
