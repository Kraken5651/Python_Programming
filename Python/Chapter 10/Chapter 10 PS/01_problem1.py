class Programmer:
    company = "Microsoft"
    
    def __init__(self, name, salary, pincode):
        self.name = name
        self.salary = salary
        self.pincode = pincode
        
p = Programmer("Rahul", 120000, 223421)
print(p.name, p.salary, p.pincode)
