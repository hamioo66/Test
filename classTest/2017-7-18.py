#import Tkinter
#from Tkinter import *
#widget=Label(None,text='this is my first Gui')
#widget.pack(expand=YES,fill=BOTH)
#widget.mainloop()

#root=Tk()
#widget=Label(root)
#widget.config(text='My first GUI')
#widget.pack(side=TOP,expand=YES,fill=BOTH)
#root.mainloop()


import sys
from Tkinter import *
#widget=Button(None,text='Click Me',command=sys.exit)
#widget.pack()
#widget.mainloop()
def result():
    print ("The sum of 2+2 is",2+2)
win=Frame()
win.pack()
Label(win,text='Click Add to get the sum or Quit to Exit').pack(side=TOP)
Button(win,text='Add',command=result).pack(side=LEFT)
Button(win,text='Quit',command=win.quit).pack(side=RIGHT)
win.mainloop()

