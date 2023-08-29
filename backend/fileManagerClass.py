import os

from models.filemodel import FileModel


class FileManagerClass:
    def __init__(self):
        self.fileList: FileModel = None
        self.fileVersionList: FileModel = None
        self.file_selected = ''
        self.list_items = {}

    def set_file_list(self, _obj):
        self.fileList = _obj

    def set_file_version_list(self, _obj):
        self.fileVersionList = _obj

    def add_file_to_list(self, path):
        file_name = os.path.basename(path)
        self.fileList.add_file(file_name)
        self.list_items[file_name] = ['orgin']
        if self.file_selected == '':
            self.file_selected = file_name
            self.show_file_version()

    def select_file(self, name):
        self.file_selected = name
        print('file selected change to :: ', self.file_selected)
        self.show_file_version()

    def add_version_for_file(self):
        if self.file_selected == '':
            return

        new_ver = len(self.list_items[self.file_selected]) +1
        self.list_items[self.file_selected].append(f'{self.file_selected}(ver_{new_ver})')
        self.show_file_version()

    def show_file_version(self):
        self.fileVersionList.clear()
        for item_name in self.list_items[self.file_selected]:
            self.fileVersionList.add_file(item_name)
        self.fileVersionList.add_file('+',True)
