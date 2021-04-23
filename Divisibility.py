# Used the pre computation technique here because of Run Time error. Time limit was 1 sec

n = int(input())
arr = "".join(input().split())[1::2]
print("Yes" if int(arr) % 10 == 0 else "No")
