#ex6) 계수 정렬, 174p

array = [7,5,9,0,3,1,6,2,9,1,4,8,0,5,2]
count = [0]*(max(array)+1) #array의 최고수+1만큼 크기설정

for i in range(len(array)) :
  count[array[i]] += 1 #해당수의 count 증가

for i in range(len(count)) :
  for j in range(count[i]) :
    print(i, end=" ") #해당수를 count만큼 출력