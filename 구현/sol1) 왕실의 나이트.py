#sol1) 왕실의 나이트, 115p

#도전
start = input()
x_data = ['a','b','c','d','e','f','g','h']
y_data = ['1','2','3','4','5','6','7','8']
move = [(-2,-1),(-2,1),(-1,2),(1,2),(2,1),(2,-1),(1,-2),(-1,-2)]
x = 0
y = 0
count = 0
for i in range(len(x_data)) :
  if start[0] == x_data[i] :
    x = i
  if start[1] == y_data[i] :
    y = i
for dx, dy in move :
  if x+dx > -1 and x+dx < 8 and y+dy > -1 and y+dy < 8 :
    count += 1
print(count)

#풀이방법
input_data = input()
row = int(input_data[1])
column = int(ord(input_data[0])) - int(ord('a'))+1

steps = [(-2,-1), (-1,-2), (1,-2), (2,-1), (2,1), (1,2), (-1,2), (-2,1)]
result = 0
for step in steps :
  next_row = row+step[0]
  next_column = column+step[1]

  if next_row >= 1 and next_row <= 8 and next_column >= 1 and next_column <= 8 :
    result += 1

print(result)