# """on word slicing"""
# # word=input()
# # n=len(word)
# # if n%2==0:
# #     print(word[(n//2)-1])
# # else:
# #     print(word[n//2])
# ##
# # string=input()
# # n=len(string)
# # if n>=4:
# #     print(string[0:4:1])
# # else:
# #     print(string)

# """lower upper case"""
# # def countUpperLower(s):
# #     # Write your code here
# #     upper=0
# #     lower=0

# #     for ch in s:
# #         if 'A'<= ch <='Z':
# #             upper+=1
# #         elif 'a'<= ch <='z':
# #             lower+=1
# #     return upper ,lower


# # def countUpperLower():
# #     # Write your code here
# #     word=input()
# #     uppercase=0
# #     lowercase=0
# #     for ch in word:
# #         if ch.isupper():
# #             uppercase+=1
# #         else:
# #             uppercase=0
# #         if ch.islower():
# #             lowercase+=1
# #         else:
# #             lowercase=0
# #     print(f"First line:{uppercase}")
# #     print(f"Second line:{lowercase}")
# # countUpperLower()

# """even odd"""
# # def countEvenOddDigits():
# #     # Write your code here
# #     n=int(input("enter value of n"))
# #     odd=0
# #     even=0
# #     while n!=0:
# #         digit=n%10
# #         if digit%2==0:
# #             even+=1
# #         else:
# #             odd+=1
# #         n//=10
# #     print(f"{even}")
# #     print(f"{odd}")
# # countEvenOddDigits()
# ##
# # def countEvenOddDigits(n):
# #     # Write your code here
# #     n=abs(n)  #abs()-> coverts negative n into positive

# #     if n==0:
# #         return 1,0

# #     odd=0
# #     even=0
# #     while n>0:
# #         digit=n%10
# #         if digit % 2 ==0:
# #             even+=1
# #         else:
# #             odd+=1
# #         n//=10
# #     return even , odd
# """palindrome"""
# # a, b = map(int, input().split())
# # input() reads the entire input.
# # .split() separates the values wherever there is a space.
# # map(int, ...) converts both values into integers.
# # start, end stores the two values separatel
# # for i in range(a,b+1):
# #     temp=i                               
# #     palindrome=0
# #     while i>0:
# #         digit=i%10
# #         palindrome=palindrome*10+digit
# #         i//=10
# #     if palindrome==temp:
# #         print(palindrome , end=" ")  #is type se end lagagoge to
# #                                     # ek hi line main spaces se ye print hojynge

# """reversing a string loop , slicing,built in functions"""



# """printing number that have only three factors----> a no. have only three factor if and
#                                                       only if it is square of prime no. """
# # found=False
# # n=int(input("enter"))
# # for i in range(2,n+1):
# #         if i*i>n:
# #             break
# #         is_prime=True
# #         for j in range(2,i):
# #             if i%j==0:
# #                 is_prime=False
# #         if is_prime:
# #             print(i*i,end=",")
# #             found=True      ##this gives error kuki usko list ke form main chahiye
# ##
# # def exactlyThreeFactors(n):
# #     result=[]
# #     for i in range(2,n+1):
# #         if i*i>n:
# #             break
# #         is_prime=True
# #         for j in range(2,i):
# #             if i%j==0:
# #                 is_prime=False
# #         if is_prime:
# #             result.append(i*i)
# #     return result

# """all factors in asecdign order"""
# # def findFactors(n):
# #     result=[]
# #     for i in range(1,n+1):
# #         if n%i==0:
# #             result.append(i)
# #     return result

# """factors of number in range"""
# # def factorsInRange(l, r):
# #     ans=[]
# #     for i in range(l,r+1):
# #         factors=[]
# #         for j in range(1,i+1):
# #             if i%j==0:
# #                 factors.append(j)
# #         ans.append((i,factors))
# #     return ans

# # n=int(input("enter the value of n"))
# # sum=0
# # temp=n
# # while n>0:
# #     digit=n%10
# #     fact=1
# #     for i in range(1,digit+1):
# #         fact*=i
# #     sum+=fact
# #     n//=10
# # if sum==temp:
# #     print('perfect')
# # else:
# #     print('not')
# """prime numbers"""
# # start,end=map(int,input().split())
# # found=False 
# # for num in range(start,end+1):
# #     if num>1:
# #         for i in range(2,int(num**0.5)+1):
# #             if num%i==0:
# #                 break
# #         else:
# #             print(num,end=" ")
# #             found=True
    
# # if not found:
# #     print("No prime number")
# """even and odd"""
# # n=int(input("enter number"))
# # n=abs(n)
# # if n==0:
# #     print(1,0)
# # odd=0
# # even=0
# # while n>0:
# #     digit=n%10
# #     if digit%2==0:
# #         even+=1
# #     else:
# #         odd+=1
# #     n//=10
# # print(f"{even},{odd}")
# a='akshat'
# sum=''
# for i in a:
#     sum=i+sum
# print(sum)
# n=int(input("enter number"))
# result=[]
# for i in range(2,n+1):
#     if i*i>n:
#         break
#     is_prime=True
#     for j in range(2,i):
#         if i%j==0:
#             is_prime=False
#     if is_prime:
#         result.append(i*i)
# print(result)



# m=int(input("enter value of m"))
# n=int(input("enter the value of n"))
# for i in range(m,n+1):
#     count=0
#     for j in range(1,i+1):
#         if i%j==0:
#             count+=1
#     if count==3:
#         print(i)def factorsInRange(l, r):
    # ans=[]
    # for i in range(l,r+1):
    #     factors=[]
    #     for j in range(1,i+1):
    #         if i%j==0:
    #             factors.append(j)
    #     ans.append((i,factors))
    # return ans
