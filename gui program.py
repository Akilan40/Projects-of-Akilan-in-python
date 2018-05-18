import Tkinter
import tkMessageBox

top = Tkinter.Tk()
def hello():
   tkMessageBox.showinfo("Founder and teacher of", "Hackup terchnology")

B1 = Tkinter.Button(top, text = "Dhinesh", command = hello)
B1.pack()

def hello():
   tkMessageBox.showinfo("Student of", "Hackup technology\n\n\nEthical hacker,\nLinux user,\nNCC trained person")
B2 = Tkinter.Button(top, text = "sathish", command = hello)
B2.pack()  

def hello():
   tkMessageBox.showinfo("Student of", "Hackup technology,\n\n\nPython programmer,\nC programmer,\nBuild box game designer,\nFootball player")
B3 = Tkinter.Button(top, text = "Akilan", command = hello)
B3.pack()


top.mainloop()
