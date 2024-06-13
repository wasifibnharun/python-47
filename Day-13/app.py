#import tkinter
from tkinter import *

#creating object from Tk class
app=Tk()

#application content

#Part name
part_text=StringVar()
part_label=Label(app,text="Part name",font=('bold',10),pady=20,padx=20)
part_label.grid(row=0,column=0)
part_entry=Entry(app,textvariable=part_text)
part_entry.grid(row=0,column=1)

#Customer name
customer_text=StringVar()
customer_label=Label(app,text="Customer name",font=('bold',10),pady=20,padx=20)
customer_label.grid(row=1,column=0)
customer_entry=Entry(app,textvariable=customer_text)
customer_entry.grid(row=1,column=1)

#Price
price_text=StringVar()
price_label=Label(app,text="Price",font=('bold',10),pady=20,padx=20)
price_label.grid(row=0,column=2)
price_entry=Entry(app,textvariable=price_text)
price_entry.grid(row=0,column=3)

#Retailer
retailer_text=StringVar()
retailer_label=Label(app,text="Retailer name",font=('bold',10),pady=20,padx=20)
retailer_label.grid(row=1,column=2)
retailer_entry=Entry(app,textvariable=retailer_text)
retailer_entry.grid(row=1,column=3)

#button widget
add_button=Button(app,text="Add Part",width=12)
add_button.grid(row=2,column=0,pady=20)

update_button=Button(app,text="Update",width=12)
update_button.grid(row=2,column=1,pady=20)

delete_button=Button(app,text="Delete",width=12)
delete_button.grid(row=2,column=2,pady=20)

clear_button=Button(app,text="Clear",width=12)
clear_button.grid(row=2,column=3,pady=20)

#listbox widget
parts_list=Listbox(app,height=8,width=50,border=1)
parts_list.grid(row=3,column=0,columnspan=3,rowspan=6,pady=20,padx=20)

#creating scroll bar
scrollbar=Scrollbar(app)
scrollbar.grid(row=3,column=3)

app.title('Product manager')
app.geometry('800x500')
app.mainloop()