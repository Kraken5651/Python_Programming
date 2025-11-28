class Employee:
    language = "py"
    salary = 120000
    
    def __init__(self, name, salary, language):
        self.name = name
        self.salary = salary
        self.language = language
        print("I am creating an object")
    
harry = Employee("Raja", 132000, "Java")
print(harry.language, harry.salary, harry.name)