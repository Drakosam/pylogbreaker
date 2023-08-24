import sys

from PySide6.QtCore import QUrl
from PySide6.QtGui import QGuiApplication
from PySide6.QtQml import QQmlApplicationEngine

if __name__ == '__main__':
    app = QGuiApplication()

    engine = QQmlApplicationEngine()
    engine.load(QUrl('qml/main.qml'))

    if not engine.rootObjects():
        sys.exit(-1)

    app.exec()
