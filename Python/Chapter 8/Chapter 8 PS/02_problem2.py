# c/5 = (f-32)/9

def f_to_c(f):
    c = 5*(f-32)/9
    return c


f = int(input("Enter temp in F : "))
print(f_to_c(f))