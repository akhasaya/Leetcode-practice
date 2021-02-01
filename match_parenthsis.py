# return the length of maximum valid substring
def solution(str):
    l = len(str)
    if l < 1:
        return 0

    stack = []
    index = -1
    valid = 0

    for char in str:
        if char == '(':
            stack.append('(')
            index += 1
        if char == ')':
            if index > -1 and stack[index] == '(':
                stack.pop(index)
                index -= 1
                valid += 2
    return valid

print(solution("((())()()((())))"))