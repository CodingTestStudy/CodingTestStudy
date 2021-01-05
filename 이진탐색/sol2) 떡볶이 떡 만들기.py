#sol2) 떡볶이 떡 만들기, 201p

def binary_search(array, target, start, end) :
  H = (start+end)//2
  sum = 0

  for i in array :
    if i > H :
      sum += (i-H)
  
  if target == sum :
    return H
  elif target < sum :
    return binary_search(array, target, H+1, end)
  else :
    return binary_search(array, target, start, H-1)

N, M = map(int, input().split())
data = list(map(int, input().split()))
data.sort()
print(binary_search(data, M, 0, data[N-1]))



#풀이방법

n, m = list(map(int, input().split()))
array = list(map(int, input().split()))

start = 0
end = max(array)
result = 0

while start<=end :
  total = 0
  mid = (start+end)//2
  
  for x in array :
    if x > mid :
      total += x - mid
  
  if total < m :
    end = mid - 1
  
  else :
    result = mid
    start = mid + 1

print(result)