def rem(l, word):
    for item in l:
        l.remove(word)
        return l


l = ["Harry", "Rohan", "Shubham", "am"]

print(rem(l, "am"))