from Tkinter import *
root=Tk()

root.geometry('920x850')
root.configure(bg='#131533')

Label(root,text="                    ",fg="#E2F026",bg='#131533').grid(row=0,column=0)
Label(root,text="Project Title : PhoneBook",font='Papyrus 50 bold',fg="#E2F026",bg='#131533').grid(row=1,column=1)
Label(root,text="Project of Python and Database",font='Papyrus 30 bold',fg="#E2F026",bg='#131533').grid(row=2,column=1)

Label(root,text="                    ",fg="#E2F026",bg='#131533').grid(row=3,column=0)
Label(root,text="                    ",fg="#E2F026",bg='#131533').grid(row=4,column=0)
Label(root,text="                    ",fg="#E2F026",bg='#131533').grid(row=5,column=0)
Label(root,text="                    ",fg="#E2F026",bg='#131533').grid(row=6,column=0)
Label(root,text="                    ",fg="#E2F026",bg='#131533').grid(row=7,column=0)
Label(root,text="                    ",fg="#E2F026",bg='#131533').grid(row=8,column=0)
Label(root,text="                    ",fg="#E2F026",bg='#131533').grid(row=9,column=0)
Label(root,text="                    ",fg="#E2F026",bg='#131533').grid(row=10,column=0)
Label(root,text="                    ",fg="#E2F026",bg='#131533').grid(row=11,column=0)
Label(root,text="                    ",fg="#E2F026",bg='#131533').grid(row=12,column=0)

Label(root,text="------------------------------------------",fg='#ff8000',font='Papyrus 20 bold',bg='#131533').grid(row=13,column=1)
Label(root,text="Developed By : MEDHA CHAUDHARY",fg='#ff8000',font='Papyrus 20 bold',bg='#131533').grid(row=14,column=1)
Label(root,text="Enrollment number : 181B123",fg='#ff8000',font='Papyrus 20 bold',bg='#131533').grid(row=15,column=1)
Label(root,text="------------------------------------------",fg='#ff8000',font='Papyrus 20 bold',bg='#131533').grid(row=16,column=1)


Label(root,text="                    ",fg="#E2F026",bg='#131533').grid(row=17,column=0)
Label(root,text="                    ",fg="#E2F026",bg='#131533').grid(row=18,column=0)
Label(root,text="                    ",fg="#E2F026",bg='#131533').grid(row=19,column=0)
Label(root,text="                    ",fg="#E2F026",bg='#131533').grid(row=20,column=0)
Label(root,text="                    ",fg="#E2F026",bg='#131533').grid(row=21,column=0)
Label(root,text="                    ",fg="#E2F026",bg='#131533').grid(row=22,column=0)
Label(root,text="                    ",fg="#E2F026",bg='#131533').grid(row=23,column=0)
Label(root,text="                    ",fg="#E2F026",bg='#131533').grid(row=24,column=0)

Label(root,text="Move the cursor over the screen",font='Papyrus 15 bold',fg='red',bg='#131533').grid(row=24,column=1)

def close(e=1):
    root.destroy()
root.bind('<Motion>',close)

root.mainloop()
