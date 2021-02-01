from collections import Counter

def solution(x, y):
    # Your code here
    a = Counter(x)
    b = Counter(y)

    c = (a - b) + (b - a)
    for items in c.keys():
        return items

f = [1,2]
print(f)
s = [1,2,3]
print(solution(f,s))