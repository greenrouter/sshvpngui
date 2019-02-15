from __future__ import print_function

from tkinter import *
import subprocess
import sys
import tkMessageBox


def sshconnect():
		global p
		global ssh
		global server
		global user
		global password

		server=E1.get()

		user=E2.get()
		password=E3.get()

		ssh = subprocess.Popen(["plink.exe", "-ssh",
					user+"@"+server,
					"-pw", password,
					"-D", "1080"
					"-N"],
						shell=False,
						stdout=subprocess.PIPE,
						stderr=subprocess.PIPE)
		
		p=subprocess.Popen(['Proxifier.exe'])
		B.config(state=DISABLED)
		B3.config(state=DISABLED)
		B2.config(state=ACTIVE)
		#result = ssh.stdout.readlines()

		#error = ssh.stderr.readlines()						

def exit():
	sys.exit()
def dis():

	B2.config(state=DISABLED)
	B.config(state=ACTIVE)
	B3.config(state=ACTIVE)
	p.kill()
	ssh.kill()

def donothing():
   tkMessageBox.showinfo("About", "Created by MSrouter")


top = Tk()
menubar = Menu(top)


top.title("SSHVPN GUI")
helpmenu = Menu(menubar, tearoff=0)
helpmenu.add_command(label="About...", command=donothing)
menubar.add_cascade(label="Help", menu=helpmenu)

L1 = Label(top, text = "Server")
L1.place(x = 10,y = 10)
E1 = Entry(top, bd = 5)
E1.place(x = 85,y = 10)
L2 = Label(top,text = "SshUser")
L2.place(x = 10,y = 50)
E2 = Entry(top,bd = 5)
E2.place(x = 85,y = 50)

L3 = Label(top,text = "SshPassword")
L3.place(x = 10,y = 100)
E3 = Entry(top,bd = 5)
E3.place(x = 85,y = 100)

B = Button(top, text = "Connect",command=sshconnect)
B.place(x = 150, y = 150)

B2 = Button(top, text = "Disconnect",command=dis)
B2.place(x = 80, y = 150)
B2.config(state=DISABLED)
B3 = Button(top, text = "Exit",command=exit)
B3.place(x = 50, y = 150)
top.geometry("250x250+10+10")
top.config(menu=menubar)

top.mainloop()
