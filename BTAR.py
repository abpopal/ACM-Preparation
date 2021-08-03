for i in range(int(input())):
    n = int(input())
    arr = list(map(int, input().split()))
    count1 = 0
    count2 = 0
    count3 = 0
    sum = 0
    for i in range(n):
        x = arr[i] % 4
        sum += x

        if x == 1:
            count1 += 1

        if x == 2:
            count2 += 1

        if x == 3:
            count3 += 1
    if (sum % 4) != 0:
        print(-1)
        continue

    else:

        if count2 == 0 and count1 != 0 and count3 == 0:
            tt = count1 // 4
            print(3 * tt)

        if count2 == 0 and count1 == 0 and count3 != 0:
            tt = count3 // 4
            print(3 * tt)

        if count2 % 2 == 0 and count1 == count3:
            print(count2 // 2 + count1)

        flag1 = min(count1, count3)
        flag2 = abs(count1 - count3)

        if count2 % 2 == 0 and count1 != count3:
            flag3 = flag2 // 4
            flag4 = flag3 * 3

            print(count2 // 2 + flag1 + flag4)

        if count2 % 2 != 0 and count1 != count3:
            flag3 = flag2 - 2
            flag4 = flag3 // 4
            flag5 = flag4 * 3

            print(((count2 - 1) // 2) + flag1 + flag5 + 2)

            
            
            
