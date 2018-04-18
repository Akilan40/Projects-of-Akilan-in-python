Num = int(input("\n\n\nPlease Enter the Range Number: "))

i = 0
First_Value = 0
Second_Value = 1

while (i < Num):
    if (i <= 1):
        N=i
    else:
        Next = First_Value + Second_Value
        First_Value = Second_Value
        Second_Value = N
    print(N)
    i = i + 1