print("*** Converting hh.mm.ss to seconds ***")
h,m,s = input("Enter hh mm ss : ").split()

second = (int(h) * 3600) + (int(m) * 60) + int(s)
def calculator(second):
    if int(m) >= 60: 
        return f"mm({m}) is invalid!"
    if int(m) < 0:
        return f"mm({m}) is invalid!"
    if int(m) < 60:
        return f"{int(h):02d}:{int(m):02d}:{int(s):02d} = {second:,} seconds"
    
print(calculator(second))




