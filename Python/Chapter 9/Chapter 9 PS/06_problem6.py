
with open("log.txt") as f:
    c = f.read()


if("Python" in c):
    print(f"Yes python is present")
    
else:
    print("No python is not present")