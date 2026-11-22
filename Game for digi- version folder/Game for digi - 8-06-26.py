#modules
import color

#functions
def cls():
    print ("\n" * 100)

def invalid(): #used to tell players if they inputted something invalid
    cls()
    print(color.RED + 'That is an invalid option.' + color.RESET )
    x=input(str('Please enter the number ' "\033[4m" + 'next' + "\033[0m" ' to what you want to. \nType anything to continue.\n'))
                                #Don't touch  ^^^ unless more research is done on this
    

#vairables
x=None#use to stop gltiches
      #x is used simply to emulate notifcations or type anything to countiue lines

main_loop=True
action_loop=False

#used when player upgrades tools
axe_lv=1

pick_lv=1

#players stats (will be more)
wood=0
wood_lv=1
wood_xp=0

stone=0
stone_lv=1
stone_xp=0

msg_counter=1#used to decide the colour for the task return message, this keeps it distinct.
#important for other _msg variables.

level_up=False
wood_mesg=False #used to tell the player if that their input worked
stone_mesg=False

#start here
cls()
name=input(str('What is your name? \n')) #I should use this

while main_loop == True:
    x=None
    cls()
    menu=int(input(f'Main menu \n1.Tasks \n2.Inventory \n3.Stats \n4.Craft \n'))
    if menu==1:
        task_loop=True#used so player doesnt have to go through all the menus every time
        
        while task_loop==True:
            cls()
            if level_up==True:
                print(color.GREEN + 'LEVEL UP!' + color.RESET)
                level_up=False
                
            if msg_counter>=4:
                msg_counter=1
            
            if wood_mesg==True:
                if msg_counter==1:
                    print(color.CYAN + 'Wood chopped' + color.RESET)
                elif msg_counter==2:
                    print(color.MAGENTA + 'Wood chopped' + color.RESET)
                else:
                    print(color.YELLOW + 'Wood chopped' + color.RESET)
                wood_mesg=False

            if stone_mesg==True:
                if msg_counter==1:
                    print(color.CYAN + 'Stone mined' + color.RESET)
                elif msg_counter==2:
                    print(color.MAGENTA + 'Stone mined' + color.RESET)
                else:
                    print(color.YELLOW + 'Stone mined' + color.RESET)
                stone_mesg=False
            
            act=int(input(f'What would you like to do? \n1.Chop wood \n2.Mine stone\n0.Menu \n'))
            
            if act==1:
                wood+=wood_lv+axe_lv-1
                wood_xp+=1
                wood_mesg=True
                msg_counter+=1
                
                if wood_xp==10*wood_lv:
                    wood_lv+=1
                    wood_xp=0
                    level_up=True
                    
            elif act==2:
                stone+=stone_lv+pick_lv-1
                stone_xp+=1
                stone_mesg=True
                msg_counter+=1
                
                if stone_xp==10*stone_lv:
                    stone_lv+=1
                    stone_xp=0
                    level_up=True
                    
            elif act==0:
                action_loop=False
            
            else:
                invalid()
    #Inventory
    #player goes here to see how mcuh of each mateial they have
    elif menu==2:
        cls()
        print(f'Wood={wood} \nStone={stone}')
        x=str(input('type anything to return'))
        x=None
    
    #player stats.
    elif menu==3:
        cls()
        print(f'Wood level\{wood_lv} \n 		{wood_xp}\{10*wood_lv}')
        print(f'Stone level\{stone_lv} \n 		{stone_xp}\{10*stone_lv}')
        x=str(input('type anything to countinue'))
        x=None
    
    #crafting menu
    #will add more options later
    elif menu==4:
        cls()
        print('what do you want to make.')
        x=int(input('1.axe \n2.pickaxe \n0.nothing(exit) \n'))
        if x==1:
            
            #axe upgrade option
            x=None
            cls()
            print(f'To upgrade axe you need {axe_lv*10} wood and {axe_lv*4} stone')
            x=int(input('1.upgrade axe \n2.cancel \n'))
            
            if x==1:
                x=None
                cls()
                
                if wood>=axe_lv*10 and stone>=axe_lv*4:
                    wood -= axe_lv*10
                    stone -= axe_lv*4
                    axe_lv += 1
                    print(color.MAGENTA + 'Axe crafted' + color.RESET)
                    x=str(input('type anything to countinue'))
                    x=None
                
                #for if they player doesnt have neough materials
                elif wood<axe_lv*10 and stone<axe_lv*4:
                    print(color.RED + 'You dont have enough wood or stone.' + color.RESET)
                    x=str(input('type anything to countinue'))
                    x=None
                    
                elif wood<axe_lv*10:
                    print(color.RED + 'You dont have enough wood.' + color.RESET)
                    x=str(input('type anything to countinue'))
                    x=None
                    
                else:
                      print(color.RED + 'You dont have enough stone.' + color.RESET)
                      x=str(input('type anything to countinue'))
                      x=None
        
        #pickace upgrade option
        elif x==2:
            x=None
            cls()
            print(f'To upgrade Pick you need {pick_lv*4} wood and {pick_lv*10} stone')
            x=int(input('1.upgrade Pick \n2.cancel \n'))
            
            if x==1:
                x=None
                cls()
                
                if wood>=pick_lv*4 and stone>=pick_lv*10:
                    wood-=pick_lv*4
                    stone-=pick_lv*10
                    pick_lv+=1
                    print(color.MAGENTA + 'Pick crafted' + color.RESET)
                    x=str(input('type anything to countinue'))
                    x=None
                
                #for if they player doesnt have neough materials
                elif wood<pick_lv*4 and stone<pick_lv*10:
                    print(color.RED + 'You dont have enough wood or stone.' + color.RESET)
                    x=str(input('type anything to countinue'))
                    x=None
                    
                elif wood<pick_lv*4:
                    print(color.RED + 'You dont have enough wood.' + color.RESET)
                    x=str(input('type anything to countinue'))
                    x=None
                    
                else:
                      print(color.RED + 'You dont have enough stone.' + color.RESET)
                      x=str(input('type anything to countinue'))
                      x=None
    else:
        invalid()