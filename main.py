import os
import sys
from pathlib import Path

from PySide6.QtCore import QUrl, QObject, QCoreApplication, Qt
from PySide6.QtGui import QGuiApplication
from PySide6.QtQml import QQmlApplicationEngine

from models.backend import BackendApp
from models.filemodel import FileModel

CURRENT_DIRECTORY = Path(__file__).resolve().parent

if __name__ == '__main__':
    app = QGuiApplication()
    engine = QQmlApplicationEngine()

    file_model = FileModel()
    file_version_model = FileModel()
    backend = BackendApp()
    backend.set_file_version_model(file_version_model)

    file_model.add_file(" Add File ")
    file_version_model.add_file("+")

    engine.rootContext().setContextProperty("fileModel", file_model)
    engine.rootContext().setContextProperty("fileVersionModel", file_version_model)
    engine.rootContext().setContextProperty("backendApp", backend)

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
