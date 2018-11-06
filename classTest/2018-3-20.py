# -*- coding=UTF-8 -*-
"""
author:hamioo
date:2018/1/2
describle:一个简单的猜字游戏
"""
import random
secretNumber = random.randint(1, 20)
#print(secretNumber)
print('I thinking of a number between 1 and 20.')
for guessesToken in range(1, 7):
   # print(guessesToken)
    print('Take a guess')
    guess = int(input())
    if guess < secretNumber:
        print('Your guess is too low.')
    elif guess > secretNumber:
        print('Your guess is too high')
    else:
        break
if guess == secretNumber:
    print('Good job!you guessed my number in '+str(guessesToken) + ' guesses!')
else:
    print('Nope,The number I was thinking of was '+ str(secretNumber))


catNames=[]
while True:
    print('enter the name of cat' +str(len(catNames)+1)+ ' or enter nothing to stop')
    name=raw_input()
    if name == '':
        break
    catNames = catNames +[name]
print catNames
print('the cat names are:')
for name in catNames:
    print(' '+name)
