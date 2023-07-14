print(" *** Rank score ***")

input_si = input("Enter ID and Score end with ID : ")
array_si = list(map(str, input_si.split()))
new_array = list(map(str, input_si.split()))

check = True
array_si.pop()

new_id_score_dict = {}

array_id = []
array_score = []

for index, element  in enumerate(array_si):
    if index % 2 == 0:
        array_id.append(element)
    else:
        array_score.append(float(element))

# print(array_id)
# print(array_score)

for i in range(0, len(array_score)):
    for j in range(i+1, len(array_score)):
        if(array_score[i] < array_score[j]):
            temp = array_score[i]
            array_score[i] = array_score[j]
            array_score[j] = temp

            temp = array_id[i]
            array_id[i] = array_id[j]
            array_id[j] = temp

        elif(array_score[i] == array_score[j])and (int(array_id[i]) > int(array_id[j])):
            temp = array_score[i]
            array_score[i] = array_score[j]
            array_score[j] = temp

            temp = array_id[i]
            array_id[i] = array_id[j]
            array_id[j] = temp

# print(array_id)
# print(array_score)

for i in range(len(array_id)):
    new_id_score_dict[array_id[i]] = float(array_score[i])

print(array_si)
print(new_array[-1])
print(new_id_score_dict)

if new_array[-1] in array_id:
    print(array_id.index(new_array[-1]) + 1)
else:
    print("Not Found")