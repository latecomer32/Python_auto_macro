import pyautogui as py
from tkinter import *
from tkinter import messagebox
import pyperclip
import time
import os
import shutil

#변수선언
coordinate_list=[]
#dataNum=[]
motion_num, signal_num, coordinate_num, co_signal_num=0,0,0,0
type_write_text=''
motion_log=None
#함수 선언

def start_Macro():
    create_motion_log()
    create_macro_recording_btn()
    create_macro_paly_btn()
    create_macro_exit_btn()
    create_macro_catalog()
    create_selceted_list_delete_btn()

def r_key(event):
    macro_recording_btn_click()

def p_key(event):
    macro_play_btn_click()

def f_key(event):
    recording_finish_btn_click()

def delete_key(event):
    selceted_list_delete_btn_click()

def macro_recording_btn_click():
    messagebox.showinfo("기록시작","1/2단계 기록.\n반복할 모션을 기록하세요.")
    turn_on_motion()
    create_recording_finish_btn()
    create_motion_log()
    delete_macro_paly_btn()
    delete_macro_recording_btn()
    delete_selceted_list_delete_btn()
    delete_macro_catalog()

def turn_on_motion():
    win.bind("<space>", mouse_move)
    win.bind("<c>", click)
    win.bind("<Return>", create_type_write_on_win)

def turn_off_motion():
    win.unbind("<space>")
    win.unbind("<c>")
    win.unbind("<Return>")

def create_motion_log():
    global motion_log_label,motion_log, hidden_motion_log
    motion_log_label = Label(win, text = "모션 기록")
    motion_log_label.grid(row=0,column=2)
    motion_log=Listbox(win)
    motion_log.grid(row=1, column=2, rowspan=10)

    hidden_motion_log=Listbox(win)
    hidden_motion_log.grid(row=1, column=3, rowspan=10)
    hidden_motion_log.grid_remove()
    
    

def delete_motion_log():
    global motion_log_label,motion_log, hidden_motion_log
    motion_log_label.destroy()
    motion_log.destroy()
    hidden_motion_log.destroy()

def upadete_coordinate_motion_log():
    global motion_log, hidden_motion_log
    txt = ""
    txt += str(motion_num) + "번 기록됨. 기록 중..."
    motion_log_label.configure(text = txt)
    motion_log.insert(motion_num-1,str(tuple(coordinate_list[coordinate_num-1])))
    hidden_motion_log.insert(motion_num*2-2,"mouse_move")
    hidden_motion_log.insert(motion_num*2-1,str(tuple(coordinate_list[coordinate_num-1])))

def upadete_click_motion_log():
    global motion_log, hidden_motion_log
    txt = ""
    txt += str(motion_num) + "번 기록됨. 기록 중..."
    motion_log_label.configure(text = txt)
    motion_log.insert(motion_num-1,"click()")
    hidden_motion_log.insert(motion_num*2-2,"click")
    hidden_motion_log.insert(motion_num*2-1,"click()")

def upadete_type_write_motion_log():
    global motion_log, hidden_motion_log
    txt = ""
    txt += str(motion_num) + "번 기록됨. 기록 중..."
    motion_log_label.configure(text = txt)
    motion_log.insert(motion_num-1,type_write_text)
    hidden_motion_log.insert(motion_num*2-2,"write")
    hidden_motion_log.insert(motion_num*2-1,type_write_text)

def mouse_move(event):
    check_play_coordinate_motion()
    manage_motion_num()
    manage_coordinate_list()
    upadete_coordinate_motion_log()

def click(event):
    check_play_motion()
    manage_motion_num()
    upadete_click_motion_log()

def play_macro_click(click_num=1,interval_num=0):
    py.click(clicks=click_num, interval=interval_num)


def type_write():
    check_play_motion()
    #py.typewrite('\''+type_write_text+'\'')
    write_win_destroy()
    manage_motion_num()
    upadete_type_write_motion_log()

def create_type_write_on_win(event):
    global write_win, write_entry
    
    write_win = Toplevel(win)
    write_win.title("텍스트 입력")
    write_win.geometry("250x100")
    write_win_label = Label(write_win, text = "작성할 내용을 입력하세요.")
    write_win_label.grid(row=0, column=0)
    write_win.wm_attributes("-topmost",1) #해당 창을 최상위 창으로 설정한다.
    
    write_entry=Entry(write_win)
    write_entry.bind("<Return>", send_to_type_write)
    write_entry.grid(row=1,columnspan=1)

