#fuction are block of code we use for recurrsion
#how fuction are created
#there are two types of fuc.
##imbuild
"""print()
input()
int()
len()
str()
etc.."""
##user defined fun.- esme 'def' ka use hota hai
#defining a function
"""def hello():
    print("how are you")
##calling a fuction (without closing intendation this will not run)this is called parentissis
hello()"""
#return- yeh value ko calling block main hi return krdete hai and calling block caputres it
"""def hey():
    return "how are you"
a=hey()
print(a)"""

##parameters and arguments

"""def hello(a,b):# you took the parameters here
    print(a+b)

hello(10,20)
hello(50,50)"""#and you have to(call) provide argument here 

##ab upr palindrome main prob yahi aarahi this is ham a b kab tak likhenge or hame to hazaro no. pr usekrna hai
##toh 
"""def palindrome(a):
    rev=0
    copy=a
    while a!=0:
        rev=rev*10+a%10
        a=a//10

    if copy==rev:
        print(copy)

for i in range(1,1000):
    palindrome(i)"""
##ab esme ye hua ki wo no. print hojynge jo plaindrome hai
##kuki palindrome ke andr to argument hai  toh wo sari value parameter main da;denga