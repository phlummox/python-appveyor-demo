#!/usr/bin/env python3

# gui wrapper around the pandora export script by Matthew Davis (July 2017).
# Copyright for the export code and the pandora library 
# are held by their respective creators. This file is placed in the public
# domain to the extent possible.

import tkinter as tk       
from tkinter import Frame, Button, Listbox, Entry, Label, filedialog, \
                    StringVar
import sys
import os.path


class Application(Frame):              
    def __init__(self, master=None):
        Frame.__init__(self, master, width=800, height=500)
        self.createWidgets()

    def createWidgets(self):
        # top menu bar

        self.topBar = Frame(self.master)#,height=10) #,width=50)
        topBar = self.topBar
        topBar.config(bd=3, relief=tk.GROOVE)

        self.quitBtn = Button(topBar, text='Quit',
            command=self.quit)
        self.quitBtn.pack(side="right")

        topBar.pack(side=tk.TOP,fill=tk.X)

        self.mainFrame = Frame(self.master) #,height=60) #,width=50)
        mainFrame = self.mainFrame
        mainFrame.pack(side=tk.TOP,fill=tk.BOTH, expand=1)


 
def main():
  print("main...")
  
  app = Application()
  print("made app...")
  app.master.title('Pandora exporter')
  app.master.geometry('{}x{}'.format(500, 350))
  app.mainloop()   

MAIN="__main__" 
#MAIN=None

if __name__ == MAIN:
  main()

