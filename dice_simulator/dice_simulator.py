
from tkinter import*
import tkinter as tk
from PIL import ImageTk,Image
import random as r
#create a window
win=tk.Tk()
#set background color to a window
win.configure(bg='#800080')
#set title
win.title("dice simulator")
#set geometry
win.geometry("600x600")

#images to place
img1=ImageTk.PhotoImage(file="1.jpg")
img2=ImageTk.PhotoImage(file="2.jpg")
img3=ImageTk.PhotoImage(file="3.jpg")
img4=ImageTk.PhotoImage(file="4.jpg")
img5=ImageTk.PhotoImage(file="5.jpg")
img6=ImageTk.PhotoImage(file="6.jpg") 
img7=ImageTk.PhotoImage(file="dice_sim.jpg") 
# def IMG(i):
#     img1=ImageTk.PhotoImage(file=i)

def start():
    l=[1,2,3,4,5,6]
    res=r.choice(l)
    if res==1:
        #label image
        Label(win,width=255,height=215,image=img1).place(x=200,y=100)
    elif res==2:
    #label image
        Label(win,width=255,height=215,image=img2).place(x=200,y=100)
    elif res==3:
    #label image
        Label(win,width=255,height=215,image=img3).place(x=200,y=100)
    elif res==4:
        #label image
        Label(win,width=255,height=215,image=img4).place(x=200,y=100)
    elif res==5:
        #label image
        Label(win,width=255,height=215,image=img5).place(x=200,y=100)
    elif res==6:
        #label image
        Label(win,width=255,height=215,image=img6).place(x=200,y=100)
    
Label(win,width=200,height=200,image=img7).place(x=200,y=100)
Button(win,text='throw dice ',fg="white",bg='#800080',width=12,height=2,command=start).place(x=200,y=400)  
Button(win,text='exit',fg="white",bg='#800080',width=12,height=2,command=win.destroy).place(x=330,y=400)  

win.mainloop() 