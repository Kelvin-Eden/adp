from PySide6.QtCore import Qt, Signal
from PySide6.QtGui import QIcon
from PySide6.QtWidgets import QListWidget, QListWidgetItem


class ListWidgetItem(QListWidgetItem):

    def __init__(self, name, icon_path: str = None):
        QListWidgetItem.__init__(self)
        self.name = name
        self.icon_path = icon_path

        self.setText(self.name)
        if self.icon_path:
            self.setIcon(QIcon(self.icon_path))


class ListWidget(QListWidget):
    doubleClicked = Signal(bool)

    def __init__(self, items_names: list[str] = None, icon_path=None, funLMB=None, funRMB=None):
        QListWidget.__init__(self)
        self.items_names = items_names
        self.icon_path = icon_path
        self.funRMB = funRMB
        self.funLMB = funLMB

        if self.items_names:
            for item_name in self.items_names:
                self.add_item(item_name=item_name)

    def add_item(self, item_name: str):
        self.addItem(ListWidgetItem(name=item_name, icon_path=self.icon_path))

    def mouseDoubleClickEvent(self, event):
        if event.button() == Qt.LeftButton:
            self.doubleClicked.emit(True)
            if self.funLMB:
                self.funLMB()

    def mouseReleaseEvent(self, event):
        if event.button() == Qt.RightButton:
            if self.funRMB:
                self.funRMB()
