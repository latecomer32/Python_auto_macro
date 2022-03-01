import pyautogui as py
from tkinter import *
from tkinter import messagebox
import time
import os

#변수선언
position_list=[]
dataNum=[]
coordinate_num, signal_num=0,0

#함수 선언

def start_Macro():
    create_macro_recording_btn()
    create_macro_paly_btn()
    create_macro_exit_btn()
    create_macro_listbox()

    win.bind("<r>",r_key)
    win.bind("<s>",s_key)
    win.bind("<Escape>",quit)

def r_key(event):
    macro_recording_btn_click()

def s_key(event):
    macro_play_btn_click()

def f_key(event):
    recording_finish_btn_click()




def macro_recording_btn_click():
    messagebox.showinfo("기록시작","1단계 좌표 기록.\n원하는 위치에 커서를 두고 'space'를 눌러 좌표를 기록하세요.")
    
    macro_recording_start()

    create_recording_finish_btn()
    win.bind("<f>", f_key)
    macro_paly_btn.destroy()
    macro_recording_btn.destroy()
    macro_listbox.destroy()
    


def macro_recording_start():
    win.bind("<space>", show_coordinate_on_list)
    global label1,list_xy
    label1 = Label(win, text = "space바 눌러 좌표 기록")
    label1.grid(row=0,column=1)

    list_xy=Listbox(win)
    list_xy.grid(row=1, column=1, rowspan=5)
    

def show_coordinate_on_list(event) :
        global signal_num
        signal_num = 1

        manage_signal_num()
        manage_position_list()

        txt = ""
        txt += str(coordinate_num) + "번 기록됨. 기록 중..."
        label1.configure(text = txt)
        list_xy.insert(coordinate_num-1,str(coordinate_num)+"번 : "+str(tuple(position_list[coordinate_num-1])))
        
        

def manage_position_list():
    global position_list
    
    if signal_num==1:
        position_x_y=py.position()
        print(type(position_x_y))
        position_list.append(position_x_y)
        print(position_list)
    elif signal_num==2:
        position_list=[]
        print(position_list)


def manage_signal_num():
    global coordinate_num
    
    if signal_num==1:
        coordinate_num+=1
    elif signal_num==2:
        coordinate_num=0
    






def recording_finish_btn_click():
    messagebox.showinfo("기록완료","2단계 좌표값 저장.\n 파일명을 상세히 기록하세요.")
    save_coordinate_file_name()
    recording_finish_btn.destroy()
    create_macro_recording_btn()
    create_macro_paly_btn()

    
    

    

def save_coordinate_file_name():
    global fileName
    global newWin1
    
    newWin1 = Toplevel(win)
    newWin1.title("파일명 저장")
    newWin1.geometry("200x200")
    labelExample = Label(newWin1, text = "파일명을 입력하고 엔터를 누르세요.")
    labelExample.grid(row=0, column=0)
    newWin1.wm_attributes("-topmost",1) #해당 창을 최상위 창으로 설정한다.
    fileName=Entry(newWin1)
    fileName.bind("<Return>", make_folder_and_save_file)
    fileName.grid(row=1,columnspan=1)
    
def make_folder_and_save_file(event):
    global co_file_name

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

    co_file_name=fileName.get()
    co_file_adress="C:/temp/SonMacro/"+co_file_name+".txt"

    if os.path.exists(co_file_adress):
        
        messagebox.showinfo("파일명 중복","동일한 파일명이 있습니다. 다른 이름으로 저장해주세요")
    else:
        messagebox.showinfo("파일명 저장 완료",co_file_name+"으로 저장되었습니다.")
        save_coordinate_by_txt_file()
        newWin1_destroy()
    print("co_file_adress:"+co_file_adress)

        
def newWin1_destroy():
    newWin1.destroy()
    
def save_coordinate_by_txt_file():
    outFp =  None 
    outStr = ""
    print(co_file_name+"으로 저장하기")
    outFp = open("C:/temp/SonMacro/"+co_file_name+".txt", "w",encoding='UTF8')

    inList=str(position_list)
    print("inList:"+inList)
    for inStr in inList:
        outFp.write(inStr)
    outFp.close()

    print("inStr:",inStr)
    print("inStr:",type(inStr))
    create_macro_listbox()
    recording_end()
    

