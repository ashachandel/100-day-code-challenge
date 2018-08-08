lst=[]
num=int(input("enter the number of first list"))
for i in range(num):
     numbers=int(input("enter any number"))
     lst.append(numbers)


lst2=[]
num=int(input("enter the number of second list"))
for i in range(num):
     numbers=int(input("enter any number"))
     lst2.append(numbers)

merged_lists=lst+lst2
print("merged list :",merged_lists)          


     
