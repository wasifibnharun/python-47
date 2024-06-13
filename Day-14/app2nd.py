from tkinter import *
from tkinter import messagebox
from db import Database

db=Database('store.db')

def populate_list():
    for row in db.fetch():
        parts_list.insert(END,row)

def add_item():
    if part_text.get()=='' or customer_text.get()=='' or retailer_text.get()=='' or price_text.get()=='':
        messagebox.showerror("Required fields missing","Please include all fields")
        return
    db.insert(part_text.get(),customer_text.get(),retailer_text.get(),price_text.get())
    parts_list.delete(0,END)
    parts_list.insert(END,(part_text.get(),customer_text.get(),retailer_text.get(),price_text.get()))

def update_item():
    print("Item updated")

def delete_item():
    print("Item deleted")

def clear_text():
    print("Text cleared")



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
add_button=Button(app,text="Add Part",width=12,command=add_item)
add_button.grid(row=2,column=0,pady=20)

update_button=Button(app,text="Update",width=12,command=update_item)
update_button.grid(row=2,column=1,pady=20)

delete_button=Button(app,text="Delete",width=12,command=delete_item)
delete_button.grid(row=2,column=2,pady=20)

clear_button=Button(app,text="Clear",width=12,command=clear_text)
clear_button.grid(row=2,column=3,pady=20)

#listbox widget
parts_list=Listbox(app,height=8,width=50,border=1)
parts_list.grid(row=3,column=0,columnspan=3,rowspan=6,pady=20,padx=20)

#creating scroll bar
scrollbar=Scrollbar(app)
scrollbar.grid(row=3,column=3)


populate_list()


app.title('Product manager')
app.geometry('800x500')
app.mainloop()