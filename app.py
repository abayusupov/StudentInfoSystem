# -*- coding: utf-8 -*-
"""
Created on Tue Jul 19 20:42:21 2022

@author: @Abror Baratov
"""
from tkinter import Tk, LabelFrame, Label, Button, CENTER, NO, messagebox
from tkinter.ttk import Entry, Combobox, Frame, Treeview, Scrollbar, Style
from StudentInfoClass import Students, Undergraduate, Postgraduate

root = Tk()


def add_student():
    if entry_stid.get()!='' and entry_fullname.get()!='' and entry_adminyear.get()!='' and entry_faculity.get()!='' and entry_nation.get()!='':
        if combo_level.get()=='Undergraduate':
            if entry_residhall.get()!='':
                st = Undergraduate(entry_stid.get(), combo_level.get(), entry_fullname.get(), entry_nation.get(), combo_gender.get(), entry_faculity.get(), entry_adminyear.get(), entry_residhall.get())
                st.add()
            else:
                messagebox.showwarning("Attention!", "Please, fill a 'Residential hall' field!")
        else:
            if entry_supervisor.get()!='' and entry_research.get()!='':
                st = Postgraduate(entry_stid.get(), combo_level.get(), entry_fullname.get(), entry_nation.get(), combo_gender.get(), entry_faculity.get(), entry_adminyear.get(), entry_supervisor.get(), entry_research.get())
                st.add()
            else:
                messagebox.showwarning("Attention!", "Please, fill all the fields!")
        display_all()
    else:
        messagebox.showwarning("Attention!", "Please, fill all the fields!")

def display_all():
    data = Students.all_data()
    count = 0
    for i in my_tree.get_children():
        my_tree.delete(i)
    for d in data:
        if count%2==0:
            if d[1]=='Undergraduate':
                my_tree.insert(parent='', index='end', iid=count, values=(d[0], d[2], d[3], d[4], d[5], d[6], d[7], '-', '-'), tags=('evenrow',))
            else:
                my_tree.insert(parent='', index='end', iid=count, values=(d[0], d[2], d[3], d[4], d[5], d[6],'-', d[7], d[8]), tags=('evenrow',))
        else:
            if d[1]=='Undergraduate':
                my_tree.insert(parent='', index='end', iid=count, values=(d[0], d[2], d[3], d[4], d[5], d[6], d[7], '-', '-'), tags=('oddrow',))
            else:
                my_tree.insert(parent='', index='end', iid=count, values=(d[0], d[2], d[3], d[4], d[5], d[6],'-', d[7], d[8]), tags=('oddrow',))
        count+=1

def find():
    if entry_toolstid.get()!='':
        d = Students.find(entry_toolstid.get())
        if d==0:
            messagebox.showinfo("Attention!", "Nothing found with this student ID!")
        elif d==1:
            messagebox.showinfo("Attention!", "database is an empty!")
        else:
            for i in my_tree.get_children():
                my_tree.delete(i)
            if d[1]=='Undergraduate':
                my_tree.insert(parent='', index='end', iid=0, values=(d[0], d[2], d[3], d[4], d[5], d[6], d[7], '-', '-'), tags=('evenrow',))
            else:
                my_tree.insert(parent='', index='end', iid=0, values=(d[0], d[2], d[3], d[4], d[5], d[6],'-', d[7], d[8]), tags=('evenrow',))
            
    else:
        messagebox.showwarning("Attention!", "Please, fill  a student ID field!")

def delete():
    if entry_toolstid.get()!='':
        d = Students.delete(entry_toolstid.get())
        if d==0:
            messagebox.showinfo("Attention!", "Nothing found with this student ID!")
        elif d==1:
            messagebox.showinfo("Attention!", "database is an empty!")
        else:
            for i in my_tree.get_children():
                my_tree.delete(i)
            display_all()
    else:
        messagebox.showwarning("Attention!", "Please, fill  a student ID field!")
        
        
            



def rejimtanlash(event):
    mode = event.widget.get()
    if mode=="Undergraduate":
        label_residhall.grid(row=2, column=3, padx=10, pady=10)
        entry_residhall.grid(row=3, column=3, padx=10)
        add_frame.winfo_children()[16].grid_remove()
        add_frame.winfo_children()[17].grid_remove()
        add_frame.winfo_children()[18].grid_remove()
        add_frame.winfo_children()[19].grid_remove()
        
    else:
        add_frame.winfo_children()[14].grid_remove()
        add_frame.winfo_children()[15].grid_remove()
        label_supervisor.grid(row=2, column=3, padx=10, pady=10)
        entry_supervisor.grid(row=3, column=3, padx=10)
        label_research.grid(row=2, column=4, padx=10, pady=10)
        entry_research.grid(row=3, column=4, padx=10)


root.title("Students Info System")
root.geometry("960x700")
root.wm_state('normal')

add_frame = LabelFrame(root, text="Adding students")
add_frame.pack(pady=10, fill='x')

Label(add_frame, text="Student ID (unique)").grid(row=0, column=0)
entry_stid = Entry(add_frame, font=('Courier', 8, 'bold'))
entry_stid.grid(row=1, column=0, padx=10)

