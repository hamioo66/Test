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

def print_lol(the_list):
    for i in the_list:
        if isinstance(i,list):
            print_lol(i)
        else:
            print i
print_lol(movies)