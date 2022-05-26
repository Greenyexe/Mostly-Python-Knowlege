import os
import shutil

try:
    os.remove("test.txt")
    #os.rmdir(emptyFolder) #how to remove empty folder
    #shutil.rmtree(folder) #how to delete populated folder
except FileNotFoundError:
    print("That file was not found!")
except PermissionError:
    print("you do not have permision to delete that")
except OSError:
    print("you cannot delete that using that function")