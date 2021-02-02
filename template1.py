from tkinter import* 
import random 
import time 

payroll = Tk() 
payroll.geometry("1350x650+0+0")
payroll.title("Payroll Management Systems")
payroll.resizable(False, False)
text_Input = StringVar()

Tops = Frame(payroll, width=1350, height=50)
Tops.pack(side=TOP)

Left = Frame(payroll, width=700, height=650)
Left.pack(side=LEFT)

Right = Frame(payroll, width=600, height=650)
Right.pack(side=RIGHT)

lblInfo = Label(Tops, font=('arial', 50, 'bold'), text="Payroll Management Systems", fg="Steel Blue", bd=10, anchor='w' )
lblInfo.grid(row=0,column=0)


#------------------------------------------------------
## Left Frame 
#------------------------------------------------------

LeftInsideLeft = Frame(Left, width=700, height=100)
LeftInsideLeft.pack(side = TOP)

LeftInsideLeftLeft = Frame(Left, width=325, height=400)
LeftInsideLeftLeft.pack(side = LEFT)

LeftInsideRight = Frame(Left, width=325, height=400)
LeftInsideRight.pack(side = RIGHT)


#------------------------------------------------------
## Right Frame 
#------------------------------------------------------

RightInsideLeft = Frame(Right, width=600, height=200)
RightInsideLeft.pack(side = TOP)

RightInsideLeftLeft = Frame(Right, width=300, height=400)
RightInsideLeftLeft.pack(side = LEFT)

RightInsideRight = Frame(Right, width=300, height=400)
RightInsideRight.pack(side = RIGHT)


#------------------------------------------------------
# Left Side 
#------------------------------------------------------

### Employee
lblEmployeeName = Label(LeftInsideLeft, font=('arial', 12, 'bold'), text="Employee Name", fg="black", bd=10, anchor='w')
lblEmployeeName.grid(row=0,column=0)
txtEmployeeName = Entry(LeftInsideLeft, font=('arial', 12, 'bold'), bd=10, width=36, bg="powder blue", justify = 'right')
txtEmployeeName.grid(row=0, column = 1)
### Address 
lblAddress = Label(LeftInsideLeft, font=('arial', 12, 'bold'), text="Address ", fg="black", bd=10, anchor='w')
lblAddress.grid(row=1,column=0)
## Address Text Box 
txtAddress = Entry(LeftInsideLeft, font=('arial', 12, 'bold'), bd=10, width=36, bg="powder blue", justify = 'right')
txtAddress.grid(row=1, column = 1)

### Reference
lblReference = Label(LeftInsideLeft, font=('arial', 12, 'bold'), text="Reference", fg="black", bd=10, anchor='w')
lblReference.grid(row=2,column=0)
txtReference= Entry(LeftInsideLeft, font=('arial', 12, 'bold'), bd=10, width=36, bg="powder blue", justify = 'right')
txtReference.grid(row=2, column = 1)

### Address 
lblEmployerName= Label(LeftInsideLeft, font=('arial', 12, 'bold'), text="EmployerName ", fg="black", bd=10, anchor='w')
lblEmployerName.grid(row=3,column=0)
txtEmployerName = Entry(LeftInsideLeft, font=('arial', 12, 'bold'), bd=10, width=36, bg="powder blue", justify = 'right')
txtEmployerName.grid(row=3, column = 1)


#------------------------------------------------------
# LEFT LEFT 
#------------------------------------------------------

### City
lblCity = Label(LeftInsideLeftLeft, font=('arial', 12, 'bold'), text="City Weighting", fg="black", bd=10, anchor='w')
lblCity.grid(row=0,column=0)
txtCity= Entry(LeftInsideLeftLeft, font=('arial', 12, 'bold'), bd=10, width=18, bg="powder blue", justify = 'right')
txtCity.grid(row=0, column = 1)


