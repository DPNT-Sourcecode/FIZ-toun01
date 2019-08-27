# noinspection PyUnusedLocal
def fizz_buzz(number):
if (number <=10):   
   if (number%3 == 0 and number%5 == 0) or (str(number).__contains__('3') and str(number).__contains__('5')): 
          return 'fizz buzz'
   if (number%3 == 0 and str(number).__contains__('5')) or (number%5 == 0 and str(number).__contains__('3')): 
          return 'fizz buzz'
   elif number%3 == 0 or str(number).__contains__('3'):
          return 'fizz'
   elif number%5 == 0 or str(number).__contains__('5'):
          return 'buzz'   
   else:
        return number
 elif (number > 10):
   
 identical = str(number)[0]
   if (str(number).count(identical)==len(str(number))):
        dlx = 'deluxe'  
        
        if (number%3 == 0 and number%5 == 0) or (str(number).__contains__('3') and str(number).__contains__('5')): 
           return 'fizz buzz'+' '+dlx
        if (number%3 == 0 and str(number).__contains__('5')) or (number%5 == 0 and str(number).__contains__('3')): 
           return 'fizz buzz'+' '+dlx
        elif number%3 == 0 or str(number).__contains__('3'):
           return 'fizz'+' '+dlx
        elif number%5 == 0 or str(number).__contains__('5'):
           return 'buzz'+' '+dlx   
        else:
           return dlx
    else:
       return number  