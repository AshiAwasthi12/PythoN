

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
"""n=int(input("entre the value of n"))
temp=n
sum=0
while n>0:
    digit=n%10 
    fact=1
    for i in range(1,digit+1):
        fact*=i
    sum +=fact
    n=n//10
if sum==temp:
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

## 5 fibonaci series up to N terms
"""n=int(input("enter the value of n"))
a=0
b=1
for i in range(n):
    print(a)
    c=a+b
    a=b
    b=c
"""
## 6 count vowel in string
#itrate  on input
"""text=input("enter the text")
count=0
for ch in text:
    if ch in "aeiouAEIOU":
        count+=1
print(f"total vowel:{count}")"""
## 7  count occurrences of a character in a string
"""text=input("enter the string")
target=input("enter a character")
count=0
for ch in text:
    if ch==target:
        count+=1
print(count)"""
##8
"""

def number_ending_with_7(n):
    result=[]
    for i in range(1,n+1):
        if i%10==7:
            result.append(i)
    return result

n=int(input("enter the number")) #40
print(number_ending_with_7(n))
m=int(input("enter the number")) #20
print(number_ending_with_7(m))"""


# Q. Digit Frequency

# Take an integer N as input and count how many times
# each digit from 0 to 9 occurs in the number.
#
# Example:
# Input: 122333
#
# Output:
# 1 -> 1
# 2 -> 2
# 3 -> 3

"""n = int(input("enter the number"))

for digit in range(0,10):
    temp = n
    count_digit =0
    
    while temp > 0:
        last_digit = temp%10
        if last_digit == digit:
            count_digit +=1
        temp //=10
    if count_digit >0:
        print(f"{digit} -> {count_digit}")"""


# Q Find the Smallest Digit in a Number
#
# Take an integer N as input
# and find the smallest digit present in it.
#
# Example:
# Input: 64825
# Output: 2

"""n = int(input("enter the number"))
temp = n
smallest = 9
while temp >0:
    digit = temp%10
    if digit < smallest:
        smallest = digit
    temp//=10
print(f"chota digit in {n} is {smallest}")"""

##ATM machine simulation
"""user ki attempt ke andr pin check krna hai
user se pin chcek krna hai in limits-> pin real==pin_input
1st time and 2nd time->pin is incorrect->chance dena hai
3rd time->incorrect->card blocked
1st and 2nd and 3rd ->correct-> main menu and chance stop
main menu(we have 1,2,3,4 options)
balance=5000+1000-2000
"""
#input should be taken when user have left out attempt
"""attempt=3
has_access_mainmenu = False
#this logic is for checking wheater user h
while attempt>0:
    entered_pin = int(input("enter the value of pin"))
    if entered_pin == 1234:
        #main menu openes
        has_access_mainmenu = True
        break

    else:
        attempt-=1
        if attempt>0:
            print(f"incorrect pin! you have{attempt} attempts remaining")
        else:
            print("card blocked")
