num = int(input("Enter no till you get prime no: "))


for n in range(2, num + 1):
    count = 0

    for i in range(2, n):
        if(n % i == 0):
            count = count + 1
        
    if (count == 0):
        print(n  , end=" ")