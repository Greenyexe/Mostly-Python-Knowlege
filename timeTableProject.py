# WARNING! This program is extremely powerful and should be used with care. If you want to use this program, do so with good intentions. 

# Brought to you by the nerds Bruno Greenfield and Freya Murray

import time 
from random import randint as t 

#*****************************************************************************
  
hjk = ["History", "Language", "PE", "Science", "English", "PE",  "ICT", "Geography", "Science", "Language", "Maths", "Drama", "Science",  "English", "Dance", "Art", "Religious Studies", "Science", "Games",  "English", "Maths", "Language", "Religious Studies", "Geography", "Maths",  "DT", "PSHCEE", "Science", "English", "Maths", "Games", "Maths", "Histroy",  "English", "Science", "History", "Science", "Language", "English", "Maths", "DT", "Art", "Music", "Science", "Language", "DT", "Geography", "Religious Studies", "Science", "English", "Maths", "ICT"]
snw = ["Religious Studies", "Maths", "Language", "Science", "PSHCEE", "DT", "English", "Geography", "Science", "Games", "PE", "Art", "Science", "Drama", "History", "English", "English", "Science", "Language", "Dance", "Maths", "Enlish", "ICT", "Geography", "Maths", "Language",  "History", "PE", "English", "Maths", "Science", "Maths", "Music", "English", "Science", "Games", "Science", "DT", "Religious Studies", "Maths", "Language", "Geography", "History", "Science", "DT", "Language", "Religious Studies", "ICT", "Science", "English", "Maths", "Art"]
hkl = ["Music", "Language", "PE", "Science", "English", "PE", "Geography", "Art", "Science", "Language", "Maths", "Geography", "Science", "ICT", "Religious Studies", "English", "History", "Science", "Games", "Religious Studies", "Maths", "Language", "Dance", "English", "Maths", "DT", "PSHCEE", "Science", "Drama", "Maths", "Games", "Maths", "Religious Studies", "History", "Science", "English", "Science", "Language", "English", "Maths", "DT", "ICT", "Art", "Science", "Language", "DT", "English", "Ennglish", "Science", "History", "Maths", "Geography"]
hkm = ["History", "French", "PE", "Science", "English", "PE", "Art", "Religious Studies", "Science", "Language","Maths", "English", "Science", "Geography", "Histroy", "PSHCEE", "English", "Science", "Games", "ICT", "Maths", "Language", "Music", "English", "Maths", "DT", "Geography", "Science", "English", "Maths", "Games", "Maths", "English", "Art", "Science", "History", "Science", "Language", "Dance", "Maths", "DT", "Religious Studies", "Religious Studies", "Science", "Language", "DT", "Drama", "ICT", "Science", "Englsih", "Maths", "Geography"]
stf = ["Art", "Maths", "French", "Science", "Religious Studies", "DT", "History", "English Launguage", "Science", "Games", "PE", "Geography", "Science", "English", "ICT", "History", "Drama", "Science", "French", "English", "Maths"]
nbd = [""]
slo = [""]

#*****************************************************************************

def clear(): #Clears the screen
  print("\033c",end = "") # can't use os.system("cls") because it needs to work on both linux/mac and windows

#*****************************************************************************

