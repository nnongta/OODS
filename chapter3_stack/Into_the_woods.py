class Stack:
    def __init__(self):
        self.items = []

    def push(self, i):
        self.items.append(i)

    def pop(self):
        return self.items.pop()

    def num(self):
        return len(self.items)

    def isEmpty(self):
        return len(self.items) == 0

    def top(self):
        return self.items[-1] if self.num() > 0 else -1


inp = [[j for j in i.split()] for i in input("Enter Input : ").split(",")]
s = Stack()

for i in inp:
    if i[0] == 'A':
        while int(i[1]) >= s.top() and s.num() > 0:
            s.pop()
        s.push(int(i[1]))
    else:
        print(s.num())
