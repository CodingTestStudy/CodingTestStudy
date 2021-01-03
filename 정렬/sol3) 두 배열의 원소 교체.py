#sol3) 두 배열의 원소 교체

N, K = map(int, input().split())
arrA = list(map(int, input().split()))
arrB = list(map(int, input().split()))

arrA.sort()
arrB.sort(reverse = True)

for i in range(K) :
  if arrA[i] < arrB[i] :
    arrA[i], arrB[i] = arrB[i], arrA[i]
  else :
    break

print(sum(arrA))
