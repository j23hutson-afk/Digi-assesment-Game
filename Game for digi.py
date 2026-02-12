#functions
def cls(): print ("\n" * 100)

#vairables
main_loop = True

wood=0
stone=0

#start here
cls()
name=input(str('What is your name? \n'))

while main_loop == True:
    choice=input(str('What would you like to do? \n1.Chop wood \nMine stone\n'))
    if choice==1:
        wood+=1
        print(wood)