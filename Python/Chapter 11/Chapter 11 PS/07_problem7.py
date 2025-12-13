class Vector:
    def __init__(self, l):
        self.l = l
    
    def __len__(self):
        return len(self.l)
    
#Test the implementation
v1 = Vector(1, 2, 3)
print(len(v1))
# v2 = Vector(4, 5, 6)
# v3 = Vector(7, 8, 9)

# print(v1 + v2)
# #print(v1 * v2)


# print(v1 + v3)
# #print(v1 * v3)