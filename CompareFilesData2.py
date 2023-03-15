with open('OldFile.txt', 'r') as file1, open('NewFile.txt', 'r') as file2:
    # Read the contents of the files
    file1_contents = file1.read()
    file2_contents = file2.read()

    # Split the contents of the files into lines
    file1_lines = file1_contents.split('\n')
    file2_lines = file2_contents.split('\n')

    # Compare the contents
    if file1_contents == file2_contents:
        print("The files are the same")
    else:
        print("The files are different")
