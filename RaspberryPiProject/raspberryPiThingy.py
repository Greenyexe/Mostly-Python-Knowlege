import os

def play_music():
  pass

def stop_music():
  pass


def music():
  os.system("clear")
  print("Welcome to the music player! Chose one of the following options:")
  print("\n1. Play music")
  print("2. Stop music")
  print("3. Exit to main screen")

  choice = str(input())
  
  if choice == "1":
    play_music()
  elif choice == "2":
    stop_music()
  elif choice == "3":
    main_screen()
  else:
    print("Invalid input\n")
    music()


def main_screen():
  os.system("clear")
  print("Welcome to the great OS! Chose one of the following options:")
  print("\n1. Music")
  print("2. Settings")
  print("3. Exit to linux")
  print("4. Shutdown")

  choice = input()
  
  if choice == "1":
    music()
  elif choice == "2":
    os.system("sudo raspi-config")
  elif choice == "3":
    exit()
  elif choice == "4":
    os.system("sudo shutdown -h now")
  else:
    print("Invalid input\n")
    main_screen()

main_screen()