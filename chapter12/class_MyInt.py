class MyInt:
    def __init__(self, num):
       self.num = num

    def isPrime(self):
        # if self.num <=  1:
        #     return False
        # elif self.num > 1:
        #     for i in range(2, int(self.num**0.5) + 1):
        #         if self.num % i == 0:
        #             return False   
        #     return True

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
        primes = []

        if self.num < 2:
            return primes
        for num in range(2, self.num + 1):
            if MyInt(num).isPrime():
                primes.append(num)
        return primes

    def __sub__(self, other):
        subtractor = other.num
        setter = self.num
        return setter - round(subtractor / 2)
    
print(" *** class MyInt ***")
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