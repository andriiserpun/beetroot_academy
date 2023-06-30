def is_balanced(sequence):
    stack = []
    opening_brackets = ['(', '{', '[']
    closing_brackets = [')', '}', ']']
    brackets_map = {')': '(', '}': '{', ']': '['}

    for char in sequence:
        if char in opening_brackets:
            stack.append(char)
        elif char in closing_brackets:
            if not stack or brackets_map[char] != stack.pop():
                return False
    return len(stack) == 0

if is_balanced("(hello)"):
    print("The sequence is balanced")
else:
    print("the sequence is not balanced")