def load(): #Loading screen
  suc = "\033[1m\033[38;2;255;0;0m" #Red
  what = ["Establishing SSH conection to Thomas-Hardye.Net", "Extracting TimeTable Data", "Conection failed -retrying","Conection Successful", "Brute-Forcing Password Hack", "Testing Data", "Verifying Your Time Table", "Patching attack"] #what is displayed
  lLen = ["_", "_","_","_","_","_","_", "_","_","_", "_", "_", "_", "_", "_", "_", "_", "_", "_", "_", "_", "_", "_", "_", "_", "_", "_", "_", "_", "_", "_"] #length of the loading bar
  
  try: 
    for j in range(len(what)): #for loop to display the loading bar
      for c in range(t(1, 3)): #for loop to display the loading bar
        for i in range(len(lLen)): #for loop to display the loading bar
          
          timeStart = time.time() #start time
          lLen[i] = suc + "__\033[0m" 
          print("\033[48;2;255;50;75m             \033[1mLOADING             \033[0m\n\nStatus [\033[93m" + str(j + 1) + "\033[0m - \033[93m"+ str(len(what)) + "\033[0m]\n\033[1m" + what[j]+"\033[0m\n\033[1m"+ "".join(lLen)+ "\033[0m\n\n\033[48;2;255;50;75m             \033[1mLOADING             \033[0m")

          lLen[i] = "\033[0m_\033[0m"
          time.sleep(0.065)
          print("\033c",end = "")


    clear()        
    print("\033[48;2;50;255;75m               \033[1mDONE              \033[0m\n") 
    lLen[i] = suc + "__\033[0m"
    print("Status [\033[38;2;0;255;0m" + str(j + 1) + "\033[0m - \033[38;2;0;255;0m"+ str(len(what)) + "\033[0m]")
    #print("\033[1m" + what[j]+"\033[0m") #
    #print("\033[1m"+ "".join(lLen)+ "\033[0m")#
    print("\n\033[48;2;50;255;75m               \033[1mDONE              \033[0m")    
    timeEnd = time.time() - timeStart #end time
    with open("output.txt","a") as f: #write to file
      f.write(str(timeEnd) + '\n') #write to file
    
    time.sleep(3) #wait 3 seconds
          

  except KeyboardInterrupt: #if the user presses ctrl+c
    timeEnd = time.time() - timeStart #end time
    with open("output.txt","a") as f: #write to file
      f.write(str(timeEnd) + '\n') #write to file

#*****************************************************************************

def difload(): #different loading screen
  clear()  
  print("[=--------------] 0%")
  time.sleep(t(1,2))
  clear()
  print("[===------------] 17%")
  time.sleep(t(1,2))
  clear()
  print("[=====----------] 34%")
  time.sleep(t(1,2))
  clear()
  print("[========-------] 47%")
  time.sleep(t(1,2))
  clear()
  print("[==========-----] 54%")
  time.sleep(t(1,2))
  clear()
  print("[===========----] 68%")
  time.sleep(t(1,2))
  clear()
  print("[============---] 81%")
  time.sleep(t(1,2))
  clear()
  print("[===============] 100%")
  time.sleep(2.5)
  clear()

#*****************************************************************************

def mainFunction(): #main function
  load() #load the loading screen
  print("\nYour TimeTable is listed below:") 
  print("\nWeek 1 Mon: ", ', '.join(yearClass[0:5])) #print the timetable
  print("\nWeek 1 Tue: ", ', '.join(yearClass[5:10])) #print the timetable
  print("\nWeek 1 Wed: ", ', '.join(yearClass[10:16])) #print the timetable
  print("\nWeek 1 Thu: ", ', '.join(yearClass[16:21])) #print the timetable
  print("\nWeek 1 Fri: ", ', '.join(yearClass[21:26])) #print the timetable
  print("\nWeek 2 Mon: ", ', '.join(yearClass[26:31])) #print the timetable
  print("\nWeek 2 Tue: ", ', '.join(yearClass[31:36])) #print the timetable
  print("\nWeek 2 Wed: ", ', '.join(yearClass[36:42])) #print the timetable
  print("\nWeek 2 Thu: ", ', '.join(yearClass[42:47])) #print the timetable
  print("\nWeek 2 Fri: ", ', '.join(yearClass[47:52])) #print the timetable
  time.sleep(6) #wait 6 seconds
  print("\nHopefully we sucessfully creeped you out! Have a nice day :)") #print the end message
  time.sleep(10) #wait 10 seconds
  difload() #load the different loading screen

#*****************************************************************************

print("Welcome to The TimeTable Project™!") #print the welcome message
time.sleep(2) #wait 2 seconds
print("\nDeveloped by Bruno and Freya") #print the developer message
time.sleep(2) #wait 2 seconds

Class = input("\nInput your tutor group (lower case, collage then group no space): ") #ask for the class

if_dict = {"hjk":list(hjk), # create a dictionary with the classes
          "snw":list(snw),
          "hkl":list(hkl),
          "hkm":list(hkm),
          "stf":list(stf),
          "nbd":list(nbd),
          "slo":list(slo)}

for i in if_dict.keys(): # for loop to check if the class is in the dictionary
  if Class in i: # if the class is in that particular index of the dictionary
    yearClass = if_dict[Class] # assign the class to the yearClass variable
    mainFunction() # call the main function
else: # if the class is not in the dictionary
  print("That is not a tutor group!") #print the error message
  time.sleep(4) #wait 4 seconds
  difload() #load the different loading screen