b=int(input("Enter the table that you want:"))
a=1
d=int(input("Enter the number until which you want the table to :"))
while(a<d+1):
    c=a*b
    print("{0}*{1}={2}".format(a,b,c))
    a=a+1
print("Thank you")
