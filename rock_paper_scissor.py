#rock paper scissors
import random
def fun3(p1,p2):
    if(p1=='r' and p2=='p'):
        return p2
    elif(p1=='r' and p2=='s'):
        return p1
    elif(p1=='s' and p2=='r'):
        return p2
    elif(p1=='s' and p2=='p'):
        return p1
    elif(p1=='p' and p2=='r'):
        return p1
    elif(p1=='p' and p2=='s'):
        return p2

    
def fun1():
    rsc=0
    psc=0
    while(rsc!=3 and psc!=3):
        k=['r','p','s']
        robot=random.choice(k)
        player=input("enter rock (r) paper (p) scissor (s) :")
        if(robot==player):
            print(f"robot choice :{robot}")
            pass
        else:
            res=fun3(robot,player)
            print(f"robot choice :{robot}")
            if(res==robot):
                rsc+=1
                print(f"robot score {rsc}")
                print(f"your score {psc}")
            elif(res==player):
                psc+=1
                print(f"robot score {rsc}")
                print(f"your score {psc}")
    if(rsc>psc):
        print("\nRobot won the game\n");
    else:
        print("\nYou won the game\n");
def fun2():
    p1=0
    p2=0
    while(p1!=3 and p2!=3):
        k=['r','p','s']
        pla1=input("P1: enter rock (r) paper (p) scissor (s) :")
        pla2=input("P2: enter rock (r) paper (p) scissor (s) :")
        if(pla1==pla2):
            pass
        else:
            res=fun3(pla1,pla2)
            if(res==pla1):
                p1+=1
                print(f"player 1 score {p1}")
                print(f"player 2 score {p2}")
            elif(res==pla2):
                p2+=1
                print(f"player 1 score {p1}")
                print(f"player 2 score {p2}")
    if(p1>p2):
        print("\nPlayer 1 won the game\n");
    else:
        print("\Player 2 won the game\n");

while(1):
    print("enter 0 to quit game ")
    p=int(input(("Enter 1 or 2 players :")))
    if(p==1):
        fun1()
    elif(p==2):
        fun2()
    elif(p==0):
        print("Thank You Have a nice day")
        break
    else:
        print("enter valid option (1 or 2) !!!")
        
    
