def triangle(n):
    z=int(input("Enter the number of rows that you want:")) 
    k = 2*n - 2
 
    for i in range(0, z):
     
        for j in range(0, k):
            print(end=" ")
     
        k = k - 1
     
        for j in range(0, i+1):
         
            print("* ", end="")
     

        print("\r")
 
n = 5
triangle(n)
