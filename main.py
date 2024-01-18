# Sorting Program Fast and Furious characters

#Add-ons:
#1.Cowntdown
#2.Ask name and emoticons
#3.Discription in script form
#4.Pictures for each character
#5.Specialized descriptions for each character
#6.Lists and dictionaries
 
import time
import sys
from tkinter import *
from PIL import ImageTk, Image

#This function is where the questions are being asked to the user. 
def play():
  print('')
  print('\x1b[3;35;91m' + "Welcome to game,\n" + '\x1b[0m' + "think of a character from the list above and answer the following questions. If you do not know the answer you can always scroll up to the description provided earlier for referance" + "\U0001F60E" + " . First question:")
  #This is where the dictionary and lsit in lines 171 and 200 come to play
  #Starts with question 1 always, and depending on the users answer the definition of the question wioll be either 0 or 1. If yes then 0 (left side), if no then 1 (right side).
  q=1
  result = False
  while not result:
    ans = input(questions[q])
    #If user says no then the definition of the question asked in dictionary in line 200 is index of 0(on the left)
    if ans == "Y" or ans == "y":
      if q_list[q-1][0].isdigit():
        q = int(q_list[q-1][0])
      else:
        for i in range(3):
          #end = '\r' is a built in function that returns the program to the beginning of the line. This repeats three times with the delay of 1 second.
          print('\x1b[3;35;91m' + "Drumroll please..." + str(3-i) , end = '\r' + '\x1b[0m')
          time.sleep(1)
        #This prints what character is omitted from the users answers
        print("The person you chose is " + '\x1b[3;35;91m' + q_list[q-1][0] + "\U0001F60E" + "!" + '\x1b[0m')
        result = True
    #If user says no then the definition of the question asked in dictionary in line 200 is index of 1(on the right)
    elif ans == "N" or ans == "n":
      if q_list[q-1][1].isdigit():
        q = int(q_list[q-1][1])
      #print error message
      else:
        for i in range(3):
          #end = '\r' is a built in function that returns the program to the beginning of the line. This repeats three times with the delay of 1 second.
          print('\x1b[3;35;91m' + "Drumroll please..." + str(3-i) , end = '\r' + '\x1b[0m')
          time.sleep(1)
          #Prints the name of the character
        print("The person you chose is " + '\x1b[3;35;91m' + q_list[q-1][1] +  "\U0001F60E" + "!" + '\x1b[0m')
        result = True
    #Prints error message
    else:
      print('\x1b[3;35;91m' + "Please enter 'Y' for yes or 'N' for no, lowercase works too!" + '\x1b[0m')

#This is for the image presentation
def quit(root):
  root.destroy()

#This function is responsible for printing the descriptions of the characters chosen by the user
def show_description():
  #This shows a list of all the possible characters the user can choose from
  print('\x1b[3;35;91m' + "\nHere are all the characters:\n" + '\x1b[0m' + "1.Dominic Toretto\n 2.Brian O'Conner\n 3.Letty Ortiz\n 4.Mia Toretto\n 5.Roman Pearce\n 6.Tej Parker\n 7.Han Lue\n 8.Gisele Yashar\n 9.Luke Hobbs\n 10.Elena Neves\n 11.Ramsey\n 12.Tego Leo\n 13.Rico Santos\n 14.Vince\n 15.Sean Boswell\n 16.Suki\n 17.Mr. Nobody\n 18.Deckard Shaw\n 19.Owen Shaw\n 20.Cipher\n 21.Braga\n 22.D.K\n 23.Reyes\n 24.Brian toretto (Dominic's son)\n 25.Jack O’Conner (Brian’s son)\n 26.Nico (Vince’s son)")
  print('')
  result = False 
  while not result:
    #This asks for the number of the character the user would like to see 
    character = input("Input the number of the character you would like to see the description of" + "\U0001F60E" + ": ")
    #If the user did not input a number, a message is printed to tell them to input a number
    if character.isdigit() == False:
      print('\x1b[3;35;91m' + "Please make sure you enter a number." + '\x1b[0m')
    #If the number is in range a picture is displayed of the chosen character and a description is taken from the dictionary in line 141
    elif int(character) in range(1,27):
      print('')
      print('\x1b[3;35;91m' + description[int(character)] + '\x1b[0m')
      #This shows the image in console
      root = Tk()
      canvas = Canvas(root, width = 300, height = 300)
      canvas.pack()
      img = ImageTk.PhotoImage(Image.open(pic_dictionary[int(character)]))
      canvas.create_image(20,20,anchor=NW, image=img)
      print("(To continue with the game or to select another description, press the exit button " + '\x1b[3;35;91m' + "on the top right corner of the image " + '\x1b[0m' + "to close the image before proceeding)")
      #This closes the picture
      root.mainloop()
      #After the description is shown, the user is asked if they want to see another description
      like = input("Would you like to see a different description?[Y/N]: ")
      #If the user says no, the program continues to the play() function in line 24 
      if like == "N" or like == "n":
        play()
        result = True
      #if the user says anything but yes 
      elif like != "Y" and like != "y" and like != "N" and like != "n":
        print('\x1b[3;35;91m' + "Im sorry, I didnt get that. Please try again, make sure to input either 'y' or 'n'." + '\x1b[0m')
      else:
        show_description() 
    #If the user inputs a number that is higher than 26 or lower than 1, then a message is printed telling the user they are out of range
    else:
      print('\x1b[3;35;91m' + "Please make sure you choose a number between 1 and 26." + '\x1b[0m')