### Salary 
lblSalary = Label(LeftInsideLeftLeft, font=('arial', 12, 'bold'), text="Salary", fg="black", bd=10, anchor='w')
lblSalary.grid(row=1,column=0)
txtSalary= Entry(LeftInsideLeftLeft, font=('arial', 12, 'bold'), bd=10, width=18, bg="powder blue", justify = 'right')
txtSalary.grid(row=1, column = 1)

### Over Time
lblOverTime = Label(LeftInsideLeftLeft, font=('arial', 12, 'bold'), text="Over Time", fg="black", bd=10, anchor='w')
lblOverTime.grid(row=2,column=0)
txtOverTime= Entry(LeftInsideLeftLeft, font=('arial', 12, 'bold'), bd=10, width=18, bg="powder blue", justify = 'right')
txtOverTime.grid(row=2, column = 1)


### Gross Pay
lblGrossPay = Label(LeftInsideLeftLeft, font=('arial', 12, 'bold'), text="Gross Pay", fg="black", bd=10, anchor='w')
lblGrossPay.grid(row=3,column=0)
txtGrossPay= Entry(LeftInsideLeftLeft, font=('arial', 12, 'bold'), bd=10, width=18, bg="powder blue", justify = 'right')
txtGrossPay.grid(row=3, column = 1)


#------------------------------------------------------
# Right Right 
#------------------------------------------------------

### Taxes 
lblTaxes = Label(LeftInsideRight, font=('arial', 12, 'bold'), text="Taxes", fg="black", bd=10, anchor='w')
lblTaxes.grid(row=0,column=0)
txtTaxes= Entry(LeftInsideRight, font=('arial', 12, 'bold'), bd=10, width=18, bg="powder blue", justify = 'right')
txtTaxes.grid(row=0, column = 1)

### Pension
lblPension = Label(LeftInsideRight, font=('arial', 12, 'bold'), text="Pensions", fg="black", bd=10, anchor='w')
lblPension.grid(row=1,column=0)
txtPension= Entry(LeftInsideRight, font=('arial', 12, 'bold'), bd=10, width=18, bg="powder blue", justify = 'right')
txtPension.grid(row=1, column = 1)

### Student Loans
lblStudentLoans = Label(LeftInsideRight, font=('arial', 12, 'bold'), text="Student Loans", fg="black", bd=10, anchor='w')
lblStudentLoans.grid(row=2,column=0)
txtStudentLoans= Entry(LeftInsideRight, font=('arial', 12, 'bold'), bd=10, width=18, bg="powder blue", justify = 'right')
txtStudentLoans.grid(row=2, column = 1)

### Payment
lblPayment = Label(LeftInsideRight, font=('arial', 12, 'bold'), text="Payment", fg="black", bd=10, anchor='w')
lblPayment.grid(row=3,column=0)
txtPayment= Entry(LeftInsideRight, font=('arial', 12, 'bold'), bd=10, width=18, bg="powder blue", justify = 'right')
txtPayment.grid(row=3, column = 1)

#------------------------------------------------------
# Right Side
#------------------------------------------------------

### Post Code
lblPostCode = Label(RightInsideLeft, font=('arial', 12, 'bold'), text="Post Code", fg="black", bd=10, anchor='w')
lblPostCode.grid(row=0,column=0)
txtPostCode = Entry(RightInsideLeft, font=('arial', 12, 'bold'), bd=10, width=36, bg="powder blue", justify = 'right')
txtPostCode.grid(row=0, column = 1)


### Gender
lblGender = Label(RightInsideLeft, font=('arial', 12, 'bold'), text="Gender ", fg="black", bd=10, anchor='w')
lblGender.grid(row=1,column=0)
txtGender = Entry(RightInsideLeft, font=('arial', 12, 'bold'), bd=10, width=36, bg="powder blue", justify = 'right')
txtGender.grid(row=1, column = 1)

#------------------------------------------------------

payroll.mainloop() 
