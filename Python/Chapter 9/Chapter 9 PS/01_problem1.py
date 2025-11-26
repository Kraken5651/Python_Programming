f = open("poem.txt")

c = f.read()

if("twinkle" in c):
    print("The word twinkle is present")
else:
    print("The word twinkle is not present")
f.close()