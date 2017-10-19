# -*- coding:UTF-8 -*-
#笨方法
movies=["The Holy Grai","Terry",["Eric Idle","Terry Jones",["hello","goods"]]]
for each_item in movies:
    if isinstance(each_item,list):
        for nestes_item in each_item:
            if isinstance(nestes_item,list):
                for deeper_item in nestes_item:
                    print deeper_item
            else:
                print nestes_item
    else:
        print each_item


#定义一个函数来获取序列数据
"""提供一个名为print_lol的函数用来打印列表，其中包含或不包含嵌套列表"""
def print_lol(the_list,indent=False,level=0):
    for i in the_list:
        if isinstance(i,list):
            print_lol(i,indent,level+1)
            #print("\t",end='')
        else:
            if indent:
                for tab_stop in range(level):
                    #print("\t",end='') #python3可用
                    print("\t")
            print i
print_lol(movies)