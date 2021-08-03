for i in range(int(input())):
    subs = int(input())
    arr = list(input().split(","))
    res = []
    for j in range(int(input())):
        sub1 = arr[0][0]
        cre1 = int(arr[0][-1])
        sub2 = arr[1][0]
        cre2 = int(arr[1][-1])
        name, mark1, mark2 = input().split(",")
        failed = 0
        if int(mark1) < 50:
            failed = 4
        elif int(mark2) < 50:
            failed = 2

        avg = (int(mark1)*cre1 + int(mark2)*cre2)/(cre1+cre2)
        if int(avg) == avg:
            avg = int(avg)
        else:
            s = str(avg)
            avg = float(s[0:5])
        res.append(f"{name},{avg},{failed},{'true' if failed == 4 else 'false'}")

    final = reversed(sorted(res, key=lambda x: int(x.split(",")[1].split(".")[0])))
    for k in final:
        print(k)
