# -*- coding:UTF-8 -*-
#事件处理模型
# 定义一个entry类，操纵4个entry文本字段，一旦用户在活动字段中按下回车键，程序就会显示字段中输入的文本
from Tkinter import *
from tkMessageBox import *
class EntryDemo(Frame):
    def __init__(self):
        Frame.__init__(self)
        self.pack(expand=YES,fill=BOTH)
        self.master.title("Testing Entry Components")
        self.master.geometry("325x100")
        self.frame1=Frame(self)
        self.frame1.pack(pady=5)
        self.text1=Entry(self.frame1,name="text1")
        self.text1.bind("<Return>",self.showContents)
        self.text1.pack(side=LEFT,padx=5 )
    def showContents(self,event):
        theName=event.widget.winfo_name()
        theContents=event.widget.get()
        showinfo("Message",theName+"："+theContents)
def main():
    EntryDemo().mainloop()
if __name__=="__main__":
    main()
