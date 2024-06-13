from tkinter import *

app=Tk()

#Part name
part_name=StringVar()
part_label=Label(app,text='Part Name',font=('bold',12),pady=20,padx=20)
part_label.grid(row=0,column=0)
part_entry=Entry(app,textvariable=part_name)
part_entry.grid(row=0,column=1)

#Customer name
customer_name=StringVar()
customer_label=Label(app,text='Customer Name',font=('bold',12),pady=20,padx=20)
customer_label.grid(row=1,column=0)
customer_entry=Entry(app,textvariable=customer_name)
customer_entry.grid(row=1,column=1)

#Price
price=StringVar()
price_label=Label(app,text='Price',font=('bold',12),pady=20,padx=20)
price_label.grid(row=2,column=0)
price_entry=Entry(app,textvariable=price)
price_entry.grid(row=2,column=1)

#Retailer name
retailer_name=StringVar()
retailer_label=Label(app,text='Retailer Name',font=('bold',12),pady=20,padx=20)
retailer_label.grid(row=3,column=0)
retailer_entry=Entry(app,textvariable=retailer_name)
retailer_entry.grid(row=3,column=1)

#adding buttons
add_button=Button(app,text="Add",width=15)
add_button.grid(row=4,column=1)

update_button=Button(app,text="Update",width=15)
update_button.grid(row=5,column=1)

delete_button=Button(app,text="Delete",width=15)
delete_button.grid(row=6,column=1)

clear_button=Button(app,text="Clear",width=15)
clear_button.grid(row=7,column=1)

#adding listbox
parts_list=Listbox(app,height=10,width=50,border=1)
parts_list.grid(row=8,column=0,rowspan=6,columnspan=3,padx=20,pady=20)

#adding scrollbar
scrollbar=Scrollbar(app)
scrollbar.grid(row=8,column=3)

app.title("Homework")
app.geometry("500x500")
app.mainloop()