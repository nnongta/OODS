def rotate_string(s):
    return s[1:] + s[0]

def string_rotation(str1, str2):
    if len(str1) != len(str2):
        return False

    rounds = 0
    while True:
        str1 = rotate_string(str1)
        if str1 == str2:
            rounds += 1
            break
        rounds += 1

    return rounds

# Test case
str1 = "123"
str2 = "456"
rounds = string_rotation(str1, str2)

print("*** String Rotation ***")
print("Enter 2 strings:", str1, str2)
print(str1, str2)
for i in range(rounds - 1):
    str1 = rotate_string(str1)
    print(str1, str2)
print("Total of", rounds, "rounds.")
