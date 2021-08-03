for i in range(int(input())):
    st = input().split()
    N = int(st[0])
    Q = int(st[1])
    A = [0 for x in range(N + 2)]
    n = 0
    st = input().strip()
    for p in range(3, N + 1):
        if (st[p - 1] == st[p - 2]) or (st[p - 1] == st[p - 3]) or (st[p - 2] == st[p - 3]):
            n += 1
        A[p] = n
    for k in range(Q):
        st = input().split()
        L = int(st[0])
        R = int(st[1])
        if (A[L] < A[R]) and (A[L + 1] < A[R]):
            print('YES')
        else:
            print('NO')

            
            
