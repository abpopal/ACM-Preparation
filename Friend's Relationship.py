for _ in range(int(input())):
    n = int(input()) - 1
    j = n*2
    for i in range(1, n + 2):
        print("*" * i, end="")
        print("#" * j, end="")
        print("*" * i)
        j -= 2
