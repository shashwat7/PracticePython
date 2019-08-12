"""
This is the main class for the file system. This file system supports following
functions:
1. mkdir <dir name>: create a directory
2. touch <file name>: creates a file in the current directory.
3. ls [dir name]: list all non-hidden files in the directory. Supports argument, `-a` and `-l`.
4. cd [dir name]: move to a different directory
"""

import argparse
from file_system.directory import Directory
from file_system.file import File

USER_NAME = 'shashwat'


def init():
    """Initializes the file system"""
    # Create root directory
    root_dir = Directory(directory_name='/', parent_directory=None)
    # Create home directory
    Directory(
        directory_name='/home/'+USER_NAME,
        parent_directory=Directory(directory_name='/home', parent_directory=root_dir)
    )


def cd(current_dir: Directory, path: str) -> Directory:
    """This function implements the `cd` function in command line"""
    dir_path = path if path.startswith('/') else str(current_dir) + '/' + path
    if dir_path.endswith('/'):
        dir_path = path[0:-1]
    if dir_path == '..':
        if current_dir.parent_directory is not None:
            return current_dir.parent_directory
        else:
            raise Exception('There is no parent directory for a root directory')
    elif dir_path not in Directory.directories:
        raise Exception('Directory {} does not exist!'.format(dir_path))
    else:
        return Directory.directories[dir_path]


def ls(current_dir: Directory, path: str = None, display_hidden: bool = False, recursively: bool = False):
    """This function implements the `ls` function"""
    if path is None:
        current_dir.list_all_files(recursively, display_hidden)
    else:
        if path != '/' and path.endswith('/'):
            path = path[0:-1]
        if path not in Directory.directories:
            raise Exception('Directory {} does not exist!'.format(path))
        else:
            Directory.directories[path].list_all_files(recursively, display_hidden)


def mkdir(current_dir: Directory, path: str, create_parent_dir: bool = False):
    """This function implements the `mkdir` function. It supports -p option, if enabled
    then it will create parent directory first if it doesn't exist"""
    dir_name = path if path.startswith('/') else current_dir.directory_name + '/' + path
    parent_dir_path = dir_name[0:dir_name.rfind('/')]
    if create_parent_dir and parent_dir_path not in Directory.directories:
        mkdir(current_dir, parent_dir_path, True)
    if not create_parent_dir and parent_dir_path not in Directory.directories:
        raise Exception('Unable to create directory because parent dir {} does not exist'.format(parent_dir_path))
    Directory(directory_name=dir_name, parent_directory=Directory.directories[parent_dir_path])


def touch(current_dir: Directory, path: str) -> File:
    """This function implements the `touch` function"""
    file_path = path if path.startswith('/') else current_dir.directory_name + '/' + path
    dir_name = file_path[0:file_path.rfind('/')]
    if dir_name not in Directory.directories:
        raise Exception('Directory {} does not exist'.format(dir_name))
    return File(file_path, Directory.directories[dir_name])


def main():
    init()  # Initialize
    current_dir = Directory.directories['/home/'+USER_NAME]
    # TODO: Make it an CLI app
    ls(current_dir=current_dir, path='/', recursively=True)
    mkdir(current_dir, path='/home/shashwat/testing', create_parent_dir=True)
    current_dir = cd(current_dir, 'testing')
    touch(current_dir, 'hello_world.py')
    ls(current_dir, path=None, recursively=True)


if __name__ == '__main__':
    main()