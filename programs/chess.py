result = input("Enter Result of 14 Matches :")
prize = int(input("Enter Prize Money:"))
if len(result) != 14:
   sys.exit(0)
chandru = 0
nirmal = 0
for i in result:
   if i.lower() == 'c':
      chandru += 2
   if i.lower() == 'n':
      nirmal += 2
   if i.lower() == 'd':
      chandru += 1
      nirmal += 1
if chandru > nirmal:
   print(60*prize)
elif chandru == nirmal:
   print(55*prize)
else:
   print(40*prize)
