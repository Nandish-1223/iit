a = int(input("Enter a Year :"))
print("Leap year" if (a % 4 == 0 and a % 100 != 0) or (a % 400 == 0) else "Not Leap year")
