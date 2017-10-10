# -*- coding:UTF-8 -*-
#Label组件
from Tkinter import *
class LabelDemo(Frame):
    def __init__(self):
        Frame.__init__(self)
        self.pack(expand=YES,fill=BOTH)
        self.master.title("Labels")
        self.label1=Label(self,text="Label with text")
        self.label1.pack()
        self.label2=Label(self,text="Labels with text and a bitmap")
        self.label2.pack(side=LEFT)
        self.label3=Label(self,bitmap="warning")
        self.label3.pack(side=LEFT)
def main():
    LabelDemo().mainloop()
if __name__=="__main__":
    main()

