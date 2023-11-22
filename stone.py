#THIS PROGRAM WAS MADE BY 1. Ma.NITYANAND MAURYA (BTech 1st Year CSE (AIML D )) RA2311026030209
#                         2. Raunak Sharma (BTech 1st Year CSE (AIML D )) RA2311026030210
#                         3. Preet Singh (BTech 1st Year CSE (AIML D )) RA2311026030208
#GUIDED BY : Prof. Uma Meena Mam
#SRM IST Delhi NCR Campus

print("\n--------------------------------WELCOME TO ROCK, PAPER, SCISSOR-------------------------------------\n")

from termcolor import colored
import random
arr=["Stone","Paper","Scissor"]

b=0
y=0
def p2p():                              # THIS IS FOR PLAYER TO PLAYER
    n=int(input(colored("Enter 1st player Choice (1/2/3)\n1.Stone\n2.Paper\n3.Scissor\n",'yellow')))
    print(colored("-->","blue"))
    n2=int(input("Enter 2nd player Choice (1/2/3)\n1. Stone\n2. Paper\n3. Scissor\n-->"))
    print("")
    if n==n2:
        print("Tie")
    elif (n==1 and n2==3) or (n==2 and n2==1) or (n==3 and n2==2):
        print("Player 1 Won !")
    elif (n2==1 and n==3) or (n2==2 and n==1) or (n2==3 and n==2):
        print("Player 2 Won !")
    else:
        print("Please Enter Either 1, 2 or 3 ")
        p2p()

def wthpc():                   #THIS IS TO PLAY WITH BOT
    global b
    global y
    try:
        print(colored("\nEnter Your Choice (1/2/3)\n1.Stone\n2.Paper\n3.Scissor\n","yellow"))
        n=int(input(colored("-->","magenta")))
        n2=random.randint(1,3)
        print("")
        if n==n2:
            print("Bot choosed : ",arr[n2-1])
            print("You choosed : ",arr[n-1])
            print(colored("Almost There, Tie !","light_blue",attrs=["bold"]))
        elif (n==1 and n2==3) or (n==2 and n2==1) or (n==3 and n2==2):
            print("Bot choosed : ",arr[n2-1])
            print("You choosed : ",arr[n-1])
            y+=1
            print(colored("Congrats!!! You Won !","light_green",attrs=["bold"]))
        elif (n2==1 and n==3) or (n2==2 and n==1) or (n2==3 and n==2):
            print("Bot choosed : ",arr[n2-1])
            print("You choosed : ",arr[n-1])
            b+=1
            print(colored("Better Luck Next Time !","light_red",attrs=["bold"]))
        else:
            print(colored("Please Enter Either 1, 2 or 3 \n","red",attrs=["reverse"]))
            wthpc()
    except Exception:
        print(colored("\nPLEASE ENTER A VALID NUMBER\n","red",attrs=["reverse"]))
        wthpc()
def inita():                    #THIS IS INITIALIZATION
    global stt
    try:
        print(colored("\nHow many rounds you wanna play ?\n","green"))
        stt=int(input(colored("-->","magenta")))
        if stt>0:
            for i in range(stt):
                wthpc()
        else:
            print(colored("\nPLEASE ENTER A NUMBER GREATER THAN ZERO\n","red",attrs=["reverse"]))
            inita()
        pa()
    except Exception:
        print(colored("\nPLEASE ENTER A VALID NUMBER\n","red",attrs=["reverse"]))
        inita()
def pa():                       # THIS IS END GREETING
    print(colored("\nWould You like to play again ? (Y/N)\n","magenta"))
    d=str(input(colored("-->","magenta")))
    if ('Y' in d) or ('y' in d):
        inita()
    elif ('N' in d) or ('n' in d):
        print("")
        print("Your Total Score : ",y)
        print("Bot Scored       : ",b)
        print("Game Tie         : ",stt-(y+b))
        print(colored("\nThank You, We Hope You Enjoyed !!!\n","cyan",attrs=["underline"]))
        lpa=input(colored('\nPRESS ENTER TO EXIT\n',"magenta",attrs=['reverse']))
        if lpa==True:
            exit()
        else:
            exit()
    else:
        print(colored("\nPlease write (y/n)\n","red",attrs=["reverse"]))
        pa()
        
inita()

