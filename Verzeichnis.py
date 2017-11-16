import os

for folderName, subfolders, filenames in os.walk("C:\\Users\Anass.Ben\Downloads"):
    print('The current folder is '+folderName)

    for filename in filenames:
        print('          FILE INSIDE '+ folderName + ': ' + filename)
    for subfolder in subfolders:
        print('         SUBFOLDER OF '+ folderName + ': ' + subfolder)
    print('')
        

