import os
import copy

from backend.logItem import LogItem
from models.filemodel import FileModel


class FileManagerClass:
    def __init__(self):
        self.fileList: FileModel = None
        self.fileVersionList: FileModel = None
        self.show_log_lines = None
        self.file_selected = ''
        self.list_items = {}
        self.file_version = {}

    def set_file_list(self, _obj):
        self.fileList = _obj

    def set_file_version_list(self, _obj):
        self.fileVersionList = _obj

    def set_show_log_lines(self, _obj):
        self.show_log_lines = _obj

    def add_file_to_list(self, path):
        file_name = os.path.basename(path)
        self.fileList.add_file(file_name)
        self.list_items[file_name] = ['orgin']
        if self.file_selected == '':
            self.file_selected = file_name
            self.show_file_version()

        self.file_version[file_name] = LogItem(file_name, path)

    def select_file(self, name):
        self.file_selected = name
        print('file selected change to :: ', self.file_selected)
        self.show_file_version()

        self.show_log_lines.clear()

        for i in range(5):
            self.show_log_lines.add_line(self.file_version[self.file_selected].lines[i])

    def add_version_for_file(self):
        if self.file_selected == '':
            return

        new_ver = len(self.list_items[self.file_selected]) + 1
        new_ver_name = f'{self.file_selected}(ver_{new_ver})'
        self.list_items[self.file_selected].append(new_ver_name)
        self.show_file_version()
        self.file_version[new_ver_name] = copy.deepcopy(self.file_version[self.file_selected])

    def show_file_version(self):
        self.fileVersionList.clear()
        for item_name in self.list_items[self.file_selected]:
            self.fileVersionList.add_file(item_name)
        self.fileVersionList.add_file('+', True)
