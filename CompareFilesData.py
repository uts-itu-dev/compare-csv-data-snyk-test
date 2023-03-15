import os

OldFile = "OldFile.txt"
NewFile = "NewFile.txt"

OldPath = os.path.abspath(OldFile)
NewPath = os.path.abspath(NewFile)

if os.path.exists(OldPath) and os.path.exists(NewPath):
    
    OldFileObj = open(OldPath, mode = 'r')
    NewFileObj = open(NewPath, mode = 'r')

    OldList = OldFileObj.read().split('\n')
    NewList = NewFileObj.read().split('\n')

    OldList.sort()
    NewList.sort()

    if OldList == NewList: 
        print("Files are the same.")
    else:
        print("Files are not the same.")

        #lol