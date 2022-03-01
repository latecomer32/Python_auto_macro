import pyautogui as py
from tkinter import *
from tkinter import messagebox
import pyperclip
import time
import os
import shutil

#변수선언
coordinate_list=[]
dataNum=[]
motion_num, signal_num, coordinate_num, co_signal_num=0,0,0,0
type_write_text=''
motion_log=None
selectmode_signal=''
select_num=int
#함수 선언

#프로그램 시작시 발동하는 함수
def start_Macro():
    global select_num
    print("start_Macro()")
    create_macro_recording_btn()
    create_macro_paly_btn()
    create_macro_file_edit_btn()
    create_macro_exit_btn()
    select_num=1
    selectmode_signal_func()
    create_macro_catalog()

    #test_create_delete_preview_btn()

def test_create_delete_preview_btn():
    print("create_macro_recording_btn()")
    global test_delete_preview_btn
    test_delete_preview_btn=Button(win, text = "테스트_프리뷰 삭제)", fg="black",bg="gray",command=delete_preview_motion_log_box)
    test_delete_preview_btn.grid(row=6, column=0, padx=10, pady=5, ipadx=10, ipady=5)
    #win.bind("<r>",recording_key)





# 매크로 녹화 버튼 클릭 함수
def macro_recording_btn_click():
    print("macro_recording_btn_click()")
    try:
        delete_preview_motion_log_box()
    except:
        pass
    messagebox.showinfo("기록시작","1/2단계 기록.\n반복할 모션을 기록하세요.")
    turn_on_motion_shortcut_key()
    create_recording_finish_btn()
    create_motion_log()
    delete_macro_recording_btn()
    delete_macro_paly_btn()
    delete_macro_file_edit_btn()
    try:
        delete_macro_catalog()
        delete_preview_motion_log_box
    except:
        pass

# 마우스 좌표, 클릭, 키보드 입력등 실행 단축키 On & off
def turn_on_motion_shortcut_key():
    print("turn_on_motion_shortcut_key()")
    win.bind("<space>", mouse_move)
    win.bind("<c>", left_click)
    win.bind("<v>", right_click)
    win.bind("<Return>", type_write)

def turn_off_motion_shortcut_key():
    print("turn_off_motion_shortcut_key()")
    win.unbind("<space>")
    win.unbind("<c>")
    win.unbind("<v>")
    win.unbind("<Return>")

# 마우스 좌표, 클릭, 키보드 입력등 실행 로그를 On&off 할 수 있는 박스창 
def create_motion_log():
    print("create_motion_log()")
    global motion_log_label,motion_log, hidden_motion_log
    motion_log_label = Label(win, text = "모션 기록")
    motion_log_label.grid(row=0,column=2)
    motion_log=Listbox(win)
    motion_log.grid(row=1, column=2, rowspan=10)

    hidden_motion_log=Listbox(win)
    hidden_motion_log.grid(row=1, column=3, rowspan=10)
    hidden_motion_log.grid_remove()

def delete_motion_log():
    print("delete_motion_log()")
    global motion_log_label,motion_log, hidden_motion_log
    motion_log_label.destroy()
    motion_log.grid_remove()
    hidden_motion_log.grid_remove() #이거 destroy하는 순간 매크로 재생시 로그 정보가 꼬여서 에러뜸



# motion(마우스 무브, 왼쪽 클릭, 우측 클릭, 키보드 타이핑)에 대한 실행 시그널 발생, 관리, 저장, 업데이트
def mouse_move(event):
    print("mouse_move(event)")
    turn_on_mouse_move_motion_signal()
    manage_motion_num()
    Create_and_initialize_coordinates()
    update_coordinate_motion_log()

def left_click(event):
    print("click(event)")
    turn_on_motion_signal()
    manage_motion_num()
    update_left_click_motion_log()

def right_click(event):
    print("click(event)")
    turn_on_motion_signal()
    manage_motion_num()
    update_right_click_motion_log()

def type_write(event):
    print("type_write()")
    turn_on_motion_signal()
    manage_motion_num()
    create_win_for_type_write()
    

# 마우스 시그널 발생
def turn_on_mouse_move_motion_signal():
    print("turn_on_mouse_move_motion_signal()")
    global signal_num, co_signal_num
    signal_num = 1
    co_signal_num=1

# 마우스 클릭, 키보드 시그널 발생
def turn_on_motion_signal():
    print("turn_on_motion_signal()")
    global signal_num
    signal_num = 1

