'''
1. Number of Steps to Reduce a Number to Zero

Steps | Number | New Number
  1       43        42
  2       42        21
  3       21        20
  4       20        10
  5       10        5
  6       5         4
  7       4         2
  8       2         1
  9       1         0
'''

def reduce_to_zero(num):
    count = 0 # Create the number of steps counter
    while num > 0:
        if num % 2 == 0: # Checks if num can be divided by 2 
            num //= 2
            count += 1
        else: # Number cannot be divided by 2, so subtract 1 and continue loop
            num -= 1
            count += 1
    return count