print'\n\n\n\n\n\n\t\t\t\t\tThis program is to interogate you'
a=str(input("Enter your name: "))
print("\n\n\t\tWelcome {0}".format(a))
print'\n\nFrom now enter correct spelling for what you type, and the type according to the question asked'
b=int(input('\nWhat is your age:'))
print'{0},age {1} what made you to run this program'.format(a,b)
c=str(input("What are your intrests \n\tChoose from the following below without caps and with same words and gaps\nFootball\nVolleyball\nBasketball\nComputer game:"))
if (c==Football):
  print"\n\nAs you like football i'am going to ask you some questions in football"
  print"\n\tQuestion :Who is the famous football star in this world currently(Choose from the hints)\nHints:ronaldo or messi or neymar or dybala: "
  d=str(input('Answer:'))
  if (d==ronaldo):
    print'Correct answer:)'
    print'As you like Football try fifa mobile a mobile game for android'
    print'It was nice talking to you, bye' 
  else:
    print'Wrong answer:('
    print'This interogation is over and it was nice talking to you, bye'
elif (d==Volleyball):
   print"\n\nAs you like volleyball i'am going to ask you a questions in valleyball"
   print"\n\tQuestion :What is the gamepoint in a proper volleyball match (Choose from the hints)\nHints:10 or 15 or 20 or 25:"
   d=str(input('Answer:'))
  if (d<25):
    print'Wrong answer:('
    print'It was nice tlking to you, bye'
  else(d==25):
    print'Correct answer'
    print'It was nice talking to you, bye'
elif (d==Basketball):    
  print"\n\nAs you like basketball i'am going to ask you some questions in basketball"
  print"\n\tQuestion :Which country is basketball a major sport:\nunited states of america or india or africa"
  d=str(input('Answer:'))
  if (d==United states of america):
    print'Correct answer'
    print'It was nice tlking to you, bye'
  else:
    print'Wrong answer'
    print'It was nice tlking to you, bye'
elif (d==computer games):
   print"\n\nAs you like computer games i'am going to ask you some questions in it"
  print"\n\tQuestion :Which was the first computer game invented \n hint:Mario or carrom or tic-tac-toe or something else  "
  d=str(input('Answer:'))
  if (d==tic-tac-toe):
    print'Correct answer'
    print'It was nice tlking to you, bye'
  else:
    print'Wrong answer'
    print'It was nice tlking to you, bye'
else:
  print'\n\t\tPlease run the program again without caps and check for spelling'
  
  
