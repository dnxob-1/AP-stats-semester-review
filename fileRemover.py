import os

def removeFiles(wantGone):
    directory = './'  

    textFilesInDir = [f for f in os.listdir(directory) if f.endswith('.txt')]

    if textFilesInDir:
        try:
            for i in range(len(wantGone)):
                os.remove(wantGone[i])
                print("Removed:", wantGone[i])
        except FileNotFoundError:
            print("Error: The file does not exist")

    else:
        print("No text files left in this current directory.")
