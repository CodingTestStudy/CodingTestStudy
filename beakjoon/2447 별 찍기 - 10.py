#2447 별 찍기 - 10
def printStar(i, j, N):
  if((i//N)%3 == 1 and (j//N)%3 == 1):
    print(" ", end="")
  else:
    if N//3 == 0:
      print("*", end="")
    else:
      printStar(i, j, N//3)

N = int(input())
for i in range(0, N):
  for j in range(0, N):
    # print(i, j)
    printStar(i, j, N)
  print()