def send_to_type_write(event):
    global type_write_text
    type_write_text=write_entry.get()
    type_write()

def write_win_destroy():
    write_win.destroy()

def manage_motion_num():
    global motion_num, coordinate_num
    if signal_num==1:
        motion_num+=1
    elif signal_num==2:
        motion_num=0
    elif co_signal_num==1:
        coordinate_num+=1
    else:
        pass
    return

def check_play_motion():
    global signal_num
    signal_num = 1

def check_stop_motion():
    global signal_num
    signal_num = 2

def check_play_coordinate_motion():
    global signal_num, co_signal_num
    signal_num = 1
    co_signal_num=1

def manage_coordinate_list():
    global coordinate_list
    if signal_num==1:
        coordinate_x_y=py.position()
        print(type(coordinate_x_y))
        coordinate_list.append(coordinate_x_y)
        print(coordinate_list)
    elif signal_num==2:
        coordinate_list=[]
        print(coordinate_list)



def recording_finish_btn_click():
    messagebox.showinfo("기록완료","2/2단계 저장.\n 파일명을 입력하세요.")
    save_motion_file_name()
    create_macro_catalog()
    create_macro_recording_btn()
    create_macro_paly_btn()
    create_selceted_list_delete_btn()
    turn_off_motion()
    delete_recording_finish_btn()
    delete_motion_log()
    

def save_motion_file_name():
    global motion_win, motion_entry
    
    motion_win = Toplevel(win)
    motion_win.title("파일명 저장")
    motion_win.geometry("250x100")
    motion_win_label = Label(motion_win, text = "파일명을 입력하고 엔터를 누르세요.")
    motion_win_label.grid(row=0, column=0)
    motion_win.wm_attributes("-topmost",1) #해당 창을 최상위 창으로 설정한다.
    
    motion_entry=Entry(motion_win)
    motion_entry.bind("<Return>", make_folder_and_save_file)
    motion_entry.grid(row=1,columnspan=1)
    
def make_folder_and_save_file(event):
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
        motion_win_destroy()
    print("motion_file_address:"+motion_file_address)

        
def motion_win_destroy():
    motion_win.destroy()
    
def save_coordinate_by_txt_file():
    outFp =  None 
    outStr = ""
    print(motion_fName+"으로 저장하기")
    outFp = open("C:/temp/SonMacro/"+motion_fName+".txt", "w",encoding='UTF8')

    inList=str(hidden_motion_log.get(0,END))
    
    print("mo:",motion_log.get(0,END))
    print("molen:",len(motion_log.get(0,END)))
    for inStr in inList:
        outFp.write(inStr)
    print("in:",type(inStr))
    print("in:",type(outFp.writelines(inStr)))
    outFp.close()

    print("inStr:",inStr)
    print("inStr:",type(inStr))
    create_macro_catalog()
    recording_end()
    

def recording_end():
    check_stop_motion()
    manage_motion_num()
    manage_coordinate_list()
    

def macro_catalog_click(evt):
    global currentDir, searchDirList, dirName, dirNames, select_count
    select_count=len(list(macro_catalog.curselection()))

    if select_count>=1:
        dirNames=[]
    
        selected=macro_catalog.curselection()

        print("s:",selected)

        dirNames=[]
        for idx in selected:
            dirNames.append(macro_catalog.get(idx))

        print("d:",dirNames)


def selceted_list_delete_btn_click():
    for address_to_delete in dirNames:
        total_address_to_delete='C:/temp/SonMacro/'+address_to_delete
        os.remove(total_address_to_delete)
    macro_catalog.destroy()
    create_macro_catalog()

def macro_play_btn_click():
    load_file_and_content()




