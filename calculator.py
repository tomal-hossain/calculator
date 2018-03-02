import sys
from tkinter import *
import math

calc = Tk()
calc.title("Calculator")
calc.geometry('335x530')
calc.configure(background='DeepSkyBlue3')
calc.resizable(0,0)

value = StringVar()
exprsn = ""
ans = ""
eqpress = 0
show = ""
mem = ""

display = Entry(calc, textvariable=value, relief=RIDGE, bd=10, width=32,justify='right' ,insertwidth=1, font=50,bg='deep sky blue',fg='Blue')
display.pack(ipady=30)
display.place(x=13,y=10)

def BtnPress(num):
	global ans
	global eqpress
	global exprsn
	global show
	if eqpress > 0:
		if num =="+" or num =="-" or num=="*" or num=="/":
			exprsn = ans + str(num)
			value.set(exprsn)
			eqpress = 0
		else:
			exprsn = exprsn + str(num)
			show = show + str(num)
			value.set(show)
			eqpress = 0
	else:
		exprsn = exprsn + str(num)
		value.set(exprsn)

def EqualPress():
	global eqpress
	global exprsn
	global ans
	global show
	i=0
	for val in exprsn:
		if val == '^':
			exprsn = exprsn[:i]+'*'+'*'+exprsn[i+1:]
		i += 1

	try:
		if exprsn=="":
			value.set("")
		else:
			result = str(eval(exprsn))
			ans = result
			value.set(result)
			exprsn = ""
			show = ""
	except:
		value.set("Not valid")
		exprsn = ""
		show = ""

def AnsPress():
	global ans
	global exprsn
	if exprsn=="":
		exprsn = str(ans) + exprsn
	else:
		exprsn = exprsn + str(ans)
	value.set(exprsn)

def ClearOne():
	try:
		global exprsn
		l = len(exprsn)
		exprsn = exprsn[:l-1]
		value.set(exprsn)
	except:
		value.set("")

def ClearAll():
	global exprsn
	global show
	show = ""
	exprsn = ""
	value.set(exprsn)

def TrigonoMetry(operation):
	global exprsn
	global ans
	if exprsn == "":
		value.set("")
	else:
		try:
			exprsn = float(exprsn)
			if operation == "sin":
				ans = math.sin(math.radians(exprsn))
			elif operation == "cos":
				ans = math.cos(math.radians(exprsn))
			elif operation == "tan":
				ans = math.tan(math.radians(exprsn))
			elif operation == "sinInv":
				ans = math.degrees(math.asin(exprsn))
			elif operation == "cosInv":
				ans = math.degrees(math.acos(exprsn))
			elif operation == "tanInv":
				ans = math.degrees(math.atan(exprsn))
			elif operation == "log":
				ans = math.log10(exprsn)
			elif operation == "ePower":
				ans = math.exp(exprsn)
			value.set(str(ans))
			exprsn = ""
		except:
			value.set("Error Expression...")
			exprsn = ""

def Factorial():
	global exprsn
	global ans
	if exprsn == "":
		value.set("")
	else:
		try:
			num = int(exprsn)
			ans = math.factorial(num)
			ans = str(ans)
			value.set(ans)
			exprsn = ""
		except:
			exprsn=""
			value.set("Not valid")


def Square():
	global exprsn
	global ans
	if exprsn == "":
			value.set("")
	else:
		flag = 1
		for s in exprsn:
			if s=="+" or s=="-" or s=="*" or s=="/":
				flag = 0
				break
		if flag == 1:
			try:
				number = float(exprsn)
				sqr = str(number*number)
				ans = sqr
				value.set(sqr)
				exprsn = ""
			except:
				value.set("Not valid...")
				exprsn = ""
		else:
			sqr = "Error Expression..."
			value.set(sqr)
			exprsn = ""

def Root():
	global exprsn
	global ans
	if exprsn == "":
			value.set("")
	else:
		try:
			number = float(exprsn)
			root = str(number**(0.5))
			ans = root
			value.set(root)
			exprsn = ""
		except:
			value.set("Not valid...")
			exprsn = ""