def recording_end():
    global signal_num

    signal_num = 2
    list_xy.destroy()
    label1.destroy()
    manage_signal_num()
    manage_position_list()
    win.unbind("<space>")





def macro_listbox_click(evt):
    global currentDir, searchDirList, dirName
    if (macro_listbox.curselection()==()):
        return
    dirName=str(macro_listbox.get(macro_listbox.curselection()))



def macro_play_btn_click():

    inFp = None	# 입력 파일
    inFp = open('C:/Temp/SonMacro/'+dirName, "r",encoding='UTF8' )
    inStr=""
    inList=""
    inList=inFp.readlines()
    
    outStr = ""
    for i in range(0, len(str(inList))) :
        if (str(inList)[i] != 'y') and(str(inList)[i] != '=') and(str(inList)[i] != 'x') and(str(inList)[i] != 'P') and (str(inList)[i] != '[') and (str(inList)[i] != '\'') and (str(inList)[i] != 'o') and (str(inList)[i] != 'n') and (str(inList)[i] != 'i') and (str(inList)[i] != 't') and (str(inList)[i] != ']') and (str(inList)[i] != ' ') and (str(inList)[i] != '(') and (str(inList)[i] != ')'):
            
            outStr += str(inList)[i]

    loaded_co_list=outStr.split(',')
    print("loaded_co_list:",loaded_co_list)
    list_tuple1=[]
    
    for i in range(0,len(loaded_co_list)):
        if i!=0:
            if i%2==0:
                tuple1=tuple(list_tuple1)
                time.sleep(1)
                coordinate=py.click(tuple1,duration=1)
                coordinate
                tuple1=()
                list_tuple1=[]
        list_tuple1.append(int(loaded_co_list[i]))
        print("list_tuple1:",list_tuple1)












def create_macro_recording_btn():
    global macro_recording_btn
    macro_recording_btn=Button(win, text = "매크로 녹화(R)", fg="black",bg="gray",command=macro_recording_btn_click)
    macro_recording_btn.grid(row=1, column=0, padx=10, pady=5, ipadx=10, ipady=5)

def create_macro_paly_btn():
    global macro_paly_btn
    macro_paly_btn=Button(win, text = "매크로 재생(S)", fg="black",bg="gray",command=macro_play_btn_click)
    macro_paly_btn.grid(row=4, column=0,  padx=10, pady=5, ipadx=10, ipady=5)

def create_macro_exit_btn():
    global macro_exit_btn
    macro_exit_btn=Button(win, text = "프로그램 종료(Esc)", fg="black",bg="gray",command=quit)
    macro_exit_btn.grid(row=5, column=0,  padx=10, pady=5, ipadx=10, ipady=5)

def create_recording_finish_btn():
    global recording_finish_btn
    recording_finish_btn=Button(win, text = "기록 완료(f)", fg="black",bg="gray",command=recording_finish_btn_click)
    recording_finish_btn.grid(row=2, column=0, padx=10, pady=5, ipadx=10, ipady=5)

def create_macro_listbox():
    global macro_listbox
    macro_listbox=Listbox(win, selectmode='single')
    macro_listbox.bind('<<ListboxSelect>>', macro_listbox_click)
    macro_listbox.grid(row=1, column=1, rowspan=10, padx=10, pady=5, ipadx=10, ipady=5)
    listboxlabel=Label(win, text="저장된 매크로 목록")
    listboxlabel.grid(row=0, column=1)
    
    index_num=0
    
    for dirNames, subDirLists, fnames in os.walk('C:/Temp/SonMacro'):
        for fname in fnames:
            macro_listbox.insert(index_num,fname)
            index_num+=1

    if index_num==0:
        listboxlabel.configure(text="저장된 매크로 없음")
    

#메인 코드#

win = Tk()
win.title("매크로")
win.geometry("350x230")
#win.resizable(width=False, height=False)
#win.attributes('-alpha',0.5) 투명도

start_Macro()

win.mainloop()

