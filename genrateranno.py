# Program to generate random numbers in a given range
import random

start = int(input("Enter the start of the range: "))

end = int(input("Enter the end of the range: "))

print("Random number between", start, "and", end, "is:", random.randint(start, end))
