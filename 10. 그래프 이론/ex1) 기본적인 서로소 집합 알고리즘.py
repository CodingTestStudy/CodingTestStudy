#ex1) 기본적인 서로소 집합 알고리즘, 273p

#루트노드 찾아서 반환한다
def find_parent(parent, x) :
  #루트 노드가 아니라면, 루트 노드를 찾을 때까지 재귀적으로 호출
  if parent[x] != x :
    return find_parent(parent, parent[x])
  #최종 루트노드값을 반환한다
  return x

#두 노드의 루트를 한 루트로 연결한다
def union_parent(parent, a, b) :
  #두 노드의 루트를 각각 찾는다
  a = find_parent(parent, a)
  b = find_parent(parent, b)
  #작은 값의 노드를 루트로 설정한다
  if a < b :
    parent[b] = a
  else :
    parent[a] = b

#노드수, 간선수 입력
v, e = map(int, input().split())
parent = [0]*(v+1)

#자기자신을 루트로 초기화한다
for i in range(1, v+1) :
  parent[i] = i

#간선을 입력받아 한 루트로 연결한다
for i in range(e) :
  a, b = map(int, input().split())
  union_parent(parent, a, b)

#재귀적으로 찾은 루트값
print('각 원소가 속한 집합: ', end='')
for i in range(1, v+1) :
  print(find_parent(parent, i), end=' ')

print()

#부모 테이블에 저장된 값
print('부모 테이블: ', end='')
for i in range(1, v+1) :
  print(parent[i], end=' ')