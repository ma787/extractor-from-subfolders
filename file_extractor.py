import configparser
import os
import shutil


def move_files(path, folder_path, file_types, copy=False):
    """Copies/moves the user's files to the destination directory."""
    for elem in os.listdir(path):  # loops over every file in the current directory
        current_path = path + "/" + elem

        if os.path.isfile(current_path):
            file_name, file_ext = os.path.splitext(current_path)

            if file_ext in file_types:
                if copy:
                    shutil.copy(current_path, folder_path)
                else:
                    shutil.move(current_path, folder_path)
        
        elif os.path.isdir(current_path):
            move_files(current_path, folder_path, file_types, copy=copy)  # calls itself on sub-directories

def get_dir():
    """Asks the user for the destination directory to copy/move their files to."""
    path = os.path.abspath(os.getcwd())

    directory = input("Please enter the destination path for your files: ")
    
    while (not os.path.isdir(directory)) or (directory in path) :
        directory = input("Please enter a valid directory (different to the current destination): ")

    directory += "/Extracted Files"
    
    os.mkdir(directory)
    return directory

def main():
    path = os.path.abspath(os.getcwd())
    destination = get_dir()

    config = configparser.ConfigParser()
    config.read("extensions.ini")
    extensions = config["DEFAULT"]["file_types"].split(", ")  
    # gets the file extensions to check for from the config file

    copy_pref = input("""
    Please enter 'y' if you would like to preserve the existing files and copy them instead of moving
    them: """).lower()

    if copy_pref == "y":
        chose_copy = True
    else:
        chose_copy = False

    move_files(path, destination, extensions, copy=chose_copy)


main()
