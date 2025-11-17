a = (1,2,3,4,7)
b = (1,) # Tuple With Single Element.
c = () #Empty Tuple

print(type(a))
print(type(b))
print(type(c))

ab = (1,2,3,4,"Rohan", 5.23456)

#ab[0] = 45 #Tuple Cannot be changed like List
print(ab)

no = ab.count(2)
print(no)

aab = a + ab
print(aab)

aa = a * 2
print(aa)

print(2 in a)
print(100 in a)

print(len(ab))

print(min(a))
print(max(a))

sliced = ab[1:5]
print(sliced)

x = (1, 5, 7)
#x = (1, 5, 7, 3) # 1 extra element to unpack

a, b, c = x
print(a, b, c)


