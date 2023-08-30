import typing
from dataclasses import dataclass, fields

from PySide6.QtCore import QObject, QModelIndex, QByteArray, Qt, QAbstractListModel


@dataclass
class LogItem:
    name: str


class LogItemList(QAbstractListModel):
    def __init__(self, parent=QObject | None) -> None:
        super().__init__()
        self._items = []

    def rowCount(self, index: QModelIndex = QModelIndex()) -> int:
        return len(self._items)

    def roleNames(self) -> dict[int, QByteArray]:
        d = {}
        for i, field in enumerate(fields(LogItem)):
            d[Qt.DisplayRole + i] = field.name.encode()
        return d

    def data(self, index: QModelIndex, role: int = Qt.DisplayRole) -> typing.Any:
        if 0 <= index.row() < self.rowCount():
            item = self._items[index.row()]
            name = self.roleNames().get(role)
            if name:
                return getattr(item, name.decode())

    def add_line(self, text: str):
        self.beginInsertRows(QModelIndex(), self.rowCount(), self.rowCount())
        print('add line :: ', text)
        self._items.append(LogItem(text))
        self.endInsertRows()

    def clear(self):
        self.beginResetModel()
        self._items = []
        self.endResetModel()
