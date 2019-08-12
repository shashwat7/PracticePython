files = {}  # A dictionary to keep names of all files


class File:
    """
    This file represents a file in a file system
    """

    def __init__(self, file_path: str, location):
        if file_path in files:
            raise Exception('File {} already exists!'.format(file_path))
        self.file_path = file_path
        self.location = location
        files[file_path] = self
        location.add_file(self)

    def __str__(self):
        return str(self.location) + '/' + self.file_path

    def is_hidden(self) -> bool:
        return self.file_path.startswith('.')
