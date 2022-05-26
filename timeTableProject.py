# WARNING! This program is extremely powerful and should be used with care. If you want to use this program, do so with good intentions. 

# Brought to you by the nerds Bruno Greenfield and Freya Murray

import time
from random import randint as t
  
hjk = ["History", "Language", "PE", "Science", "English", "PE",  "ICT", "Geography", "Science", "Language", "Maths", "Drama", "Science",  "English", "Dance", "Art", "Religious Studies", "Science", "Games",  "English", "Maths", "Language", "Religious Studies", "Geography", "Maths",  "DT", "PSHCEE", "Science", "English", "Maths", "Games", "Maths", "Histroy",  "English", "Science", "History", "Science", "Language", "English", "Maths", "DT", "Art", "Music", "Science", "Language", "DT", "Geography", "Religious Studies", "Science", "English", "Maths", "ICT"]
snw = ["Religious Studies", "Maths", "Language", "Science", "PSHCEE", "DT", "English", "Geography", "Science", "Games", "PE", "Art", "Science", "Drama", "History", "English", "English", "Science", "Language", "Dance", "Maths", "Enlish", "ICT", "Geography", "Maths", "Language",  "History", "PE", "English", "Maths", "Science", "Maths", "Music", "English", "Science", "Games", "Science", "DT", "Religious Studies", "Maths", "Language", "Geography", "History", "Science", "DT", "Language", "Religious Studies", "ICT", "Science", "English", "Maths", "Art"]
hkl = ["Music", "Language", "PE", "Science", "English", "PE", "Geography", "Art", "Science", "Language", "Maths", "Geography", "Science", "ICT", "Religious Studies", "English", "History", "Science", "Games", "Religious Studies", "Maths", "Language", "Dance", "English", "Maths", "DT", "PSHCEE", "Science", "Drama", "Maths", "Games", "Maths", "Religious Studies", "History", "Science", "English", "Science", "Language", "English", "Maths", "DT", "ICT", "Art", "Science", "Language", "DT", "English", "Ennglish", "Science", "History", "Maths", "Geography"]
hkm = ["History", "French", "PE", "Science", "English", "PE", "Art", "Religious Studies", "Science", "Language","Maths", "English", "Science", "Geography", "Histroy", "PSHCEE", "English", "Science", "Games", "ICT", "Maths", "Language", "Music", "English", "Maths", "DT", "Geography", "Science", "English", "Maths", "Games", "Maths", "English", "Art", "Science", "History", "Science", "Language", "Dance", "Maths", "DT", "Religious Studies", "Religious Studies", "Science", "Language", "DT", "Drama", "ICT", "Science", "Englsih", "Maths", "Geography"]
stf = ["Art", "Maths", "French", "Science", "Religious Studies", "DT", "History", "English Launguage", "Science", "Games", "PE", "Geography", "Science", "English", "ICT", "History", "Drama", "Science", "French", "English", "Maths"]
nbd = [""]
slo = [""]

def clear():
  print("\033c",end = "") # can't use os.system("cls") because it needs to work on both linux/mac and windows

def load():
  suc = "\033[1m\033[38;2;255;0;0m"
  what = ["Establishing SSH conection to Thomas-Hardye.Net", "Extracting TimeTable Data", "Conection failed -retrying","Conection Successful", "Brute-Forcing Password Hack", "Testing Data", "Verifying Your Time Table", "Patching attack"]
  lLen = ["_", "_","_","_","_","_","_", "_","_","_", "_", "_", "_", "_", "_", "_", "_", "_", "_", "_", "_", "_", "_", "_", "_", "_", "_", "_", "_", "_", "_"] 
  
  try:
    for j in range(len(what)):
      for c in range(t(1, 3)):
        for i in range(len(lLen)):
          
          timeStart = time.time()
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
    timeEnd = time.time() - timeStart
    with open("output.txt","a") as f:
      f.write(str(timeEnd) + '\n')
    
    time.sleep(3)
          

  except KeyboardInterrupt:
    timeEnd = time.time() - timeStart
    with open("output.txt","a") as f:
      f.write(str(timeEnd) + '\n')

def difload():
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

def mainFunction():
  load()
  print("\nYour TimeTable is listed below:")
  print("\nWeek 1 Mon: ", ', '.join(yearClass[0:5]))
  print("\nWeek 1 Tue: ", ', '.join(yearClass[5:10]))
  print("\nWeek 1 Wed: ", ', '.join(yearClass[10:16]))
  print("\nWeek 1 Thu: ", ', '.join(yearClass[16:21]))
  print("\nWeek 1 Fri: ", ', '.join(yearClass[21:26]))
  print("\nWeek 2 Mon: ", ', '.join(yearClass[26:31]))
  print("\nWeek 2 Tue: ", ', '.join(yearClass[31:36]))
  print("\nWeek 2 Wed: ", ', '.join(yearClass[36:42]))
  print("\nWeek 2 Thu: ", ', '.join(yearClass[42:47]))
  print("\nWeek 2 Fri: ", ', '.join(yearClass[47:52]))
  time.sleep(6)
  print("\nHopefully we sucessfully creeped you out! Have a nice day :)")
  time.sleep(10)
  difload()

print("Welcome to The TimeTable Project™!")
time.sleep(2)
print("\nDeveloped by Bruno and Freya")
time.sleep(2)

Class = input("\nInput your tutor group (lower case, collage then group no space): ")

if Class == "hjk":
  yearClass = list(hjk)
  mainFunction()
elif Class == "snw":
  yearClass = list(snw)
  mainFunction()  
elif Class == "hkl":
  yearClass = list(hkl)
  mainFunction()
elif Class == 'hkm':
  yearClass = list(hkm)
  mainFunction()
elif Class == "stf":
  yearClass = list(stf)
  mainFunction()
elif Class == "nbd":
  yearClass = list(nbd)
  mainFunction()
elif Class == "slo":
  yearClass = list(slo)
  mainFunction()
else:
  print("That is not a tutor group!")
  time.sleep(4)
  difload()