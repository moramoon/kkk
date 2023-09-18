from tkinter import *

window=Tk()
window.title("Report Card")
window.geometry("700x250")

def result():
    total=0
    if e_1.get()=="A" : m1=40
    if e_1.get()=="B" : m1=36
    if e_1.get()=="C" : m1=32
    if e_1.get()=="D" : m1=28
    if e_1.get()=="P" : m1=24
    if e_1.get()=="F" : m1=0
    total+=m1
    Label(window,text=str(m1)).grid(row=3,column=4)
    if e_2.get()=="A" : m2=40
    if e_2.get()=="B" : m2=36
    if e_2.get()=="C" : m2=32
    if e_2.get()=="D" : m2=28
    if e_2.get()=="P" : m2=24
    if e_2.get()=="F" : m2=0
    total+=m2
    Label(window,text=str(m2)).grid(row=4,column=4)
    if e_3.get()=="A" : m3=30
    if e_3.get()=="B" : m3=27
    if e_3.get()=="C" : m3=24
    if e_3.get()=="D" : m3=21
    if e_3.get()=="P" : m3=28
    if e_3.get()=="F" : m3=0
    total+=m3
    Label(window,text=str(m3)).grid(row=5,column=4)
    if e_4.get()=="A" : m4=40
    if e_4.get()=="B" : m4=36
    if e_4.get()=="C" : m4=32
    if e_4.get()=="D" : m4=28
    if e_4.get()=="P" : m4=24
    if e_4.get()=="F" : m4=0
    total+=m4
    Label(window,text=str(m4)).grid(row=6,column=4)
    
    Label(window,text=str(total)).grid(row=7,column=4)
    Label(window,text=str(total/15)).grid(row=8,column=4)
            

Label(window,text="Name").grid(row=0,column=0)
Label(window,text="Roll.No").grid(row=1,column=0)
Label(window,text="Reg.No").grid(row=0,column=3)

Label(window,text="Srl.No").grid(row=2,column=0)
Label(window,text="1").grid(row=3,column=0)
Label(window,text="2").grid(row=4,column=0)
Label(window,text="3").grid(row=5,column=0)
Label(window,text="4").grid(row=6,column=0)

Label(window,text="Subject").grid(row=2,column=1)
Label(window,text="CS 201").grid(row=3,column=1)
Label(window,text="CS 202").grid(row=4,column=1)
Label(window,text="MA 201").grid(row=5,column=1)
Label(window,text="EC 201").grid(row=6,column=1)

Label(window,text="Grade").grid(row=2,column=2)

Label(window,text="Sub Credit").grid(row=2,column=3)
Label(window,text="4").grid(row=3,column=3)
Label(window,text="4").grid(row=4,column=3)
Label(window,text="3").grid(row=5,column=3)
Label(window,text="4").grid(row=6,column=3)

Label(window,text="Total credit").grid(row=7,column=3)
Label(window,text="SGPA").grid(row=8,column=3)

Label(window,text="Credit obtained").grid(row=2,column=4)

e_name=Entry(window)
e_roll=Entry(window)
e_reg=Entry(window)
e_1=Entry(window)
e_2=Entry(window)
e_3=Entry(window)
e_4=Entry(window)

e_name.grid(row=0,column=1)
e_roll.grid(row=1,column=1)
e_reg.grid(row=0,column=4)
e_1.grid(row=3,column=2)
e_2.grid(row=4,column=2)
e_3.grid(row=5,column=2)
e_4.grid(row=6,column=2)

submit=Button(window,text="Submit",bg="blue",fg="black",command=result)
submit.grid(row=8,column=1)

window.mainloop()
