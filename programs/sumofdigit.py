a = int(input("Enter a Number :"))
sum = 0
for i in range(len(str(a))):
   sum += a % 10
   a = a//10
print(sum)
