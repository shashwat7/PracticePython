"""
This a class represents a directory in a file system. It contains set of files and set of directories
"""
from file_system.file import File


class Directory:
    directories = {}  # dict to keep references of all directories

    def __init__(self, parent_directory, directory_name):
        if directory_name in Directory.directories:
            raise Exception('Directory {} already exists!'.format(directory_name))
        self.parent_directory = parent_directory # Can be None for root directory
        self.directory_name = directory_name
        self.files = set()
        self.sub_directories = set()
        Directory.directories[directory_name] = self
        if parent_directory:
            parent_directory.add_subdir(self)

    def __str__(self):
        return self.directory_name

    def list_all_files(self, recursively=False, list_hidden_files=False):
        """
        List all files in this directory.
        """
        for file in sorted(self.files):
            if not file.is_hidden() or list_hidden_files:
                print('- ' + str(file))
        if recursively:
            for sub_dir in sorted(self.sub_directories):
                print('> ' + str(sub_dir))
                sub_dir.list_all_files(recursively=True, list_hidden_files=list_hidden_files)

    def add_subdir(self, sub_dir):
        assert type(sub_dir) is Directory, 'sub_dir must be an instance of Directory'
        self.sub_directories.add(sub_dir)

    def add_file(self, file: File):
        assert type(file) is File, 'file must be an instance of File'
        self.files.add(file)

