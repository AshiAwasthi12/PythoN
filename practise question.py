##1
"""n=int(input("enter the number"))
count=0
for i in range(1,n+1):
    if i%3==0 and i%5==0:
        count+=1
print(f"count:{count}")"""

##2
"""n=int(input("enter the value of n"))
fact=1
for i in range(1,n+1):
    fact=fact*i
print(f"{n}! is {fact}")"""

##3(strong no.are no.s addition of factorial of whose digits give no. itself)
""" n=int(input("entre the value of n"))
temp=n
sum=0
while n>0:
    digit=n%10
    fact=1
    for i in range(1,digit+1):
        fact*=i
    sum +=fact
    n=n//10
if n==temp:
    print("strong number")
else:
    print("not a strongnumber") """
##4
"""
n=int(input("entr the value of n"))
sum=0
for i in range(1,n+1):
    if i%2!=0:
        sum+=i
print(f"sum of odd no. from 1 to{n}is {sum}")"""

"""
n=int(input("enter the value of n"))
temp=n
sum=0
while n>0:
    digit=n%10

    fact=1
    for i in range(1,digit+1):#5 
        fact=fact*i 
    sum=sum+fact
    n=n//10
print(f"{sum}")
if temp==sum:
    print(f"{temp} is strong number")
else:
    print(f"{temp} is not a strong number")"""

#sum of odd no. from 0 to n
"""n=int(input("enter the value of n"))
sum=0
for i in range(1,n+1):
    if i%2!=0:
        sum+=i
print(f"{sum} is sum of odd no. from 1 to n")"""
#
"""n=int(input("enter the value of n"))
a=0
b=1
for i in range(n):
    print(a,end=" ")
    c=a+b
    a=b
    b=c
n=int(input("enter the value of n"))
a=0
b=1
for i in range(n):
    print(a,end=" ")
    c=a+b
    a=b
    b=c"""
##
"""text=input("enter the word")
count=0
for ch in text:
    if ch in "aeiouAEIOU":
        count+=1
print(f" there are {count} vowels in {text}")"""

##
"""text=input("enter the word")
target=input("enter the character")
count=0
for ch in text:
    if ch==target:
        count+=1
print(f" {target} is occured {count} times in {text}")"""
##
"""text=input("enter your text")
target=input("enter the character")
count=0
for ch in text:
    if ch==target:
        count+=1
print(f"{count} time {target} appers in {text}")"""
##
"""n=int(input("enter your number"))
for i in range(1,n+1):
    if i%10==7:
     print(i)"""
##
""" 
n=int(input("enter the value of number"))
temp=n
sum=0
while n>0:
    digit=n%10
    sum+=digit
    n=n//10
if sum>0 and temp%sum==0:
    print("it is a harshad no.")
else:
    print("it is not a harshad no.")
n=int(input("enter the value of n))
temp=n
sum=0
while>0:
    digit=n%10
    sum+=digit
    n=n//10
if sum>0 and temp%sum==0:
    print("harshad no.")
else:
     print("no) """
##



