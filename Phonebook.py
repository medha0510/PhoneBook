from Tkinter import *
import FirstPage
from tkMessageBox import *
def Insert():
    try:
        a=((e1.get(),e2.get(),e3.get(),e4.get(),e7.get(),e8.get(),e9.get(),e10.get(),e11.get()))
        cur.execute('insert into Contact_details (Ph_Fname,Ph_Mname,Ph_Lname,Ph_company,Ph_address,Ph_city,Ph_Pin,Ph_website,Ph_DOB) values(?,?,?,?,?,?,?,?,?)',a)
        cur.execute('select Id from Contact_details')
        xy=cur.fetchall()
        xy=xy[-1][0]
        global b
        b=''
        if v1.get()==1:
            b="Office"
        elif v1.get()==2:
            b="Home"
        elif v1.get()==3:
            b="Mobile"
        cur.execute('insert into P_number_details (Id,Ph_Pno,Ph_Pno_type) values (?,?,?)',(xy,e5.get(),b))
        global c
        c=''
        if v2.get()==1:
            c="Office"
        elif v2.get()==2:
            c="Mobile"
        cur.execute('insert into Email_details (Id,Ph_EmailId,Ph_EID_type) values (?,?,?)',(xy,e6.get(),c))
        con.commit()
        e1.delete(0,END)
        e2.delete(0,END)
        e3.delete(0,END)
        e4.delete(0,END)
        e5.delete(0,END)
        e6.delete(0,END)
        e7.delete(0,END)
        e8.delete(0,END)
        e9.delete(0,END)
        e10.delete(0,END)
        e11.delete(0,END)
            
        showinfo('Message','Saved Successfully')
    except:
        showerror('Error','Oops! Something went wrong.')
    
    
def Search():
    root.destroy()
    global output1
    root1=Tk()
    root1.geometry("550x580")
    Label(root1,text='SEARCH HERE ',font='times 20',fg='BLUE',relief="ridge").grid(column=3,row=1)
    search=Entry(root1)
    search.grid(column=3,row=2)
    lb=Listbox(root1,width=60, height=30)

    cur.execute("select Id,Ph_Fname,Ph_Mname,Ph_Lname from Contact_details")
    output1=cur.fetchall()
    for i in output1:
            lb.insert(END,i[1]+' '+i[2]+' '+i[3])

            
    def select(event):
        widget=event.widget
        selection=widget.curselection()
        v=selection[0]
        root2=Tk()
        root2.geometry("550x530")
        c_id=(output1[v][0],)
        cur.execute('select * from Contact_details where Id=?',c_id)
        L=cur.fetchall()
        Label(root2,text='INFORMATION',font='times20',fg='BLUE').pack()
        f='First Name: '+L[0][1]
        Label(root2,text=f).pack()
        f='Middle Name: '+L[0][2]
        Label(root2,text=f).pack()
        f='Last Name: '+L[0][3]
        Label(root2,text=f).pack()
        f='Company Name: '+L[0][4]
        Label(root2,text=f).pack()
        f='Address: '+L[0][5]
        Label(root2,text=f).pack()
        f='City: '+L[0][6]
        Label(root2,text=f).pack()
        f='Pincode: '+L[0][7]
        Label(root2,text=f).pack()
        f='Website URL: '+L[0][8]
        Label(root2,text=f).pack()
        f='Date of Birth: '+L[0][9]
        Label(root2,text=f).pack()
        cur.execute('select * from P_number_details where Id=?',c_id)
        L=cur.fetchall()
        f='Phone No: '+L[0][1]
        Label(root2,text=f).pack()
        f='Phone No type: '+L[0][2]
        Label(root2,text=f).pack()
        cur.execute('select * from Email_details where Id=?',c_id)
        L=cur.fetchall()
        f='Emai ID: '+L[0][1]
        Label(root2,text=f).pack()
        f='Email ID Type: '+L[0][2]
        Label(root2,text=f).pack()

        #Button(root2,text="EDIT",command=edit).pack(side=LEFT)
        
        def delete():
            v=askyesno('Conform','Are you sure to delete?')
            if v==True:
                a=(c_id)
                cur.execute("delete from Contact_details where Id=?",a)
                cur.execute("delete from P_number_details where Id=?",a)
                cur.execute("delete from Email_details where Id=?",a)
                con.commit()
                root2.destroy()
                showinfo('Info','Contact Deleted')
                root1.destroy()
            else:
                pass
        Button(root2,text="DELETE",command=delete).pack()
        
    lb.bind("<<ListboxSelect>>",select)
    lb.grid(column=3,row=3)
    
    
    def s(key):
        global se
        se=search.get()+key.char
        global output1
        if key.char=='\x7f':                 #Backspace value is taken according to Macintosh OS for Windows Unicode for Backspace is \x08 
            se=se[:len(se)-2]
        a=('%'+se+'%','%'+se+'%')
        print a,type(a)
        cur.execute("select Id,Ph_Fname,Ph_Mname,Ph_Lname from Contact_details where Ph_Fname like ? or Ph_Lname like ?",a)
        output1=cur.fetchall()
        
        lb.delete(0,END)
        for i in output1:
            lb.insert(END,i[1]+' '+i[2]+' '+i[3])
        print output1
        
    search.bind('<Key>',s)


