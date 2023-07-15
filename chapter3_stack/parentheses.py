def matced(input_st):
    stack = [] 

    opening_bracket = [ '(' , '[']
    closing_bracket = [ ')' , ']']
    pairs = {'(': ')', '[': ']'}

    for char in input_st:
        if char in opening_bracket:
            stack.append(char)
        elif char in closing_bracket:
            if not stack or pairs[stack.pop()] != char:
                return False
    
    return len(stack) == 0

      

input_text = input("Enter Input : ")

if matced(input_text):
    print("Parentheses : Matched ! ! !")
else:
    print("Parentheses : Unmatched ! ! !")