# 각종 값 초기화를 위한 중지(완료) 시그널 발생
def turn_on_stop_motion_signal():
    print("turn_on_stop_motion_signal()")
    global signal_num
    signal_num = 2

# 모션 시그널 관리
def manage_motion_num():
    print("manage_motion_num()")
    global motion_num, coordinate_num
    if signal_num==1:
        motion_num+=1
    elif signal_num==2:
        motion_num=0
    elif co_signal_num==1:
        coordinate_num+=1
    else:
        pass

# 마우스 좌표값 리스트 타입으로 대량 생성 및 보관
def Create_and_initialize_coordinates():
    print("Create_and_initialize_coordinates()")
    global coordinate_list
    if signal_num==1:
        coordinate_x_y=py.position()
        print(type(coordinate_x_y))
        coordinate_list.append(coordinate_x_y)
        print(coordinate_list)
    elif signal_num==2:
        coordinate_list=[]
        print(coordinate_list)

# 키보드 타이핑을 위한 타이핑 윈도우창 생성 및 타이핑 값 입력 받음
def create_win_for_type_write():
    print("create_win_for_type_write(event)")
    global typing_win, write_entry
    
    typing_win = Toplevel(win)
    typing_win.title("텍스트 입력")
    typing_win.geometry("250x100")
    typing_win_label = Label(typing_win, text = "작성할 내용을 입력하세요.")
    typing_win_label.grid(row=0, column=0)
    typing_win.wm_attributes("-topmost",1) #해당 창을 최상위 창으로 설정한다.
    
    write_entry=Entry(typing_win)
    write_entry.bind("<Return>", send_to_type_write)
    write_entry.grid(row=1,columnspan=1)

# 키보드 타이핑 값 전역에 공유 (write_entry.bind("<Return>", send_to_type_write)->write_entry.bind("<Return>", update_type_write_motion_log)로 변경하고 update_type_write_motion_log(event)바디부분에 type_write_text=write_entry.get(); typing_win_destroy()를 추가하는 식이면 아래 함수를 없애도 될거 같음.)
def send_to_type_write(event):
    print("send_to_type_write(event)")
    global type_write_text
    type_write_text=write_entry.get()
    typing_win_destroy()
    update_type_write_motion_log()
    

# 타이핑 윈도우 제거
def typing_win_destroy():
    print("typing_win_destroy()")
    typing_win.destroy()





# 모션 로그 박스창에 좌표값 업데이트 및 로그값 임시저장
def update_coordinate_motion_log():
    print("update_coordinate_motion_log()")
    global motion_log, hidden_motion_log
    txt = ""
    txt += str(motion_num) + "번 기록됨. 기록 중..."
    motion_log_label.configure(text = txt)
    motion_log.insert(motion_num-1,str(tuple(coordinate_list[coordinate_num-1])))
    hidden_motion_log.insert(motion_num*2-2,"mouse_move")
    hidden_motion_log.insert(motion_num*2-1,str(tuple(coordinate_list[coordinate_num-1])))

# 모션 로그 박스창에 좌클릭 로그 업데이트 및 로그값 임시저장
def update_left_click_motion_log():
    print("update_left_click_motion_log()")
    global motion_log, hidden_motion_log
    txt = ""
    txt += str(motion_num) + "번 기록됨. 기록 중..."
    motion_log_label.configure(text = txt)
    motion_log.insert(motion_num-1,"LeftClick")
    hidden_motion_log.insert(motion_num*2-2,"leftclick")
    hidden_motion_log.insert(motion_num*2-1,"LeftClick")

# 모션 로그 박스창에 우클릭 로그 업데이트 및 로그값 임시저장
def update_right_click_motion_log():
    print("update_right_click_motion_log()")
    global motion_log, hidden_motion_log
    txt = ""
    txt += str(motion_num) + "번 기록됨. 기록 중..."
    motion_log_label.configure(text = txt)
    motion_log.insert(motion_num-1,"RightClick")
    hidden_motion_log.insert(motion_num*2-2,"rightclick")
    hidden_motion_log.insert(motion_num*2-1,"RightClick")

# 모션 로그 박스창에 타이핑 로그 업데이트 및 로그값 임시저장
def update_type_write_motion_log():
    print("update_type_write_motion_log()")
    global motion_log, hidden_motion_log
    txt = ""
    txt += str(motion_num) + "번 기록됨. 기록 중..."
    motion_log_label.configure(text = txt)
    motion_log.insert(motion_num-1,type_write_text)
    hidden_motion_log.insert(motion_num*2-2,"write")
    hidden_motion_log.insert(motion_num*2-1,type_write_text)


















































