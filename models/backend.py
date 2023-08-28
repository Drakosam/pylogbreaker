from PySide6.QtCore import QObject, Slot
from PySide6.QtQml import QmlElement


class BackendApp(QObject):

    def __int__(self):
        super().__init__()
        self.file_version = None

    @Slot(str)
    def test(self, name):
        print('test', name)

    def set_file_version_model(self, f_ver):
        self.file_version = f_ver

    @Slot()
    def addVersion(self):
        self.file_version.add_file("ver 1")
