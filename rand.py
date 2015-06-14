""" This is an example of the Random Number Generation process
    Which I am hoping to replicate in the Java code. """

from random import SystemRandom

values = ""
numbers = []

# Retrieve a Securely Random number.
def get_rand():
    n = SystemRandom().getrandbits(3)

    if (n == 0):
        return get_rand()
    elif (n > 1):
        n -= 1
    
    return n


# Fill the list "numbers".
for i in range(5):
    numbers.append(get_rand())


# Concatenate the items in "numbers" into a single string.
for number in numbers:
    values += str(number) 


# Print the values to the console.
print values 