# 녹화 완료 버튼 클릭
def recording_finish_btn_click():
    print("recording_finish_btn_click()")
    messagebox.showinfo("기록완료","2/2단계 저장.\n 파일명을 입력하세요.")
    Create_win_to_save_motion_log_and_input_file_name()
    create_macro_recording_btn()
    create_macro_paly_btn()
    create_macro_file_edit_btn()
    turn_off_motion_shortcut_key()
    delete_recording_finish_btn()
    delete_motion_log()
    create_macro_catalog()

# 임시 보관중인 키보드 타이핑 내용과 좌표 값을 텍스트 파일로 영구 보관하기 위한 텍스트 파일명 작성을 위한 윈도우창 생성 및 파일명 입력 
def Create_win_to_save_motion_log_and_input_file_name():
    print("Create_win_to_save_motion_log_and_input_file_name()")
    global file_name_win, motion_entry
    file_name_win = Toplevel(win)
    file_name_win.title("파일명 저장")
    file_name_win.geometry("250x100")
    file_name_win_label = Label(file_name_win, text = "파일명을 입력하고 엔터를 누르세요.")
    file_name_win_label.grid(row=0, column=0)
    file_name_win.wm_attributes("-topmost",1) #해당 창을 최상위 창으로 설정한다.
    
    motion_entry=Entry(file_name_win)
    motion_entry.bind("<Return>", make_folder_and_save_file)
    motion_entry.grid(row=1,columnspan=1)

#입력 받은 파일명을 저장할 폴더 생성
def make_folder_and_save_file(event):
    print("make_folder_and_save_file(event)")
    global motion_fName
    if os.path.exists("C:/temp"):
        pass
        print("C:/temp 있어")
    else:
        os.mkdir("C:/temp")
        print("C:/temp 없어")   

    if os.path.exists("C:/temp/SonMacro"):
        pass
        print("C:/temp/SonMacro 있어")
    else:
        os.mkdir("C:/temp/SonMacro") 
        print("C:/temp/SonMacro 없어")  

    motion_fName=motion_entry.get()
    motion_file_address="C:/temp/SonMacro/"+motion_fName+".txt"

    if os.path.exists(motion_file_address):
        messagebox.showinfo("파일명 중복","동일한 파일명이 있습니다. 다른 이름으로 저장해주세요")
    else:
        messagebox.showinfo("파일명 저장 완료",motion_fName+"으로 저장되었습니다.")
        save_coordinate_by_txt_file()
        file_name_win_destroy()
    print("motion_file_address:"+motion_file_address)

# 모션로그 저장을 위한 파일명 입력창 제거
def file_name_win_destroy():
    print("file_name_win_destroy()")
    file_name_win.destroy()

# 입력 받은 파일명으로 파일 저장과 임시 저장된 모션 로그 창 파일로 영구 저장
def save_coordinate_by_txt_file():
    print("save_coordinate_by_txt_file()")
    outFp =  None 
    outStr = ""
    print(motion_fName+"으로 저장하기")
    outFp = open("C:/temp/SonMacro/"+motion_fName+".txt", "w",encoding='UTF8')

    inList=str(hidden_motion_log.get(0,END))
    
    print("hidden_motion_log.get(0,END):",hidden_motion_log.get(0,END))
    print("len(hidden_motion_log.get(0,END)):",len(hidden_motion_log.get(0,END)))
    for inStr in inList:
        outFp.write(inStr)
    print("in:",type(inStr))
    print("in:",type(outFp.writelines(inStr)))
    outFp.close()

    print("inStr:",inStr)
    print("inStr:",type(inStr))
    recording_end()


# 녹화 끝
def recording_end():
    print("recording_end()")
    turn_on_stop_motion_signal()
    manage_motion_num()
    Create_and_initialize_coordinates()
    update_macro_catalog()












































# 매크로 카탈로그 클릭 : ->프리뷰 모션 로그창 생성
def macro_catalog_click(evt):
    print("macro_catalog_click(evt)")
    global currentDir, searchDirList, dirName, dirNames, select_count
    select_count=len(list(macro_catalog.curselection()))
    
    if select_count>=1:
        dirNames=[]
    
        selected=macro_catalog.curselection()

        print("selected:",selected)

        dirNames=[]
        for idx in selected:
            dirNames.append(macro_catalog.get(idx))

        print("dirNames:",dirNames)
        try:
            delete_preview_motion_log_box()
        except:
            pass
        create_preview_motion_log_box()
        


