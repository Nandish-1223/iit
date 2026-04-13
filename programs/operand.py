a = int(input("Enter Number 1:"))
b = int(input("Enter Number 2:"))
operand = input("Enter operand:")
match operand:
   case "+":
      print(a+b)
   case "-":
      print(a-b)
   case "*":
      print(a*b)
   case "/":
      print(a/b)
   case _:
      print("Invalid Operation")
