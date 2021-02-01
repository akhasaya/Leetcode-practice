# i am in the middle of foo.bar challenge
# https://foobar.withgoogle.com/


def solution(l, t):
    # Your code here
    k = 0
    s = []
    n = len(l)
    for i in l:
        k = k + i
        s.append(k)

    for i in range(n):
        if s[i] == t:
            return [0, i]

    for i in range(n - 2):
        for j in range(i + 1, n):
            if s[j] - s[i] == t:
                return [i + 1, j]

    return [-1, -1]

l = [4,3,5,7,8]
t = 12

print(solution(l,t))