#This function starts the actual game
def start_play(): 
  #This prints the script letter by letter to explain how the game works 
  print('\x1b[3;35;91m' + "\nGreat! here are the rules:" + '\x1b[0m')
  explanation = "\nI will give you descriptions of 26 people from the Fast and Furious saga! \nAfter reading a few of the descriptions, chose a singular character in your head and proceed with the game. \nTo make this game more difficult I will only be asking you YES or NO questions, each of your answers should only be answered with a 'Y' or a 'N' (lowercase works too!). \nPlease make sure to read the questions carefully and remeber you can always scroll up to see the description you chose previously for referance. Enojy!\n"
  for char in explanation:
    time.sleep(0.06)
    sys.stdout.write(char)
    sys.stdout.flush()
  #A while loop that is responsible for asking the user if they want to see the description of characters
  result1 = False
  while not result1:
    description_ask = input("\nWould you like to see the descriptions of the charaters?[Y/N]: ")
    #If the user says yes then the program goes to the show_description() function in line 62
    if description_ask == "Y" or description_ask == "y":
      show_description()
      result1 = True
    #If the user says no then the program skips the show_description() function and goes straight to the play() function in line 24. This also shows the avalible characters for the user to choose 
    elif description_ask == "N" or description_ask == "n":
      print("\nLooks like we have a fast and furious fan among us" + "\U0001F60E" " awesome!\nLets get right into the game, but " + '\x1b[3;35;91m' "make sure you chose one of these characters:\n" + '\x1b[0m' + "Here are all the characters:\n 1.Dominic Toretto\n 2.Brian O'Conner\n 3.Letty Ortiz\n 4.Mia Toretto\n 5.Roman Pearce\n 6.Tej Parker\n 7.Han Lue\n 8.Gisele Yashar\n 9.Luke Hobbs\n 10.Elena Neves\n 11.Ramsey\n 12.Tego Leo\n 13.Rico Santos\n 14.Vince\n 15.Sean Boswell\n 16.Suki\n 17.Mr. Nobody\n 18.Deckard Shaw\n 19.Owen Shaw\n 20.Cipher\n 21.Braga\n 22.D.K\n 23.Reyes\n 24.Brian toretto (Dominic's son)\n 25.Jack O’Conner (Brian’s son\n 26.Nico (Vince’s son)\n")
      play()
      result1 = True
      #If the user inputs anything but yes or no, the while loop loops and asks the question in line 110 again
    else:
      print('\x1b[3;35;91m' + "Im sorry, I didnt get that. Please try again, make sure to input either 'Y' or 'N'." + '\x1b[0m')

