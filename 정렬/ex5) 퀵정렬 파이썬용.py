#ex5) 퀵정렬-파이썬용, 169p

array = [5,7,9,0,3,1,6,2,4,8]

def quick_sort(array) :
  if len(array) <= 1 :
    return array

  pivot = array[0] #pivot 설정
  tail = array[1:] #pivot 뒤의 array

  left_side = [x for x in tail if x <= pivot] #array 에서 pivot 보다 작은값을들 left_side로 넣는다
  right_side = [x for x in tail if x > pivot] #array 에서 pivot 보다 큰값들을 right_size로 넣는다

  return quick_sort(left_side) + [pivot] + quick_sort(right_side) #작은값들, 기준점, 큰값들을 한 리스트로 묶는다

print(quick_sort(array))