balance=5000
if has_access_mainmenu == True:
    while True:
        print("ATM Menu")
        print("1 -> check balance")
        print("2 -> deposite cash")
        print("3 -> withdraw cash")
        print("4 -> exit")

        choice=int(input("enter the choice"))
        if choice ==1:
            print(f"balance is {balance} only")
        elif choice ==2:
            deposite_amount= int(input("enter the amount to deposite"))
            if deposite_amount >0:
                balance += deposite_amount
                print(f"updated balance is {balance}")
            else:
                print("invalid deposite amount")
        elif choice ==3:
            withdraw_amount = int(input("enter the amount to withdraw"))
            if withdraw_amount <= balance:
                balance-=withdraw_amount
                print(f"withdraw done and updated balance is {balance}")
            else:
                print("insufficient balance")
        elif choice == 4:
            print("thankyou for using our atm")
            break
        else:
            print("invalid choice! please enter number from 1-4")"""



"""
# Print List Elements in Reverse Order
#
# Reverse the list using the two-pointer approach.
#
# Example:
# Input: [10, 20, 30, 40, 50]
# Output: [50, 40, 30, 20, 10]
"""

# arr = [10, 20, 30, 40, 50]
# n = len(arr)
# mid = n//2
# for i in range(mid):
#     arr[i] , arr[n-i-1] = arr[n-i-1] ,arr[i]

"""
# Print Positive and Negative Elements of a List
#
# Print positive and negative elements separately.
# Ignore zero.
#
# Example:
# Input: [10, -5, 20, -3, 0, 8][10, -5, 20, -3, 0, 8]
# Output:
# Positive: 10 20 8
# Negative: -5 -3
"""
# arr = [10, -5, 20, -3, 0, 8]

# print("positive:")
# for elem in arr:
#     if elem>0:
#         print(elem)
        
# print("negative: ")
# for elem in arr:
#     if elem<0:
#         print(elem)
        
"""
# Mean of List Elements
#
# Calculate the average of all elements in a list.
#
# Example:
# Input: [10, 20, 30, 40]
# Output: Mean = 25.0
"""


# list = [10, 20, 30, 40]
# n = len(list)
# sum =0
# for elem in list:
#     sum+=elem
# print(f"mean is {sum/n}")
    
"""
# Find the Greatest Element and Its Index
#
# Find the greatest element and 
# print its index.
#
# Example:
# Input: [2, 96, 69, 77, 145, 20]
# Output: Max element = 145 
# found at 4 index
"""
# arr =[2, 96, 69, 77, 145, 20]
# max = arr[0]
# index =0
# for i in range(1,len(arr)):
#     elem = arr[i]
#     if elem > max:
#         max = elem
#         index = i
    
# print(f"max is {max} at index {index}")
"""
# Find the Smallest Element and Its Index
#
# Find the smallest element and print its index.
#
# Example:
# Input: [2, 96, 69, 77, 145, 20]
# Output: Min element = 2 found at 0 index
"""
# arr=[2,96,69,77,145,20]
# greatest=0
# for i in arr:
#     if i>greatest:
#         greatest=i
# smallest=greatest
# for i in arr:
#     if i<smallest:
#         smallest=i
# print(smallest)

# Sum of List Elements
#
# Accept N elements and print their sum in the given format.
#
# Example:
# Input: [10, 20, 30]
# Output: 10 + 20 + 30 = 60
 
#frequency
"""a=[1,2,3,4,5,5,5,5,6,6,6,7,7,7]
d={}
for i in a:
    if i in d.keys():
        d[i]+=1
    else:
        d[i]=1
print(d)
"""
# Find the Second Greatest Element
#
# Find the second-greatest distinct element.
#
# Example:
# Input: [2, 96, 69, 77, 145, 20]
# Output: Second greatest element = 96
"""arr=[2,96,69,77,145,20]
def secondgreatest(arr):
    greatest=0
    for i in arr:
        if i >greatest:
            greatest=i
    arr.remove(greatest)
    sgreatest=0
    for i in arr:
        if i >sgreatest:
            sgreatest=i
    print(sgreatest)
secondgreatest(arr)"""

"""arr=[2,96,69,77,145,20]
greatest=0
sgratest=0
for i in arr:
    if i>greatest:
        sgratest=greatest
        greatest=i
    elif i>sgratest:
        sgratest=i
print(sgratest)"""

"""largest=float("-inf")
n=int(input("enter the value of n"))
for i in range(1,n):
    a=int(input("enter the value of a"))
    
if n>largest:
    n=largest
print(f"{largest}")"""

# Check Whether a List Is Sorted
#
# Check if the list is sorted in ascending order.
#
# Example:
# Input: [10, 20, 30, 40, 50]
# Output: List is Sorted
"""arr=[10,20,30,40,50]
n=len(arr)
is_sorted=True
for i in range(n-1):
    if n[i]>n[i+1]:
        is_sorted=False
        break
if is_sorted==False:
    print("is not sorted")
