#-*- coding:utf-8 -*-
#!/usr/bin/python3
#!/usr/bin/env python3

from tkinter import *
root = Tk()
lbl = Label(root, text = "이름")
lbl.pack()

txt = Entry(root)
txt.pack()

btn = Button(root, text = "OK")
btn.pack()

root.mainloop()