#This function asks whether the user would like to start the game, it carries the inputed value for 'name' as a parameter
def start(name):
  start = input("\n" + name.title() + " \U0001F60E" + "," +" would you like to play a game where I guess your character?[Y/N]: ")
  #If the user inputted yes then the program proceeds to the function start_play() on line 99
  if start == "Y" or start == "y":
    start_play()
    return False
  #If the user inputs no then the program returns the variabl return as true which stops the while loop in the beginning in line 236
  elif start == "N" or start == "n":
    print("Thats okay, have a good rest of your day!" + "\U0001F60E")
    return True
  #If the user inputs anything but yes or no, they get a message saying to try again
  else:
    print('\x1b[3;35;91m' + "Im sorry, I didnt get that. Please try again, make sure to input either 'y' or 'n'." + '\x1b[0m')
    return False

#These are the descriptions that are printed based on the input of line 74
description = {
  1 : "Dominic Toretto:\n-Adult\n-Male\n-Was NOT introduced in Tokyo\n-Is part of the main group of racers\n-Is bald\n-Has a son (Brian Torreto)\n",
  2 : "Brian O'Conner:\n-Adult\n-Male\n-Was NOT introduced in Tokyo\n-Is part of the main group of racers\n-Is not bald\n-Does not speak spanish\n-Is NOT a hacker\n-Was never shown in Tokyo\n",
  3 : "Letty Ortiz:\n-Adult\n-Female\n-Is a protagonist\n-Is alive after the eighth movie\n-Married to Dominic Torreto\n",
  4 : "Mia Toretto:\n-Adult\n-Female\n-Is a protagonist\n-Is alive after the eighth movie\n-Is NOT married to Dominic Torreto\n-Is married to Brian O'Connor\n",
  5 : "Roman Pearce:\n-Adult\n-Male\n-Was NOT introduced in Tokyo\n-Is part of the main group of racers\n-Is bald\n-Does NOT have a son\n",
  6 : "Tej Parker:\n-Adult\n-Male\n-Was NOT introduced in Tokyo\n-Is part of the main group of racers\n-Is NOT bald\n-Does NOT speak spanish\n-Is a hacker\n",
  7 : "Han Lue:\n -Adult\n-Male\n-Was NOT introduced in Tokyo\n-Is part of the main group of racers\n-Is NOT bald\n-Does NOT speak spanish\n-Is NOT a hacker\n-Was seen in Tokyo\n",
  8 : "Gisele Yashar:\n-Adult\n-Female\n-Is a protagonist\n-Is NOT alive after the eighth movie\n-Is NOT a cop\n",
  9 : "Luke Hobbs:\n-Adult\n-Male\n-Was NOT introduced in Tokyo\n-Is NOT part of the main group of racers\n-Is a cop/ government worker\n-Is bald\n",
  10 : "Elena Neves:\n-Adult\n-Female\n-Is a protagonist\n-Is NOT alive after the eighth movie\n-Is a cop\n",
  11 : "Ramsey:\n-Adult\n-Female\n-Is a protagonist\n-Is alive after the eighth movie\n-Is NOT married to Dominic Torreto\n-Is NOT married to Brian O'Connor\n-Is a hacker\n",
  12 : "Tego Leo:\n-Adult\n-Male\n-Was NOT introduced in Tokyo\n-Is part of the main group of racers\n-Is NOT bald\n-Speaks spanish\n-Is NOT thr taller person out of the legendary duo\n",
  13 : "Rico Santos:\n-Adult\n-Male\n-Was NOT introduced in Tokyo\n-Is part of the main group of racers\n-Is NOT bald\n-Speaks spanish\n-Is thr taller person out of the legendary duo\n",
  14 : "Vince:\n-Adult\n-Male\n-Was NOT introduced in Tokyo\n-Is NOT part of the main group of racers\n-Is NOT a cop or government worker\n-Did NOT have a brother in the movie\n-Did NOT have a vault full of money\n-Saved Dominic Torreto and the main crew or racers\n",
  15 : "Sean Boswell:\n -Adult\n-Male\n-Is introduced in Tokyo\n-Is a protagonist\n",
  16 : "Suki:\n-Adult\n-Female\n-Is a protagonist\n-Is alive after the eighth movie\n-Is NOT married to Dominic Torreto\n-Is NOT married to Brian O'Connor\n-Is NOT a hacker\n",
  17 : "Mr. Nobody:\n-Adult\n-Male\n-Was NOT introduced in Tokyo\n-Is NOT part of the main group of racers\n-Is a cop/ government worker\n-Is NOT bald\n",
  18 : "Deckard Shaw:\n-Adult\n-Male\n-Was NOT introduced in Tokyo\n-Is NOT part of the main group of racers\n-Is NOT a cop or government worker\n-Had a YOUNGER brother in the movie(Makes him the older brother)\n",
  19 : "Owen Shaw:\n-Adult\n-Male\n-Was NOT introduced in Tokyo\n-Is NOT part of the main group of racers\n-Is NOT a cop or government worker\n-Had an OLDER brother in the movie(Makes him NOT the older brother)\n",
  20 : "Cipher:\n-Adult\n-Female\n-Is NOT a protagonist\n",
  21 : "Braga:\n-Adult\n-Male\n-Was NOT introduced in Tokyo\n-Is NOT part of the main group of racers\n-Is NOT a cop or government worker\n-Did NOT have a brother in the movie\n-Did NOT have a vault full of money\n-Did NOT save Dominic Torreto and the main crew or racers\n",
  22 : "D.K:\n-Adult\n-Male\n-Is introduced in Tokyo\n-Is NOT a protagonist\n",
  23 : "Reyes:\n-Adult\n-Male\n-Was NOT introduced in Tokyo\n-Is NOT part of the main group of racers\n-Is NOT a cop or government worker\n-Did NOT have a brother in the movie\n-Had a vault full of money\n",
  24 : "Brian toretto (Dominic's son):\n-Child\n-Their father is alive\n",
  25 : "Jack O’Conner (Brian’s son):\n-Child\n-Their father is NOT alive\n-Their father did NOT die of a gunshot\n",
  26 : "Nico (Vince’s son):\n-Child\n-Their father is NOT alive\n-Their father died of a gunshot\n",
}

