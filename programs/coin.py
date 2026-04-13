a = int(input("Enter No. of Coin Suresh Have :"))
b = int(input("Enter No. of Coin Sundar Have :"))
c = int(input("Enter No. of Coin Raja Have :"))
d = int(input("Enter No. of Coin Suresh Have :"))
if a < b :
   a = a + c
elif a == b or b < a :
   b = b + c
if a < b :
   a = a + d
elif a == b or b < a :
   b = b + d
print("N") if a > b or a == b else print("S")
