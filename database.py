from tkinter import *
from PIL import ImageTk, Image
import sqlite3

win = Tk()
win.title("Student Database")
win.iconbitmap("icons/dbms.ico")
win.geometry("415x710")
win.resizable(False, True)

# CREATE AND CONNECT
con = sqlite3.connect("STUDENT_DATABASE.db")
cur = con.cursor()

# CREATE THE TABLE IF IT DOES NOT EXIST
cur.execute("""CREATE TABLE IF NOT EXISTS STUDENT(
	ID integer PRIMARY KEY,
	FIRST_NAME text NOT NULL,
	SUR_NAME text,
	ROLL_NO text,
	DOB text,
	AGE integer,
	ADDRESS text,
	MOBILE integer
	)""")

id = StringVar()
fna = StringVar()
sna = StringVar()
roll = StringVar()
dobe = StringVar()
age1 = StringVar()
addr1 = StringVar()
ph1 = StringVar()

#=========================================FUNCTIONS======================================#

def clearAll():
	# CLEAR ALL DATA
	id.set("")
	fna.set("")
	sna.set("")
	roll.set("")
	dobe.set("")
	age1.set("")
	addr1.set("")
	ph1.set("")

def show():
	# CONNECT
	con = sqlite3.connect("STUDENT_DATABASE.db")
	cur = con.cursor()

	# EXECUTE
	cur.execute("SELECT * FROM STUDENT")
	records = cur.fetchall()
	printRec = ''
	for record in records:
		printRec += str(record[0]) + "\t" + str(record[1]) + " "+ str(record[2]) + "\n"
	lbl = Label(showFrame, text=printRec, padx=105, pady=2).grid(row=0, column=0)
	
	# COMMIT AND CLOSE
	con.commit()
	con.close()

def update():
	# CONNECT
	con = sqlite3.connect("STUDENT_DATABASE.db")
	cur = con.cursor()

	# EXECUTE
	id1 = int(id.get())
	fn = fna.get()
	sn = sna.get()
	rol = roll.get()
	do = dobe.get()
	ag = int(age1.get())
	ad = addr1.get()
	p = int(ph1.get())

	# UPDATE
	sqlInsert = "UPDATE STUDENT SET FIRST_NAME=?, SUR_NAME=?, ROLL_NO=?, DOB=?, AGE=?, ADDRESS=?, MOBILE=? WHERE ID=?;"
	data = ( fn, sn, rol, do, ag, ad, p, id1)
	cur.execute(sqlInsert, data)

	# CLEAR ALL DATA
	clearAll()

	updateBtn = Button(buttonFame, text="UPDATE RECORD", command=update, state=DISABLED)
	updateBtn.grid(row=4, column=0, ipadx=123, pady=5)

	# SHOW RECORDS
	show();

	# COMMIT AND CLOSE
	con.commit()
	con.close()

def edit():
	# CONNECT
	con = sqlite3.connect("STUDENT_DATABASE.db")
	cur = con.cursor()

	# EXECUTE
	cur.execute("SELECT * FROM STUDENT WHERE ID = " + str(id.get()))
	record = cur.fetchall()
	
	# LOOP THROUGH THE DATA
	for i in record:
		id.set(i[0])
		fna.set(i[1])
		sna.set(i[2])
		roll.set(i[3])
		dobe.set(i[4])
		age1.set(i[5])
		addr1.set(i[6])
		ph1.set(i[7])
	
	# ENABLE UPDATE BUTTON
	updateBtn = Button(buttonFame, text="UPDATE RECORD", bg="green", command=update, state=ACTIVE)
	updateBtn.grid(row=4, column=0, ipadx=123, pady=5)
	
	# COMMIT AND CLOSE
	con.commit()
	con.close()

def showTable():
	# CONNECT
	tab = Tk()
	tab.title("Student Table")
	tab.iconbitmap("icons/table.ico")
	tab.resizable(False, True)
	con = sqlite3.connect("STUDENT_DATABASE.db")
	cur = con.cursor()

	# EXECUTE
	cur.execute("SELECT * FROM STUDENT")
	records = cur.fetchall()
	
	Label(tab,text="ID", font=('arial', 10, 'bold')).grid(row=0, column=0, padx=(20,20))
	Label(tab,text="FIRST NAME", font=('arial', 10, 'bold')).grid(row=0, column=1, padx=(0, 20))
	Label(tab,text="SUR MAME", font=('arial', 10, 'bold')).grid(row=0, column=2,padx=(0, 20))
	Label(tab,text="ROLL NO", font=('arial', 10, 'bold')).grid(row=0, column=3,padx=(0, 20))
	Label(tab,text="DATE OF BIRTH", font=('arial', 10, 'bold')).grid(row=0, column=4,padx=(0, 20))
	Label(tab,text="AGE", font=('arial', 10, 'bold')).grid(row=0, column=5,padx=(0, 20))
	Label(tab,text="ADDRESS", font=('arial', 10, 'bold')).grid(row=0, column=6,padx=(0, 20))
	Label(tab,text="MOBILE", font=('arial', 10, 'bold')).grid(row=0, column=7,padx=(0, 20))
	i=1
	for record in records:
		Label(tab,text=str(record[0])).grid(row=i+1, column=0, padx=(20,20))
		Label(tab,text=str(record[1])).grid(row=i+1, column=1, padx=(0, 20))
		Label(tab,text=str(record[2])).grid(row=i+1, column=2, padx=(0, 20))
		Label(tab,text=str(record[3])).grid(row=i+1, column=3, padx=(0, 20))
		Label(tab,text=str(record[4])).grid(row=i+1, column=4, padx=(0, 20))
		Label(tab,text=str(record[5])).grid(row=i+1, column=5, padx=(0, 20))
		Label(tab,text=str(record[6])).grid(row=i+1, column=6, padx=(0, 20))
		Label(tab,text=str(record[7])).grid(row=i+1, column=7, padx=(0, 20))
		i+=1
	
	# COMMIT AND CLOSE
	con.commit()
	con.close()
	tab.mainloop()

