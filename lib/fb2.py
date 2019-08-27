
def fizz_buzz2(number):
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
     print(identical)
     print(str(number).count(identical))
     print(len(str(number)))
     
     if (str(number).count(identical)==len(str(number))):
       dlx = 'deluxe'  
     
       if (number%3 == 0 and number%5 == 0) or (str(number).__contains__('3') and str(number).__contains__('5')): 
          return 'fizz buzz'+' '+dlx
       if (number%3 == 0 and str(number).__contains__('5')) or (number%5 == 0 and str(number).__contains__('3')): 
          return 'fizz buzz'+' '+dlx
       elif number%3 == 0 or str(number).__contains__('3'):
          return 'fizz'+' '+dlx
       elif number%5 == 0 or str(number).__contains__('5'):
          return 'buzz'+dlx   
       else:
          return dlx
     else:
        return number  

   
if __name__ == '__main__':
   print(fizz_buzz2(55))