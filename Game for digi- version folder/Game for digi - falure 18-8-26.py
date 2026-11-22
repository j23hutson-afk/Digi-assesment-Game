#modules
import color

#functions
def cls():
    print ("\n" * 100)

def invalid(): #used to tell players if they inputted something invalid
    cls()
    print(color.RED + 'That is an invalid option.' + color.RESET )
    x = input(str('Please enter the number ' "\033[4m" + 'next' + "\033[0m" ' to what you want to. \nType anything to continue.\n'))
                                #Don't touch  ^^^ unless more research is done on this
    x=None
    

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
        print(color.CYAN + bone['name'] + color.RESET, end="")
        print(color.CYAN + ' gathered' + color.RESET)
        
    elif msg_counter == 2:
        print(color.MAGENTA + bone['name'] + color.RESET, end="")
        print(color.MAGENTA + ' gathered' + color.RESET)
        
    else:
        print(color.YELLOW + bone['name'] + color.RESET, end="")
        print(color.YELLOW + ' gathered' + color.RESET)
        
    bone['task_msg'] = False
    
    return bone
def tool_upgrade_check(bone, *stick):

    cls()
    check=False
        
    print(f'To upgrade {bone["item_name"]} you need {bone["item"] * bone["upgrade_1"]} {bone["upgrade_1_name"]} and {bone["item"] * bone["upgrade_2"]} {bone["upgrade_2_name"]}')
    x=int(input(f'1.upgrade {bone["item_name"]} \n2.cancel \n'))
            
    if x == 1:
        x = None
        cls()
                
        if stick[1]['amount'] == bone["item"]*bone['upgrade_1'] and stick[2]['amount'] == bone["item"]*bone["upgrade_2"]:
            check = True
            return check
            
        #for if they player doesnt have neough materials
        else:
            print(color.RED + 'You dont have enough materials.' + color.RESET)
            x = str(input('type anything to countinue'))
            x = None
            return check
    
    elif x == 2:
        x = None
        return check
    
    
def tool_upgrade(bone, *stick):   

    words = {
        "1" : None,
        "2" : None
        }
    
    stick[1]['amount'] -= bone['item'] * bone['upgrade_1']
    stick[2]['amount'] -= bone['item'] * bone['upgrade_2']
    bone['item'] += 1
    print(color.MAGENTA + bone['item_name'] + color.RESET, end='')
    print(color.MAGENTA + ' crafted' + color.RESET)            
    x = str(input('type anything to countinue'))
    x = None
    
    bone['amount'] = stick[1]['amount']
    words['1'] = bone
    words['2'] = stick[2]
    
    return words
    
    
    
    

        
#players stats (will be more)
test={
}
trial={
}

wood = {
    "name" : 'wood',
    "amount" : 10,
    "level" : 1,
    "xp" : 0,
    "item" : 1,
    "item_name" : 'axe',
    "task_msg" : False,
    "upgrade_1" : 10,
    "upgrade_1_name" : "wood",
    "upgrade_2" : 4,
    "upgrade_2_name" : 'stone'
}


stone = {
    "name" : 'stone',
    "amount" : 4,
    "level" : 1,
    "xp" : 0,
    "item" : 1,
    "item_name" : 'pick',
    "task_msg" : False,
    "upgrade_1" : 10,
    "upgrade_1_name" : 'stone',
    "upgrade_2" : 4,
    "upgrade_1_name" : 'wood'
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
    elif menu == 2:
        cls()
        print(f'Wood =',wood['amount'], '\nStone =',stone['amount'])
        print(test)
        x = str(input('type anything to return'))
        x = None
    
    #player stats.
    elif menu==3:
        cls()
        print(f'Wood level\{wood["level"]} \n 		{wood["xp"]}\{10*wood["level"]}')
        print(f'Stone level\{stone["level"]} \n 		{stone["xp"]}\{10*stone["level"]}')
        x = str(input('type anything to countinue'))
        x = None
    
    #crafting menu
    #will add more options later
    elif menu == 4:
 
        cls()
        print('What do you want to make.')
        x=int(input('1.axe \n2.pickaxe \n0.nothing(exit) \n'))
        if x == 1:
            x=None
            trial = wood
            #if tool_upgrade_check(wood, wood, stone) == True:
            test=tool_upgrade(wood, wood, stone)
            wood=test['1']
            stone=test['2']
                
            #else:
                #x = None
            #axe upgrade option

    else:
        invalid()