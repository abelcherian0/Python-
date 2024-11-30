num_list1=int(input("Enter the number of elements in list1"))
list1=[]
for num in range(num_list1):
    list1.append(int(input()))
print(list1)






list1=[1,2,3,7,9,9,1]
list2=[]
for number in list1:
    if number not in list2:
        list2.append(number)
print(F"THE ORIGINAL LIST IS {list1}")
print(list2)

