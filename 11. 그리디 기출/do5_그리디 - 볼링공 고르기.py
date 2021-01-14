#do5_볼링공 고르기, 315p
#그리디 유형

#1차 : 성공
#정렬한 다음 버블소트처럼 숫자를 확인하며
#숫자가 다른경우의 회수를 센다
N, M = map(int, input().split())
bolls = list(map(int, input().split()))
bolls.sort()

result = 0
for i in range(len(bolls)-1) :
  for j in range(i+1, len(bolls)) :
    if bolls[i] != bolls[j] :
      result += 1

print(result)


#해설코드
n, m = map(int, input().split())
data = list(map(int, input().split()))

# 1부터 10까지의 무게를 담을 수 있는 리스트
array = [0] * 11

for x in data:
    # 각 무게에 해당하는 볼링공의 개수 카운트
    array[x] += 1

result = 0
# 1부터 m까지의 각 무게에 대하여 처리
for i in range(1, m + 1):
    n -= array[i] #전체 공 개수 - 무게 i중 A가 선택할 수 있는 공의 개수 = B가 선택 가능한 공의 개수
    result += array[i] * n #무게 i중 A의 선택가능수 ✕ B의 나머지 공 선택가능수

print(result)