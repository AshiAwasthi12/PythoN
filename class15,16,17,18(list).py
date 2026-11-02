"""#data types
1.numbers()
2.string("abc)
3.boolean(true,false,)"""

#data structures.
"""
list
1.square bracket->list,
2.heterogeneous data structure(a list can store different data types together)"""

#marks=[]#empty list
#you can store any type of data in it 
#you can store duplicate value in list
"""
marks=[80,78,80,90,65,88,"Abhishek,3.14"]
print(marks[3])#indexing is possible
print(marks[1:6])"""
#bhut sari value ko ek sth store krhe hai
#list are ordered becuse they have indexing
#and indexing start from 0.
#list are mutable-> we can change or reaasign any value at any index
"""marks=[80,78,90,"sheriyans"]
marks[2]="modiji"
print(marks)"""
#Traversing- ham list ke har e;ement par jate hai use dekhte hai or print karwate hai
"""a="sheriyans"
for i in a:
    print(i)
#ye no. main bhi hoskta hai
a=[10,20,30,40,50]
for i in a:
    print(i)"""

#agar kisi keyword ke age dot nahi lagaa to wo function if dot laga hai toh method
##methods in list
#1. .append() this add the value at last of list
"""marks1=[10,20,30,40,50]
marks1.append(90)
print(marks1)"""

#2. .extend()-add (take multiple argumnet)and can insert one list in another
"""marks2=[60,80,90]
marks1.extend(marks2)
marks2.extend(marks1)
print(marks1)"""

#3. .insert(index,value)-take two argumnet
"""marks=[10,20,30,40,50]
marks.insert(3,90)
marks.insert(-1,90)
print(marks)"""
#4. .remove(value)- ye sirf value mangega-works on first occurnece mtlv jompehle aayga value wo hat jyga 
#if value reppet hue toh
"""a=[10,20,30,40,50]
a.remove(10)
print(a)"""
#5. .pop (index)- remove any value on basis of index if index is not given defaltly it is taken last 
"""a=[10,20,30,10,50]
a.pop(3)
print(a)"""
#6. .clear()- removes every element and gives empty list
"""a=[10,20,30,40,50]
a.clear()
print(a)
"""
#7. .del()-remove list from memory-print krte time error show krdega
"""a=[10,20,30,40]
del a
print(a)"""

##shallow copy-.copy ka use nahi hota and change dono main hota hai##
"""a=[1,2,3,4,5]
b=a
b[3]=100
print(a)
print(b)"""
##deep copy-dono change nahi honge##
"""a=[1,2,3,4,5]
b=a.copy()
b[3]=100
print(a)
print(b)
"""
##imp
"""l=[10,20,30,40,50,60,70,80]
for i in l:
    print(i)#use to print individual values
print(len(l))
for i in range(len(l)):
    print(i,l[i])#index and value print karenge
                #index print krne ke lie hamesha range ka use hoga"""

"""l=[10,20,30,40,50,60,70,80]
for i in range(7,-1,-1):#start karenge index no.7 se stop -1 kuki tab wo jakr index value 0 par rukega
    print(l[i])         #ulta print krn hai to -1 lia steps
for i in range(len(l)-1,-1,-1):
    print(l[i])"""
##to print this list in reverse by creating some other list then inserting it inside other
"""l=[10,20,30,40,50,60,70,80]
l2=[]
for i in range(len(l)-1,-1,-1):
    l2.append(l[i])
print(l2)"""
#pehle length 0 then 80 would be printed due to 80 length will become 1 then at index 1 70 will be printed then so on

#another way of reversing by making formula for indexing known as two pointer
#using a,b=b,a 
"""arr =[10,20,30,40,50]
n=len(arr)
mid=n//2 
for i in range(mid):
    arr[i],arr[n-i-1]=arr[n-i-1],arr[i]
print(arr)"""
#hmne swap kia positions ko using indexing

##question
"""arr=[10,-5,20,-3,0,8]
print("positive:")
for elem in arr:
    if elem>0:
        print(elem)

print("negative:")
for elem in arr:
    if elem<0:
        print(elem)"""
##question
"""arr=[10,20,30,40]
n=len(arr)
sum=0
for elem in arr:
    sum=sum+elem
mean=sum/n
print(mean)"""
#question
"""arr=[2,96,69,77,145,20]
max=arr[0]
index=0
for i in range(len(arr)):
    elem=arr[i]
    if elem>max:
        max=elem
        index=i
print(f"max is {max} at index{index}")"""
#question
"""arr=[1,2,4,5]
n=len(arr)
org_n=n+1
org_sum=(org_n)*(org_n +1)//2
real_sum=0
for elem in arr:
    real_sum+=elem
missing=org_sum - real_sum
print(missing)"""
#question- chcek if list is asecding(sorted) or not
"""arr=[10,20,30,40,50]
is_sorted=True
n=len(arr)
for i in range(0,n-1):#indexing 0 is shuru hogy to hame uske hisb se n-1 lena padega
    if arr[i]>arr[i+1]:
        is_sorted=False
        break
if is_sorted:
    print("list is sorted")
else:
    print("list is unsorted")"""
##question- plINDROME
"""arr=[2,3,15,15,3,2]
n=len(arr)
mid=n//2
is_palindrome=0
for i in range(mid):
    if arr[i]!=arr[n-i-1]:
        is_palindrome = False
        break
if is_palindrome:
    print("list is palindrome")
else:
    print("list is not palindrome")"""
##another way using approch of cantecinationusing string but limited to single digit
"""arr=[64,34,25,12,22,11,9]          #buble sort
n=len(arr)
for i in range(n):
    for j in range(n-i-1):
        if arr[j] > arr[j+1]:
         arr[j],arr[j+1]=arr[j+1],arr[j]
print(arr)"""





