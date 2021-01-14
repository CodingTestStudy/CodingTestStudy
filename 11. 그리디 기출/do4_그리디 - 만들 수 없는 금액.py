#do4_그리디 - 만들 수 없는 금액, 314p
#그리디 유형

#1차 : 실패
#정렬을 하여 1에 작은값부터 차례로 누적하며 더한다
#누적된 값보다 더할값이 더 큰경우 공백이 생기므로 누적된값(계산가능+1) 값이 정답이다.
N = int(input())
money = list(map(int, input().split()))
money.sort()

check = 1
result = 0
sum = 0
for i in money :
  if i > check :
    break
  check += i

print(check)
