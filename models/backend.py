from PySide6.QtCore import QObject, Slot
from PySide6.QtQml import QmlElement
from backend import fileManager


class BackendApp(QObject):

    def __init__(self):
        super().__init__()
        self.file_version = None

    @Slot(str)
    def test(self, name):
        print('test', name)

    def set_file_version_model(self, f_ver):
        self.file_version = f_ver

    @Slot()
    def addVersion(self):
        fileManager.add_version_for_file()

    @Slot(str)
    def openFileProc(self, path):
        fileManager.add_file_to_list(path)

    @Slot(str)
    def selectFile(self, file_name):
        fileManager.select_file(file_name)

    @Slot(int)
    def setLogDisplayArea(self, log_area):
        fileManager.recalculate_log_display_size(log_area)

    @Slot(int)
    def swichPage(self,direction):
        fileManager.swich_page(direction)
