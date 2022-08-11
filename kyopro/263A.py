num = list(map(int, input().split()))
num.sort()
if (num[0] == num[2] and num[3] == num[4]) or (num[0] == num[1] and num[2] == num[4]):
  print("Yes")
else:
  print("No")
