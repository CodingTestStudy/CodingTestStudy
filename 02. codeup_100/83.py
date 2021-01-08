#83
a = int(input())
for i in range(a) :
  if((i+1)%3 == 0) :
    print("X", end=" ")
  else :
    print(i+1, end=" ")