#import tkinter 
from tkinter import *
#create database and table
import mysql.connector
#import xlrd to read xcel files
import xlrd

root = Tk()
root.title("EXCEL to Mysql")
root.geometry("1000x1000+0+0")
root.configure(bg="black")
#INSTRUCTIONS :
lel = Label(root,text="INSTRUCTIONS : ",font=("arial",20)).pack()
lel = Label(root,text="1 . RENAME ALL FILES TO NUMBERS IN ASCENDING ORDER AND PLACE IN A FOLDER: ",font=("arial",15)).pack()
lel = Label(root,text="eg: if there are 3 files then 1.xlxs,2.xlxs,3.xlxs should be their names",font=("arial",20)).pack()
lel = Label(root,text="CHOOSE DEFAULT OR CUSTOM NOT BOTH",font=("arial",10)).pack()


#declare all variables 
hst = StringVar()
usr = StringVar()
passd = StringVar()
tbname = StringVar()
dbname = StringVar()
aloc = StringVar()
n = IntVar()
lel = Label(root,text="ENTER YOUR SERVER DETAILS  : ",font=("arial",15,"bold")).pack()
lel = Label(root,text="host : ",font=("arial",15,"bold")).pack()
eb1 = Entry(root,textvariable=hst,width=25).pack()
lel = Label(root,text="user : ",font=("arial",15,"bold")).pack()
eb2 = Entry(root,textvariable=usr,width=25).pack()
lel = Label(root,text="password  : ",font=("arial",15,"bold")).pack()
eb3 = Entry(root,textvariable=passd,width=25).pack()


#custom settings 
lel = Label(root,text="INSERT DATA  : ",font=("arial",30,"bold")).pack()
n = IntVar()
lel = Label(root,text="enter your DB NAME ",font=("arial",15,"bold")).pack()
eb4 = Entry(root,textvariable=dbname,width=25).pack()
lel = Label(root,text="enter your TABLE NAME ",font=("arial",15,"bold")).pack()
eb5 = Entry(root,textvariable=tbname,width=25).pack()

def default_insert():
	mydb = mysql.connector.connect(
	 host=hst.get(),
	 user=usr.get(),
	 passwd=passd.get())
	cursor = mydb.cursor()
	cursor.execute("create "+"database "+dbname.get())
	cursor.execute("use "+dbname.get())
	cursor.execute("create table "+tbname.get()+" (name varchar(30),job varchar(30),mobile varchar(30))")
	lel = Label(root,text="CREATED SUCCESFULLY",font=("arial",15,"bold")).pack()
btnd = Button(root,text="CLICK TO CREATE DATABASE AND TABLE",width=30,height=1,bg="Lightblue",command =default_insert).pack()

#read number of xcel files 
lel = Label(root,text="enter your Number of EXCEL SHEETS ",font=("arial",15,"bold")).pack()
eb6 = Entry(root,textvariable=n,width=25).pack()

jobs = ["housemaids","babysitters","cooks","nannies","patientcare","helpers"] 
names = ["mumbai"," new delhi","kolkata","bengaluru","hyderabad"," chennai"," ahmedabad","vishakapatnam","pune","surat","jaipur","lucknow","kanpur","nagpur","indore","jamshedpur","patna","durgapur","dhanbad","Vadodara"]
def lcs(X, Y, m, n): 
      
    LCSuff = [[0 for k in range(n+1)] for l in range(m+1)] 
    result = 0 
    for i in range(m + 1): 
        for j in range(n + 1): 
            if (i == 0 or j == 0): 
                LCSuff[i][j] = 0
            elif (X[i-1] == Y[j-1]): 
                LCSuff[i][j] = LCSuff[i-1][j-1] + 1
                result = max(result, LCSuff[i][j]) 
            else: 
                LCSuff[i][j] = 0
    return result 

def potential(name,ip):
	print(name,ip)
	l = 0
	pt = 0
	if(len(ip)<len(name)):
		l = len(ip)
		l1 = len(name)
		for c in range(0,l):
			if(ord(ip[c]) == ord(name[c])):
				pt = pt + 1
		pt = pt + lcs(name,ip,l1,l) * 0.5
	else:
		l = len(name)
		li = len(ip)
		for c in range(0,l):
			if(ord(ip[c]) == ord(name[c])):
				pt = pt + 1
		pt = pt + lcs(name,ip,l,li) * 0.5
	return pt

def selfcorrectn(ip):
	min = -9999999999999
	final = ""
	ipl = len(ip)
	for name in names:
		y = potential(name,ip)
		if(min < y):
			min = y
			final = name
			print(min)
	return final

def selfcorrectj(ip):
	min = -9999999999999
	final = ""
	ipl = len(ip)
	for job in jobs:
		y = potential(job,ip)
		if(min < y):
			min = y
			final = job
	return final

def custom_insert():
	mydb = mysql.connector.connect(
	 host=hst.get(),
	 user=usr.get(),
	 passwd=passd.get())
	cursor = mydb.cursor()
	lel = Label(root,text="CONNECTED SUCCESFULLY",font=("arial",15,"bold")).pack()
	#INSERT DATA FROM EXCEL FILES 
	cursor = mydb.cursor()
	#using database xlproject(any name)
	sr = "use " + str(dbname.get())
	cursor.execute(sr)
	#create arrays of data from xl sheets
	name=[]
	job=[]
	mobile=[]
	for k in range(1,n.get()+1):
		loc = (str(k)) 
		wb = xlrd.open_workbook(loc) 
		sheet = wb.sheet_by_index(0) 
		for i in range(0,3):
			for j in range(1,sheet.nrows):
				if(sheet.cell_value(0,i)=='name'):
					x = selfcorrectn(sheet.cell_value(j,i))
					name.append(x)
				if(sheet.cell_value(0,i)=='job'):
					x = selfcorrectj(sheet.cell_value(j,i))
					job.append(x)
				if(sheet.cell_value(0,i)=='mobile'):
					mobile.append(sheet.cell_value(j,i))

	#insert touples into emp(rename) table database
	sql = 'insert into '+tbname.get() +' (name,job,mobile) values(%s,%s,%s)'
	for i in range(0,len(name)):
		tup = (name[i],job[i],str(mobile[i]))
		cursor.execute(sql,tup)
		mydb.commit()

	lel = Label(root,text="Dumped ,check your database",font=("arial",15,"bold")).pack()

btn = Button(root,text="CLICK TO INSERT into table",width=30,height=1,bg="Lightblue",command =custom_insert).pack()

#loop this file 
root.mainloop()