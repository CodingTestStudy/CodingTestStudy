#sol1) 부품 찾기, 197p

def binary_search(array, target, start, end) :
  if start > end :
    return None

  mid = (start+end)//2
  if target == array[mid] :
    return mid
  elif target < array[mid] :
    return binary_search(array, target, start, mid-1)
  else :
    return binary_search(array, target, mid+1, end)

N = int(input())
data = list(map(int, input().split()))
data.sort()
M = int(input())
question = list(map(int, input().split()))

for i in question :
  if binary_search(data, i, 0, N-1) == None :
    print("no", end=" ")
  else :
    print("yes", end=" ")



#풀이방법1 - 계수정렬

N = int(input())
array = [0]*1000001

for i in input().split() :
  array[int(i)] = 1

M = int(input())
question = list(map(int, input().split()))

for i in question :
  if array[i] == 1 :
    print("yes", end=" ")
  else :
    print("no", end=" ")



#풀이방법2 - 집합 set

N = int(input())
array = set(map(int, input().split()))

M = int(input())
question = list(map(int, input().split()))

for i in question :
  if i in array :
    print("yes", end=" ")
  else :
    print("no", end=" ")