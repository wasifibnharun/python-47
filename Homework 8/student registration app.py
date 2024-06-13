from tkinter import *
from tkinter import messagebox
from student_db import Database

db=Database('student.db')

def populate_list():
    registration_details.delete(0,END)
    for row in db.fetch():
        registration_details.insert(END,row)

def enroll():
    if student_name_text.get()=='' or student_class_text.get()=='' or student_roll_text.get()== '' or student_section_text.get()=='' or guardian_contact_text.get()=='':
        messagebox.showerror("Required field/fields missing","Please include all fields")
        return
    db.insert(student_name_text.get(),student_class_text.get(),student_roll_text.get(),student_section_text.get(),guardian_contact_text.get())
    registration_details.delete(0,END)
    registration_details.insert(END,(student_name_text.get(),student_class_text.get(),student_roll_text.get(),student_section_text.get(),guardian_contact_text.get()))
    clear_text()
    populate_list()

def select_item(event):
    global selected_item
    index=registration_details.curselection()[0]
    selected_item=registration_details.get(index)
    student_name_entry.delete(0,END)
    student_name_entry.insert(END,selected_item[1])
    student_class_entry.delete(0,END)
    student_class_entry.insert(END,selected_item[2])
    student_roll_entry.delete(0,END)
    student_roll_entry.insert(END,selected_item[3])
    student_section_entry.delete(0,END)
    student_section_entry.insert(END,selected_item[4])
    guardian_contact_entry.delete(0,END)
    guardian_contact_entry.insert(END,selected_item[5])

def delete_item():
    db.delete(selected_item[0])
    clear_text()
    populate_list()

def update_info():
    db.update(selected_item[0],student_name_text.get(),student_class_text.get(),student_roll_text.get(),student_section_text.get(),guardian_contact_text.get())
    populate_list()

def clear_text():
    student_name_entry.delete(0,END)
    student_class_entry.delete(0,END)
    student_roll_entry.delete(0,END)
    student_section_entry.delete(0,END)
    guardian_contact_entry.delete(0,END)

#creating object from Tk class
app=Tk()

#application content

# student name
student_name_text=StringVar()
student_name_label=Label(app,text="Name",font=('bold',10),pady=20,padx=20)
student_name_label.grid(row=0,column=0)
student_name_entry=Entry(app,textvariable=student_name_text)
student_name_entry.grid(row=0,column=1)

#class
student_class_text=StringVar()
student_class_label=Label(app,text="Class",font=('bold',10),padx=20,pady=20)
student_class_label.grid(row=1,column=0)
student_class_entry=Entry(app,textvariable=student_class_text)
student_class_entry.grid(row=1,column=1)

#roll
student_roll_text=StringVar()
student_roll_label=Label(app,text="Roll",font=('bold',10),padx=20,pady=20)
student_roll_label.grid(row=2,column=0)
student_roll_entry=Entry(app,textvariable=student_roll_text)
student_roll_entry.grid(row=2,column=1)

#section
student_section_text=StringVar()
student_section_label=Label(app,text="Section",font=('bold',10),padx=20,pady=20)
student_section_label.grid(row=3,column=0)
student_section_entry=Entry(app,textvariable=student_section_text)
student_section_entry.grid(row=3,column=1)

#guardian contact number
guardian_contact_text=StringVar()
guardian_contact_label=Label(app,text="Guardian contact no",font=('bold',10),padx=20,pady=20)
guardian_contact_label.grid(row=4,column=0)
guardian_contact_entry=Entry(app,textvariable=guardian_contact_text)
guardian_contact_entry.grid(row=4,column=1)

#button widget
enroll_btn=Button(app,text="Enroll",width=12,command=enroll)
enroll_btn.grid(row=5,column=0,padx=20)

update_btn=Button(app,text="Update info",width=12,command=update_info)
update_btn.grid(row=5,column=1,padx=20)

delete_btn=Button(app,text="Delete",width=12,command=delete_item)
delete_btn.grid(row=5,column=2,padx=20)

clear_btn=Button(app,text="Reset",width=12,command=clear_text)
clear_btn.grid(row=5,column=3,padx=20)

#listbox widget
registration_details=Listbox(app,height=8,width=50,border=1)
registration_details.grid(row=6,column=0,columnspan=3,rowspan=6,pady=20,padx=20)

#create scrollbar
scrollbar=Scrollbar(app)
scrollbar.grid(row=6,column=3)

#Binding select function
registration_details.bind('<<ListboxSelect>>',select_item)

populate_list()

app.title('Student registration form')
app.geometry('550x700')
app.mainloop()