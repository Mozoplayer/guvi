print("1.Rock  2.Paper   3.Scissor")
p1=int(input("enter your option"))
print("1.Rock  2.Paper   3.Scissor")
p2=int(input("enter your option"))
if(p1==1):
      if(p2==1):
        print("tie")
      elif(p2==2):
        print("player 2 is win")
      elif(p2==3):
        print("Player 1 is win")
      else:
        print("enter valid option")
if(p1==2):
      if (p2 == 1):
        print("player 1 win")
      elif (p2 == 2):
        print("tie")
      elif (p2 == 3):
        print("Player 2 is win")
      else:
        print("enter valid option")
if(p1==3):
    if (p2 == 1):
        print("player 2 win")
    elif (p2 == 2):
        print("tie")
    elif (p2 == 3):
        print("Player 1 is win")
    else:
        print("enter valid option")
elif(p1<1&p1>3):
    print("enter valid option")