sin = Button(calc, text='Sin',font=50, width=7, height=2, bg='slate gray', fg='Blue',command = lambda:TrigonoMetry("sin")).place(x=10,y=135)
cos = Button(calc, text='Cos',font=50, width=7, height=2, bg='slate gray', fg='Blue',command = lambda:TrigonoMetry("cos")).place(x=90,y=135)
tan = Button(calc, text='Tan',font=50, width=7, height=2, bg='slate gray', fg='Blue',command = lambda:TrigonoMetry("tan")).place(x=170,y=135)
log = Button(calc, text='Log',font=50, width=7, height=2, bg='slate gray', fg='Blue',command = lambda:TrigonoMetry("log")).place(x=250,y=135)
sinIn = Button(calc, text='Sin^-1',font=50, width=7, height=2, bg='slate gray', fg='Blue',command = lambda:TrigonoMetry("sinInv")).place(x=10,y=190)
cosIn = Button(calc, text='Cos^-1',font=50, width=7, height=2, bg='slate gray', fg='Blue',command = lambda:TrigonoMetry("cosInv")).place(x=90,y=190)
tanIn = Button(calc, text='Tan^-1',font=50, width=7, height=2, bg='slate gray', fg='Blue',command = lambda:TrigonoMetry("tanInv")).place(x=170,y=190)
eBase = Button(calc, text='e^',font=50, width=7, height=2, bg='slate gray', fg='Blue',command = lambda:TrigonoMetry("ePower")).place(x=250,y=190)
zero = Button(calc, text='0',font=50, width=7, height=2, bg='slate gray', fg='Blue',command = lambda:BtnPress(0)).place(x=10,y=465)
point = Button(calc, text='.',font=50, width=7, height=2, bg='slate gray', fg='Blue',command = lambda:BtnPress(".")).place(x=90,y=465)
ans = Button(calc, text='Ans',font=50, width=7, height=2, bg='slate gray', fg='Blue',command = lambda:AnsPress()).place(x=170,y=465)
equal = Button(calc, text='=',font=50, width=7, height=5, bg='slate gray', fg='Blue',command = lambda:EqualPress()).place(x=250,y=410)
one = Button(calc, text='1',font=50, width=7, height=2, bg='slate gray', fg='Blue',command = lambda:BtnPress(1)).place(x=10,y=410)
two = Button(calc, text='2',font=50, width=7, height=2, bg='slate gray', fg='Blue',command = lambda:BtnPress(2)).place(x=90,y=410)
three = Button(calc, text='3',font=50, width=7, height=2, bg='slate gray', fg='Blue',command = lambda:BtnPress(3)).place(x=170,y=410)
divide = Button(calc, text='/',font=50, width=7, height=2, bg='slate gray', fg='Blue',command = lambda:BtnPress("/")).place(x=250,y=355)
four = Button(calc, text='4',font=50, width=7, height=2, bg='slate gray', fg='Blue',command = lambda:BtnPress(4)).place(x=10,y=355)
five = Button(calc, text='5',font=50, width=7, height=2, bg='slate gray', fg='Blue',command = lambda:BtnPress(5)).place(x=90,y=355)
six = Button(calc, text='6',font=50, width=7, height=2, bg='slate gray', fg='Blue',command = lambda:BtnPress(6)).place(x=170,y=355)
multi = Button(calc, text='x',font=50, width=7, height=2, bg='slate gray', fg='Blue',command = lambda:BtnPress("*")).place(x=250,y=300)
seven = Button(calc, text='7',font=50, width=7, height=2, bg='slate gray', fg='Blue',command = lambda:BtnPress(7)).place(x=10,y=300)
eight = Button(calc, text='8',font=50, width=7, height=2, bg='slate gray', fg='Blue',command = lambda:BtnPress(8)).place(x=90,y=300)
nine = Button(calc, text='9',font=50, width=7, height=2, bg='slate gray', fg='Blue',command = lambda:BtnPress(9)).place(x=170,y=300)
minus = Button(calc, text='-',font=50, width=7, height=2, bg='slate gray', fg='Blue',command = lambda:BtnPress("-")).place(x=250,y=245)
sqr = Button(calc, text='sqr',font=50, width=7, height=2, bg='slate gray', fg='Blue',command = lambda:Square()).place(x=10,y=245)
root = Button(calc, text='root',font=50, width=7, height=2, bg='slate gray', fg='Blue',command = lambda:Root()).place(x=90,y=245)
plus = Button(calc, text='+',font=50, width=7, height=2, bg='slate gray', fg='Blue',command = lambda:BtnPress("+")).place(x=170,y=245)
Clear = Button(calc, text='Clear',font=50, width=7, height=2, bg='slate gray', fg='Blue',command = lambda:ClearAll()).place(x=10,y=80)
cancel = Button(calc, text='C',font=50, width=7, height=2, bg='slate gray', fg='Blue',command = lambda:ClearOne()).place(x=250,y=80)
fact = Button(calc, text='!',font=100, width=7, height=2, bg='slate gray', fg='Blue',command = lambda:Factorial()).place(x=90,y=80)
power = Button(calc, text='^',font=50, width=7, height=2, bg='slate gray', fg='Blue',command = lambda:BtnPress("^")).place(x=170,y=80)

calc.mainloop()