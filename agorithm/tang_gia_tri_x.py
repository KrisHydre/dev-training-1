#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Nov 18 11:08:12 2020

@author: krish
"""
def tang_x_x(x,y):
    buoc = 0
    # Gia su x, va y la 2 so nguyen
    if x>y:
        tang_x(y,x)
    else:
        a = int (y/x)
        if a == 1:
            b = y-x
            for i in range (b):
                x +=1
                buoc +=1
            # print ('Gia tri moi cua x:', x)
            # print ('Gia tri cua y:', y)
            print ('So buoc de tang gia tri:', b)
        else:
            x *= a
            b = y - x
            for i in range (b):
                x +=1
                buoc +=1
            # print ('Gia tri moi cua x:', x)
            # print ('Gia tri cua y:', y)
            print ('So buoc de tang gia tri:', b)
            
def tang_x(x,y):
    buoc=0
    if x > y:
        tang_x(y,x)
    else:
        while y > x:
            x *= 2
            buoc += 1
        for i in range (x-y):
            x -= 1
            buoc += 1
        print ('Tăng giá trị của x bằng y sau ', buoc)
if __name__== '__main__':
    tang_x(x=int(input ('So be la\n>>')), y=int(input ('So lon la\n>>')))
    
