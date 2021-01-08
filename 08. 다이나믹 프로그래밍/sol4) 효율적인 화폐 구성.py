#sol4) 효율적인 화폐 구성, 226p

N, M = map(int, input().split())
money = []
for i in range(N) :
  money.append(int(input()))

money.sort()

d = [10001]*(M+1)
d[0] = 0

#현재 금액 - 화폐단위 값+1로 수정한다 이때, min 함수를 활용하여 이전값이 없는경우 10001 유지가 된다.
for i in range(N) :
  for j in range(money[i], M+1) :
    d[j] = min(d[j], d[j-money[i]]+1)

if d[M] == 10001 :
  print(-1)
else :
  print(d[M])