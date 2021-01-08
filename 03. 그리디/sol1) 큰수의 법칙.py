#실전1) 큰수의 법칙, 92p
#M : 더하는 회수, K : 최대중복회수

#첫번쩨 풀이방법
N, M, K = map(int, input().split())
data = list(map(int, input().split()))

data.sort(reverse=True)
result = 0

#종료조건을 잘 생각하여 if문과 break를 먼저 적은 후 그 뒤에
#반복되며 더해질 내용을 적는다
while True :
  for i in range(K) :
    if M == 0 :
      break
    result += data[0]
    M -= 1
  if M == 0 :
    break
  result += data[1]
  M -= 1
print(result)

#두번째 풀이방법
N, M, K = map(int, input().split())
data = list(map(int, input().split()))
data.sort(reverse=True)
result = 0

#반복되는 것을 찾자. K+1 크기의 숫자가 반복되어 더해진다
#K+1만큼 큰수를 K번 더하는게 반복된다. 또한 K+1로 나눈 나머지만큼도 반복된다.
count = M//(K+1)*K + M%(K+1)
result += data[0]*count
result += data[1]*(M-count)
print(result)