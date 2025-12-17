def devby5(n):
    if(n%5 ==0):
        return True
    return False

a = [1, 2, 2332, 3223, 3221, 22234,5, 5432,2235, 33215]

f = list(filter(devby5, a))
print(f)