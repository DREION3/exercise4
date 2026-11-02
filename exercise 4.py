# Question 1: Using a for loop with a list

# TODO: Create a list of fruits
# TODO: Use a for loop to print each fruit in the list

fruits= ('Strawberry', 'Banana', 'Apple', 'Pear', 'Kiwi')
for x in fruits:
    print(x) 




#-------------------------------------------------------------------------
# Question 2: Using a while loop for countdown

# TODO: Use a while loop to create a countdown from 5 to 1
from random import random
import time

countdown= 5
start_time= time.time()
elapsed_time= 0
while (remaining_time := countdown - elapsed_time) >0:
    print(f'Countdown: {int(remaining_time)} seconds remaining')
    time.sleep(1) #wait for 1 second 
    elapsed_time = time.time() - start_time


#-------------------------------------------------------------------------
# Question 3: Using a for loop with range()

# TODO: Use a for loop to print the first 10 square numbers
for i in range(1, 11):
    sq= i * i
    print(sq, end=" ")  

    

#-------------------------------------------------------------------------

# Question 4: Using the random module

# TODO: Import the random module

# TODO: Create a list of colors
# TODO: Use a for loop to select and print 3 random colors from the list

import random
class random_colours:
        ...

coulours= ('Blue', 'Pink', 'Green', 'Black', 'Purple', 'Red', 'Yellow')



for _ in range (3):
    random_colour= random.choice (coulours)
    print( random_colours)

    
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


# TODO: Use a while loop to create a simple calculator
