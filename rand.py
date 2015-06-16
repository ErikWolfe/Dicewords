""" 
This is an example of the Random Number Generation process
Which I am hoping to replicate in the Java code. 
"""

#==================================================================
from random import SystemRandom

count = raw_input("How many sets of numbers? ")
groups = []

#==================================================================
# Retrieves a Securely Random number.
def get_rand():
    n = SystemRandom().getrandbits(3)

    if (n == 0):
        return get_rand()
    elif (n > 1):
        n -= 1
    
    return n

#==================================================================
# Grabbing $count sets of numbers
def random_numbers(count):

    numbers = []

    # Check for integer values & intelligent count size.
    if (count.isdigit() and int(count) > 0):

        for i in range(0, int(count)):
            values = ""

            # Fill the list "numbers".
            for i in range(5):
                numbers.append(get_rand())

            # Concatenate the items in "numbers" into a single string.
            for number in numbers:
                values += str(number) 

            # Reset "numbers" and append "values" to the "groups" list.
            numbers = []
            groups.append(values)

    else:
        count = raw_input("Please enter a number: ")
        random_numbers(count)

#==================================================================
# Perform the "random_numbers" function $count number of times.
random_numbers(count) 

# Print out the groups of numbers.
print groups 

#==================================================================
# Destroy the "evidence".
groups = []
numbers = []
values = ""
count = -1
