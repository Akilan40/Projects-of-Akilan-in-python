print'\n\n\n\t\t\t\t\t\tCalculator'
d=int(input('Enter a value from the choice below:\nPress1,for addition\nPress2 for subraction\npress3 for multiplication\npress4 for division\nYour choice:'))
if d==1:
    import addition
    a=int(input('Enter a value for 1st number:'))
    b=int(input('Enter a value for 2nd number:'))
    c=a+b
    addition.add(c)
if d==2:
    import subraction
    a=int(input('Enter a value for 1st number:'))
    b=int(input('Enter a value for 2nd number:'))
    e=a-b
    subraction.sub(e)

if d==3:
    import multiplication
    a=int(input('Enter a value for 1st number:'))
    b=int(input('Enter a value for 2nd number:'))
    f=a*b
    multiplication.mul(f)
if d==4:
    import divition
    a=int(input('Enter a value for 1st number:'))
    b=int(input('Enter a value for 2nd number:'))
    g=a/b
    divition.div(g)
else:
    print"Sometin went wrong"