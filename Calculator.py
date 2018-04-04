print("\n\n\n\t\t\tCalculator")
print("Select operation:")
print("1.Add")
print("2.Subtract")
print("3.Multiply")
print("4.Divide")

c = input("Enter choice(1/2/3/4):")

a = int(input("Enter first number: "))
b = int(input("Enter second number: "))

if c==1:
      d=a+b
      print("{0}+{1}={2}".format(a,b,d))

elif c==2:
      d=a-b
      print("{0}-{1}={2}".format(a, b, d))

elif c==3:
      d=a*b
      print("{0}*{1}={2}".format(a, b, d))

elif c==4:
      d=a/b
      print("{0}/{1}={2}".format(a, b, d))

else:
      print("Invalid input")