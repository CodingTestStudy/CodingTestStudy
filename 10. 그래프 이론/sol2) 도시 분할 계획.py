#sol2) 도시 분할 계획, 300p

def findParent(parent, x) :
  if parent[x] != x :
    parent[x] = findParent(parent, parent[x])
  return parent[x]

def union(parent, a, b) :
  a = findParent(parent, a)
  b = findParent(parent, b)
  if a < b :
    parent[b] = a
  else :
    parent[a] = b

N, M = map(int, input().split())
parent = [0]*(N+1)
for i in range(1, N+1) :
  parent[i] = i

edges = []

for i in range(M) :
  A, B, C = map(int, input().split())
  edges.append((C, A, B))

edges.sort()
result = 0
last = 0

#크루스칼을 실행하며, 간선값이 가장 큰 값을 last로 저장한다
for edge in edges :
  cost, a, b = edge
  if findParent(parent, a) != findParent(parent, b) :
    union(parent, a, b)
    result += cost
    last = cost

#last를 제거하여 가장적은 비용으로 두개의 마을로 분리가 된다
result -= last
print(result)
