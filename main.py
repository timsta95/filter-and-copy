import os, shutil, sys

def validate_dir(msg):
    while True:
        input_dir = input(msg)
        if not os.path.exists(input_dir):
            print('This path does not exist, please try again.')
            continue
        break
    return input_dir

def find_matching_files(root, strings, extensions):
    files = []
    for file in os.listdir(root):
        if any(x in file for x in strings) and any(file.endswith(ext) for ext in extensions):
            files.append(file)
    print(f'Number of files found: {len(files)}')
    return files

def copy_files(root, files, to_dir):
    if files:
        for idx, file in enumerate(files):
            shutil.copyfile(root + '\\' + file, to_dir + '\\' + file)
            print(f'Number of files copied: {idx + 1}/{len(files)} -- Current file: {file}')
        print(f'Files copied to {to_dir}')
    else:
        print('No files were copied')

def search_new_pattern():
    yes = {'yes', 'y', 'ye', ''}
    no = {'no', 'n'}
    given_answer = 'invalid'
    while given_answer == 'invalid':
        choice = input('Search for new pattern? [yes/ no]: ').lower()
        if choice in yes:
            given_answer = True
            return given_answer
        elif choice in no:
            given_answer = False
            return given_answer
        else:
            sys.stdout.write('Please respond with \'yes\' or \'no\'\n' )
        

def main():
    root = validate_dir('Root directory: ')
    target = validate_dir('Target directory: ')
    while True:
        match = input('Match pattern(s): ').split()
        file_ext = input('File extension(s): ').split()
        matching_files = find_matching_files(root, match, file_ext)
        copy_files(root, matching_files, target)
        answer = search_new_pattern()
        if answer == False:
            break

if __name__ == '__main__':
    main()
