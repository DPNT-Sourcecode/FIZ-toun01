
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
     c = int(identical)
     
     print(c % 2)
       
     if (str(number).count(identical)==len(str(number))) and (c % 2 == 1):
       dlx = ' fake deluxe'
     elif (str(number).count(identical)==len(str(number))):
       dlx = ' deluxe'
     else:
       dlx = ''
     
     if (number%3 == 0 and number%5 == 0) or (str(number).__contains__('3') and str(number).__contains__('5')): 
          return 'fizz buzz'+dlx
     if (number%3 == 0 and str(number).__contains__('5')) or (number%5 == 0 and str(number).__contains__('3')): 
          return 'fizz buzz'+dlx
     elif number%3 == 0 or str(number).__contains__('3'):
          return 'fizz'+dlx
     elif number%5 == 0 or str(number).__contains__('5'):
          return 'buzz'+dlx   
     elif dlx==' deluxe':
          #dlx=='deluxe'
          return 'deluxe'
     else:
        return number  

   
if __name__ == '__main__':
   print(fizz_buzz2(1111))
