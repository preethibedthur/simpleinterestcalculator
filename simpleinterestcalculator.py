from tkinter import *
root=Tk()
root.title("Simple Interest Calculator")
root.geometry("500x300")
def Calculate():
    princi=int(principalentry.get())
    rat=int(rateentry.get())
    tim=int(timeentry.get())
    amount=(princi*rat*tim)/100
    Label(text=f"{amount}",font="arial 30 bold").place(x=200,y=220)
def Exit():
    root.destroy()
    
principal=Label(root,text="Principal:",font="arial 15")
rate=Label(root,text="Rate Of Interest:",font="arial 15")
time=Label(root,text="Time:",font="arial 15")
interest=Label(root,text="Interest:",font="arial 15")
principal.place(x=50,y=20)
rate.place(x=50,y=90)
time.place(x=50,y=160)
interest.place(x=50,y=220)
principalvalue=StringVar()
ratevalue=StringVar()
timevalue=StringVar()
principalentry=Entry(root,textvariable=principalvalue,font="arial 15",width=8)
rateentry=Entry(root,textvariable=ratevalue,font="arial 15",width=8)
timeentry=Entry(root,textvariable=timevalue,font="arial 15",width=8)
principalentry.place(x=200,y=20)
rateentry.place(x=200,y=90)
timeentry.place(x=200,y=160)
Button(root,text="Calculate",command=Calculate,font="arial,15").place(x=350,y=20)
Button(root,text="Exit",command=Exit,font="arial 15",width=8).place(x=350,y=90)

root.mainloop()
