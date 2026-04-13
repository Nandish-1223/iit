a = int(input("Enter Number:"))
reverse = 0
for i in range(len(str(a))):
   rem = a % 10
   reverse = reverse * 10 + rem
   a = int(a / 10)
print(reverse)
