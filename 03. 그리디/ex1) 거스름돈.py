#ex1) 거스름돈, 89P
#500, 100, 50, 10원
#동전의 최소 개수를 구하라

#큰 동전값이 작은 동전값의 배수일 경우에 사용이 가능한 구조이다.

#도전
N = int(input())
result = 0
while(N>0) :
  if N>500 :
    result += 1
    N -= 500
  elif N>100 :
    result += 1
    N -= 100
  elif N>50 :
    result += 1
    N -= 50
  else :
    result += 1
    N -= 10
print(result)

#best code
N = int(input())
count = 0
list = [500, 100, 50, 10]
#list에 넣어 for문으로 각 나누는 숫자에 대해 접근을 한방에 끝내고
#몫만큼 개수를 증가, n값은 나머지값으로 수정한다
for coin in list:
  count += N//coin
  N %= coin

print(count)