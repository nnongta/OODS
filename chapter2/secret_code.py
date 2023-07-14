
def bon(w):
    repeat_char = ""

    for char in w:
        if w.count(char) > 1 and char not in repeat_char:
            repeat_char += char

    # return repeat_char

    numbers = [ord(char.lower()) - 96 for char in repeat_char]
    sum_value = int(''.join(map(str, numbers))) * 4
    return sum_value

secretCode = input("Enter secret code : ")
print(bon(secretCode))