levels = ['Undergraduate', 'Postgraduate']
Label(add_frame, text="level").grid(row=0, column=1)
combo_level = Combobox(add_frame, font=('Courier', 8, 'bold'))
combo_level.set(levels[0])
combo_level['state'] = 'readonly'
combo_level['values'] = levels
combo_level.grid(row=1, column=1, padx=10)

combo_level.bind("<<ComboboxSelected>>", rejimtanlash)

Label(add_frame, text="full name").grid(row=0, column=2)
entry_fullname = Entry(add_frame, font=('Courier', 8, 'bold'))
entry_fullname.grid(row=1, column=2, padx=10)

Label(add_frame, text="nationality").grid(row=0, column=3)
entry_nation = Entry(add_frame, font=('Courier', 8, 'bold'))
entry_nation.grid(row=1, column=3, padx=10)

gender =['male', 'female']
Label(add_frame, text="gender").grid(row=2, column=0)
combo_gender = Combobox(add_frame, font=('Courier', 8, 'bold'))
combo_gender.set(gender[0])
combo_gender['values'] = gender
combo_gender['state'] = 'readonly'
combo_gender.grid(row=3, column=0, padx=10)

Label(add_frame, text="faculity").grid(row=2, column=1)
entry_faculity = Entry(add_frame, font=('Courier', 8, 'bold'))
entry_faculity.grid(row=3, column=1, padx=10)

Label(add_frame, text="admission year").grid(row=2, column=2)
entry_adminyear = Entry(add_frame, font=('Courier', 8, 'bold'))
entry_adminyear.grid(row=3, column=2, padx=10)

label_residhall = Label(add_frame, text='Residential hall')
entry_residhall = Entry(add_frame, font=('Courier', 8, 'bold'))
label_residhall.grid(row=2, column=3, padx=10, pady=10)
entry_residhall.grid(row=3, column=3, padx=10)

label_supervisor = Label(add_frame, text='Supervisor name')
entry_supervisor = Entry(add_frame, font=('Courier', 8, 'bold'))

label_research = Label(add_frame, text='Research topic')
entry_research = Entry(add_frame, font=('Courier', 8, 'bold'))

add_button = Button(add_frame, text="Add", width=15, bg='#38A8E3', command=add_student)
add_button.grid(row=1, column=4, padx=10, pady=10)

tool_frame = LabelFrame(root, text="Find, delete, display")
tool_frame.pack(padx=30, fill='x')

Label(tool_frame, text="Student ID").grid(row=0, column=0)
entry_toolstid = Entry(tool_frame, font=('Courier', 8, 'bold'))
entry_toolstid.grid(row=1, column=0, padx=10)

find_button = Button(tool_frame, text="Find", width=15, bg='#38A8E3', command=find)
find_button.grid(row=1, column=2, padx=10, pady=10)

delete_button = Button(tool_frame, text="Delete", width=15, bg='#38A8E3', command=delete)
delete_button.grid(row=1, column=3, padx=10, pady=10)

display_button = Button(tool_frame, text="Display all", width=15, bg='#38A8E3', command=display_all)
display_button.grid(row=1, column=4, padx=10, pady=10)

tree_frame = Frame(root)
tree_frame.pack(fill='both', pady=20, expand=1)

tree_scroll = Scrollbar(tree_frame)
tree_scroll.pack(side='right', fill='y')

my_tree = Treeview(tree_frame, yscrollcommand=tree_scroll, selectmode="extended")
tree_scroll.config(command=my_tree.yview)
my_tree.pack(fill="both", pady=10, expand=True)


uz = my_tree.winfo_width()
wk = int(uz/9)
my_tree['columns'] = ("ID", "FullName", "Nation", "Gender", "Faculity", "AdmYear", "ResHall", "SupName", "ResTop")

style = Style()
style.theme_use("default")
style.configure("Treeview", 
                rowheight=25,)
style.map('Treeview',
          background=[("selected", '#347083')])

my_tree.column('#0', width=0, stretch=NO)
my_tree.column("ID", anchor=CENTER, width=wk)
my_tree.column("FullName", anchor=CENTER, width=wk)
my_tree.column("Nation", anchor=CENTER, width=wk)
my_tree.column("Gender", anchor=CENTER, width=wk)
my_tree.column("Faculity", anchor=CENTER, width=wk)
my_tree.column("AdmYear", anchor=CENTER, width=wk)
my_tree.column("ResHall", anchor=CENTER, width=wk)
my_tree.column("SupName", anchor=CENTER, width=wk)
my_tree.column("ResTop", anchor=CENTER, width=wk)

my_tree.heading('#0', text='', anchor=CENTER)
my_tree.heading('ID', text='ID', anchor=CENTER)
my_tree.heading('FullName', text='Full Name', anchor=CENTER)
my_tree.heading('Nation', text='Nationality', anchor=CENTER)
my_tree.heading('Gender', text='Gender', anchor=CENTER)
my_tree.heading('Faculity', text='Faculity', anchor=CENTER)
my_tree.heading('AdmYear', text='Admission Year', anchor=CENTER)
my_tree.heading('ResHall', text='Resid. Hall', anchor=CENTER)
my_tree.heading('SupName', text='Sup Name', anchor=CENTER)
my_tree.heading('ResTop', text='Res. Top', anchor=CENTER)

my_tree.tag_configure('oddrow', background="white")
my_tree.tag_configure('evenrow', background="lightblue")

display_all()


root.mainloop()