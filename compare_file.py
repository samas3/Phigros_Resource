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
def compare_folders(path1, path2):
    """
    Compare files in two folders with the same structure.
    Returns a dict with 'missing' (files only in path1) and 'different' (files that differ).
    """
    missing = []
    different = []
    for i in os.listdir(path1):
        file1_path = os.path.join(path1, i)
        file2_path = os.path.join(path2, i)
        if os.path.isfile(file1_path):
            if os.path.isfile(file2_path):
                if not compare_files(file1_path, file2_path):
                    print(f'{path1}/{i} is different')
                    different.append(i)
            else:
                print(f'New file: {file1_path}')
                missing.append(i)
    return {'missing': missing, 'different': different}

def compare_folders_interactive():
    """Interactive version that prompts for folder paths."""
    path1 = input('First folder path: ')
    path2 = input('Second folder path: ')
    return compare_folders(path1, path2)

if __name__ == '__main__':
    compare_folders_interactive()