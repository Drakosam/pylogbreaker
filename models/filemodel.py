import typing
from dataclasses import dataclass, fields

from PySide6.QtCore import  QObject, QModelIndex, QByteArray, Qt, QAbstractListModel


@dataclass
class FileItem:
    name: str
    isStatic: bool


class FileModel(QAbstractListModel):
    def __init__(self, parent=QObject | None) -> None:
        super().__init__()
        self._items = []

    def rowCount(self, index: QModelIndex = QModelIndex()) -> int:
        return len(self._items)

    def roleNames(self) -> dict[int, QByteArray]:
        d = {}
        for i, field in enumerate(fields(FileItem)):
            d[Qt.DisplayRole + i] = field.name.encode()

        return d

    def data(self, index: QModelIndex, role: int = Qt.DisplayRole) -> typing.Any:
        if 0 <= index.row() < self.rowCount():
            item = self._items[index.row()]
            name = self.roleNames().get(role)
            if name:
                return getattr(item, name.decode())

    def add_file(self, name: str, is_static: bool = False):
        self.beginInsertRows(QModelIndex(), self.rowCount(), self.rowCount())
        self._items.append(FileItem(name, is_static))
        self.endInsertRows()
