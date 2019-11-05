#coding: utf-8

import math

def sum(a, b):
    return a+b

def sum2(a,b):
    total = 0
    for i in range(a,b+1):
        total += i
    return total

def mysin(d):
    ad = math.pi*d/180
    return math.sin(ad)

if __name__ == '__main__':
    print(sum(1,2))
    print(sum2(1,10))
    print(mysin(30))