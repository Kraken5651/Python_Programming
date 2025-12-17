a = int(input("Enter a number: "))
b = int(input("Enter second number: "))
# a = int("Enter a number: ")

# print(f"The division a/b is {a/b}")

if(b==0):
    raise ZeroDivisionError("Hey zero cannot be used to Divide.")
else:
    print(f"The division a/b is {a/b}")