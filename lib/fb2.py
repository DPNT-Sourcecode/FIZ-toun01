
def fizz_buzz2(number):
    
   #if number%3 == 0 and number%5 == 0: 
   #       return 'fizz buzz'
   #elif number%3 == 0:
   #       return 'fizz'
   #elif number%5 == 0:
   #       return 'buzz'   
   
   if str(number).__contains__('3'):
          return 'fizz'
   elif str(number).__contains__('5'):   
          return 'buzz'
   #else:
   #     return number
    
if __name__ == '__main__':
   print(fizz_buzz2(13))