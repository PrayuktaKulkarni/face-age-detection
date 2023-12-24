import tkinter as tk
import os
from tkinter import*
from PIL import Image,ImageTk


def callback():
    filename ='AgeGender.py'
    os.system(filename)


root = tk.Tk()  
title=Label(root,text="Know Yourself Better!!",font=("times new roman",20,"bold"),bg="white",fg="black").place(x=240,y=50) 
root.centre=ImageTk.PhotoImage(file="images/homepagepic.png")
centre=Label(root,image=root.centre).place(x=20,y=50,width=200,height=300)

btn=tk.Button(root , text="start camera" , bg="black" , fg="white" ,command=callback).place(x=260,y=280)

root.mainloop()