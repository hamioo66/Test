# -*-coding:UTF-8 -*-
#利用Tkinter创建一个用户登录界面
from Tkinter import*
root=Tk()
def reg():
    User = userName.get()
    Pwd = password.get()
    len_user=len(User)
    len_pwd=len(Pwd)
    if User=='15599155289' and Pwd=='123456':
        l_msg['text']=u'登录成功'
        userName.delete(0,len_user)
        password.delete(0,len_pwd)
    elif User=='' and Pwd=='':
        l_msg['text']='用户名或密码不能为空'
    else:
        l_msg['text']='用户名或密码错误'


root.title(u"用户登录")
root.geometry("300x200")
root.resizable(width=False,height=True)
Label(root,text=u"用户名",font=("Arial",12)).grid(row=0,sticky=W)
userName=Entry(root)
userName.grid(row=0,column=1,sticky=E)
Label(root,text=u"密码",font=("Arial",12)).grid(row=1,sticky=W)
password=Entry(root)
password.grid(row=1,column=1,sticky=E)
#password['show']='*'
login=Button(root,text=u"登录",command=reg)
login.grid(row=2,column=1,sticky=E)
l_msg=Label(root,text='')
l_msg.grid(row=3,column=1)
root.mainloop()
