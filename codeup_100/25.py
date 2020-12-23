#25
num = int(input())
print("[" + str(num//10000) + "0000]")
print("["+str(num//1000%10)+"000]")
print("["+str(num//100%10)+"00]")
print("["+str(num//10%10)+"0]")
print("["+str(num%10)+"]")