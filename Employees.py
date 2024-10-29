from tkinter import *
from tkinter import ttk
import pymysql
from tkinter import messagebox


# Function to connect to the database
def connect_database():
    try:
        connection = pymysql.connect(host='localhost', user='root', password='Csb@sql12')
        cursor = connection.cursor()
    except: 
        messagebox.showerror('Error', 'Database connection error. Please open MySQL command line.')
        return None, None
    
    cursor.execute('CREATE DATABASE IF NOT EXISTS inventory_system1')
    cursor.execute('USE inventory_system1')
    
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS employee_data1 (
            empid INT PRIMARY KEY,
            name VARCHAR(100),
            email VARCHAR(30),
            gender VARCHAR(20),
            dob VARCHAR(30),
            contact VARCHAR(20),
            employement_type VARCHAR(22),
            education VARCHAR(30),
            work_shift VARCHAR(30),
            address VARCHAR(255),  
            doj VARCHAR(30),
            salary VARCHAR(20),
            user_type VARCHAR(40),
            password VARCHAR(30)
        )
    ''')
    return cursor, connection

# Function to fetch data and display it in the TreeView
def treeview_data():
    cursor, connection = connect_database()
    if not cursor or not connection:
        return
    cursor.execute('SELECT * FROM employee_data1')
    employee_records = cursor.fetchall()
    employee_treeview.delete(*employee_treeview.get_children())

    for records in employee_records:
        employee_treeview.insert('', END, values=records)

# Function to add an employee to the database
def add_employee(empid, name, email, gender, dob, contact, employement_type, education, work_shift, address, doj, salary, user_type, password):
    if (empid == '' or name == '' or email == '' or gender == 'Select gender' or dob == '' or contact == '' or 
        employement_type == '' or education == '' or  work_shift == 'select type' or  address == '' or doj == 'select date' or  salary == '' or user_type == 'Select type'  or password == '' ):
        
        messagebox.showerror('Error', 'Please fill all the fields')
        return
    else:
        cursor, connection = connect_database()
        if not cursor or not connection:
            return
        
        query = '''INSERT INTO employee_data1 
           (empid,name,email,gender,dob,contact,employement_type,education,work_shift,address,doj,salary,user_type,password) 
           VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)'''
        values = (empid,name,email,gender,dob,contact,employement_type,education,work_shift,address,doj,salary,user_type,password)
        
        try:
            cursor.execute(query, values)
            connection.commit()
            treeview_data()
            messagebox.showinfo('Success', 'Data is inserted successfully')
        except Exception as e:
            messagebox.showerror('Error', f'Error inserting data: {str(e)}')
        finally:
            connection.close()

# Function to clear the input fields
def clear_fields(empid_entry,  name_entry,email_entry, gender_combobox,dob_combobox,contact_entry, employement_type_combobox,education_type_combobox,work_shift_combobox, address_textarea,doj_combobox, salary_entry, user_type_combobox,   password_entry   ):
    empid_entry.delete(0, END)
    name_entry.delete(0, END)
    email_entry.delete(0, END)
    gender_combobox.set('Select gender')
    contact_entry.delete(0, END)
    employement_type_combobox.set('select type')
    education_type_combobox.set('Select type')
    work_shift_combobox.set('Select type')
    address_textarea.delete(0, END)
    salary_entry.delete(0, END)
    user_type_combobox.set('Select type')
    password_entry.delete(0, END)
    from datetime import date 
    dob_combobox.set_date(date.today())
    doj_combobox.set_date(date.today())
    

# Employee form UI
def employee_form(window):
    global back_image, employee_treeview
    employee_frame = Frame(window, height=567, width=1070, bg='white')
    employee_frame.place(x=200, y=100)
    
    heading_label = Label(employee_frame, text='Manage Employee Details', font=('times new roman', 16, 'bold'), bg='#0f4d7d', fg='white')
    heading_label.place(x=0, y=0, relwidth=1)
   
    topFrame = Frame(employee_frame, bg='white')
    topFrame.place(x=0, y=40, relwidth=1, height=235)
    
    back_image = PhotoImage(file='back.png')
    back_Button = Button(topFrame, image=back_image, bd=0, cursor='hand2', bg='white', command=lambda: employee_frame.place_forget())
    back_Button.place(x=0, y=0)
    
    search_frame = Frame(topFrame, bg='white')
    search_frame.pack()
    
    search_combobox = ttk.Combobox(search_frame, values=('ID', 'Name', 'Email'), font=('times new roman', 12), state='readonly', justify='center')
    search_combobox.set('Search By')
    search_combobox.grid(row=0, column=0, padx=20)
    
    search_entry = Entry(search_frame, font=('times new roman', 12), bg='lightyellow')
    search_entry.grid(row=0, column=1, padx=10, pady=10)
    
    search_Button = Button(search_frame, text='Search', font=('times new roman', 12), width='10', cursor='hand2', fg='white', bg='#0f4d7d')
    search_Button.grid(row=0, column=2, padx=20)
    
    show_all_Button = Button(search_frame, text='Show All', font=('times new roman', 12), cursor='hand2', fg='white', bg='#0f4d7d')
    show_all_Button.grid(row=0, column=3)

    horizental_scrollbar = Scrollbar(topFrame, orient=HORIZONTAL)
    vertical_scrollbar = Scrollbar(topFrame, orient=VERTICAL)
    
    employee_treeview = ttk.Treeview(topFrame, columns=('EmpId', 'Name', 'Email', 'Gender', 'DoB', 'Contact', 'Employement_type', 'Education', 'Work_shift', 'Address', 'Doj', 'Salary', 'User_type'), show='headings', yscrollcommand=vertical_scrollbar.set, xscrollcommand=horizental_scrollbar.set)
    
    horizental_scrollbar.pack(side=BOTTOM, fill=X)
    vertical_scrollbar.pack(side=RIGHT, fill=Y, pady=(10, 0))
    horizental_scrollbar.config(command=employee_treeview.xview)
    vertical_scrollbar.config(command=employee_treeview.yview)

    employee_treeview.pack(pady=(10, 0))

    employee_treeview.heading('EmpId', text='EmpId')
    employee_treeview.heading('Name', text='Name')
    employee_treeview.heading('Email', text='Email')
    employee_treeview.heading('Gender', text='Gender')
    employee_treeview.heading('DoB', text='DoB')
    employee_treeview.heading('Contact', text='Contact')
    employee_treeview.heading('Employement_type', text='Employement_type')
    employee_treeview.heading('Education', text='Education')
    employee_treeview.heading('Work_shift', text='Work_shift')
    employee_treeview.heading('Address', text='Address')
    employee_treeview.heading('Salary', text='Salary')
    employee_treeview.heading('Doj', text='Doj')
    employee_treeview.heading('User_type', text='User_type')

    employee_treeview.column('EmpId', width=60)
    employee_treeview.column('Name', width=140)
    employee_treeview.column('Email', width=180)
    employee_treeview.column('Gender', width=80)
    employee_treeview.column('DoB', width=100)
    employee_treeview.column('Contact', width=100)
    employee_treeview.column('Employement_type', width=120)
    employee_treeview.column('Education', width=120)
    employee_treeview.column('Work_shift', width=120)
    employee_treeview.column('Address', width=100)
    employee_treeview.column('Doj', width=100)
    employee_treeview.column('Salary', width=100)
    employee_treeview.column('User_type', width=200)
    
    
    treeview_data()

    # Detail frame for employee information input
    detail_frame = Frame(employee_frame,bg='white')
    detail_frame.place(x=20,y=280)

    empid_label = Label(detail_frame,text='EmpId',font=('times new roman',12),bg='white')
    empid_label.grid(row=0,column=0,padx=20)
    empid_entry = Entry(detail_frame,font=('times new roman',12),bg='lightyellow')
    empid_entry.grid(row=0,column=1,pady=10)


    name_label = Label(detail_frame,text='Name',font=('times new roman',12),bg='white')
    name_label.grid(row=0,column=2,padx=20)
    name_entry = Entry(detail_frame,font=('times new roman',12),bg='lightyellow')
    name_entry.grid(row=0,column=3,pady=10,padx=20)

    email_label = Label(detail_frame,text='Email',font=('times new roman',12),bg='white')
    email_label.grid(row=0,column=4,padx=20)
    email_entry = Entry(detail_frame,font=('times new roman',12),bg='lightyellow')
    email_entry.grid(row=0,column=5,pady=10,padx=20)

    '''empid_label = Label(detail_frame,text='EmpId',font=('times new roman',12),bg='white')
    empid_label.grid(row=0,column=0,padx=20)
    empid_entry = Entry(detail_frame,font=('times new roman',12),bg='lightyellow')
    empid_entry.grid(row=0,column=1,pady=10,padx=20)'''

    gender_label = Label(detail_frame,text='Gender',font=('times new roman',12),bg='white')
    gender_label.grid(row=1,column=0,padx=20)

    gender_combobox = ttk.Combobox(detail_frame,values=('Male','Female'),font=('times new roman',12),width=18,state='readonly')
    gender_combobox.set('Select Gender')
    gender_combobox.grid(row=1,column=1)
   
    dob_label = Label(detail_frame,text='Date of Birth',font=('times new roman',12),bg='white')
    dob_label.grid(row=1,column=2,padx=20)

    dob_combobox = ttk.Combobox(detail_frame,font=('times new roman',12),width=18)
    dob_combobox.set('DD/MM/YYYY')
    dob_combobox.grid(row=1,column=3)

    contact_label = Label(detail_frame,text='Contact Number',font=('times new roman',12),bg='white')
    contact_label.grid(row=1,column=4,padx=20)
    contact_entry = Entry(detail_frame,font=('times new roman',12),bg='lightyellow')
    contact_entry.grid(row=1,column=5,pady=10,padx=20)


    employement_type_label = Label(detail_frame,text='Emp Type',font=('times new roman',12),bg='white')
    employement_type_label.grid(row=2,column=0,padx=20,pady=10)

    employement_type_combobox = ttk.Combobox(detail_frame,values=('Full Time','Part Tme','Intern','Contract'),font=('times new roman',12),width=18,state='readonly')
    employement_type_combobox.set('Select Type')
    employement_type_combobox.grid(row=2,column=1)

    education_type_label = Label(detail_frame,text='Education Type',font=('times new roman',12),bg='white')
    education_type_label.grid(row=2,column=2,padx=20,pady=10)

    education_type_combobox = ttk.Combobox(detail_frame,values=('BE','ME','Bcom','Bsc','Mcom','BA','Any Drgree','Other'),font=('times new roman',12),width=18,state='readonly')
    education_type_combobox.set('Select Education Type')
    education_type_combobox.grid(row=2,column=3)

    work_shift_label = Label(detail_frame,text='Work Shifts',font=('times new roman',12),bg='white')
    work_shift_label.grid(row=2,column=4,padx=20,pady=10)

    work_shift_combobox = ttk.Combobox(detail_frame,values=('Day','Night','Evening'),font=('times new roman',12),width=18,state='readonly')
    work_shift_combobox.set('Select Type')
    work_shift_combobox.grid(row=2,column=5)


    address_label = Label (detail_frame,text='Address',font=('times new roman',12),bg='white')
    address_label.grid(row=3,column=0)
    address_textarea = Text(detail_frame,width=20,height=3,bg='lightblue')
    address_textarea.grid(row=3,column=1,rowspan=2)


    doj_label = Label(detail_frame,text='Date of Joining',font=('times new roman',12),bg='white')
    doj_label.grid(row=3,column=2,padx=20,pady=10)

    doj_combobox = ttk.Combobox(detail_frame,font=('times new roman',12),width=18)
    doj_combobox.set('DD/MM/YYYY')
    doj_combobox.grid(row=3,column=3)


    
    salary_label = Label(detail_frame,text='Salary',font=('times new roman',12),bg='white')
    salary_label.grid(row=3,column=4,padx=20)
    salary_entry = Entry(detail_frame,font=('times new roman',12),bg='lightyellow')
    salary_entry.grid(row=3,column=5,pady=10,padx=20)

    user_type_label = Label(detail_frame,text='User Type',font=('times new roman',12),bg='white')
    user_type_label.grid(row=4,column=2,padx=20,pady=10)

    user_type_combobox = ttk.Combobox(detail_frame,values=('Admin','Employee'),font=('times new roman',12),width=18,state='readonly')
    user_type_combobox.set('Select User Type')
    user_type_combobox.grid(row=4,column=3)


    password_label = Label(detail_frame,text='Password',font=('times new roman',12),bg='white')
    password_label.grid(row=4,column=4,padx=20)
    password_entry = Entry(detail_frame,font=('times new roman',12),bg='lightyellow')
    password_entry.grid(row=4,column=5,pady=10,padx=20)

    Button_frame =Frame(employee_frame)
    Button_frame.place(x=200,y=515)

    add_Button = Button(Button_frame, text='Add', font=('times new roman', 12), width='10', cursor='hand2', fg='white', bg='#0f4d7d', 
                    command=lambda: add_employee(empid_entry.get(), 
                                                 name_entry.get(), 
                                                 email_entry.get(), 
                                                 gender_combobox.get(),  # Corrected typo here
                                                 dob_combobox.get(), 
                                                 contact_entry.get(), 
                                                 employement_type_combobox.get(), 
                                                 education_type_combobox.get(), 
                                                 work_shift_combobox.get(), 
                                                 address_textarea.get(1.0, END), 
                                                 doj_combobox.get(), 
                                                 salary_entry.get(), 
                                                 user_type_combobox.get(), 
                                                 password_entry.get()))
    add_Button.grid(row=0, column=0, padx=20)

    update_Button = Button(Button_frame,text='Update',font=('times new roman',12),width='10',cursor='hand2',fg='white',bg='#0f4d7d')
    update_Button.grid(row=0,column=1,padx=20)

    delete_Button = Button(Button_frame,text='Delete',font=('times new roman',12),width='10',cursor='hand2',fg='white',bg='#0f4d7d')
    delete_Button.grid(row=0,column=2,padx=20)

    clear_Button = Button(Button_frame,text='Clear',font=('times new roman',12),width='10',cursor='hand2',fg='white',bg='#0f4d7d',command=lambda:clear_fields(empid_entry,name_entry,email_entry,gender_combobox,dob_combobox,contact_entry,employement_type_combobox,education_type_combobox,work_shift_combobox,address_textarea,doj_combobox,salary_entry,user_type_combobox,password_entry))
    clear_Button.grid(row=0,column=3,padx=20)



   