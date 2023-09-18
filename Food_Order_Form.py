from tkinter import *
from tkinter import ttk,Frame,Button,Checkbutton,Radiobutton,IntVar,HORIZONTAL

window=Tk()
window.title("Food Order Form")
window.geometry("400x450")

def result():
    order="Your order:"
    if sandwich.get()==1: order+="Sandwich "
    if salad.get()==1: order+="Salad "
    if soup.get()==1: order+="Soup "
    if pizza.get()==1: order+="Pizza "
    print(order)
    pay_method="Pay method is "
    if pay.get()==1: pay_method+=" KBZpay"
    if pay.get()==2: pay_method+=" Credit card"
    if pay.get()==3: pay_method+=" Other"
    print(pay_method)
    
    

Label(window,text="Food Order Form",font=('Helvetica',20),bd=10).pack()

ttk.Separator(window,orient=HORIZONTAL).pack(fill='x')

Label(window,text="What would you like to order?",bd=10).pack(anchor='w')
sandwich=IntVar()
salad=IntVar()
soup=IntVar()
pizza=IntVar()
Checkbutton(window,text="Sandwich",variable=sandwich).pack(anchor='w')
Checkbutton(window,text="Salad",variable=salad).pack(anchor='w')
Checkbutton(window,text="Soup",variable=soup).pack(anchor='w')
Checkbutton(window,text="Pizza",variable=pizza).pack(anchor='w')

Label(window,text="How do you want to pay?",bd=10).pack(anchor='w')
pay=IntVar()
Radiobutton(window,text="KBZpay",variable=pay,value=1).pack(anchor='w')
Radiobutton(window,text="Credit Card",variable=pay,value=2).pack(anchor='w')
Radiobutton(window,text="Other",variable=pay,value=3).pack(anchor='w')

Button(window,text="Next",command=result,width=10,bg="lightgrey",fg="black").pack()


window.mainloop()
