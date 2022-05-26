text = "Yooooooo!\nThis is some text!\nSee ya!"

with open("test.txt", "a") as file: # the w will overwrite any existing text and a will append some text on the end
    file.write(text)