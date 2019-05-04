print("\n\n\t\t\tUpdating a list")
list=['phy','chem',1,2]
c=list
print("List before update",c)
print("value available at index 2:",list[2])
list[2]=2;
print("New value at index 2:",list[2])
b=len(list)
print("length of the list:",b)
a=list
print("list after Updating:",a)
z=float(input("now if u want to delete the contents in list \n\n\t\tpress 1\nif you want to add a value to the list \n\t\tpress 2\n\n\t\t\t\t\tenter your choice:"))
if z==1:
    x=list.clear()
    print("the values in the list is:  ",x)
elif z==2:
    list[3]=(input("Enter one value that u want to add to the list:"))
    list.extend(list[3])
    print("contents present in the list after adding the values: ",list)
else:
    print("something went wrong")
