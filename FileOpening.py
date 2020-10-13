def fileopening():
    file_path = input("Enter you binary file path")
    file = open(file_path, "r+")
    lines = file.readlines()
    for line in lines:
        print(line)
    file.close()
