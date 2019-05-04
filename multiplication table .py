b=int(input("Enter the multiplication table that you want:"))
d=int(input("Enter the number until youwant your table to be:"))
a=1
while(a<d+1):
	c=a*b
	print("{0}*{1}={2}".format(a,b,c))
	a=a+1
print("\n Thank you")
