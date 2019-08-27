
def fizz_buzz2(number):
    
   if (number%3 == 0 and number%5 == 0) or (str(number).__contains__('3') and str(number).__contains__('5')): 
          return 'fizz buzz'
   if (number%3 == 0 and str(number).__contains__('5')) or (number%5 == 0 and str(number).__contains__('3')): 
          return 'fizz buzz'
   elif number%3 == 0 or str(number).__contains__('3'):
          return 'fizz'
   elif number%5 == 0 or str(number).__contains__('5'):
          return 'buzz'   
   
   #if str(number).__contains__('3'):
  #       return 'fizz'
   #elif str(number).__contains__('3') and str(number).__contains__('5'):   
    #      return 'fizz buzz'
   else:
        return number
    
if __name__ == '__main__':
   print(fizz_buzz2(546))