#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)

if number > 0:
    last_digit = number % 10
elif number < 0:
    last_digit = number % -10

if last_digit == 0:
    print("Last digit of {} is 0".format(number),
          "and is 0")
elif last_digit < 6:
    print("Last digit of {} is {}".format(number, last_digit),
          "and is and is less than 6")
else:
    print("Last digit of {} is {}".format(number, last_digit), 
          "and is greater than 5")
