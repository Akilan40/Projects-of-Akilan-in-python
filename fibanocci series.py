range1 = int(raw_input("Enter the number of elements of the series: "))
n1 = 0
n2 = 1
i = 2
if range1 <= 0:
    print "Enter a positive integer.."
elif range1 == 1:
    print "Fibonacci series up to", range1, ":"
    print n1
else:
    print "Fibonacci series up to", range1, ":"
    print n1
    print n2
    while i < range1:
        n3 = n1 + n2
        print n3
        n1 = n2
        n2 = n3
        i = i + 1