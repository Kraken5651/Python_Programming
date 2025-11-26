words = ["Donkey", "not", "Cool", "Good"]

with open("Donkey.txt", "r") as f:
    content = f.read()
    
for word in words:
    contentNew = content.replace(word, "#" * len(word))

with open("Donkey.txt", "w") as f:
    f.write(contentNew)