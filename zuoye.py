import numpy as np
from PIL import Image
from pyzbar import pyzbar
import cv2
import tkinter as tk
from threading import *
from tkinter import filedialog
students = {}
daoru = 1
idnum = []
list1 = 1
#1

def dao():
    global students,daoru,idnum,list1
    file_path = filedialog.askopenfilename(filetypes=[('csv格式', '*.csv')])
    print(file_path)
    with open(file_path, 'r', newline='') as csvfile:
        stu_name = csvfile.read().split('\r\n')
    for x in stu_name:
        if x == '':
            continue
        students[x.split(',')[0]] = [x.split(',')[1],0,0]
        
        idnum.append(int(x.split(',')[0]))
    print(idnum)
    daoru.destroy()
      
    
    for item in idnum:
        list1.insert('end', str(item) + '  '+students[str(item)][0])  # 从最后一个位置开始加入值
    
    t2 = Thread(target=camera)
    t2.start()
def save_file():
    
    
    file_path = filedialog.asksaveasfilename(title=u'保存文件',filetypes=[('csv格式', '*.csv')])

    print('保存文件：', file_path)
    if(file_path[-3:] != '.csv'):
        file_path = file_path + '.csv'
    print('保存文件：', file_path)
    if file_path != None:
        with open(file=file_path, mode='a+', encoding='utf-8') as file:
            file.write('1')
        
        
        print('保存完成')

def show():
    global daoru,list1
    window = tk.Tk()
    window.title("作业批改助手")
    window.geometry('800x700')
    daoru = tk.Button(window, text='导入学生名册', font=('宋体', 15), width=15, height=1, command=dao)
    daoru.place(x=15, y=5, anchor='nw')
    answer = tk.Text(window,show = None,height = 19,width = 25,font=('黑体', 25))
    answer.place(x=10,y=45,anchor='nw')
    answer.insert('1.0', '参考答案填写处')
    l = tk.Label(window, text='(当学生姓名后显示“已改”，\n按下1为优秀，2为良好，\n3为合格，4为不合格)\n\n批改情况：',  font=('等线', 15))
    l.place(x=500,y=20)
    list1 = tk.Listbox(window,width = 45 ,height = 25)
    list1.place(x=460,y=140)
    save = tk.Button(window, text='导出批改数据',font=('宋体', 15),width=15,height=1,command=save_file)
    save.place(x=550,y=620,anchor='nw')
    window.mainloop()
    
def OR_read(img):
    
    im = np.array(img)
    py_decode = pyzbar.decode(im)
    if len(py_decode) != 0:
        return py_decode[0].data.decode("utf-8")
    else:
        return None
    

def camera():
    global list1,idnum
    cap = cv2.VideoCapture(1, cv2.CAP_DSHOW)
    while cap.isOpened():
        ok, frame = cap.read()  # 读取一帧数据
        if not ok:
             break
        a = OR_read(frame)
        if a != None:
            print(a)
            if(students[a][1] == 0):
                try:
                    students[a][1] = 1
                    print(students)
                    numb = idnum.index(int(a))
                    print(numb)
                    list1.delete(numb)
                    list1.insert(numb,a +'  '+students[a][0]+'  -已改- ')
                except:
                    print('error')
            c = cv2.waitKey(10)
            keyword = c & 0xFF
            if keyword == ord('1'):
                list1.delete(numb)
                list1.insert(numb,a+'  '+students[a][0]+'  -已改-  优秀')
                students[a][1] = 1
            if keyword == ord('2'):
                list1.delete(numb)
                list1.insert(numb,a+'  '+students[a][0]+'  -已改-  良好')
                students[a][1] = 2
            if keyword == ord('3'):
                list1.delete(numb)
                list1.insert(numb,a+'  '+students[a][0]+'  -已改-  合格')
                students[a][1] = 3
            if keyword == ord('4'):
                list1.delete(numb)
                list1.insert(numb,a+'  '+students[a][0]+'  -已改-  不合格')
                students[a][1] = 4
        cv2.imshow("frame", frame)
        c = cv2.waitKey(10)
        if c & 0xFF == ord('q'):
            break
        
        
            
        

    # 释放摄像头并销毁所有窗口
    cap.release()
    cv2.destroyAllWindows()
t1 = Thread(target=show)

t1.start()


