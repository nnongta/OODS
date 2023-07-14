
def threeofsum(num):
    num.sort()
    length = len(num)
    result = []
    for i in range(0,length):
        for j in range(i+1,length):
            for k in range(j+1,length):
                if num[i] + num[j] + num[k] == 5 and [num[i],num[j],num[k]] not in result:
                    result.append([num[i],num[j],num[k]])
    
    return result
 

List = list(input("Enter Your List : ").split())
List = [int(i) for i in List]
if len(List) > 2:
    print(threeofsum(List))
else:
    print("Array Input Length Must More Than 2")