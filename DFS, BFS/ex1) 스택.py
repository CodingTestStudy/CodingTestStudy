#ex1) 스택, 126p

stack = []
stack.append(5) #5
stack.append(2) #52
stack.append(3) #523
stack.append(7) #5237
stack.pop()     #523
stack.append(1) #5231
stack.append(4) #52314
stack.pop()     #5231

print(stack)
print(stack[::-1])