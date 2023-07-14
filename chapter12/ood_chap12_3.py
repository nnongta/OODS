print(" *** String count ***")

ms = (input("Enter message : "))
d={"UPPER_CASE":0, "LOWER_CASE":0}

unique_upper = set()
unique_lower = set()

for c in ms:
        if c.isupper():
            d["UPPER_CASE"]+=1
        elif c.islower():
            d["LOWER_CASE"]+=1

def unique(ms):
    for char in ms:
        if char.isupper():
            unique_upper.add(char)
    upper_sort = sorted(unique_upper)
    print("Unique Upper case characters :", '  '.join(upper_sort))

def unique_small(ms):
    for char in ms:
        if char.islower():
            unique_lower.add(char)
    lower_sort = sorted(unique_lower)
    print("Unique Lower case characters :", '  '.join(lower_sort))

print ("No. of Upper case characters :", d["UPPER_CASE"])
unique(ms)
print ("No. of Lower case Characters :", d["LOWER_CASE"])
unique_small(ms)