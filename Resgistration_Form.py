from tkinter import *
import tkinter.messagebox

def validate():
    name=f_entry.get()
    em=e_entry.get()
    gen=var.get()
    cou=c.get()
    program=(var1.get() or var2.get())
    if(name=="" or em=="" or cou=="Select your country" or gen==0):
        tkinter.messagebox.showinfo("Invalid Message Alert","Fields cannot be left empty!")
    else:
        tkinter.messagebox.showinfo("Success Message","Successfully registered!")

window=Tk()
window.geometry('500x500')
window.title("Resgistration Form")
rs_form=Label(window,text="Resgistration form",width=20,font=("bold",20))
rs_form.place(x=90,y=53)

f_name=Label(window,text="Full Name",width=20,font=("bold",10))
f_name.place(x=80,y=130)

Email=Label(window,text="Email",width=20,font=("bold",10))
Email.place(x=68,y=180)

Gender=Label(window,text="Gender",width=20,font=("bold",10))
Gender.place(x=70,y=230)

Country=Label(window,text="Country",width=20,font=("bold",10))
Country.place(x=70,y=280)

Programming=Label(window,text="Programming",width=20,font=("bold",10))
Programming.place(x=85,y=330)

f_entry=Entry(window)
f_entry.place(x=240,y=130)

e_entry=Entry(window)
e_entry.place(x=240,y=180)

var=IntVar()
male=Radiobutton(window,text="Male",variable=var,value=1)
female=Radiobutton(window,text="Female",variable=var,value=2)
male.place(x=240,y=230)
female.place(x=295,y=230)

list=['Myanmar','Canada','India','UK','Nepal','Iceland','South Africa'];
c=StringVar()
droplist=OptionMenu(window,c,*list)
droplist.config(width=15)
c.set("Select your country")
droplist.place(x=240,y=280)

var1=IntVar()
var2=IntVar()
cplus=Checkbutton(window,text="C++",variable=var1)
python=Checkbutton(window,text="Python",variable=var2)
cplus.place(x=240,y=330)
python.place(x=295,y=330)

submit=Button(window,text="Submit",width=20,bg='green',fg='white',command=validate)
submit.place(x=180,y=380)



window.mainloop()
