#modules
import color

#functions
def cls(): print ("\n" * 100)

#vairables
main_loop=True
action_loop=False

wood=0
wood_lv=1
wood_xp=0

stone=0
stone_lv=1
stone_xp=0

level_up=False

#start here
cls()
name=input(str('What is your name? \n'))

while main_loop == True:
    cls()
    menu=int(input(f'Main menu \n1.Actions \n2.Inventory \n3.Stats \n'))
    if menu==1:
        action_loop=True
        
        while action_loop==True:
            cls()
            if level_up==True:
                print(color.GREEN + 'LEVEL UP!' + color.RESET)
            act=int(input(f'What would you like to do? \n1.Chop wood \n2.Mine stone\n0.Menu \n'))
            
            if act==1:
                wood+=wood_lv
                wood_xp+=1
                
                if wood_xp==10*wood_lv:
                    wood_lv+=1
                    wood_xp=0
                    level_up=True
                    
            elif act==2:
                stone+=stone_lv
                stone_xp+=1
                
                if stone_xp==10*stone_lv:
                    stone_lv+=1
                    stone_xp=0
                    level_up=True
                    
            elif act==0:
                action_loop=False
                
    elif menu==2:
        cls()
        print(f'Wood={wood} \nStone={stone}')
        x=str(input('type anything to countinue'))
        
    elif menu==3:
        cls()
        print(f'Wood level\{wood_lv} \n 		{wood_xp}\{10*wood_lv}')
        print(f'Stone level\{stone_lv} \n 		{stone_xp}\{10*stone_lv}')
        x=str(input('type anything to countinue'))
