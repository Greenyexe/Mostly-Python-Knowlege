import os


def artists():
  pass

def albums():
  pass

def songs():
  pass

def shuffle():
  pass

def search():
  pass

def back():
  os.system("clear")
  main_screen()

def chose_option_music(option):
  if option == "1":
    artists()
  elif option == "2":
    albums()
  elif option == "3":
    songs()
  elif option == "4":
    shuffle()
  elif option == "5":
    search()
  elif option == "6":
    back()
  else:
    print("\nInvalid option")
    music()

def music():
  os.system("clear")
  print("\n1: Artists")
  print("2: Albums")
  print("3: Songs")
  print("4: Shuffle")
  print("5: Search")
  print("6: Back")

  chose_option_music(input())


def chose_option_main(option):
  if option == "1":
      music()
  elif option == "2":
      os.system("sudo raspi-config")
  elif option == "3":
      os.system("sudo shutdown now")


def main_screen():
  print("\nChose one of the following options:")
  print("\n1: Music")
  print("2: Settings")
  print("3: Shutdown")

  chose_option_main(input())

print("Welcome to the great greatness")

main_screen()