import pyautogui as pag
import random, time, subprocess
#터미널에서 CMD 탭에 가서 'pip install pyautogui' 를 입력하면 pyautogui 모듈을 설치한다.

def countdown(t):
    while t:
        mins, secs = divmod(t, 60)
        timeformat = '{:02d}:{:02d}'.format(mins, secs)
        print(timeformat, end='\r')
        time.sleep(1)
        t-=1








'''
def bring_window():
    time.sleep(0.5)
    apple="""
tell application "BlueStacks"
activate
end tell
    """

    apple=apple.encode()
    p = subprocess.Popen('osascript', stdin=subprocess.PIPE, stdout=subprocess.PIPE, stderr=subprocess.STDOUT)
    p.communicate(apple)[0]

bring_window()
exit()
'''






'''
while True:
    duration=random.uniform(0.1,1.5)
    pag.moveTo(
    x=random.uniform(combat_button['top_left']['x'], combat_button['bottom_right']['x']),
    y=random.uniform(combat_button['top_left']['y'], combat_button['bottom_right']['y']),
    )

combat_button = {
    'top_left':{
        'x':771,
        'y':453
        },
    'bottom_right':{
        'x':912,
        'y':542
        }
    }

pag.mouseDown()
time.sleep(random.uniform(0.10201, 0.3994))
pag.mouseUp
time.sleep(random.uniform(0.25001, 0.9994))
'''




'''
drag={
    'from':{
        'x':1364.1,
        'y':192.1},
        'to':{
            'x':1623.9,
            'y':530.9
        }
    }

while True:
    drag_start_x = random.uniform(drag['from']['x'], drag['to']['x'])
    drag_end_x = random.uniform(drag['from']['x'], drag['to']['x'])

    drag_start_y = random.uniform(drag['from']['y'], drag['to']['y'])
    drag_end_y = random.uniform(drag['from']['y'], drag['to']['y'])
    
    pag.moveTo(drag_start_x, drag_start_y, duration=random.uniform(0.1,0.9))
    pag.dragTo(drag_end_x, drag_end_y, random.uniform(0.3, 1.1), button='left')
'''