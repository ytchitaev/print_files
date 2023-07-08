import os
import argparse
import glob


def print_files(directory, exclude_git=False, filters=None, extension=None, list_files=False, write=False):
    files_to_print = []

    for filter_pattern in filters:
        filter_pattern = os.path.join(directory, filter_pattern)
        matching_files = glob.glob(filter_pattern)
        
        for file_path in matching_files:
            if exclude_git and '.git' in file_path:
                continue

            if extension is None or file_path.endswith(extension):
                files_to_print.append(file_path)

    if write:
        with open("files_content.txt", 'w') as file:
            if list_files:
                for file_path in files_to_print:
                    file.write(file_path + '\n')
            else:
                for file_path in files_to_print:
                    file.write("-- FILE: " + file_path + " BEGINS\n")
                    with open(file_path, 'r') as f:
                        file.write(f.read())
                    file.write('\n' + '-' * 50 + '\n')
    else:
        if list_files:
            for file_path in files_to_print:
                print(file_path)
        else:
            for file_path in files_to_print:
                print_file_contents(file_path)


def print_file_contents(file_path):
    with open(file_path, 'r') as file:
        contents = file.read()
        print(f"-- FILE: {file_path} BEGINS")
        print(contents, '\n')
        print('-' * 50)  # Print a line of dashes


# Create the argument parser
parser = argparse.ArgumentParser(
    description='Print files and their contents in a directory and subdirectories.')

# Add the 'start_directory' argument
parser.add_argument('--start_directory', metavar='start_directory',
                    type=str, help='the directory to start the search')

# Add the '--exclude-git' flag
parser.add_argument('--exclude-git', dest='exclude_git',
                    action='store_true', help='exclude the .git directory')

# Add the '--filter' flag with multiple values
parser.add_argument('--filter', dest='filter', type=str, nargs='+',
                    help='filter the files and directories to be printed')

# Add the '--extension' argument
parser.add_argument('--extension', dest='extension', type=str,
                    help='filter files by extension')

# Add the '--list_files' flag
parser.add_argument('--list_files', dest='list_files',
                    action='store_true', help='list the files without printing their contents')

# Add the '--write' flag
parser.add_argument('--write', dest='write',
                    action='store_true', help='write the output to files_content.txt')

# Parse the command-line arguments
args = parser.parse_args()

# Call the function with the specified directory, flags, and extension
print_files(args.start_directory,
            exclude_git=args.exclude_git,
            filters=args.filter,
            extension=args.extension,
            list_files=args.list_files,
            write=args.write)
