#import test1
#import sys
#print(dir(sys))
#test1.sayhi()
#print('Version',test1._version_)

for i in range(1, 10):
    print
    for j in range(1, i+1):
        print "%d*%d=%d" % (i, j, i*j),

print "enter two integers,and i will tell you"