print("\n\n\n\t\t\tCalculator")
print("Select operation:")
print("1.Add")
print("2.Subtract")
print("3.Multiply")
print("4.Divide")

c = input("Enter choice(1/2/3/4):")
print("\n\n\n\n\n\t\t\t\tThe first value will be added,multiplied,divided and subracted by the second value")

a = int(input("Enter first number: "))
b = int(input("Enter second number: "))

if c=='1':
  print("\n\n\t\t\t\tAddition")
  d=a+b
  print(a,"+",b,"=",d)

elif c=='2':
  print("\n\n\t\t\t\tSubraction")
  d=a-b
  print(a,"-",b,"=",d)

elif c=='3':
  print("\n\n\t\t\t\tMultiplication")
  d=a*b
  print(a,"*",b,"=",d)

elif c=='4':
  print("\n\n\t\t\t\tDivision")
  d=a/b
  print(a,"/",b,"=",d)

else:
  print("Invalid input")
