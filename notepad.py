from tkinter import *
from tkinter import messagebox as msg
from tkinter.filedialog import askopenfilename,asksaveasfilename
import os
root=Tk()
root.geometry("493x353")
root.title("Untitled-Notepad")

# text area
text=Text(root,font='lucida 10')
text.pack(expand=TRUE,fill=BOTH)
file=None

def new():
    global file
    root.title("Untitled-Notepad")
    file= None
    text.delete(1.0,END)
def op():
    global file
    file=askopenfilename(defaultextension='.txt',
                         filetypes=[("All Files","*.*"),
                                    ("Text Documents","*.txt")])
    if file=="":
        file=None
    else:
        root.title(os.path.basename(file)+ "-Notepad")
        text.delete(1.0,END)
        f=open(file,'r')
        text.insert(1.0,f.read())
        f.close()

def save():
    global file
    if file==None:
        file = asksaveasfilename(initialfile='Untitled.txt',defaultextension='.txt',
                         filetypes=[("All Files","*.*"),
                                    ("Text Documents","*.txt")])
        if file=='':
            file=None
        else:
           f= open(file,'w')
           f.write(text.get(1.0,END))
           f.close()

           root.title(os.path.basename(file)+ "-Notepad")
    else:
        f= open(file,'w')
        f.write(text.get(1.0,END))
        f.close()


def ex():
    root.destroy()
def cut():
    text.event_generate(("<<Cut>>"))
def copy():
    text.event_generate(("<<Copy>>"))
def paste():
    text.event_generate(("<<Paste>>"))
def about():
    msg.showinfo("Notepad","Notepad Made By Khushi")

# file menu
menubar=Menu(root)
m1=Menu(menubar,tearoff=0)
m1.add_command(label='New',command=new)
m1.add_command(label='Open',command=op)
m1.add_command(label='Save',command=save)
m1.add_separator()
m1.add_command(label='Exit',command=ex)
root.config(menu=menubar)
menubar.add_cascade(label='File',menu=m1)

# edit menu
m2=Menu(menubar , tearoff=0)
m2.add_command(label='Cut',command=cut)
m2.add_command(label='Copy',command=copy)
m2.add_command(label='Paste',command=paste)
root.config(menu=menubar)
menubar.add_cascade(label='Edit',menu=m2)

# help menu
m3=Menu(menubar,tearoff=0)
m3.add_command(label="About Notepad",command=about)
root.config(menu=menubar)
menubar.add_cascade(label='Help',menu=m3)

# scrollbar
scroll=Scrollbar(text)
scroll.pack(side='right',fill=Y)
scroll.config(command=text.yview)
text.config(yscrollcommand=scroll.set)

root.mainloop()
