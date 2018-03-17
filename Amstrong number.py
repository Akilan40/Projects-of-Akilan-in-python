print("\n\n\t\t\tFinding the amstrong number")
a=int(input("\n\nEnter the number that you want to check: "))
b=0
c=a
d=0
while(c>0):
    d=c%10
    b+=d**3
    c//=10
if a==b:
    print("\n\n\t\tThe number that you entered is an !!amstrong number!!:)")
else:
    print("\n\n\tt\oh no the number entered was not an amstrong number:(")