def create_preview_motion_log_box():
    global preview_motion_log_label,preview_motion_log
    print("create_preview_motion_log()")
    preview_motion_log_label=Label(win, text = "모션 기록")
    preview_motion_log_label.grid(row=0,column=3)

    preview_motion_log=Listbox(win)
    preview_motion_log.grid(row=1, column=3, rowspan=10, padx=10, pady=5, ipadx=10, ipady=5)

    load_preview_motion_log()



def delete_preview_motion_log_box():
    global preview_motion_log_label,preview_motion_log
    print("delete_preview_motion_log()")
    preview_motion_log_label.destroy()
    preview_motion_log.destroy()


def load_preview_motion_log():
    inFp = None	# 입력 파일
    inFp = open('C:/Temp/SonMacro/'+str(dirNames[0]), "r",encoding='UTF8' )
    #inStr=""
    inList=""
    inList=inFp.readlines()
    print("len(inList):",len(str(inList)))
    outStr = ""
    for i in range(0, len(str(inList))) :
        outStr += str(inList)[i]

    print("outStr:",outStr)
    loaded_co_list=outStr.split('\'')

    for list_index in loaded_co_list:
        print("list_index:",list_index)

    print("loaded_co_list:",loaded_co_list)
    print("len(loaded_co_list):",len(loaded_co_list))
    inFp.close()
    k=0
    for i in range(1,len(loaded_co_list)+1):
        if i%4==0:
            preview_motion_log.insert(k,str(loaded_co_list[i-1]))
            k+=1
    try:
        if select_count>1:
            preview_motion_log.delete(0,END)
            preview_motion_log.insert(0,"매크로 파일 다중 클릭시")
            preview_motion_log.insert(1,"로그를 확인 할 수 없습니다.")
        elif select_count==0:
            preview_motion_log.insert(0,"선택된 파일 없음_elif")
    except:
        preview_motion_log.insert(0,"선택된 파일 없음_except")



























#매크로 재생버튼 클릭 :
def macro_play_btn_click():
    print("macro_play_btn_click()")
    load_file_and_content()

# 파일안에 저장된 내용 불러오기 : 불러오려는 목록이 여러개면 경고창 생성. 1개이면 해당 파일 불러와서 안에 내용 읽음. 그리고 리스트 타입으로 정리하여 공유
def load_file_and_content():
    print("load_file_and_content()")
    global loaded_co_list,list_index
    if select_count==1:
        inFp = None	# 입력 파일
        inFp = open('C:/Temp/SonMacro/'+str(dirNames[0]), "r",encoding='UTF8' )
        #inStr=""
        inList=""
        inList=inFp.readlines()
        print("len(inList):",len(str(inList)))
        outStr = ""
        for i in range(0, len(str(inList))) :
            outStr += str(inList)[i]

        print("outStr:",outStr)
        loaded_co_list=outStr.split('\'')

        for list_index in loaded_co_list:
            print("list_index:",list_index)

        print("loaded_co_list:",loaded_co_list)
        play_motion_func()
        inFp.close()

# 리스트 타입으로 공유된 파일 내용을 읽고 해당 모션 실행 : 마우스 무브, 좌클릭, 우클릭, 키보드 입력
def play_motion_func():
    print("play_motion_func()")
    outStr=""
    print("pla_len:",len(loaded_co_list))
    print("dd:",tuple(loaded_co_list[3]))
    print("dd:",type(loaded_co_list[3]))
    for i in range(0,len(loaded_co_list)):
        if "mouse_move"==loaded_co_list[i]:
            print("loaded_co_list[i+2]-------------------------------------:",loaded_co_list[i+2])
            for inStr in loaded_co_list[i+2]:
                if (inStr != '(') and (inStr != ')'):  #inStr는 한글자 한글자 
                    outStr+=inStr
            
            print("outStr:",outStr)
            play_motion=outStr.split(',')
            
            #play_motion=tuple(map(int, outStr))
            print("motype:",type(play_motion))
            print("motype:",play_motion)
            py.moveTo(play_motion)
            outStr=""
            play_motion=[]
            print("motype:",type(play_motion))
            print("motype:",play_motion)
            time.sleep(0.3)
        elif "leftclick"==loaded_co_list[i]:
            mouse_left_click()
            time.sleep(0.1)
        elif "rightclick"==loaded_co_list[i]:
            mouse_right_click()
            time.sleep(0.1)
        elif "write"==loaded_co_list[i]:
            play_motion=loaded_co_list[i+2]
            print("loaded_co_list[i+2]:",loaded_co_list[i+2])
            print("play_motion:",play_motion)
            print("play_motion:",type(play_motion))
            pyperclip.copy(play_motion)
            time.sleep(1)
            py.hotkey("ctrl", "v")
            play_motion=[]
        else:
            pass

