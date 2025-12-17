a = 82
print(a)

def fun():
    global a
    a = 40
    print(a)
    
fun()
print(a)