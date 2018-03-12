#!/bin/python3

import sys

def getMoneySpent(keyboards, drives, s):    
    # Complete this function
    keyboards.sort(reverse=True)
    drives.sort()
    max = 0
    for keyboard in keyboards:
        for drive in drives:
            if(keyboard+drive > s):
                break
            if(keyboard+drive>=max):
                max = keyboard+drive
    return -1 if max==0 else max            

s,n,m = input().strip().split(' ')
s,n,m = [int(s),int(n),int(m)]
keyboards = list(map(int, input().strip().split(' ')))
drives = list(map(int, input().strip().split(' ')))
#  The maximum amount of money she can spend on a keyboard and USB drive, or -1 if she can't purchase both items
moneySpent = getMoneySpent(keyboards, drives, s)
print(moneySpent)