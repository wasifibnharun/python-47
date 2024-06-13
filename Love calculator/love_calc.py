from tkinter import *
import random 

app=Tk() 

app.geometry('400x240') 
app.title('❤Love Calculator❤') 


def calculate_love(): 
	st = '0123456789'
	digit = 2
	temp="".join(random.sample(st, digit)) 
	result.config(text=temp) 


# Heading on Top 
heading=Label(app,text='❤Love Calculator❤',font=('')) 
heading.pack() 

# Slot/input for the first name 
slot1=Label(app,text="Enter Your Name:") 
slot1.pack() 
name1=Entry(app,border=5) 
name1.pack() 

# Slot/input for the partner name 
slot2=Label(app,text="Enter Your Partner Name:") 
slot2.pack() 
name2=Entry(app,border=5) 
name2.pack() 

bt=Button(app,text="Calculate",height=1,width=7,command=calculate_love) 
bt.pack() 

result = Label(app,text='Love Percentage between both of You:') 
result.pack() 

app.mainloop()