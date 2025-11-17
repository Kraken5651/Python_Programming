iq = {
    "Kira": 100,
    "Josuke": 99,
    "Jotaro": 101,
    1000:"Jospeh"
}

print(iq.items())
print(iq.keys())
print(iq.values())

iq.update({"Kira": 90})
print(iq)

#print(iq.get("Kira1")) #Returns None as Output
#print(marks["Kira1"]) #Returns an error as Output

print(iq.clear())
