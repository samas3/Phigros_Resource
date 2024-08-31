import os
def compare_files(file1, file2):
    with open(file1, 'rb') as f1:
        with open(file2, 'rb') as f2:
            while True:
                b1 = f1.read(1024)
                b2 = f2.read(1024)
                if b1 != b2:
                    return False
                if not b1:
                    return True
path1 = input('First folder path: ')
path2 = input('Second folder path: ')
for i in os.listdir(path1):
    if os.path.isfile(os.path.join(path1, i)):
        if os.path.isfile(os.path.join(path2, i)):
            if not compare_files(os.path.join(path1, i), os.path.join(path2, i)):
                print(path1 + '/' + i, 'is different')