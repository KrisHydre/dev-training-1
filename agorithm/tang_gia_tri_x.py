#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Nov 18 11:08:12 2020

@author: krish
"""        
def tang_x(x,y):
    buoc = 0 # số bước để tăng giá trị của x
    if x > y:
        tang_x(y,x)
       # Đảo ngược giá trị của hàm nếu người dùng nhập lẫn giá trị x và y
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
    
