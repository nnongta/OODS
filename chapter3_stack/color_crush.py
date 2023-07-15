class Stack():
    def __init__(self):
        self.items = []
    
    def push(self, i):
        self.items.append(i)

    def pop(self):
        return self.items.pop() if not self.isEmpty() else None

    def size(self):
        return len(self.items)
    
    def isEmpty(self):
        return self.size() == 0

inp = input('Enter Input : ').split()

S = Stack()
Combo, count = 0, 1

for i in inp:
    S.push(i)

while True:
    LastSta = S.size()
    temp = Stack()
    c = ""
    while not S.isEmpty():
        x = S.pop()
        if c != x:
            c = x
            count = 1
        else:
            count += 1
        temp.push(x)
        if count == 3:
            Combo += 1
            for i in range(3):
                temp.pop()
    while not temp.isEmpty():
        S.push(temp.pop())

    if LastSta == S.size():
        break

print(S.size())
if S.size() == 0:
    print("Empty")
else:
    print(''.join(S.items[::-1]))
if Combo > 1:
    print(f"Combo : {Combo} ! ! !")