else:
    print("is sorted")"""

# Palindromic List
#
# Check whether the list reads the same forwards and backwards.
#
# Example:
# Input: [2, 3, 15, 15, 3, 2]
# Output: Palindromic List
"""arr=[2,3,15,15,3,2]
temp=arr.copy()
n=len(arr)
mid=n//2
for i in range(mid):
    temp[i],temp[n-i-1]=temp[n-i-1],temp[i]
if temp==arr:
    print("is palindrome")
else:
    print("is not palindrome")"""

#frequency
# a=[1,2,3,4,5,5,5,5,6,6,6,7,7,7]
# d={}
# for i in a:
#     if i in d.keys():
#         d[i]+=1
#     else:
#         d[i]=1
# print(d)
# . Print All Numbers Ending with 7 from 1 to N
#
# Take an integer N as input and 
# print all numbers from 1 to N that end with the digit 7.
#
# Example:
# Input: 40
# Output:
# 7 17 27 37

# Q9. Check Harshad (Niven) Number

# Take an integer N as input and 
# check whether it is a Harshad Number.
# A Harshad number is a number 
# that is completely divisible by the sum of its digits.
#
# Example 1:
# Input: 18  -> Sum of digits: 1 + 8 = 9 -> 18 % 9 == 0
# Output: Harshad Number
#
# Example 2:
# Input: 14  -> Sum of digits: 1 + 4 = 5 -> 14 % 5 != 0
# Output: Not a Harshad Number
"""
n = int(input("enter the number"))
temp = n
sum =0
while n >0:
    digit = n %10
    sum +=digit  
    n = n //10
if sum > 0  and temp % sum == 0:
    print("harshad number")
else:
    print("NOt a harshad number")

#!!PATTERN PRINTING!!#
#outer loop controls which row 
#and inner loop control how many stars in it 
"""
# Example (N = 5):
# * * * * * 
# * * * * * 
# * * * * * 
# * * * * * 
# * * * * * 
"""
"******"
# for i in range(5):
#     for j in range(5):
#       print("*",end="")
#     print()
"""
# Example (N = 5):
# * 
# * * 
# * * * 
# * * * * 
# * * * * * 
"""
# N =5
# for i in range(1,N+1):
#     for j in range(1,i+1):
#         print("*",end="")
#     print()

"""
# Example (N = 5):
# * * * * * 
# * * * * 
# * * * 
# * * 
# * 
"""
# N= 5
# for i in range(N ,0 ,-1):
#     for j in range(i):
#         print("*",end="")
#     print()
#**
# N =5
# for i in range(1,N+1):
#     for j in range(1,N-i+1+1):
#         print("*",end="")
#     print()
#**
# n=int(input("enter n"))
# for i in range(n):
#     for j in range(n-i):
#         print("*",end="")
#     print()

"""
# Example (N =5):
# _____*****
# _____*****
# _____*****
# _____*****
# _____*****
"""

# N =5
# for i in range(1,N+1):
#     for j in range(1,N+1):
#         print(" " ,end="")
#     for k in range(1,N+1):
#         print("*" , end="")
#     print()

"""
# # Example (N =5):
# _*****
# __*****
# ___*****
# ____*****
# _____*****
# """
# N =5
# for i in range(1,N+1):
#     for j in range(1,i+1):
#         print(" " ,end="")
#     for k in range(1,N+1):
#         print("*" , end="")
#     print()

"""
# Example (N =5):
     *****
    *****
   *****
  *****
 *****
"""
# N =5
# for i in range(1,N+1):
#     for j in range(1,N-i+1+1):
#         print(" " ,end="")
#     for k in range(1,N+1):
#         print("*" , end="")
#     print()
#*
# n=5
# for i in range(n,0,-1):
#     for j in range(i):
#         print(" ",end="")
#     for k in range(n,0,-1):
#         print("*",end="")
#     print()

"""
# Example (N =5):
 *****
  *****
   *****
    *****
     *****
    *****
   *****
  *****
 *****
"""

