#do2) 곱하기 혹은 더하기, 312p
#그리디 유형

#1차 : 접근 실패
#결과값 또는 현재값이 1보다 작거나 같은경우는 덧셈, 그외는 곱셈

data = input()
result = int(data[0])

for i in range(1, len(data)) :
  num = int(data[i])
  if result <= 1 or num <= 1 :
    result += num
  else :
    result *= num

print(result)