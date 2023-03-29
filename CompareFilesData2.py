with open('OldFile.txt', 'r') as OldFile, open('NewFile.txt', 'r') as NewFile:
    
    # Read the contents of the files
    OldFile_contents = OldFile.read()
    NewFile_contents = NewFile.read()

    # Split the contents of the files into lines
    OldFile_lines = OldFile_contents.split('\n')
    NewFile_lines = NewFile_contents.split('\n')

    # Compare the contents
    if OldFile_contents == NewFile_contents:
        print("The files are the same")
    else:
        print("The files are different")