# N = 5

# for i in range(N):
#     for j in range(i):
#         print(" ", end="")
#     for j in range(N):
#         print("*", end="")
#     print()

# for i in range(N - 2, -1, -1):
#     for j in range(i):
#         print(" ", end="")
#     for j in range(N):
#         print("*", end="")
#     print()

"""
# Example (N = 5):
#         * 
#       * * 
#     * * * 
#   * * * * 
# * * * * * 
"""
# N =5
# for i in range(1,N+1):
#     for j in range(1,N-i+1+1):
#         print(" " ,end="")
#     for k in range(1,i+1):
#         print("*" , end="")
#     print()









"""
# Example (N = 5):
# *****
#  ****
#   ***
#    **
#     *
"""



 
"""
Example (N = 5):
*****
 ****
  ***
   **
    *   
   ** 
  *** 
 **** 
***** 
"""














"""
# Example (N = 5):
#     *
#    ***
#   *****
#  *******
# *********
"""




"""
# Example (N = 5):
# *********
#  *******
#   *****
#    ***
#     *
"""


"""
#    *
#   ***
#  *****
# *******
#  *****
#   ***
#    *
"""

"""
# Example (N = 4):
# *      *
# **    **
# ***  ***
# ********
# ********
# ***  ***
# **    **
# *      *
"""

# N =5
# for i in range(1,N+1):
#     for j in range(1,i+1):
#         print("*" ,end="")
#     for k in range(1,2*N -2*i +1):
#         print(" " , end="")
#     for l in range(1,i+1):
#         print("*",end="")
#     print()

# for i in range(1,N+1):
#     for j in range(1,N-i+1+1):
#         print("*" ,end="")
#     for k in range(1,2*i -2 +1):
#         print(" " , end="")
#     for l in range(1,N-i+1+1):
#         print("*",end="")
#     print()

"""
# Example (N = 5):
# 1 
# 1 2 
# 1 2 3 
# 1 2 3 4 
# 1 2 3 4 5 
"""
# N =5
# for i in range(1 , N+1):
#     for j in range(1,i+1):
#         print(j,end=" ")
#     print()

"""
# Example (N = 5):
# 1 
# 2 2 
# 3 3 3 
# 4 4 4 4 
# 5 5 5 5 5 
"""

# N =5
# for i in range(1 , N+1):
#     for j in range(1,i+1):
#         print(i,end=" ")
#     print()

"""
# Example (N = 4):
# 1 
# 2 3 
# 4 5 6 
# 7 8 9 10 
#11 12 13 14 15
"""
# N =5
# num = 1
# for i in range(1 , N+1):
#     for j in range(1,i+1):
#         print(num,end=" ")
#         num +=1
#     print()
"""
# write a function of this code and return me list
# return 
# list [] 
# append 

def numbers_ending_with_7(n):
    result = []
    for i in range(1,n+1):
        if i%10==7:
            result.append(i)
    return result

n = int(input("enter the number")) #40
ans1 =numbers_ending_with_7(n)
m = int(input("enter the number"))  #20
ans2 = numbers_ending_with_7(m)
print(f" fist ans : {ans1}  , second ans : {ans2}")
    
"""
#finding missing no.
"""arr=[2,3,5,6]
n=len(arr)
og=n+1
ogs=0
for i in range(2,og+2):
    ogs=ogs+i
ogr=0
for elem in arr:
    ogr=ogr+elem
missing=ogs-ogr
print(missing)"""

