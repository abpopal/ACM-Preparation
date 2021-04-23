t = int(input())
for _ in range(t):
    n = int(input())
    s = input()
    v = ['a', 'e', 'i', 'o', 'u']
    res = 0
    for i in range(n):
        if s[i] not in v and s[i+1] in v:
            res += 1
    print(res)
