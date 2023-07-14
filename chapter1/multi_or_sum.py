print("*** multiplication or sum ***")

num_one, num_two = input("Enter num1 num2 : ").split()
sum_result = int(num_one) * int(num_two)

def calculator(sum):
    if sum > 1000:
        return "The result is " + str(int(num_one) + int(num_two))
    else:
        return f"The result is {sum}"

print(calculator(sum_result))
