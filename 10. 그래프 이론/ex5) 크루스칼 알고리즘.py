#ex5) 크루스칼 알고리즘, 288p

def find_parent(parent, x) :
  if parent[x] != x :
    parent[x] = find_parent(parent, parent[x])
  return parent[x]

def union_parent(parent, a, b) :
  a = find_parent(parent, a)
  b = find_parent(parent, b)
  if a < b :
    parent[b] = a
  else :
    parent[a] = b

v, e = map(int, input().split())
parent = [0]*(v+1)
#간선 테이블, 합산 비용
edges = []
result = 0

for i in range(1, v+1) :
  parent[i] = i

for i in range(e) :
  a, b, cost = map(int, input().split())
  #비용, 시작점, 끝점 순서로 간선 저장
  edges.append((cost, a, b))

edges.sort()

#간선이 사이클이 아닌 경우 union으로 합친다
for edge in edges :
  cost, a, b = edge
  if find_parent(parent, a) != find_parent(parent, b) :
    union_parent(parent, a, b)
    result += cost

print(result)