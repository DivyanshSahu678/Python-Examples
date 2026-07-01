a = int(input("Enter a number: "))
b = int(input("Enter another number: "))

print("Before swapping: a =", a, "and b =", b)

# Swapping the values using a temporary variable
temp = a
a = b
b = temp

print("After swapping: a =", a, "and b =", b)