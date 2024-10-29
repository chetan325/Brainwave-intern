from tkinter import *
from Employees import employee_form


#defining
 



# GUI Part
window = Tk()

window.title('Dashboard')
window.geometry('1270x668+0+0')
window.resizable(0,0)
window.config(bg='white')

bg_image = PhotoImage(file='inventory.png')
titleLabel = Label(window, image=bg_image,compound=LEFT,text = 'Inventory Management System  ',font=('times new roman',40,'bold'),bg='#010c48',fg='white',anchor='w',padx=20)

titleLabel.place(x=0,y=0,relwidth=1)

logoutButton = Button(window,text='Logout',font=('Times New Roman',20,'bold' ),fg='#010c48')
logoutButton.place(x=1100,y=10)

subtitelLabel = Label(window,text='Welcome Admin\t\t Date:08-02-2024\t\t Time: 12:25:8pm',font=('times new roman',15),bg='#4d636d',fg='white')
subtitelLabel.place(x=0,y=70,relwidth=1)


leftFrame = Frame(window)
leftFrame.place(x=0,y=102,width=200,height=555)
logoImage = PhotoImage(file='logo.png')
imageLabel = Label(leftFrame,image=logoImage)
imageLabel.pack()

MenuLabel = Label(leftFrame,text='Menu',font=('times new roman',20),bg='#009688')
MenuLabel.pack(fill=X)

employee_icon = PhotoImage(file='employee.png')
employeeButton = Button(leftFrame,image=employee_icon,compound=LEFT,text='   Employee',font=('times new roman',20,'bold'),command=lambda: employee_form(window))
employeeButton.pack(fill=X)

supplier_icon = PhotoImage(file='supplier.png')
supplierButton = Button (leftFrame,image=supplier_icon,compound=LEFT,text ='   Supplier',font=('times new roman',20,'bold'))
supplierButton.pack(fill=X)


category_icon = PhotoImage(file='category.png')
categoryButton = Button(leftFrame,image=category_icon,compound=LEFT,text='   Category',font=('times new roman',20,'bold'))
categoryButton.pack(fill=X)

product_icon = PhotoImage(file='product.png')
productButton = Button(leftFrame,image=product_icon,compound=LEFT,text='   Product',font=('times new roman',20,'bold'))
productButton.pack(fill=X)

sales_icon = PhotoImage(file='sales.png')
salesButton = Button (leftFrame,image=sales_icon,compound=LEFT,text='     Sales  ',font=('times new roman',20,'bold'))
salesButton.pack(fill=X)

exit_icon = PhotoImage(file='exit.png')
exitButton = Button(leftFrame,image=exit_icon,compound=LEFT,text='     Exit',font=('times new roman',20,'bold'))
exitButton.pack(fill=X)

# eployess box
emp_frame = Frame(window,bg='#2C3E50',bd=3,relief=RIDGE)
emp_frame.place(x=400,y=125,height=170,width=280) 
tot_emp_icon = PhotoImage (file ='tot_emp.png')
tot_emp_icon_label = Label(emp_frame,image=tot_emp_icon,bg='#2C3E50')
tot_emp_icon_label.pack()



tot_emp_label = Label(emp_frame,text='Total Employees',bg='#2C3E50',fg='white',font=('times new roman',20,'bold'))
tot_emp_label.pack()



tot_emp_count_label = Label(emp_frame,text='0',bg='#2C3E50',fg='white',font=('times new roman',30,'bold'))
tot_emp_count_label.pack()



#sales Box
sales_frame = Frame(window,bg='#2C3E50',bd=3,relief=RIDGE)
sales_frame.place(x=800,y=125,height=170,width=280) 
tot_sales_icon = PhotoImage (file ='tot_sales.png')
tot_sales_icon_label = Label(sales_frame,image=tot_sales_icon,bg='#2C3E50')
tot_sales_icon_label.pack()



tot_sales_label = Label(sales_frame,text='Total Sales',bg='#2C3E50',fg='white',font=('times new roman',20,'bold'))
tot_sales_label.pack()



tot_sales_count_label = Label(sales_frame,text='0',bg='#2C3E50',fg='white',font=('times new roman',30,'bold'))
tot_sales_count_label.pack()


#sulliper box
supplier_frame = Frame(window,bg='#2C3E50',bd=3,relief=RIDGE)
supplier_frame.place(x=400,y=300,height=170,width=280) 
tot_supplier_icon = PhotoImage (file ='tot_supplier.png')
tot_supplier_icon_label = Label(supplier_frame,image=tot_supplier_icon,bg='#2C3E50')
tot_supplier_icon_label.pack()



tot_supplier_label = Label(supplier_frame,text='Total Supplier',bg='#2C3E50',fg='white',font=('times new roman',20,'bold'))
tot_supplier_label.pack()



tot_supplier_count_label = Label(supplier_frame,text='0',bg='#2C3E50',fg='white',font=('times new roman',30,'bold'))
tot_supplier_count_label.pack()


#total Product box
product_frame = Frame(window,bg='#2C3E50',bd=3,relief=RIDGE)
product_frame.place(x=800,y=300,height=170,width=280) 
tot_product_icon = PhotoImage (file ='tot_supplier.png')
tot_product_icon_label = Label(product_frame,image=tot_product_icon,bg='#2C3E50')
tot_product_icon_label.pack()



tot_product_label = Label(product_frame,text='Total Producct',bg='#2C3E50',fg='white',font=('times new roman',20,'bold'))
tot_product_label.pack()



tot_product_count_label = Label(product_frame,text='0',bg='#2C3E50',fg='white',font=('times new roman',30,'bold'))
tot_product_count_label.pack()


#tot category box
cat_frame = Frame(window,bg='#2C3E50',bd=3,relief=RIDGE)
cat_frame.place(x=600,y=480,height=170,width=280) 
tot_cat_icon = PhotoImage (file ='tot_cat.png')
tot_cat_icon_label = Label(cat_frame,image=tot_cat_icon,bg='#2C3E50')
tot_cat_icon_label.pack()



tot_cat_label = Label(cat_frame,text='Total Categories',bg='#2C3E50',fg='white',font=('times new roman',20,'bold'))
tot_cat_label.pack()



tot_cat_count_label = Label(cat_frame,text='0',bg='#2C3E50',fg='white',font=('times new roman',30,'bold'))
tot_cat_count_label.pack()

window.mainloop()

