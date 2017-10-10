import random
def rollDice():
    die1=random.randrange(1,7)
    die2=random.randrange(1,7)
    workSum=die1+die2
    print "Player rolled %d + %d = %d" %(die1,die2,workSum)
    return workSum
sum=rollDice()
if sum==7 or sum==11:
    gameStatus="WON"
elif sum==2 or sum==3 or sum==12:
    gameStatus="Lost"
else:
    gameStatus="CONTINUE"
    myPoint=sum
    print "point is",myPoint
while gameStatus=="CONTINUE":
    sum=rollDice()
    if sum==myPoint:
        gameStatus="WON"
    elif sum==7:
        gameStatus="LOST"
if gameStatus=="WON":
    print "Player wins"
else:
    print "Player loses"


import time
def printHeaer(title):
    print """ Content-type:text/html\
    <?xml version="1.0" encoding="utf-8"?>
    < !DOCTYPE HTML PUBLIC
    "-//W3C//DTD HTML 4.01 Transitional//EN"
    "http://www.w3.org/TR/html4/loose.dtd" >
    < html xmls="http://www.w3.org/1999/xhtml">
    <head><title>%s</title></head>
    <body>""" %title
printHeaer("Current date and time")
print time.ctime(time.time())
print "</body></html>"