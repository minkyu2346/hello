from PIL import Image, ImageTk
from tkinter import*
import random
from menu import whatmenu

global newmenu
newmenu= whatmenu()
def btncl():
    global newmenu
    newmenu = whatmenu()
    label1.config(text="오늘의 메뉴는 {}입니다".format(newmenu.food))
    newmenu= img[newmenu.food]
    label2.config(image=newmenu)
   

root = Tk ()

root.title("오늘 뭐 먹지?")
root.geometry('640x540')
btn1=Button(root,text="오늘 메뉴는?",command=btncl)

btn1.pack()
label1=Label(root,text="오늘의 메뉴는 {}입니다".format(newmenu.food))
label1.pack()

img = {"라면":ImageTk.PhotoImage(file=r'C:\Users\USER\hello\hello\ra.Png'),
        "돈까스":ImageTk.PhotoImage(file=r'C:\Users\USER\hello\hello\don.Png'),
        "김밥":ImageTk.PhotoImage(file=r'C:\Users\USER\hello\hello\gim.Png'),
        "짜장면":ImageTk.PhotoImage(file=r'C:\Users\USER\hello\hello\ja.Png'),
        "짬뽕":ImageTk.PhotoImage(file=r'C:\Users\USER\hello\hello\jam.Png')}



label2= Label(root, image = img[newmenu.food])
label2.pack()




root.mainloop()