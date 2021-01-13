#do3) 문자열 뒤집기, 313p
#그리디 유형

#1차 : 성공
#첫번째 수를 기준으로 다른숫자 덩어리 개수를 센다 (0기준 1덩어리수)
data = input()
count = 0
before = int(data[0])
for i in range(1, len(data)) :
  if int(data[i]) == before :
    continue
  if int(data[i]) != int(data[0]) :
    count += 1
  before = int(data[i])

print(count)

#해설코드
data = input()
count0 = 0 # 전부 0으로 바꾸는 경우
count1 = 0 # 전부 1로 바꾸는 경우

# 첫 번째 원소에 대해서 처리
if data[0] == '1':
    count0 += 1
else:
    count1 += 1

# 두 번째 원소부터 모든 원소를 확인하며
for i in range(len(data) - 1):
    if data[i] != data[i + 1]:
        # 다음 수에서 1로 바뀌는 경우
        if data[i + 1] == '1':
            count0 += 1
        # 다음 수에서 0으로 바뀌는 경우
        else:
            count1 += 1

print(min(count0, count1))