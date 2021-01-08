#ex4) 퀵정렬, 168p

array = [5,7,9,0,3,1,6,2,4,8]

def quick_sort(array, start, end) :
  if start >= end : #종료조건
    return

  pivot = start
  left = start+1
  right = end

  while left <= right :
    while left <= end and array[left] <= array[pivot] :
      left += 1 #pivot 보다 큰 값을 찾는다
    while right > start and array[right] >= array[pivot] :
      right -= 1 #pivot 보다 작은 값을 찾는다
    
    if left > right :
      array[right], array[pivot] = array[pivot], array[right] #엇갈린 경우 povot과 위치를 바꾼다
    else :
      array[left], array[right] = array[right], array[left] #정상의 경우 크고 작은 값끼리 바꾼다

  quick_sort(array, start, right-1) #povot 왼쪽을 정렬한다
  quick_sort(array, right+1, end) #pivot 오른쪽을 정렬한다

quick_sort(array, 0, len(array)-1)

print(array)