import tkinter as tk
import pyautogui as pa

run = False

def get_mouse_position():
    if run:
        x,y = pa.position()
        s1.set(f'{x},{y}')
        a1.after(20,get_mouse_position)

def start_get():
    global run
    run = True
    get_mouse_position()

def stop_get(event):
    global run
    run = False

a1 = tk.Tk()
s1 = tk.StringVar()
a1.geometry('400x100+2000+100')
a1.title('获取鼠标位置')
tk.Label(a1,text = '按空格暂停').place(x=100,y=50)
tk.Entry(a1,textvariable=s1,state="readonly",font = ('黑体',13),width=20).place(x=10,y=10)
tk.Button(a1,text = '获取坐标',command = start_get,font = ('黑体',10)).place(x=300,y=10)
a1.attributes('-topmost',True)
a1.bind('<space>', stop_get)
a1.mainloop()