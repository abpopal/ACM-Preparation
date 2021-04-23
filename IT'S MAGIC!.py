n = int(input())
arr = [int(x) for x in input().split()]
temp = []
for i in range(n):
    t = 0
    for j in range(n):
        if j != i:
            t += arr[j]
    if t % 7 == 0:
        temp.append(arr[i])
print(arr.index(min(temp)))
