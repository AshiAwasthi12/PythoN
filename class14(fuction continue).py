##default parameter
#there are value you can assign to parameter that are set as default if you aasign argument it will take it 
#and if you do not it will take default value
#you should always use default parameter before general parameter
'''def hello(a,b,c,d,e=30):
    print(a+b)'''
#here e is defalt parameter
'''hello(50,50,30,20)'''

#default argument
"""
def information(name,age,number):
    print("hello your info is")
    print(name)
    print(age)
    print(number)

information(number=67876435,name="harsh,age=25")
information()"""
##this too flows same defaulth argument should not come before positional argument
##yaha number name likhna padha hai

#print number
#  from 1 t0 30
#without using for while and print more than omce
#here come recurssion it is default till 1000
"""def numbers(n):
    if n==30:
        return
    print(n)
    numbers(n+1)

numbers(1)"""

#backtrekking and stack
#when you are calling a function inside other one and one failed to execute  those which does not 
#excecute goes inside stack
# stack-last in first out
"""def hello1():
    hello2()
    print("hello1")

def hello2():
    hello3()
    print("hello2")

def hello3():
    hello4()
    print("hello3")

def hello4():
    print("hello4")

hello1()"""

# this will first print hello4 and then reverse

