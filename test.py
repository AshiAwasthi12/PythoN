##1
# n=int(input("enter the value of n"))
# count=0
# for i in range(2,n+1):
#     for j in range(2,i+1):
#         if n%j==0:
#             count+=1
#         if count==2:
#     print(j)
            


##2
# n=int(input("enter the value of n"))
# sum=0
# temp=n

# while n>0:
#     digit=n%10
#     fact=1
#     for i in range(1,digit+1):
#         fact=fact*i
#     n=n//10
#     sum=sum+fact
# if temp==sum:
#     print(f"it is strong no.")
# else:
#     print(f"it is not a strong no.")
##3
# n=int(input("enter the value of n"))
# temp=n
# l=len(str(n))
# sum=0
# while n>0:
#     digit=n%10
#     sum=sum+digit**l
#     n//10
# if temp==sum:
#     print("it is armstrong no.")
# else:
#     print("it is not a armstrong no.")
##4
# n=int(input("enter the value of n"))
# temp=n
# rev=0
# while n>0:
#     digit=n%10
#     rev=rev*10+digit
#     n=n//10
# if temp==rev:
#     print("it is palindrome")
# else:
#     print("it is not palindrome")
##
