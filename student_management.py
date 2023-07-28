
from tkinter import *
from tkinter import ttk
import datetime as dt

from PIL import Image,ImageTk

import pymysql as pm


class NTHstudents:
    def __init__(self,root):
        self.root=root #this is for main frame in window
        #this is for form title
        self.root.title('NTH students data')
        self.root.geometry('1500x800') #for height and weidth for main window
        
        #this is for header of the form
        title=Label(self.root,text='Welcome To Narayana Tech House',bd=4,relief=GROOVE,background='green',fg='white',font=('italic',20,'bold'))

        title.pack(fill=X,side=TOP)
        
        
        
        #create 10 instance variables 
        self.roll_no=StringVar()
        self.first_name=StringVar()
        self.last_name=StringVar()
        self.mobno=StringVar()
        self.gmail_id=StringVar()
        self.course_name=StringVar()
        self.feess=StringVar()
        self.faculty_name=StringVar()
        self.locations=StringVar()
        self.genders=StringVar()
        self.searchby=StringVar()
        self.searchtxt=StringVar()

        #this is for creating a frame in left side
        dataentryframe=Frame(self.root,bg='yellow',bd=5,relief=GROOVE)
        dataentryframe.place(x=10,y=50,width=420,height=740)
        
        
        #this is 2nd side create
        datadisplay=Frame(self.root,bg='red',bd=5,relief=GROOVE)
        
        datadisplay.place(x=440,y=50,width=1090,height=325)
        
        photoframe=Frame(self.root,bg='blue',bd=5,relief=GROOVE)
        
        photoframe.place(x=440,y=380,width=1090,height=410)
        #test=ImageTk.PhotoImage(Image.open('C:\\python programms\\python projects\\msahu.png'))
        #lab=Label(photoframe,image=test)
        #lab.pack()
        
        
        
        
        
        #this is for title showing in top of the page
        title=Label(dataentryframe,text='Enter your Details...',bg='yellow',fg='red',font=('roman',20,'bold'))
        title.grid(row=0,columnspan=2,padx=50,pady=10)
        #creating Roll no,first name,lastname,mob no,college name,etc
        rollno=Label(dataentryframe,text='Enter Roll No : ',bg='yellow',fg='red',font=('roman',15,'bold'))
        rollno.grid(row=1,column=0,sticky='W',padx=5,pady=10)
        #this is for entry the data in roll no
        txt_rollno=Entry(dataentryframe,textvariable=self.roll_no, font=('times new roman',15,'bold'))
        txt_rollno.grid(row=1,column=1)
        #this is for blank form create
        #first name
        firstname=Label(dataentryframe,text='Enter first Name : ',bg='yellow',fg='red',font=('roman',15,'bold'))
        firstname.grid(row=2,column=0,sticky='W',padx=5,pady=10)
        #first name entry box 
        txt_firstname=Entry(dataentryframe,textvariable=self.first_name,font=('times new roman',15,'bold'))
        txt_firstname.grid(row=2,column=1)
        #lastname
        lastname=Label(dataentryframe,text='Enter Last Name : ',bg='yellow',fg='red',font=('roman',15,'bold'))
        lastname.grid(row=3,column=0,sticky='W',padx=5,pady=10)
        #last name entry box
        txt_lastname=Entry(dataentryframe,textvariable=self.last_name,font=('times new roman',15,'bold'))
        txt_lastname.grid(row=3,column=1)
        #mobno
        mob_no=Label(dataentryframe,text='Enter Mobile No : ',bg='yellow',fg='red',font=('roman',15,'bold'))
        mob_no.grid(row=4,column=0,sticky='W',padx=5,pady=10)
        #mob no entry box
        txt_mobno=Entry(dataentryframe,textvariable=self.mobno,font=('times new roman',15,'bold'))
        txt_mobno.grid(row=4,column=1)
        #gmailid
        gmail=Label(dataentryframe,text='Enter Gmail id : ',bg='yellow',fg='red',font=('roman',15,'bold'))
        gmail.grid(row=5,column=0,sticky='W',padx=5,pady=10)
        #gmail entry box
        txt_gmail=Entry(dataentryframe,textvariable=self.gmail_id,font=('times new roman',15,'bold'))
        txt_gmail.grid(row=5,column=1)
        #coursename
        coursename=Label(dataentryframe,text='Enter Course Name : ',bg='yellow',fg='red',font=('roman',15,'bold'))
        coursename.grid(row=6,column=0,sticky='W',padx=5,pady=10)
        #course name entry box
        txt_coursename=Entry(dataentryframe,textvariable=self.course_name,font=('times new roman',15,'bold'))
        txt_coursename.grid(row=6,column=1)
        #fees
        fees=Label(dataentryframe,text='Enter Your Fees :',bg='yellow',fg='red',font=('roman',15,'bold'))
        fees.grid(row=7,column=0,sticky='W',padx=5,pady=10)
        #fees entry box
        txt_fees=Entry(dataentryframe,textvariable=self.feess,font=('times new roman',15,'bold'))
        txt_fees.grid(row=7,column=1)
        #faculty
        faculty=Label(dataentryframe,text='Enter faculty Name : ',bg='yellow',fg='red',font=('roman',15,'bold'))
        faculty.grid(row=8,column=0,sticky='W',padx=5,pady=10)
        #faculty 
        txt_faculty=Entry(dataentryframe,textvariable=self.faculty_name,font=('times new roman',15,'bold'))
        txt_faculty.grid(row=8,column=1,sticky='W')
        #location
        location=Label(dataentryframe,text='Enter Location : ',bg='yellow',fg='red',font=('roman',15,'bold'))
        location.grid(row=9,column=0,sticky='W',padx=5,pady=10)
        txt_location=Entry(dataentryframe,textvariable=self.locations,font=('times new roman',15,'bold'))
        txt_location.grid(row=9,column=1)
        #gender
        gender=Label(dataentryframe,text='Enter Your Gender : ',bg='yellow',fg='red',font=('roman',15,'bold'))
        gender.grid(row=10,column=0,sticky='W',padx=5,pady=10)
        txt_gender=Entry(dataentryframe,textvariable=self.genders,font=('times new roman',15,'bold'))
        txt_gender.grid(row=10,column=1)
        #this is for 3rd frame creating
        submitframe=Frame(dataentryframe,bd=4,bg='yellow',relief=GROOVE)
        submitframe.place(x=10,y=570,width=390,height=80)
        #add button in 3rd frame
        btn_add=Button(submitframe,text='Add',width=7,bg='pink',font=('times new roman',12,'bold'),command=self.adding_data)
        btn_add.grid(row=0,column=0,padx=7,pady=15)
        #update button in 3rd frame
        btn_update=Button(submitframe,text='Update',width=7,bg='pink',command=self.update_data,font=('times new roman',12,'bold'))
        btn_update.grid(row=0,column=1,padx=7,pady=15)
        #clear button in 3rd frame
        btn_clear=Button(submitframe,text='Clear',command=self.clear_data,width=7,bg='pink',font=('times new roman',12,'bold'))
        btn_clear.grid(row=0,column=2,padx=7,pady=15)
        #add delete button 
        btn_delete=Button(submitframe,text='Delete',width=10,bg='pink',command=self.delete_data,font=('times new roman',12,'bold'))
        btn_delete.grid(row=0,column=3,padx=7,pady=15)
        time1=Frame(dataentryframe,relief=GROOVE,bd=10,bg='yellow')

        time1.place(x=10,y=670,width=380,height=50)
        time_var=Label(time1,text=dt.datetime.now(),bg='yellow',fg='red',font=('roman',17,'bold'))
        time_var.grid(row=0,column=0,padx=30,sticky='E')

        #create search button
        lbl_search=Label(datadisplay,text='Search : ',width=10,bg='red',fg='blue',font=('times new roman',20,'bold'))
        lbl_search.grid(row=0,column=0,padx=5,sticky='W',pady=10)


        combo_search=ttk.Combobox(datadisplay,width=20,textvariable=self.searchby,font=('times new roman',15,'bold'))
        combo_search['values']=('coursename','location','Faculty')
        combo_search.grid(row=0,column=1,sticky='W',padx=10,pady=10)
        txt_search=Entry(datadisplay,width=15,textvariable=self.searchtxt,font=('times new roman',15,'bold'))        
        txt_search.grid(row=0,sticky='W',column=2,padx=10)
        btn_search=Button(datadisplay,text='search',width=15,command=self.searchdata,font=('times new roman',15,'bold'))
        btn_search.grid(row=0,column=3,padx=10,pady=10)
        btnshow=Button(datadisplay,text='showall',command=self.fetch_all,font=('times new roman',15,'bold'),width=15)
        btnshow.grid(row=0,column=4,padx=10,pady=10)
        tableframe=Frame(datadisplay,bd=5,relief=GROOVE)
        tableframe.place(x=10,y=60,width=1060,height=250)
        self.student_table=ttk.Treeview(tableframe,columns=('rollno','firstname','lastname','mob_no','gmail','coursename','fees','faculty','location','gender'))
        self.student_table.heading('rollno',text='Roll No')
        self.student_table.heading('firstname',text='First Name')
        self.student_table.heading('lastname',text='Last Name')
        self.student_table.heading('mob_no',text='Mob No')
        self.student_table.heading('gmail',text='Gmail ID')
        self.student_table.heading('coursename',text='Course')
        self.student_table.heading('fees',text='Fees')
        self.student_table.heading('faculty',text='Faculty')
        self.student_table.heading('location',text='Location')
        self.student_table.heading('gender',text='Gender')
        self.student_table['show']='headings'
        self.student_table.column('rollno',width=70,anchor=CENTER)
        self.student_table.column('firstname',width=120,anchor=CENTER)
        self.student_table.column('lastname',width=80,anchor=CENTER)
        self.student_table.column('mob_no',width=150,anchor=CENTER)
        self.student_table.column('gmail',width=180,anchor=CENTER)
        self.student_table.column('coursename',width=80,anchor=CENTER)
        self.student_table.column('fees',width=60,anchor=CENTER)
        self.student_table.column('faculty',width=130,anchor=CENTER)
        self.student_table.column('location',width=90,anchor=CENTER)
        self.student_table.column('gender',width=100,anchor=CENTER)

        
        self.student_table.pack()

        self.fetch_all()
        self.student_table.bind('<ButtonRelease-1>',self.get_cursor)



        

