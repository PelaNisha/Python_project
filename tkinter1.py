from tkinter import *
root = Tk()
root.title("Calculator")
e = Entry(root, width=50,borderwidth=5,)
e.grid(column = 0, row = 0, columnspan = 4, padx= 10, pady = 10)

def buttonNum(number):
    current = e.get()
    e.delete(0,END)
    e.insert(0, str(current)+str(number))

def clearNum():
    e.delete(0,END)

input1 = Button(root, text = "1",padx=60, pady= 20,command =lambda: buttonNum(1))
input2 = Button(root, text = "2",padx=60, pady= 20,command =lambda: buttonNum(2))
input3 = Button(root, text = "3",padx=60, pady= 20,command =lambda: buttonNum(3))
input4 = Button(root, text = "4",padx=60, pady= 20,command =lambda: buttonNum(4))
input5 = Button(root, text = "5",padx=60, pady= 20,command =lambda: buttonNum(5))
input6 = Button(root, text = "6",padx=60, pady= 20,command =lambda: buttonNum(6))
input7 = Button(root, text = "7",padx=60, pady= 20,command =lambda: buttonNum(7))
input8 = Button(root, text = "8",padx=60, pady= 20,command =lambda: buttonNum(8))
input9 = Button(root, text = "9",padx=60, pady= 20,command =lambda: buttonNum(9))
input0 = Button(root, text = "0",padx=60, pady= 20,command =lambda: buttonNum(0))

input2.grid(row=4, column=0)
input1.grid(row=4, column=1)
input3.grid(row=3, column=0)
input4.grid(row=3, column=1)
input5.grid(row=2, column=0)
input6.grid(row=2, column=1)
input7.grid(row=1, column=0)
input8.grid(row=1, column=1)
input9.grid(row=5, column=0)
input0.grid(row=5, column=1) 

def add():
    first_num = e.get()
    global f
    f= int(first_num)
    global math 
    math= 'add'
    e.delete(0,END)
    
def sub():
    first_num = e.get()
    global f
    f= int(first_num)
    global math 
    math= 'sub'
    e.delete(0,END)

def mul():
    first_num = e.get()
    global f
    f= int(first_num)
    global math 
    math= 'mul'
    e.delete(0,END)    

def div():
    first_num = e.get()
    global f
    f= int(first_num)
    global math 
    math= 'div'
    e.delete(0,END)

def result():
    second_num = e.get()
    e.delete(0,END)
    if math == 'add':
        e.insert(0,f+int(second_num))
    elif math == 'sub':
        e.insert(0,f-int(second_num))
    elif math == 'mul':
        e.insert(0,f*int(second_num))   
    elif math == 'div':
        e.insert(0,f/int(second_num))     
ad = Button(root, text = "add",padx=60, pady= 20, bg="#ebc2cb", command=add)
ad.grid(row=4, column=2) 
ad = Button(root, text = "sub",padx=60, pady= 20, bg="#ebc2cb", command=sub)
ad.grid(row=3, column=2) 
ad = Button(root, text = "mul",padx=60, pady= 20, bg="#ebc2cb", command=mul)
ad.grid(row=2, column=2) 
ad = Button(root, text = "div",padx=60, pady= 20, bg="#ebc2cb", command=div)
ad.grid(row=1, column=2) 
clear = Button(root, text = "clear",padx=60, pady= 20,bg="#ebc2cb", command=clearNum)
clear.grid(row=5, column=2) 
clear = Button(root, text = "=",padx=60, pady= 20,bg="#ebc2cb", command=result)
clear.grid(row=6, column=2) 
root.mainloop()