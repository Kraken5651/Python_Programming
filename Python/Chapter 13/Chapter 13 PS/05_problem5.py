from functools import reduce

a = [1, 2, 2332, 3223, 3221, 22234,5, 5432,2235, 33215]


def great(a,b):
    if(a>b):
        return a
    return b

print(reduce(great, a))