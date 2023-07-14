print("*** Fun with permute ***")

num_input = input("input : ").split(",")
num_input = [int(num) for num in num_input]  # Convert to integers

num_ori = '[' + ', '.join([str(num) for num in num_input]) + ']'


def permute(n):
    if len(n) == 0:
        return []
    if len(n) == 1:
        return [n]
    
    result = [[]]
    for i in n:
        lst = []
        for j in result:
            for k in range(len(j) + 1):
                lst.append(j[:k] + [i] + j[k:])
                result = lst
    return result


print("Original Cofllection: ", num_ori)
print("Collection of distinct numbers: ")
output = [int(e) for e in num_input]
print("", permute(output))

