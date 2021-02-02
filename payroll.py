from tkinter import* 
import random 
import time 

payroll = Tk() 
payroll.geometry("1350x650+0+0")
payroll.title("Payroll Management Systems")

text_Input = StringVar()

Tops = Frame(payroll, width=1350, height=50, bg="sky blue")
Tops.pack(side=TOP)

Left = Frame(payroll, width=700, height=650, bg="sky blue")
Left.pack(side=LEFT)

Right = Frame(payroll, width=600, height=650, bg="sky blue")
Right.pack(side=RIGHT)

lblInfo = Label(Tops, font=('arial', 50, 'bold'), text="Payroll Management Systems", fg="Steel Blue", bd=10, anchor='w' )
lblInfo.grid(row=0,column=0)


#############################################################

## Left Frame 
LeftInsideLeft = Frame(Left, width=700, height=200, bg="dark blue")
LeftInsideLeft.pack(side = TOP)

LeftInsideLeftLeft = Frame(Left, width=325, height=400, bg="red")
LeftInsideLeftLeft.pack(side = LEFT)

LeftInsideRight = Frame(Left, width=325, height=400, bg="black")
LeftInsideRight.pack(side = RIGHT)


#####################################################

## Right Frame 
RightInsideLeft = Frame(Right, width=600, height=200, bg="dark blue")
RightInsideLeft.pack(side = TOP)

RightInsideLeftLeft = Frame(Right, width=300, height=400, bg="red")
RightInsideLeftLeft.pack(side = LEFT)

RightInsideRight = Frame(Right, width=300, height=400, bg="black")
RightInsideRight.pack(side = RIGHT)

### Employee
lblEmployeeName = Label(LeftInsideLeft, font=('arial', 12, 'bold'), text="Employee Name", fg="black", bd=10, anchor='w')
lblEmployeeName.grid(row=0,column=0)
## Employee Text Box
txtEmployeeName = Entry(LeftInsideLeft, font=('arial', 16, 'bold'), bd=10, insertwidth=8, bg="powder blue", justify = 'right')
txtEmployeeName.grid(row=0, column = 1)
### Address 
lblAddress = Label(LeftInsideLeft, font=('arial', 12, 'bold'), text="Address ", fg="black", bd=10, anchor='w')
lblAddress.grid(row=1,column=0)
## Address Text Box 
txtAddress = Entry(LeftInsideLeft, font=('arial', 16, 'bold'), bd=10, insertwidth=8, bg="powder blue", justify = 'right')
txtAddress.grid(row=0, column = 1)




payroll.mainloop() 
