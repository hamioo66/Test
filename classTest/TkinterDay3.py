# -*- coding:UTF-8 -*-
#Button组件

from Tkinter import *
from tkMessageBox import *
import image
class PlainAndFancy(Frame):
    def __init__(self):
        Frame.__init__(self)
        self.pack(expand=YES)
        self.master.title("Buttons")
        #创建带有文字按钮
        self.plainButton=Button(self,text="Plain Button",command=self.pressedPlain)
        self.plainButton.bind("<Enter>",self.rolloverEnter)
        self.plainButton.bind("<Leave>",self.rolloverLeave)
        self.plainButton.pack(side=LEFT,padx=5,pady=5)
        #创建带有图片按钮
        myimages=image.open("../images/img.jpg")
        self.myimage=PhotoImage(file=myimages)
        self.fancyButton=Button(self,image=self.myimage,command=self.pressedFancy)
        self.fancyButton.bind("<Enter>",self.rolloverEnter)
        self.fancyButton.bind("Leave",self.rolloverLeave)
        self.fancyButton.pack(side=LEFT,padx=5,pady=5)
    def pressedPlain(self):
        showinfo("Message","you pressed:plain button")
    def pressedFancy(self):
        showinfo("Message","You pressed:Fancy button")
    def rolloverEnter(self,event):
        event.widget.config(relief=GROOVE)
    def rolloverLeave(self,event):
        event.widget.config(relief=RAISED)
def main():
    PlainAndFancy().mainloop()
if __name__ == '__main__':
    main()