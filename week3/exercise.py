#!/usr/bin/env python

# Week 3 Exercises: Functions

# EXERCISE 1:

# Implement FizzBuzz using function(s) with Clean Code standards

# -----FIZZBUZZ CODE HERE-----

def Fizz(number):
   '''
   Returns true if the number is divisible by 3
   '''
   return (False,True)[number % 3 == 0]

def Buzz(number):
   '''
   Returns true if the number is divisible by 5
   '''
   return (False,True)[number % 5 == 0]

def FizzBuzz(number):
  '''
  Brief: Checks for divisibility of the number by 3, 5 and 15.
  Details:
  1. Prints number itself if the number is not divisible by 3 and not divisible by 5.
  2. Prints "Fizz " if the number is divisible by 3.
  3. Prints "Buzz " if the number is divisible by 5.
  4. Prints "Fizz Buzz " if the number is divisible by 15.
  '''
   if not Fizz(number) and not Buzz(number):
       print(number, end=' ')
       return
   if Fizz(number):
       print("Fizz", end=' ')
   if Buzz(number):
       print("Buzz", end=' ')

if __name__ == "__main__":
   '''
   Main function. Uses function FizzBuzz() to check for divisibility of numbers 0 to 100 (both inclusive).
   '''
   for number in range(101):
       FizzBuzz(number)

# -----END FIZBUZZ CODE-----

# EXERCISE 2:

# Review the payroll.java code in Listing 3-4 in the book

# Re-implement it as clean Python code. See Listing 3-5 for guidance.

# -----PAYROLL CODE HERE-----


# -----END PAYROLL CODE-----
