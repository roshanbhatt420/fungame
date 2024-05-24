print("LETS PLAY SCISSSOR PAPER ROCK ")
import random
items=['scissor','paper','rock']
pc_choice=random.choice(items)
print("enter 1 for scissor,2 for paper,3 for rock")
user_choice=int(input())
while not user_choice:
    print("you must enter")
    user_choice=int(input("enter 1 for scissor,2 for paper,3 for rock"))
if(user_choice==1):
    print("you entered scissor")
    print("I entered ",pc_choice)
    user_choice='scissor'
    if(pc_choice=='scissor' ):
        print("match is drawn")
    elif(pc_choice=='rock'):
        print("hureey, I win")
    else:
        print(" wow,you won")
elif(user_choice==2):
    print("you entered Paper")
    print("I entered ",pc_choice)
    user_choice='paper'
    if(pc_choice=='scissor' ):
        print("hureey ,I won")
    elif(pc_choice=='rock'):
        print("wow, you won")
    else:
        print("match is drawn")
elif(user_choice==3):
    print("you entered  Rock ")
    print("I entered ",pc_choice)
    user_choice='rock'
    if(pc_choice=='scissor' ):
        print("wow ,you won")
    elif(pc_choice=='rock'):
        print("match is drawn")
    else:
        print(" Hureet ,I won")
else:
    print("you entered invalid number so you lose")