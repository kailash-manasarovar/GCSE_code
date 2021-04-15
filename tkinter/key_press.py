from tkinter import *
import tkinter as tk

def hello(e=None):
    print('Hello')



tk.Button(root, text='say hello', command=hello).pack()

root.bind('<Escape>', lambda e: root.quit())
root.bind('h', hello)
root.mainloop()