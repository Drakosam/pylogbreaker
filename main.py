import os
import sys
from pathlib import Path

from PySide6.QtCore import QUrl, QObject, QCoreApplication, Qt
from PySide6.QtGui import QGuiApplication
from PySide6.QtQml import QQmlApplicationEngine

from models.filemodel import FileModel

CURRENT_DIRECTORY = Path(__file__).resolve().parent

if __name__ == '__main__':
    app = QGuiApplication()
    engine = QQmlApplicationEngine()

    file_model = FileModel()
    file_model.add_file(" Add File ")
    file_model.add_file("file1")
    file_model.add_file("file2")
    file_model.add_file("file3")
    engine.rootContext().setContextProperty("fileModel", file_model)

    file_version_model = FileModel()
    file_version_model.add_file("Version1")
    file_version_model.add_file("Version2")
    file_version_model.add_file("Version3")
    file_version_model.add_file("+")
    engine.rootContext().setContextProperty("fileVersionModel", file_version_model)

    filename = os.fspath(CURRENT_DIRECTORY / "qml/main.qml")
    url = QUrl.fromLocalFile(filename)


    def handle_object_created(obj: QObject | None, obj_url: QUrl) -> None:
        if obj is None and url == obj_url:
            QCoreApplication.exit(-1)


    engine.objectCreated.connect(handle_object_created, Qt.QueuedConnection)

    engine.load(url)

    if not engine.rootObjects():
        sys.exit(-1)

    app.exec()
