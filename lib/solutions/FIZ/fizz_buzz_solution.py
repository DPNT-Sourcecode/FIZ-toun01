# noinspection PyUnusedLocal
def fizz_buzz(number):
    if (number%3 == 0 and number%5 == 0) or (str(number).__contains__('3') and str(number).__contains__('5')): 
          return 'fizz buzz'
    elif number%3 == 0 or str(number).__contains__('3'):
          return 'fizz'
    elif number%5 == 0 or str(number).__contains__('5'):
          return 'buzz'  

