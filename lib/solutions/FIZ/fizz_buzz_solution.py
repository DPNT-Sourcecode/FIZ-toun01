# noinspection PyUnusedLocal
def fizz_buzz(number):

     if ((number%3 == 0 and str(number).__contains__('3')) or (number%5 == 0 and str(number).__contains__('5'))) and (number % 2 == 1):
       dlx = ' fake deluxe'
     elif ((number%3 == 0 and str(number).__contains__('3')) or (number%5 == 0 and str(number).__contains__('5'))):
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
          return 'deluxe'
     elif dlx==' fake deluxe':
          return 'fake deluxe' 
     else:
        return number  

