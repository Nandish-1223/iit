a = int(input("Enter Salary :"))
if 0 < a <= 250000:
   print("No Tax")
elif 250000 < a <= 50000:
   print("Tax :",a*0.05)
elif 50000 < a <= 1000000:
   print("Tax :",a*0.1)
else:
   print("Tax :",a*0.15)
