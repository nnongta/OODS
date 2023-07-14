class MyInt:
  def __init__(self, num) -> None:
    self.num = num
  
  def isPrime(self):
    flag= False
    if self.num <= 1:
        return False
    elif self.num > 1:
        for i in range(2, self.num):
            if (self.num % i) == 0:
                flag = True
                break
            
        if flag:
          return False
        else:
          return True
        
  def showPrime(self):
    nums  = []
    for num in range(2, self.num + 1):
      if num > 1:
          for i in range(2, num):
              if (num % i) == 0:
                  break
          else: 
              nums.append(num)
    return nums

  def __sub__(self, other):
        return int(self.num - (other.num // 2))

print(' *** class MyInt ***')

num1, num2= [int(i) for i in input("Enter 2 number : ").split()]
a = MyInt(num1)
b = MyInt(num2)

c = a - b



print(str(num1), "isPrime :", a.isPrime())
print(str(num2), "isPrime :", b.isPrime())

# print("Prime numbers between 2 and", a.num, ":", " ".join(map(str, a.showPrime())))
if (a.num < 2):
    print("Prime number between 2 and", a.num, ":", "!!!A prime number is a natural number greater than 1")
else:
    print("Prime number between 2 and", a.num, ":", " ".join(map(str, a.showPrime())))

# print("Prime number between 2 and", b.num, ":", " ".join(map(str, b.showPrime())))
if (b.num < 2):
    print("Prime number between 2 and", b.num, ":", "!!!A prime number is a natural number greater than 1")
else:
    print("Prime number between 2 and", b.num, ":", " ".join(map(str, b.showPrime())))
    
print(str(num1) + " - " + str(num2) + " =", str(int(c)))