# 마우스 좌클릭 실행
def mouse_left_click(click_num=1,interval_num=0):
    print("mouse_left_click(click_num=1,interval_num=0)")
    py.click(clicks=click_num, interval=interval_num)

# 마우스 우클릭 실행
def mouse_right_click(click_num=1,interval_num=0):
    print("mouse_right_click(click_num=1,interval_num=0)")
    py.click(clicks=click_num, interval=interval_num, button='right')































def macro_file_edit_btn_click():
    global select_num
    delete_macro_recording_btn()
    delete_macro_paly_btn()
    delete_macro_file_edit_btn()
    create_selected_list_delete_btn()
    select_num=2
    selectmode_signal_func()
    update_macro_catalog()

# 목록 제거 버튼 클릭 : 공유받은 다중 클릭 목록에 해당하는 파일 제거
def selected_list_delete_btn_click():
    global select_num
    print("selected_list_delete_btn_click()")
    for address_to_delete in dirNames:
        total_address_to_delete='C:/temp/SonMacro/'+address_to_delete
        os.remove(total_address_to_delete)
    delete_preview_motion_log_box()
    create_macro_recording_btn()
    create_macro_paly_btn()
    create_macro_file_edit_btn()
    select_num=1
    selectmode_signal_func()
    update_macro_catalog()
    delete_selected_list_delete_btn()
    


def selectmode_signal_func():
    global selectmode_signal
    
    if select_num==1:
        selectmode_signal=BROWSE
    elif select_num==2:
        selectmode_signal=MULTIPLE































def create_macro_recording_btn():
    print("create_macro_recording_btn()")
    global macro_recording_btn
    macro_recording_btn=Button(win, text = "매크로 녹화(R)", fg="black",bg="gray",command=macro_recording_btn_click)
    macro_recording_btn.grid(row=1, column=0, padx=10, pady=5, ipadx=10, ipady=5)
    win.bind("<r>",recording_key)




def create_selected_list_delete_btn():
    print("create_selected_list_delete_btn()")
    global selected_list_delete_btn
    selected_list_delete_btn=Button(win, text = "선택된 목록 삭제(D)", fg="black",bg="gray",command=selected_list_delete_btn_click)
    selected_list_delete_btn.grid(row=3, column=0, padx=10, pady=5, ipadx=10, ipady=5)
    win.bind("<d>",delete_key)

def create_macro_paly_btn():
    print("create_macro_paly_btn()")
    global macro_paly_btn
    macro_paly_btn=Button(win, text = "매크로 재생(p)", fg="black",bg="gray",command=macro_play_btn_click)
    macro_paly_btn.grid(row=2, column=0,  padx=10, pady=5, ipadx=10, ipady=5)
    win.bind("<p>",play_key)

def create_macro_exit_btn():
    print("create_macro_exit_btn()")
    global macro_exit_btn
    macro_exit_btn=Button(win, text = "프로그램 종료(Esc)", fg="black",bg="gray",command=quit)
    macro_exit_btn.grid(row=5, column=0,  padx=10, pady=5, ipadx=10, ipady=5)
    win.bind("<Escape>",quit)

def create_recording_finish_btn():
    print("create_recording_finish_btn()")
    global recording_finish_btn
    recording_finish_btn=Button(win, text = "기록 완료(f)", fg="black",bg="gray",command=recording_finish_btn_click)
    recording_finish_btn.grid(row=2, column=0, padx=10, pady=5, ipadx=10, ipady=5)
    win.bind("<f>",finish_key)

def create_macro_catalog():
    print("create_macro_catalog()")
    global macro_catalog, macro_catalog_label
    print("select_num:",select_num)
    print("selectmode_signal:",selectmode_signal)
    macro_catalog=Listbox(win, selectmode=selectmode_signal)
    macro_catalog.bind('<<ListboxSelect>>', macro_catalog_click)
    macro_catalog.grid(row=1, column=1, rowspan=10, padx=10, pady=5, ipadx=10, ipady=5)
    macro_catalog_label=Label(win, text="매크로 파일")
    print("주범---------------")
    macro_catalog_label.grid(row=0, column=1)
    
    index_num=0
    
    for dirNames, subDirLists, fnames in os.walk('C:/Temp/SonMacro'):
        for fname in fnames:
            macro_catalog.insert(index_num,fname)
            index_num+=1

    if index_num==0:
        macro_catalog_label.configure(text="매크로 파일:현재 없음")

