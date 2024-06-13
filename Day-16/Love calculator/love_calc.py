from tkinter import *
from tkinter.ttk import *

app=Tk()

app_name=StringVar()
app_name_label=Label(app,text='Love calculator😍',font=('bold',15),pady=20)
# app_name_label.grid(row=0)

my_name=StringVar()
my_name_label=Label(app,text='Enter your name:',font=('bold',12))
#my_name_label.grid(row=1)
my_name_entry=Entry(app,textvariable=my_name,justify='center')
#my_name_entry.grid(row=2)

mfriend_name=StringVar()
mfriend_name_label=Label(app,text='Enter your friend name:',font=('bold',12))
#mfriend_name_label.grid(row=3)
mfriend_name_entry=Entry(app,textvariable=mfriend_name)
#mfriend_name_entry.grid(row=4)

calc_button=Button(app,text='Calculate',width=15)
#calc_button.grid(row=5,pady=20)

app.title("Love Calculator😍")
app.geometry("500x300")
app.mainloop()