n = int(input())
arr = [x for x in input().split()]
temp = []
for i in range(n):
    if i < n / 2:
        temp.append(arr[i][0])
    else:
        temp.append(arr[i][-1])
num = int("".join(temp))
print("OUI" if num % 11 == 0 else "NON")
