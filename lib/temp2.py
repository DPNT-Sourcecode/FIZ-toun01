# -*- coding: utf-8 -*-
"""
Created on Tue Aug 27 16:54:51 2019

@author: admin
"""

def fizz_buzz(number):
    
   if number%3 == 0 and number%5 == 0: 
          return 'fizz buzz'
   elif number%3 == 0:
          return 'fizz'
   elif number%5 == 0:
          return 'buzz'   
   else:
        return number
if __name__ == '__main__':
   print(fizz_buzz(16))