def change(mylist):
    mylist.append([1,2,3,4]);
    print'value inside the function',mylist
    return

mylist=[10,20,30];
change(mylist);
print'Value outside the function',mylist
