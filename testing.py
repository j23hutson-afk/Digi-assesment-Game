"""
print("Hello World!")
#print means to say something
print(7+3)
print("7+3=",7+3)
#dont give commors for math proplems

num=7+3
print(num)
print(num+num)

num1=int(input("give me a number ")) #int is only for numbers
print(num1)

name=str(input("teel me your name ")) #str mean any charcters or symbols
print(name)


animals=str(input("give me an animal "))
leg=int(input("how many legs does it have "))
print(f"{animals} has {leg} legs")
#f before "" to show that varibles are in this part
#use {} to show that what is inside is a varible rember to have f
numanimals=int(input("how many animals do you have "))
totallegs=(numanimals * leg)
#use * for multiplecation
print(f"you have {numanimals} amount of {animals} which means the total legs is {totallegs}")

num1=int(input("please give me a number"))
num2=int(input("please give me a scond number"))

sum=num1+num2
print(f"{num1} + {num2} = {sum}")
multi=num1*num2
print(f"{num1} times {num2} is {multi}")

sub=num1-num2
print(f"{num1} - {num2} = {sub}")

div=num1/num2
print(f"{num1} divided by {num2} is {div}")
"""

ans=int(input("please enter a a number less than 10\n "))
#\n is new line
if ans<10:
    print("well done")
else:
    print("you IDIOT thats MORE than 10")
