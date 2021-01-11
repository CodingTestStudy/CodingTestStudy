#ex3) 개선된 서로소 집합 알고리즘, 275p

#find 함수, 계속 갱신하며 루트값을 찾는다
def find_parent(parent, x) :
  if parent[x] != x :
    parent[x] = find_parent(parent, parent[x])
  return parent[x]

#union 함수, 두 노드의 루트값 중 작은값을 루트로 묶는다
def union_parent(parent, a, b) :
  a = find_parent(parent, a)
  b = find_parent(parent, b)
  if a < b :
    parent[b] = a
  else :
    parent[a] = b

#노드개수, 간선수 입력
v, e = map(int, input().split())
parent = [0]*(v+1)

#부모테이블 초기화
for i in range(1, v+1) :
  parent[i] = i

#간선 입력
for i in range(e) :
  a, b = map(int, input().split())
  union_parent(parent, a, b)

#각 노드의 루트를 구하여 출력
print('각 원소가 속한 집합: ', end='')
for i in range(1, v+1) :
  print(find_parent(parent, i), end=' ')

print()

#부모테이블 저장된 노드 출력
print('부모 테이블: ', end = '')
for i in range(1, v+1) :
  print(parent[i], end = ' ')