def Showall():
    e1.delete(0,END)
    e1.insert(0,' ')
    e2.delete(0,END)
    e2.insert(0,' ')
    e3.delete(0,END)
    e3.insert(0,' ')
    e4.delete(0,END)
    e4.insert(0,' ')
    e5.delete(0,END)
    e5.insert(0,' ')
    e6.delete(0,END)
    e6.insert(0,' ')
    e7.delete(0,END)
    e7.insert(0,' ')
    e8.delete(0,END)
    e8.insert(0,' ')
    e9.delete(0,END)
    e9.insert(0,' ')
    e10.delete(0,END)
    e10.insert(0,' ')
    e11.delete(0,END)
    e11.insert(0,' ')
    
    cur.execute("select * from Contact_details")
    con.commit()
    x=cur.fetchall()
    root1=Tk()
    root1.geometry("700x500")
    root1.title("Records")
    Label(root1,text="Id",font="Comic 10",relief="ridge").grid(row=0,column=0)
    Label(root1,text="First Name",font="Comic 10",relief="ridge").grid(row=0,column=1)
    Label(root1,text="Last Name",font="Comic 10",relief="ridge").grid(row=0,column=2)
    Label(root1,text="Company Name",font="Comic 10",relief="ridge").grid(row=0,column=3)
    Label(root1,text="Phone Number",font="Comic 10",relief="ridge").grid(row=0,column=4)
    Label(root1,text="Email ID",font="Comic 10",relief="ridge").grid(row=0,column=5)
    Label(root1,text="Address",font="Comic 10",relief="ridge").grid(row=0,column=6)
    Label(root1,text="Website",font="Comic 10",relief="ridge").grid(row=0,column=7)
    Label(root1,text="Date of Birth",font="Comic 10",relief="ridge").grid(row=0,column=8)
    
    k=1
    for i in x:
        Label(root1,text=i[0]).grid(row=k,column=0)
        Label(root1,text=i[1]).grid(row=k,column=1)
        Label(root1,text=i[2]).grid(row=k,column=2)
        Label(root1,text=i[3]).grid(row=k,column=3)
        Label(root1,text=i[4]).grid(row=k,column=4)
        Label(root1,text=i[5]).grid(row=k,column=5)
        Label(root1,text=i[6]).grid(row=k,column=6)
        Label(root1,text=i[7]).grid(row=k,column=7)
        Label(root1,text=i[8]).grid(row=k,column=8)
        k+=1   
    

    

