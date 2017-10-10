from Time import Time
time1=Time()
print "Calling method printMilitary:",time1.printMilitary()
print "The attributes of time1 are:"
print "time1_hour:",time1._hour
print "time1.minute:",time1._minute
print "time1.second:",time1._second
time1.setHour(4)
time1.setMinute(3)
time1.setSecond(34)
print "Calling method printStandard fter alteration",time1.printStandard()
print "Calling method printStandard fter alteration",time1.printMilitary()