#this function is used for connect database
    def adding_data(self):
        connection=pm.connect(host='localhost',user='root',passwd='pintu7077',db='nthstudentsdata')
        c=connection.cursor()
        #insert data from 
        c.execute('insert into studentsinfo values(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)',#%s is using for dynamic value like input data 
                    #get() is used for get the data from the entry form
                    (self.roll_no.get(),
                    self.first_name.get(),
                    self.last_name.get(),
                    self.mobno.get(),
                    self.gmail_id.get(),
                    self.course_name.get(),
                    self.feess.get(),
                    self.faculty_name.get(),
                    self.locations.get(),
                    self.genders.get()))

            
        connection.commit()#save the data in database
        self.fetch_all()
        self.clear_data()
        connection.close()#close the connection from database
    def clear_data(self):
        self.roll_no.set('')
        self.first_name.set('')
        self.last_name.set('')
        self.mobno.set('')
        self.gmail_id.set('')
        self.course_name.set('')
        self.feess.set('')
        self.faculty_name.set('')
        self.locations.set('')
        self.genders.set('')
    def get_cursor(self,var):
        cursor_row=self.student_table.focus()
        content=self.student_table.item(cursor_row)
        row=content['values']
        self.roll_no.set(row[0])
        self.first_name.set(row[1])
        self.last_name.set(row[2])
        self.mobno.set(row[3])
        self.gmail_id.set(row[4])
        self.course_name.set(row[5])
        self.feess.set(row[6])
        self.faculty_name.set(row[7])
        self.locations.set(row[8])
        self.genders.set(row[9])
    def update_data(self):
        connection=pm.connect(host='localhost',user='root',passwd='pintu7077',db='nthstudentsdata')
        c=connection.cursor()
        c.execute('update studentsinfo set first_name=%s,last_name=%s,mob_no=%s,gmail_id=%s,course=%s,fees=%s,faculty_name=%s,location=%s,gender=%s where rollno=%s',
        (
            self.first_name.get(),
            self.last_name.get(),
            self.mobno.get(),
            self.gmail_id.get(),
            self.course_name.get(),
            self.feess.get(),
            self.faculty_name.get(),
            self.locations.get(),
            self.genders.get(),
            self.roll_no.get()

        ))
        connection.commit()
        self.clear_data()
        self.fetch_all()


        connection.close()
    def delete_data(self):
        connection=pm.connect(host='localhost',user='root',passwd='pintu7077',db='nthstudentsdata')
        c=connection.cursor()
        c.execute('delete from studentsinfo where rollno=%s',(self.roll_no.get()))
        connection.commit()
        self.clear_data()
        self.fetch_all()
        connection.close()



    def searchdata(self):
        connection=pm.connect(host='localhost',db='nthstudentsdata',password='pintu7077',user='root')
        c=connection.cursor()
        c.execute("select * from studentsinfo "
         "where "+ str(self.searchby.get())+" like '%"+str(self.searchtxt.get())+"%'")
        rows=c.fetchall()
        if len(rows) >=1:
            self.student_table.delete(*self.student_table.get_children())
            for row in rows:
                self.student_table.insert('',END,values=row)
            connection.commit()
        connection.close()

        
    




        







    def fetch_all(self):
        connection=pm.connect(db='nthstudentsdata',password='pintu7077',host='localhost',user='root')

        c=connection.cursor()
        c.execute('select * from studentsinfo')
        rows=c.fetchall()
        if len(rows) >=1:
            self.student_table.delete(*self.student_table.get_children())
            for row in rows:
                self.student_table.insert('',END,values=row)
            connection.commit()
        connection.close()
            
            


root=Tk()
obj=NTHstudents(root)
root.mainloop()



