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

        self.log_display = 5
        self.log_display_mod = 0

        self.file_metadata = {}

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

        self.file_metadata[file_name] = {
            'line_mod': 0
        }

    def recalculate_log_display_size(self, height):
        self.log_display = int(height / 35)
        self.refresh_log_area()

    def swich_page(self, direction):
        if self.file_selected == '':
            return

        if direction == 0 and self.log_display_mod > 0:
            self.log_display_mod -= 1
        elif direction == 1 and self.log_display_mod < len(self.file_version[self.file_selected].lines) - self.log_display:
            self.log_display_mod += 1

        self.refresh_log_area()

    def refresh_log_area(self):
        if self.file_selected == '':
            return

        self.show_log_lines.clear()

        for i in range(self.log_display):
            self.show_log_lines.add_line(self.file_version[self.file_selected].lines[i+self.log_display_mod])

    def select_file(self, name):
        self.file_metadata[self.file_selected]['line_mod'] = self.log_display_mod

        self.file_selected = name
        self.show_file_version()

        self.log_display_mod = self.file_metadata[self.file_selected]['line_mod']

        self.refresh_log_area()

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
