# # ##1
# """n=int(input("enter the value of n"))
#  count=0
#  for i in range(1,n+1):
#      if i%3==0:
#          count+=1
#  print(f"{count}")"""
# # ##2

# # n=int(input("enter the value of n"))
# # for i in range(1,n):
# #     a=int(input("enter the value of a"))
    
# # if n>largest:4
# #     n=largest
# # print(f"{largest}") 
# """greatest no."""
# # n=int(input("number of input"))
# # greatest=0
# # for i in range(n):
# #     a=int(input("enter the number"))

# #     if a>greatest:
# #         greatest=a
# # print(greatest) 
# ##3
# """
# n=int(input("enter value of n"))
# sum=0
# for i in range(n+1):
#     a=int(input("enter the value of a"))
#     sum+=a
# print(sum/n)"""
# ##4

# # n=int(input("enter the value of n"))
# # temp=n
# # sum=0
# # for i in range(n+1):
# #     if i%n==0:
# #         sum+=i
# # if temp==sum:
# #     print("perfect number")

# # n=int(input("enter the value of n"))
# # temp=n
# # sum=0
# # for i in range(n+1):
# #     if i%n==0:
# #         sum+=i
# # if temp==sum:
# #     print("perfect number")

# # n=int(input("enter the value of n"))
# # temp=n
# # sum=0
# # for i in range(n+1):
# #     if i%n==0:
# #         sum+=i
# # if temp==sum:
# #     print("perfcet number")

# # n=int(input("enter the value of n"))
# # temp=n
# # sum=0
# # for i in range(n+1):
# #     if i%n==0:
# #         sum+=i
# # if temp==sum:
# #     print("perfect number")

# # n=int(input("enter the value of n"))
# # temp=n
# # sum=0
# # for i in range(n+1):
# #     if i%n==0:
# #         sum+=i
# # if temp==sum:
# #     print("it is perfect number")
# ##5
# # n=int(input("enter the value of n"))
# # for i in range(1,n+1):
# #     if i%10==0:
# #         print(i)
# ##questions on while loop
# # n=int(12345)

# # rev=0
# # while n>0:
# #     last=n%10
# #     rev=rev*10+last
# #     n//=10

# # print(rev)

# # n=int(12345)
# # while n>0:
# #     last=n%10
# #     rev=rev*10+last
# #     n//=10
# # print(rev)

# # n=int(12345)
# # while n>0:
# #     last=n%10
# #     rev=rev*10+last
# #     n//=10
# # print(rev)
# # n=int(12345)
# # rev=0
# # while n>0:
# #     last=n%10
# #     rev=rev*10+last
# #     n//=10
# # print(rev)
# # n=int(12345)
# # rev=0
# # while n>0:
# #     last=n%10
# #     rev=rev*10+last
# #     n//=10
# # print(rev)

# # n=int(121)
# # temp=n
# # rev=0
# # while n>0:
# #     last=n%10
# #     rev=rev*10+last
# #     n//=10
# # if rev==temp:
# #     print("it is palindrome")
# # else:
# #     print("it is not palindrome")
# # n=int(123)
# # temp=n
# # rev=0
# # while n>0:
# #     last=n%10
# #     rev=rev*10+last
# #     n//=10
# # if rev==temp:
# #     print("it is palindrome")
# # else:
# #     print("it is not plindrome")

# ##weekly attendence analysis
# n=int(input("enter your no."))
# present=0
# absent=0
# for i in range(n):
#     a=int(input("enter your status"))
#     if a=="P":
#         present+=1
#     else :
#         absent+=1
# print(f"you are present{present} days and you are absent {absent} days")

##greatest value 
# largest=float("-inf")   # -infinty #12  #24
# for i in range(5):  #0,1,2,3,4
#     num=int(input("enter your num : "))
#     if num >largest :  
#         largest=num
# print(largest)

##finding largest using function

# n=int(input("enter your range"))
# def largestsum(n):
#     largest=float("-inf")
#     for i in range(n):
#         num=int(input(f"enter the value {i}:"))
#         if num>largest:
#             largest=num
#     print(largest)
# largestsum(n)
##product quality inspection
# n=int(input("enter the value of n"))
# passes=0
# fail=0
# for i in range(n):
#     status=int(input("enter your status"))
#     if status==1:
# #         passes+=1
# #     else:
# #         fail+=1
# # print(f"{passes} passed the inspection and {fail} failed the inspection")

##monthly saving analysis
# n=int(input("enter the no. of days"))
# saving=0
# amt=0
# for i in range(n):
#     amount=int(input("enter the amount of savings"))
#     if amount>500:
#         saving+=1
#     amt+=amount
# print(f"total saving are {amt} and days when saving were greater than 500 are{saving}")

##electricity consumption
# n=int(input("enter no. of days"))
# units=0
# Gunit=0
# for i in range(n):
#     consumption=int(input("enter units cosnsumed per day"))
#     if consumption>10:
#         Gunit+=1
#     units+=consumption
# print(f"{units} unit electricity is consumed in {n} days and {Gunit} days units were greater then 10")

##Attendence eligibility
# n=int(input("enter the no. of classes"))
# present=0
# absent=0
# for i in range(n):
#     attendance=input("enter your status")
#     if attendance=="P":
#         present+=1
#     else:
#         absent+=1
# percentage=(present/n)*100
# if percentage>=75:
#     print("greater than 75%")
# print(f"student attendance percentage is{percentage}")


    



