import os

def selectSet(fileWorker):
    directory = './'  

    textFilesInDir = [f for f in os.listdir(directory) if f.endswith('.txt')]

    if textFilesInDir:
        for file in textFilesInDir:
            if fileWorker == file:
                print("ok")
                break
    else:
        print("No text files in current directory. Make a new set first.")

    return fileWorker
