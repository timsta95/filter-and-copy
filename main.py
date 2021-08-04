import os, shutil

ROOT = input('Root directory: ')
TARGET = input('Target directory: ')
MATCH = input('Match patterns: ').split()
FILE_EXT = input('File extension: ')

def find_matching_files(root, *strings, extension=''):
    files = []
    for file in os.listdir(root):
        if any(x in file for x in strings) and file.endswith(extension):
            files.append(file)
    print(f'Number of files found: {len(files)}')
    return files

def copy_files(root, files, to_dir):
    for idx, file in enumerate(files):
        shutil.copyfile(root + '\\' + file, to_dir + '\\' + file)
        print(f'Number of files copied: {idx + 1}/{len(files)} -- Current file: {file}')
    print(f'Files copied to {to_dir}')

def main():
    matching_files = find_matching_files(ROOT, *MATCH, extension=FILE_EXT)
    copy_files(ROOT, matching_files, TARGET)

if __name__ == '__main__':
    main()