def submit():
	# CONNECT
	con = sqlite3.connect("STUDENT_DATABASE.db")
	cur = con.cursor()

	# EXECUTE
	id1 = int(id.get())
	fn = fna.get()
	sn = sna.get()
	rol = roll.get()
	do = dobe.get()
	ag = int(age1.get())
	ad = addr1.get()
	p = int(ph1.get())
	sqlInsert = "INSERT INTO STUDENT (ID, FIRST_NAME, SUR_NAME, ROLL_NO, DOB, AGE, ADDRESS, MOBILE) VALUES (?, ?, ?, ?, ?, ?, ?, ?);"
	data = (id1, fn, sn, rol, do, ag, ad, p)
	cur.execute(sqlInsert, data)

	# CLEAR ALL DATA
	clearAll()

	# COMMIT AND CLOSE
	con.commit()
	con.close()

def delete():
	# CONNECT
	con = sqlite3.connect("STUDENT_DATABASE.db")
	cur = con.cursor()

	# EXECUTE
	cur.execute("DELETE FROM STUDENT WHERE ID=" + str(id.get()))

	# CLEAR ALL DATA
	clearAll()

	# COMMIT AND CLOSE
	con.commit()
	con.close()

	# SHOW RECORDS
	show();


#============================================FRAMES=======================================#
win.config(bg="green")

mainFrame = Frame(win)
mainFrame.config(bg='green')
mainFrame.grid()

titFrame = Frame(mainFrame, bd=2, padx=20, pady=20, bg="red", relief=RIDGE)
titFrame.pack(side=TOP)

dataFrame = Frame(mainFrame, bd=2, width=400, height=490, padx=30, pady=25, relief=RIDGE)
dataFrame.pack(pady=(15,10))

buttonFame = Frame(mainFrame, bd=2, width=400, height=50, bg="red", padx=26, pady=20, relief=RIDGE)
buttonFame.pack(pady=(5,0))

showFrame = Frame(mainFrame, bd=2, width=400, height=50, bg="ghost white", padx=15, pady=10, relief=RAISED)
showFrame.pack(pady=(20, 20))
# padx=26, pady=20,

#==========================================ENTRIES=========================================#

titLabel = Label(titFrame, text="STUDENT DATABASE MANAGEMENT SYSTEM", font=('cursive', 13, 'bold'), bg="red", fg="white")
titLabel.pack()

#LABELS
idLbl = Label(dataFrame,text="ID: ").grid(row=0, column=0)
fName = Label(dataFrame,text="FIRST NAME: ").grid(row=1, column=0)
sName = Label(dataFrame,text="SUR NAME: ").grid(row=2, column=0)
rollNo = Label(dataFrame,text="ROLL NO: ").grid(row=3, column=0)
dob = Label(dataFrame,text="DATE OF BIRTH: ").grid(row=4, column=0)
age = Label(dataFrame,text="AGE: ").grid(row=5, column=0)
address = Label(dataFrame,text="ADDRESS: ").grid(row=6, column=0)
ph = Label(dataFrame,text="MOBILE: ").grid(row=7, column=0)

#ENTRIES
idBox = Entry(dataFrame, width=40, bd=2, textvariable=id).grid(row=0, column=1)
sNameBox = Entry(dataFrame, width=40, bd=2, textvariable=fna).grid(row=1, column=1)
fNameBox = Entry(dataFrame, width=40, bd=2, textvariable=sna).grid(row=2, column=1)
rollNoBox = Entry(dataFrame, width=40, bd=2, textvariable=roll).grid(row=3, column=1)
dobBox = Entry(dataFrame, width=40, bd=2, textvariable=dobe).grid(row=4, column=1)
ageBox = Entry(dataFrame, width=40, bd=2, textvariable=age1).grid(row=5, column=1)
addressBox = Entry(dataFrame, width=40, bd=2, textvariable=addr1).grid(row=6, column=1)
phBox = Entry(dataFrame, width=40, bd=2, textvariable=ph1).grid(row=7, column=1)

#BUTTONS
submitBtn = Button(buttonFame, text="ADD RECORDS TO DATABASE", command=submit)
submitBtn.grid(row=0, column=0, ipadx=90, pady=5)

showBtn = Button(buttonFame, text="SHOW RECORDS", command=show)
showBtn.grid(row=1, column=0, ipadx=123)

deleteBtn = Button(buttonFame, text="DELETE RECORD", command=delete)
deleteBtn.grid(row=2, column=0, ipadx=125, pady=5)

editBtn = Button(buttonFame, text="ENTER ID TO EDIT RECORD", command=edit)
editBtn.grid(row=3, column=0, ipadx=98)

updateBtn = Button(buttonFame, text="UPDATE RECORD", bg="SpringGreen2", command=update, state=DISABLED)
updateBtn.grid(row=4, column=0, ipadx=123, pady=5)

clearBtn = Button(buttonFame, text="CLEAR ALL DATA", bg="yellow2", fg="black", command=clearAll)
clearBtn.grid(row=5, column=0, ipadx=123, pady=5)

tableBtn = Button(buttonFame, text="SHOW TABLE", bg="blue", fg="ghost white", command=showTable)
tableBtn.grid(row=6, column=0, ipadx=132, pady=5)

#==========================================MAIN===========================================#
# COMMIT AND CLOSE
con.commit()
con.close()

# START THE MAIN LOOP
win.mainloop()
