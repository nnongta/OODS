print("*** String Rotation ***")
left_str, right_str = input("Enter 2 strings : ").split()

copy1 = ""
copy1 += left_str[len(left_str)-1:]+left_str[:len(left_str)-1]
copy2 = ""
copy2 += right_str[1:]+right_str[:1]
num = 1
print(num,copy1,copy2)
while left_str != copy1 or right_str != copy2:
    temp1 = ""
    temp1 += copy1[len(copy1)-1:]+copy1[:len(copy1)-1]
    copy1 = temp1
    temp2 = ""
    temp2 += copy2[1:]+copy2[:1]
    copy2 = temp2
    num+=1
    if num <= 5:
        print(num,copy1,copy2)
if num == 6:
    print(num,left_str,right_str)
elif num>5:
    print(" . . . . . ")
    print(num,left_str,right_str)

print("Total of  "+str(num)+" rounds.")