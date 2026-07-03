num = int(input("Enter limit till you get the sum : "))

sum = 0
for i in range(1, num + 1):
    sum = sum + i
    
print("The sum of natural numbers from 1 to", num , "is : ", sum)