#sol1) 팀 결성, 298p

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

def find(parent, a, b) :
  a = findParent(parent, a)
  b = findParent(parent, b)
  if a == b :
    print("YES")
  else :
    print("NO")

N, M = map(int, input().split())
parent = [0]*(N+1)
for i in range(1, N+1) :
  parent[i] = i

for i in range(M) :
  case, a, b = map(int, input().split())
  if case == 0 :
    union(parent, a, b)
  else :
    find(parent, a, b)