#connection Establishment   
import sqlite3
con=sqlite3.Connection("Phonebook")
cur=con.cursor()
root=Tk()
root.title("Phonebook")
Label(root,text="Phonebook",font="Comic 46",relief="ridge").grid(row=0,column=0,columnspan=5)

#image insertion
path="image.gif"
img=PhotoImage(file=path)
Label(root,image=img).grid(row=1,column=2)

#GUI
Label(root,text="First Name:",font="times 16").grid(row=2,column=0)
e1=Entry(root)
e1.grid(row=2,column=2)

Label(root,text="Middle Name:",font="times 16").grid(row=3,column=0)
e2=Entry(root)
e2.grid(row=3,column=2)

Label(root,text="Last name:",font="times 16").grid(row=4,column=0)
e3=Entry(root)
e3.grid(row=4,column=2)

Label(root,text="Company:",font="times 16").grid(row=5,column=0)
e4=Entry(root)
e4.grid(row=5,column=2)

Label(root,text="Select Phone Type:  ",font="times10",fg='blue').grid(row=6,column=0,sticky='w')
v1=IntVar()
Radiobutton(root,text="Office",variable=v1,value=1).grid(column=1,row=6)
Radiobutton(root,text="Home",variable=v1,value=2).grid(column=2,row=6)
Radiobutton(root,text="Mobile",variable=v1,value=3).grid(column=3,row=6)

Label(root,text="Phone Number:",font="times 16").grid(row=7,column=0)
e5=Entry(root)
e5.grid(row=7,column=2)

Label(root,text="Select Email Type:  ",font="times10",fg='blue').grid(column=0,row=8,sticky='w')
v2=IntVar()
Radiobutton(root,text="Office",variable=v2,value=1).grid(column=1,row=8)
Radiobutton(root,text="Persional",variable=v2,value=2).grid(column=2,row=8)

Label(root,text="Email Id:",font="times 16").grid(row=9,column=0)
e6=Entry(root)
e6.grid(row=9,column=2)

Label(root,text="Address:",font="times 16").grid(row=10,column=0)
e7=Entry(root)
e7.grid(row=10,column=2)

Label(root,text="City:",font="times 16").grid(row=11,column=0)
e8=Entry(root)
e8.grid(row=11,column=2)

Label(root,text="Pin",font="times 16").grid(row=12,column=0)
e9=Entry(root)
e9.grid(row=12,column=2)

Label(root,text="Website:",font="times 16").grid(row=13,column=0)
e10=Entry(root)
e10.grid(row=13,column=2)

Label(root,text="Date of Birth:",font="times 16").grid(row=14,column=0)
e11=Entry(root)
e11.grid(row=14,column=2)

#Query
cur.execute('create table if not exists Contact_details( Id integer PRIMARY KEY AUTOINCREMENT,Ph_Fname varchar(20),Ph_Mname varchar(20),Ph_Lname varchar(20),Ph_Company varchar(20),Ph_Address varchar(20),Ph_City Varchar(15),Ph_Pin Varchar(10),Ph_Website Varchar(30),Ph_DOB varchar(20))')
cur.execute('create table if not exists P_number_details( Id integer,Ph_Pno varchar(10) ,Ph_Pno_type varchar(20) ,foreign key(Id) references Contact_details(Id) on delete cascade)')
cur.execute('create table if not exists Email_details( Id integer,Ph_EmailId Varchar(50) ,Ph_EID_type varchar(20) ,foreign key(Id) references Contact_details(Id) on delete cascade)')
cur.execute("PRAGMA foreign_keys=ON")
con.commit()

Button(root,text="Insert Contact",command=Insert,font="times 14").grid(row=18,column=0)
def close():
    root.destroy()

Button(root,text="Close",command=close,font="times 14").grid(column=4,row=18)
Button(root,text="Search",command=Search,font="times 14").grid(row=18,column=1)
Button(root,text="All Contact",command=Showall,font="times 14").grid(row=18,column=2)
root.geometry('600x600')
root.mainloop()

    