#These are the questions used in line 35
questions = {
 1 : "\nAre they Children?[Y/N]: ",
 2 : "\nIs their father alive?[Y/N]: ",
 3 : "\nDid his father die of a gunshot?[Y/N]: ",
 4 : "\nAre they female?[Y/N]: ",
 5 : "\nAre they a protagonist?[Y/N]: ",
 6 : "\nIs she alive after the 8th movie?[Y/N]: ",
 7 : "\nIs she married to Dominic Torreto?[Y/N]: ",
 8 : "\nIs she a cop?[Y/N]: ",
 9 : "\nIs she married to Brian O'Conner?[Y/N]: ",
 10 : "\nIs she a hacker?[Y/N]: ",
 11 : "\nWas he introduced in Tokyo?[Y/N]: ",
 12 : "\nIs he a protagonist?[Y/N]: ",
 13 : "\nIs he a part of the main group of races?[Y/N]: ",
 14 : "\nIs he bald?[Y/N]: ",
 15 : "\nDoes he have a son?[Y/N]: ",
 16 : "\nDoes he speak spanish?[Y/N]: ",
 17 : "\nIs he the taller person out of the legendary duo?[Y/N]: ",
 18 : "\nIs he a hacker?[Y/N]: ",
 19 : "\nWas he ever seen in Tokyo?[Y/N]: ",
 20 : "\nIs he a cop or Government worker?[Y/N]: ",
 21 : "\nIs he bald?[Y/N]: ",
 22 : "\nDid he have a brother in the movie?[Y/N]: ",
 23 : "\nWas he the older brother?[Y/N]: ",
 24 : "\nDid he have a value full of money in the police station?",
 25 : "\nDid he die saving Dominic Torreto and the main crew of racers?[Y/N]: ",
}

