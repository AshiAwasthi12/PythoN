# marks=int(input("enter your marks"))
# if marks>=90:
#     print('A')
# elif marks>=75 or marks<=89:
#     print('B')
# elif marks>=60 or marks<=74:
#     print('C')
# elif marks>=40 or marks<=59:
#     print('D')
# else:
#     print('FAIL')
##2
# a=int(input("enter a first no."))
# b=int(input("enter a second no."))
##3
# day=int(input("enter no. in between 1 to 7 "))


operator=input("enter your operator")
if operator=="+":
    print(10+12)
# if day==1:
#     print('monday')
# elif day==2:
#     print('tuesday')
# elif day==3:
#     print('wednesday')
# elif day==4:
#     print('thursday')
# elif day==5:
#     print('friday')
# elif day==6:
#     print('saturday')
# elif day==7:
#     print('sunday')
# else:
    # print('invalid day')
##4
# a=int(input("enter value of a"))
# if a%3==0 and a%5==0:
#     print("yes divisible by both 3 and 5")
# elif a%3==0:
#     print("divisible by 3")
# elif a%5==0:
#     print("divisible by 5")
# elif a%3!=0 or a%5!=0:
#     print("not divisible by either 3 or 5")
##5
# a=int(input("enter value of first side"))
# b=int(input("enter the value of second side"))
# c=int(input("enter the value of third side"))
# if a==b and b==c:
#     print("Equilateral")
# elif a==b:
#     print("Isosceles")
# elif a!=b and b!=c:
#     print("Scalene")
##6
# amount=int(input("enter the shopping amount"))
# if amount<500:
#     print(f" final amount{amount+50}")
# if amount>=500 and amount<=999:
#     print(f"final amount{amount+30}")
# if amount>=1000:
#     print("it is free")
##7
# time=int(input("enter the timing")) 
# if time>5 and time<11:
#     print("Morning")
# elif time>12 and time<16:
#     print("Afternoon")
# elif time>17 and time<20:
#     print("Evening")
# elif( time>21 and time<=23) or (time>=0 and time<4):
#     print("Night")
# else:
#     print("Invalid hour")
##8
# unit=int(input("total units consumed"))
# if unit>=0 and unit<=100:
#     print(f"electricity bill is{unit*5}")
# elif unit>=101 and unit<=200:
#     print(f"electricity bill is{unit*7}")
# elif unit>200:
#     print(f"electricity bill is{unit*10}")
##9
# age=int(input("age of passenger is"))
# if age<5:
#     print("ticket is free")
# elif age<18:
#     print("ticket price is 100")
# elif age<60:
#     print("ticket price is 200")
# elif age>=60:
#     print("ticket price is140")
##10
# attendence=int(input("enter your attendence percentage"))
# marks=int(input("enter your marks"))
# if attendence>=75 and marks>=40:
#     print("Eligible")
# else:
#     print("not eligible")