"""arr=[1,2,4,5]
n=len(arr)
og=n+1
ogs=0
for i in range(1,og+1):
    ogs+=i
ogr=0
for elem in arr:
    ogr+=elem
missing=ogs-ogr
print(missing)"""
##*
"""
# Find the Pair with the Given Sum
#
# Find all pairs of elements whose sum equals a given target.
#
# Example:
# Input: [2, 4, 3, 5, 7, 8]
# Target: 10
#
# Output:
# (2, 8)
# (3, 7)

arr = [2, 4, 3, 5, 7, 8]
target = 10
n = len(arr) #6
for i in range(n):
    for j in range(i+1, n):
        if (arr[i] + arr [j]) == target:
            print(arr[i],arr[j])
"""
##*
"""
Question: Rotate a List to the Right by K Positions

Write a Python program to rotate a list to the right by K positions
using a loop.

Example:
Input:
arr = [1, 2, 3, 4, 5]
k = 2

Output:
[4, 5, 1, 2, 3]
"""
# arr=[1,2,3,4,5]
# n=len(arr)
# k=4
# for i in range(k):
#     last=arr.pop()
#     arr.insert(0,last)
# print(arr)


# """
# Question: Check Whether a List Is a Sublist of Another List

# Write a Python program to check whether all elements of one list
# appear consecutively in another list.

# Example:
# Input:
# arr = [10, 20, 30, 40, 50]
# sub = [20, 30, 40]

# Output:
# Sublist Found
# """
# arr =[10, 20, 30, 40, 50]
# n = len(arr) #5
# sub =[20, 30, 40]
# m = len(sub)#3
# for i in range(0,n-m+1):
#     if arr[i:i+m] == sub:
#         print("sublist found")
#         break
# else:
#     print("not sublist found")

# """
# Question: Find Duplicate Words in a Sentence

# Find all words that appear more than once.
# Ignore uppercase and lowercase differences.

# Input:
# "Python is easy and python is powerful and easy"

# Output:
# ['python', 'is', 'easy', 'and']
# """


# sentence = "Python is easy and python is powerful and easy"

# sentence = sentence.lower()
# words = sentence.split()

# duplicates = []
# checked = []

# for word in words:
#     if word in checked:
#         continue

#     count = 0

#     for w in words:
#         if w == word:
#             count += 1

#     if count > 1:
#         duplicates.append(word)

#     checked.append(word)

# print(duplicates)

# sen = "Python.is.easY.and.python.is.powerfuL.and.Easy"
# sen = sen.lower()
# # print(sen)
# words = [] 
# words = sen.split(" ")   #USE OF SPLIT-> it breaks a sentence
# #into individual words using whitespace by default
# word =""

# for ch in sen:
#     if ch!=".":
#         word+=ch
#     else:
#         words.append(word)
#         word =""
# words.append(word)
# print(words)

# # ['python', 'is', 'easy', 'and', 'python', 'is', 'powerful', 'and' ,'easy]
# dup = []

# for i in range(len(words)):
#     count =0
#     for j in range(len(words)):
#         if words[i] == words[j]:
#             count +=1
#     if count>=2 and words[i] not in dup:
#         dup.append(words[i])
# print(dup)

"""question:group words of a sentance by their length"""

#eat sleep code and repeat code and eat clean
##*SPLIT*##
#we will convert string into list of words
"""sen="Eat sleep code and repeat code and eat clean"
sen=sen.lower()
ans={ }
words=sen.split(" ")
words=list(set(words))  #this is double conversion for removing duplicate
#since set does not contain any duplicate 
for word1 in words:
    l=len(word1)
    temp=[]
    for word2 in words:
        if len(word2)==1:
            temp.append(word2)
    ans[l]=temp
print(ans)"""

"""sen="Eat sleep code and repeat code and eat clean"
res=""
for ch in sen:
    if 'A'<=ch<='Z':
        res+=chr(ord(ch)+32)
    else:
        res+=ch
print(res)"""

"""sen="Eat sleep code and repeat code and eat clean"
res=""
for ch in sen:
    if ord('a')<=ord(ch)<=ord('z'):
        res+=chr(ord(ch)-32)
    else:
        res+=ch
print(res)"""
# ans = {}
# words = sen.split(" ")
# for word1  in words:
#     l = len(word1)
#     temp = []
#     for word2 in words:
#         if  len(word2) == l and word2 not in temp:
#             temp.append(word2)
#     ans[l] = temp
# print(ans)


   
