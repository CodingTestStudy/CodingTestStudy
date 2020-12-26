#sol3) 1이 될 때까지, 99p

#도전
import time
start_time = time.time()
N, K = map(int, input().split())
result = 0
while True :
  if N == 1 :
    break
  elif N%K == 0 :
    result += 1
    N = N//K
  else :
    N -= 1
    result += 1
print(result)
end_time = time.time()
print(end_time-start_time)

#풀이방법
import time
start_time = time.time()
N, K = map(int, input().split())
result = 0

while True :
  target = (N//K)*K
  #배수를 맞추기 위한 감소수를 바로 구하여 더한다
  result += (N-target)
  #N은 K의 배수로 수정한다
  N = target
  if N<K :
    break
  result += 1
  N = N//K

result += N-1
print(result)
end_time = time.time()
print(end_time-start_time)