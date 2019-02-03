# template for "Guess the number" mini-project
# input will come from buttons and an input field
# all output for the game will be printed in the console

import random
import simplegui

secrect_num=None
count=7
# helper function to start and restart the game
def newgame():
    global secrect_num,count
    count=7
    secrect_num=random.randrange(0,100)
    print("Guess the number You have 7 chances")
#control handler function define secrect_num //by default secrect_num is range100    
def range_100():
    global secrect_num
    secrect_num=random.randrange(0,100)
    print("Guess the number You have 7 chances")
   
def range_1000():
    global secrect_num
    secrect_num=random.randrange(100,1000)
    print("Guess the number You have 7 chances")
#user guess
def guess_input(x):
    global secrect_num,count
    
    
    if int(x)==secrect_num:
        
        print("Correct")
        print("You won")
        print("Play more")
        newgame()
        
   
    if int(x) > secrect_num:
        print("Lower\n")
    if int(x)< secrect_num:
        print("Higher")
    count=count-1
    if count==0:
        print("Game over")
    if x!=secrect_num:
        print(" chances left ",count)
    
newgame()
#start frame 
f=simplegui.create_frame("Guess Number",200,200)

f.add_button("Num b/w 100",range_100,100)
f.add_button("Num b/w 100 to 1000",range_1000,100)
f.add_input("Guess the number",guess_input,100)




f.start()
    
    