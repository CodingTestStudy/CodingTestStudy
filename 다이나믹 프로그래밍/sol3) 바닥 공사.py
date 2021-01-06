#sol3) 바닥 공사, 223p

N = int(input())
d = [0]*1000
result = 1

d[0] = 1
d[1] = 3
for i in range(2, N) :
  d[i] = (d[i-1] + 2*d[i-2])%796796

print(d[N-1])