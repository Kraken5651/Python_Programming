class Employee:
    a = 1
        

class Programmer(Employee):
    b = 2
    
class Manager(Programmer):
    c = 3

a = Employee()
print(a.a)  
   
b = Programmer()
print(b.a, b.b)   
   
c = Manager()      
print(c.a, c.b, c.c)
       
       
 