def play_motion_func():
    outStr=""
    print("pla_len:",len(loaded_co_list))
    print("dd:",tuple(loaded_co_list[3]))
    print("dd:",type(loaded_co_list[3]))
    for i in range(0,len(loaded_co_list)):
        if "mouse_move"==loaded_co_list[i]:
            #play_motion=loaded_co_list[i+2]
            for inStr in loaded_co_list[i+2]:
                if (inStr != '(') and (inStr != ')'):
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
            time.sleep(0.7)
        elif "click"==loaded_co_list[i]:
            play_macro_click()
            time.sleep(0.5)
        elif "write"==loaded_co_list[i]:
            play_motion=""
            play_motion=loaded_co_list[i+2]
            print("loaded_co_list[i+2]:",loaded_co_list[i+2])
            print("play_motion:",play_motion)
            print("play_motion:",type(play_motion))
            pyperclip.copy(play_motion)
            time.sleep(0.5)
            py.hotkey("ctrl", "v")
            play_motion=None
        else:
            pass


def load_file_and_content():
    global loaded_co_list,list_index
    if select_count>1:
        messagebox.showinfo("알람", "재생할 목록을 하나만 클릭해주세요.")

    elif select_count==1:
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








def create_macro_recording_btn():
    global macro_recording_btn
    macro_recording_btn=Button(win, text = "매크로 녹화(R)", fg="black",bg="gray",command=macro_recording_btn_click)
    macro_recording_btn.grid(row=1, column=0, padx=10, pady=5, ipadx=10, ipady=5)
    win.bind("<r>",r_key)

def create_selceted_list_delete_btn():
    global selceted_list_delete_btn
    selceted_list_delete_btn=Button(win, text = "선택된 목록 삭제(D)", fg="black",bg="gray",command=selceted_list_delete_btn_click)
    selceted_list_delete_btn.grid(row=3, column=0, padx=10, pady=5, ipadx=10, ipady=5)
    win.bind("<d>",delete_key)

def create_macro_paly_btn():
    global macro_paly_btn
    macro_paly_btn=Button(win, text = "매크로 재생(p)", fg="black",bg="gray",command=macro_play_btn_click)
    macro_paly_btn.grid(row=2, column=0,  padx=10, pady=5, ipadx=10, ipady=5)
    win.bind("<p>",p_key)

def create_macro_exit_btn():
    global macro_exit_btn
    macro_exit_btn=Button(win, text = "프로그램 종료(Esc)", fg="black",bg="gray",command=quit)
    macro_exit_btn.grid(row=5, column=0,  padx=10, pady=5, ipadx=10, ipady=5)
    win.bind("<Escape>",quit)

def create_recording_finish_btn():
    global recording_finish_btn
    recording_finish_btn=Button(win, text = "기록 완료(f)", fg="black",bg="gray",command=recording_finish_btn_click)
    recording_finish_btn.grid(row=2, column=0, padx=10, pady=5, ipadx=10, ipady=5)
    win.bind("<f>",f_key)

def create_macro_catalog():
    global macro_catalog, macro_catalog_label
    macro_catalog=Listbox(win, selectmode='multiple')
    macro_catalog.bind('<<ListboxSelect>>', macro_catalog_click)
    macro_catalog.grid(row=1, column=1, rowspan=10, padx=10, pady=5, ipadx=10, ipady=5)
    macro_catalog_label=Label(win, text="저장된 매크로 목록")
    macro_catalog_label.grid(row=0, column=1)
    
    index_num=0
    
    for dirNames, subDirLists, fnames in os.walk('C:/Temp/SonMacro'):
        for fname in fnames:
            macro_catalog.insert(index_num,fname)
            index_num+=1

    if index_num==0:
        macro_catalog_label.configure(text="저장된 매크로 없음")

def delete_macro_catalog():
    global macro_catalog, macro_catalog_label
    macro_catalog_label.destroy()
    macro_catalog.destroy()
    macro_catalog.unbind('<<ListboxSelect>>')
    

def delete_macro_recording_btn():
    macro_recording_btn.destroy()
    win.unbind("<r>")

def delete_selceted_list_delete_btn():
    selceted_list_delete_btn.destroy()
    win.unbind("<d>")

def delete_macro_paly_btn():
    macro_paly_btn.destroy()
    win.unbind("<p>")

def delete_macro_exit_btn():
    macro_exit_btn.destroy()
    #win.unbind("<Escape>")

def delete_recording_finish_btn():
    recording_finish_btn.destroy()
    win.unbind("<f>")

#메인 코드#

win = Tk()
win.title("Mr.손 매크로")
#win.geometry("520x230")
win.geometry("350x230")
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


'''