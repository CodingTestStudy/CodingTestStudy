#86
w, h, b = map(int, input().split())
print("%.2f MB"%(w*h*b/(2**23)))