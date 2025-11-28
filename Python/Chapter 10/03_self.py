class Employee:
    language = "py"
    salary = 120000
    
    def getInfo(self):
        print(f"The language is {self.language}. The salary is {self.salary}")
        
    @staticmethod
    def greet():
        print("Good Morning")
    
harry = Employee()
print(harry.language, harry.salary)
harry.getInfo()
Employee.getInfo(harry)
harry.greet()