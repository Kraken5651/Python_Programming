class Employee:
    salary = 500
    increment = 10 
    @property  
    def salaryAfterIncrement(self):
        return self.salary + self.salary * (self.increment/100)
    
    @salaryAfterIncrement.setter
    def salaryAfterIncrement(self, salary):
        self.increment = ((salary/self.salary) -1)*100
        
        
        
a = Employee()

print(a.salaryAfterIncrement)     

a.salaryAfterIncrement = 550
print(a.increment)
       
 