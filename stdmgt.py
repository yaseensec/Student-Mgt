import tkinter as tk
from tkinter import ttk,messagebox
import pymysql

class Student:
    def __init__(self,root):
        self.root=root
        self.root.title("Student Management System")
        self.root.geometry("1366x768+0+0")
        self.root.config(bg="#262223")
        
        title=tk.Label(self.root,text="Student Management System",relief=tk.GROOVE,font=('times new roman',40,'bold'),bg="#262223",fg="#DDC6B6")
        title.pack(side=tk.TOP,fill=tk.X)
        
        #####All Variables#####
        self.Roll_No_var=tk.StringVar()
        self.name_var=tk.StringVar()
        self.email_var=tk.StringVar()
        self.gender_var=tk.StringVar()
        self.contact_var=tk.StringVar()
        self.dob_var=tk.StringVar()
        
        self.search_by=tk.StringVar()
        self.search_text=tk.StringVar()
        
        ## Manage Frame ##
        Manage_Frame=tk.Frame(self.root,bd=4,relief=tk.RIDGE,bg="#262223")
        Manage_Frame.place(x=20,y=100,width=450,height=580)
        
        m_title=tk.Label(Manage_Frame,text="Manage Students",bg="#262223",fg="#DDC6B6",font=('times new roman',30,'bold'))
        m_title.grid(row=0,columnspan=2,pady=20)
        
        label_roll=tk.Label(Manage_Frame,text="Roll No.",bg="#262223",fg="#DDC6B6",font=('times new roman',20,'bold'))
        label_roll.grid(row=1,column=0,pady=9,padx=20,sticky="w")
        
        text_roll=tk.Entry(Manage_Frame,textvariable=self.Roll_No_var,font=('times new roman',13),bd=0,relief=tk.GROOVE,bg="#262223",fg="White")
        text_roll.grid(row=1,column=1,pady=9,padx=20,sticky="w")
        
        label_name=tk.Label(Manage_Frame,text="Name",bg="#262223",fg="#DDC6B6",font=('times new roman',20,'bold'))
        label_name.grid(row=2,column=0,pady=9,padx=20,sticky="w")
        
        text_name=tk.Entry(Manage_Frame,textvariable=self.name_var,font=('times new roman',13),bd=0,relief=tk.GROOVE,bg="#262223",fg="White")
        text_name.grid(row=2,column=1,pady=9,padx=20,sticky="w")
        
        label_email=tk.Label(Manage_Frame,text="Email",bg="#262223",fg="#DDC6B6",font=('times new roman',20,'bold'))
        label_email.grid(row=3,column=0,pady=9,padx=20,sticky="w")
        
        text_email=tk.Entry(Manage_Frame,textvariable=self.email_var,font=('times new roman',13),bd=0,relief=tk.GROOVE,bg="#262223",fg="White")
        text_email.grid(row=3,column=1,pady=9,padx=20,sticky="w")
        
        label_gender=tk.Label(Manage_Frame,text="Gender",bg="#262223",fg="#DDC6B6",font=('times new roman',20,'bold'))
        label_gender.grid(row=4,column=0,pady=9,padx=20,sticky="w")
        
        ##-----------TTK Styling----------------##
        style = ttk.Style()
        style.theme_use('alt')
        style.configure('TCombobox', background = 'gray',foreground="White")
        style.map('TCombobox', fieldbackground=[('readonly','#262223')])
        style.configure("Treeview",background="#262223",foreground="White",fieldbackground="#262223")
        style.map('Treeview',background=[('selected',"#262223")],foreground=[('selected','#DDC6B6')])
        
        combo_gender=ttk.Combobox(Manage_Frame,textvariable=self.gender_var,font=('times new roman',13,'bold'),state="readonly")
        combo_gender['values']=("Select","Male","Female","Other")
        combo_gender.current(0)
        combo_gender.grid(row=4,column=1,padx=20,pady=9)
        
        label_contact=tk.Label(Manage_Frame,text="Contact",bg="#262223",fg="#DDC6B6",font=('times new roman',20,'bold'))
        label_contact.grid(row=5,column=0,pady=9,padx=20,sticky="w")
        
        text_contact=tk.Entry(Manage_Frame,textvariable=self.contact_var,font=('times new roman',13),bd=0,relief=tk.GROOVE,bg="#262223",fg="White")
        text_contact.grid(row=5,column=1,pady=9,padx=20,sticky="w")
        
        label_dob=tk.Label(Manage_Frame,text="D.O.B",bg="#262223",fg="#DDC6B6",font=('times new roman',20,'bold'))
        label_dob.grid(row=6,column=0,pady=9,padx=20,sticky="w")
        
        text_dob=tk.Entry(Manage_Frame,textvariable=self.dob_var,font=('times new roman',13),bd=0,relief=tk.GROOVE,bg="#262223",fg="White")
        text_dob.grid(row=6,column=1,pady=9,padx=20,sticky="w")
        
        label_address=tk.Label(Manage_Frame,text="Address",bg="#262223",fg="#DDC6B6",font=('times new roman',20,'bold'))
        label_address.grid(row=7,column=0,pady=9,padx=20,sticky="w")
        
        self.text_address=tk.Text(Manage_Frame,width=30,height=4,font=('',10),bg="#262223",fg="White")
        self.text_address.grid(row=7,column=1,pady=9,padx=20,sticky="w")
        
        ##Button Frame##
        
        Button_Frame=tk.Frame(Manage_Frame,bd=4,relief=tk.RIDGE,bg="#262223")
        Button_Frame.place(x=15,y=515,width=420)
    
        addbtn=tk.Button(Button_Frame,text="Add",width=6,command=self.add_students,bg="#262223",fg="#DDC6B6",activebackground="#DDC6B6")
        addbtn.grid(row=0,column=0,padx=10,pady=10)
        updatetn=tk.Button(Button_Frame,text="Update",width=6,command=self.update_data,bg="#262223",fg="#DDC6B6",activebackground="#DDC6B6")
        updatetn.grid(row=0,column=1,padx=10,pady=10)
        deletebtn=tk.Button(Button_Frame,text="Delete",width=6,command=self.delete_data,bg="#262223",fg="#DDC6B6",activebackground="#DDC6B6")
        deletebtn.grid(row=0,column=2,padx=10,pady=10)
        clearbtn=tk.Button(Button_Frame,text="Clear",width=6,command=self.clear,bg="#262223",fg="#DDC6B6",activebackground="#DDC6B6")
        clearbtn.grid(row=0,column=3,padx=10,pady=10)
        
        ## Detail Frame ##
        Detail_Frame=tk.Frame(self.root,bd=4,relief=tk.RIDGE,bg="#262223")
        Detail_Frame.place(x=500,y=100,width=800,height=580)
        
        label_search=tk.Label(Detail_Frame,text="Search By",bg="#262223",fg="#DDC6B6",font=('times new roman',20,'bold'))
        label_search.grid(row=0,column=0,pady=10,padx=20,sticky="w")
        
        combo_search=ttk.Combobox(Detail_Frame,textvariable=self.search_by,width=10,font=('times new roman',13,'bold'),state="readonly")
        combo_search['values']=("Select","Roll_No","Name","Contact")
        combo_search.current(0)
        combo_search.grid(row=0,column=1,padx=20,pady=9)
        
        text_search=tk.Entry(Detail_Frame,textvariable=self.search_text,width=16,font=('times new roman',10,'bold'),bd=0,relief=tk.GROOVE,bg="#262223",fg="White")
        text_search.grid(row=0,column=2,pady=10,padx=20,sticky="w")
        
        searchbtn=tk.Button(Detail_Frame,text="Search",width=6,pady=5,command=self.search_data,bg="#262223",fg="#DDC6B6",activebackground="#DDC6B6")
        searchbtn.grid(row=0,column=3,padx=10,pady=10)
        showalltn=tk.Button(Detail_Frame,text="Show All",width=6,pady=5,command=self.fetch_data,bg="#262223",fg="#DDC6B6",activebackground="#DDC6B6")
        showalltn.grid(row=0,column=4,padx=10,pady=10)
        
        ## Table Frame
        table_Frame=tk.Frame(Detail_Frame,bd=4,relief=tk.RIDGE,bg="#262223")
        table_Frame.place(x=10,y=70,width=760,height=480)
        
        scroll_x=tk.Scrollbar(table_Frame,orient=tk.HORIZONTAL,bg="#262223")
        scroll_y=tk.Scrollbar(table_Frame,orient=tk.VERTICAL,bg="#262223")
        self.student_table=ttk.Treeview(table_Frame,column=('Roll No','Name','Email','Gender','Contact','DOB','Address'),xscrollcommand=scroll_x.set,yscrollcommand=scroll_y.set)
        scroll_x.pack(side=tk.BOTTOM,fill=tk.X)
        scroll_y.pack(side=tk.RIGHT,fill=tk.Y)
        scroll_x.config(command=self.student_table.xview)
        scroll_y.config(command=self.student_table.yview)
        self.student_table.heading("Roll No",text='Roll No')
        self.student_table.heading("Name",text='Name')
        self.student_table.heading("Email",text='Email')
        self.student_table.heading("Gender",text='Gender')
        self.student_table.heading("Contact",text='Contact')
        self.student_table.heading("DOB",text='DOB')
        self.student_table.heading("Address",text='Address')
        self.student_table['show']='headings'
        self.student_table.column('Roll No',width=100)
        self.student_table.column('Name',width=100)
        self.student_table.column('Email',width=100)
        self.student_table.column('Gender',width=100)
        self.student_table.column('Contact',width=100)
        self.student_table.column('DOB',width=100)
        self.student_table.column('Address',width=150)
        
        self.student_table.pack(fill=tk.BOTH,expand=1)
        self.student_table.bind("<ButtonRelease-1>",self.get_cursor)
        self.fetch_data()
        
    def add_students(self):
        if self.Roll_No_var.get()=="" or self.name_var.get()=="":
            messagebox.showerror("Error","All Fields are Required!!!")
        else:
            con=pymysql.connect(host="localhost",user="root",password="1234",database="stm")
            cur=con.cursor()
            cur.execute("insert into students values(%s,%s,%s,%s,%s,%s,%s)",(self.Roll_No_var.get(),self.name_var.get(),self.email_var.get(),self.gender_var.get(),self.contact_var.get(),self.dob_var.get(),self.text_address.get('1.0',tk.END)))
            con.commit()
            self.fetch_data()
            self.clear()
            con.close()
            messagebox.showinfo("Success","Record has been Inserted")
        
    def fetch_data(self):
        con=pymysql.connect(host="localhost",user="root",password="1234",database="stm")
        cur=con.cursor()
        cur.execute("select * from students")
        rows=cur.fetchall()
        if len(rows)!=0:
            self.student_table.delete(*self.student_table.get_children())
            for rows in rows:
                self.student_table.insert('',tk.END,values=rows)
            con.commit()
        con.close()

    def clear(self):
        self.Roll_No_var.set("")
        self.name_var.set("")
        self.email_var.set("")
        self.gender_var.set("Select")
        self.contact_var.set("")
        self.dob_var.set("")
        self.text_address.delete("1.0",tk.END)
        
    def get_cursor(self,ev):
        cursor_row=self.student_table.focus()
        contents=self.student_table.item(cursor_row)
        row=contents['values']
        self.Roll_No_var.set(row[0])
        self.name_var.set(row[1])
        self.email_var.set(row[2])
        self.gender_var.set(row[3])
        self.contact_var.set(row[4])
        self.dob_var.set(row[5])
        self.text_address.delete("1.0",tk.END)
        self.text_address.insert(tk.END,row[6])
        
    def update_data(self):
        con=pymysql.connect(host="localhost",user="root",password="1234",database="stm")
        cur=con.cursor()
        cur.execute("update students set name=%s,email=%s,gender=%s,contact=%s,dob=%s,address=%s where roll_no=%s",(self.name_var.get(),self.email_var.get(),self.gender_var.get(),self.contact_var.get(),self.dob_var.get(),self.text_address.get('1.0',tk.END),self.Roll_No_var.get()))
        con.commit()
        self.fetch_data()
        self.clear()
        con.close()
        
    def delete_data(self):
        con=pymysql.connect(host="localhost",user="root",password="1234",database="stm")
        cur=con.cursor()
        cur.execute("delete from students where roll_no=%s",self.Roll_No_var.get())
        con.commit()
        con.close()
        self.fetch_data()
        self.clear()
        
    def search_data(self):
        con=pymysql.connect(host="localhost",user="root",password="1234",database="stm")
        cur=con.cursor()
        cur.execute("select * from students where "+str(self.search_by.get())+" LIKE '%"+str(self.search_text.get())+"%'")
        rows=cur.fetchall()
        if len(rows)!=0:
            self.student_table.delete(*self.student_table.get_children())
            for rows in rows:
                self.student_table.insert('',tk.END,values=rows)
            con.commit()
        con.close()

root=tk.Tk()
s=Student(root)
root.mainloop()