# Question 1: Using a for loop with a list

# TODO: Create a list of fruits
# TODO: Use a for loop to print each fruit in the list

fruits= ('Strawberry', 'Banana', 'Apple', 'Pear', 'Kiwi')
for x in fruits:
    print(x) 




#-------------------------------------------------------------------------
# Question 2: Using a while loop for countdown

# TODO: Use a while loop to create a countdown from 5 to 1


from operator import mul
import time                                                 # is a built-in Python module.  allows for a certain amount of time between two specific functions

countdown = 5                                               # the countdown function is code that allows for numbers to be counted backwards from the starting point(usually  the highest value ) until 0 
while countdown >0:                                         # before running code, the programme checks if this statement is true 
    print(f' countdown: {countdown} seconds remaining')
    time.sleep (1)                                          # wait for 1 second #time.sleep means that the code will stop the time for however much time you have input; in this case, the time will stop by 1 second 
    countdown -= 1                                          #reliably decrement by 1 each time   # this basically tells the code to wait 1 second only in between each number


#-------------------------------------------------------------------------
# Question 3: Using a for loop with range()

# TODO: Use a for loop to print the first 10 square numbers
for i in range(1, 11):
    sq= i * 2
    print(sq)  

    

#-------------------------------------------------------------------------

# Question 4: Using the random module

# TODO: Import the random module

# TODO: Create a list of colors
# TODO: Use a for loop to select and print 3 random colors from the list

import random
colours= ('Blue', 'Pink', 'Green', 'Black', 'Purple', 'Red', 'Yellow')




random_colours= random.sample (colours, k=3)

for colours in random_colours:
    print(colours)

    
#-------------------------------------------------------------------------
# Question 5: Creating and using a custom module

# TODO: Create a new file named 'math_operations.py' with the following content:
"""
def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def multiply(a, b):
    return a * b

def divide(a, b):
    if b != 0:
        return a / b
    else:
        return "Error: Division by zero"
"""

# TODO: Import the custom module and use its functions
import math_operations
print(math_operations.add(13, 7))



# TODO: Use a while loop to create a simple calculator

print("Please select operation -\n"
      "1. Add\n"
      "2. Subtract\n"
      "3. Multiply\n"
      "4. Divide\n")

sel = int(input("Select operation (1-4): "))

n1 = int(input("Enter first number: "))
n2 = int(input("Enter second number: "))

if sel == 1:                             # sel means selection; it's not a built in programme but rather a custom variable that is chosen by the programmer
    print(n1, "+", n2, "=", add(n1, n2)) # type: ignore
elif sel == 2:
    print(n1, "-", n2, "=",sub(n1, n2))  # type: ignore
elif sel == 3:
    print(n1, "*", n2, "=",mul(n1, n2))
elif sel == 4:
    print(n1, "/", n2, "=", div(n1, n2)) # type: ignore
else:
    print("Invalid input")
