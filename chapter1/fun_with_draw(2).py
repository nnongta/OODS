
print("*** Fun with Drawing ***")
n = input("Enter input : ")
n = int(n)
hh = (2*n) - 1 # ความสูงแบ่งครึ่ง

# ลูปครึ่งบน
for i in range((2 * n) - 1 - 1): # วน loop แกน y 2n - 1 คือตรงกลาง - 1 อีกรอบเพราะว่าจะปริ้นแยก
    for j in range((2 * hh) - 1):
        if j >= i and j <= ((2 * hh) - 1) - i - 1:
            if i % 2 == 0:
                print("#", end = '')
            elif i % 2 != 0:
                print(".", end = '')
        else:
            if j % 2 == 0:
                print('#', end = '')
            else:
                print('.', end = '')
    print("")

# ปริ้นตรงกลาง
for i in range((2 * hh) - 1): # ลูปตรงกลาง
    if i % 2 == 0:
        print('#', end = '')
    else:
        print('.', end = '')
print("")

# ลูปครึ่งล่าง
for i in range((2 * n) - 1 - 1):
    for j in range((2 * hh) - 1):
        if j >= hh - 2 - i and j <= (2 * hh) - hh + i:
            if i % 2 == 0:
                print(".", end = '')
            elif i % 2 != 0:
                print("#", end = '')
        else:
            if j % 2 == 0:
                print('#', end = '')
            else:
                print('.', end = '')

    print("")