#This list is responsible for the responses of the previous questions from the 'questions' dictionary, if the answer is yes the question or the answer on the left is going to be printed, if the answer is no then the question or the answer on the right is going to be printed.
q_list = ["2","4"], ["Brian Torreto (Dominic's son)","3"], ["Nico (Vince's son)", 
"Jack O'Conner (Brian's son)"], ["5", "11"], ["6", "Cipher"], ["7", "8"], ["Letty Ortiz", "9"], ["Elena Neves", "Gisele Yashar"], ["Mia Toretto", "10"], ["Ramsey", "Suki"], ["12", "13"], ["Sean Boswell", "D.K"], ["14", "20"], ["15","16"], ["Dominic Torreto", "Roman Pearce"], ["17", "18"], ["Rico Santos", "Tego Leo"], ["Tej Parker", "19"], ["Han", "Brian O'Conner"], ["21", "22"], ["Luke Hobbs", "Mr. Nobody"], ["23","24"], ["Deckard Shaw", "Owen Shaw"], ["Reyes", "25"], ["Vince", "Braga"]

#This dictionary is responsible for the pictures that will be presented based on the number you inputted
pic_dictionary = {
  1 : "Dominic.jpg",
  2 : "Brian.jpg",
  3 : "Letty.jpg",
  4: "Mia.jpg",
  5: "Roman.jpg",
  6: "Tej.jpg",
  7: "Han.jpg",
  8: "Gisele.jpg",
  9: "Hobbs.jpg",
  10: "Elena.jpg",
  11: "Ramsey.jpg",
  12: "Tego.jpg",
  13: "Rico.jpg",
  14: "Vince.jpg",
  15: "Sean.jpg",
  16: "Suki.jpg",
  17: "Mr.Nobody.jpg",
  18: "Deckard.jpg",
  19: "Owen.jpg",
  20: "Cipher.jpg",
  21: "Braga.jpg",
  22: "D.K.jpg",
  23: "Reyes.jpg",
  24: "Dominic's son.jpg",
  25: "Brian's Son.jpg",
  26: "Vince's Son.jpg"
}

#*********************************This question starts up the whole program
name = input('\x1b[3;35;91m' + "What is your name?: " + '\x1b[0m')
#This is the mainloop to proceed with the game and to allow for it to be looped when done
result = False
while not result:
  result = start(name)

#Picture links:
#https://images.app.goo.gl/paRozYBuciYsM5mP6
#https://images.app.goo.gl/oRHWLn9YGyisyqJV9
#https://images.app.goo.gl/VEyR4aDZpMiEv4ue6
#https://images.app.goo.gl/m8W4D43UYL2X7JKe8
#https://images.app.goo.gl/RicPJThKDhspKqzS8
#https://images.app.goo.gl/QQcACJP1unauotok6
#https://images.app.goo.gl/wymdyzeShAjJCkq4A
#https://images.app.goo.gl/TX8BqRgZc4XiL5kx5
#https://images.app.goo.gl/PCCtzKFstNNCjHQy6
#https://images.app.goo.gl/NXNPFUmRyJXMci8E6
#https://images.app.goo.gl/N2vkpr2NRfNdHAzS9
#https://images.app.goo.gl/7JzPckiheZkYsV8x7
#https://images.app.goo.gl/7JzPckiheZkYsV8x7
#https://images.app.goo.gl/BwnxZCjTcKnMzZQbA
#https://images.app.goo.gl/WkjVtsLibqGnN4xh7
#https://images.app.goo.gl/buSTCz4L6yzYDtHx8
#https://images.app.goo.gl/YhTnHVMNhXADfZrM8
#https://images.app.goo.gl/iWYtJhoxRxHBCQ686
#https://images.app.goo.gl/dM9igZdeNaJLnxzK8
#https://images.app.goo.gl/1u9n8PypJDLL29ix5
#https://images.app.goo.gl/JDzpNwDBd6PXHwbA7
#https://images.app.goo.gl/TSxVFTjR7dkHbjj4A
#https://images.app.goo.gl/wYEmaXJWUhkciHZ19
#https://images.app.goo.gl/kTLpNpFNpSST54Xu9
#https://images.app.goo.gl/nFyN4Km4YMg8raX88
#https://images.app.goo.gl/3Epvv2Z9jbiKjd7R8