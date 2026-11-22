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

main_loop = True
action_loop = False

msg_counter = 0 #used to decide the colour for the task return message, this keeps it distinct.
#important for other _msg variables.

def task(bone):
#called bone because Cian sugested it
#I couldent think of anything better
    
   
    bone['amount'] += bone['level'] + bone['item'] - 1
    bone['xp'] += 1
    bone['task_msg'] = True
                
    if bone['xp'] == 10*bone['level']:
        bone['level'] += 1
        bone['xp'] = 0
        level_up = True
    
    return bone

def msg(bone):
        
    if msg_counter == 1:
        print(color.CYAN + bone['name'] + color.RESET)
        
    elif msg_counter == 2:
        print(color.MAGENTA + bone['name'] + color.RESET)
        
    else:
        print(color.YELLOW + bone['name'] + color.RESET)
        
    bone['task_msg'] = False
    
    return bone
    
    
        
#players stats (will be more)
wood = {
    "name" : 'wood',
    "amount" : 0,
    "level" : 1,
    "xp" : 0,
    "item" : 1,
    "task_msg" : False
}

stone = {
    "name" : 'stone',
    "amount" : 0,
    "level" : 1,
    "xp" : 0,
    "item" : 1,
    "task_msg" : False
}

level_up=False

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
            
            if wood['task_msg'] == True:
                wood = msg(wood)
                
            if stone['task_msg'] == True:
                stone = msg(stone)
                
            if msg_counter >= 3:
                msg_counter = 0
            
            act = int(input(f'What would you like to do? \n1.Chop wood \n2.Mine stone\n0.Menu \n'))
            
            msg_counter += 1
            
            if act == 1:
                wood = task(wood)
            
            elif act == 2:
                stone = task(stone)
                    
            elif act == 0:
                task_loop = False
            
            else:
                invalid()
                
    #Inventory
    #player goes here to see how mcuh of each mateial they have
    elif menu==2:
        cls()
        print(f'Wood =',wood['amount'], '\nStone =',stone['amount'])
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