def create_macro_file_edit_btn():
    print("create_macro_file_edit_btn()")
    global macro_file_edit_btn
    macro_file_edit_btn=Button(win, text = "매크로 파일 편집(e)", fg="black",bg="gray",command=macro_file_edit_btn_click)
    macro_file_edit_btn.grid(row=4, column=0, padx=10, pady=5, ipadx=10, ipady=5)
    win.bind("<e>",edit_key)

def delete_macro_file_edit_btn():
    print("delete_macro_file_edit_btn()")
    macro_file_edit_btn.destroy()
    win.unbind("<e>")

def delete_macro_catalog():
    print("delete_macro_catalog()")
    global macro_catalog, macro_catalog_label
    macro_catalog_label.destroy()
    print("주범삭제---------------")
    macro_catalog.destroy()
    macro_catalog.unbind('<<ListboxSelect>>')

def delete_macro_recording_btn():
    print("delete_macro_recording_btn()")
    macro_recording_btn.destroy()
    win.unbind("<r>")

def delete_selected_list_delete_btn():
    print("delete_selected_list_delete_btn()")
    selected_list_delete_btn.destroy()
    win.unbind("<d>")

def delete_macro_paly_btn():
    print("delete_macro_paly_btn()")
    macro_paly_btn.destroy()
    win.unbind("<p>")

def delete_macro_exit_btn():
    print("delete_macro_exit_btn()")
    macro_exit_btn.destroy()
    #win.unbind("<Escape>")

def delete_recording_finish_btn():
    print("delete_recording_finish_btn()")
    recording_finish_btn.destroy()
    win.unbind("<f>")


def update_macro_catalog():
    print("update_macro_catalog()")
    global macro_catalog, macro_catalog_label
    macro_catalog_label.destroy()
    print("주범삭제---------------")
    macro_catalog.destroy()
    
    print("select_num:",select_num)
    print("selectmode_signal:",selectmode_signal)
    macro_catalog=Listbox(win, selectmode=selectmode_signal)
    macro_catalog.bind('<<ListboxSelect>>', macro_catalog_click)
    macro_catalog.grid(row=1, column=1, rowspan=10, padx=10, pady=5, ipadx=10, ipady=5)
    macro_catalog_label=Label(win, text="매크로 파일")
    print("주범---------------")
    macro_catalog_label.grid(row=0, column=1)
    
    index_num=0
    
    for dirNames, subDirLists, fnames in os.walk('C:/Temp/SonMacro'):
        for fname in fnames:
            macro_catalog.insert(index_num,fname)
            index_num+=1

    if index_num==0:
        macro_catalog_label.configure(text="매크로 파일:현재 없음")













def recording_key(event):
    print("recording_key(event)")
    macro_recording_btn_click()

def play_key(event):
    print("play_key(event)")
    macro_play_btn_click()

def finish_key(event):
    print("finish_key(event)")
    recording_finish_btn_click()

def delete_key(event):
    print("delete_key(event)")
    selected_list_delete_btn_click()

def edit_key(event):
    print("edit_key(event)")
    macro_file_edit_btn_click()



























#메인 코드#

win = Tk()
win.title("Mr.손 매크로")
win.geometry("540x230")
#win.geometry("350x230")
#win.resizable(width=False, height=False)
#win.attributes('-alpha',0.5) 투명도

start_Macro()



win.mainloop()






























'''

def mouse_moveTo():
    list_tuple1=[]
    i=0
    for k in range(1,len(loaded_co_list)+1):
        list_tuple1.append(int(loaded_co_list[i]))
        print("list_tuple1:",list_tuple1)
        if k!=0:
            if k%2==0:
                tuple1=tuple(list_tuple1)
                time.sleep(1)
                print("i:",i)
                print("tuple:",tuple1)
                coordinate=py.moveTo(tuple1,duration=1)
                coordinate
                tuple1=()
                list_tuple1=[]
        i+=1


if select_count>1:
        messagebox.showinfo("알람", "재생할 목록을 하나만 클릭해주세요.")

    elif 
'''