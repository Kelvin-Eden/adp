import os
from PySide6.QtGui import *
from PySide6.QtWidgets import QMenu
import resources

base_dir = os.path.dirname(__file__)


class QuickActions(QMenu):
    def __init__(self, parent, listwidget=None):
        super(QuickActions, self).__init__(parent=parent)
        self.listwidget = listwidget

        self.setStyleSheet("background-color: white; color: black; font: 10pt 'Maven Pro'; icon-size: 25px;")

        self.rename_action = self.action(name='Rename', icon_path=":icons/edit.ico")
        self.export_action = self.action(name='Export', icon_path=':icons/export.ico')
        self.delete_action = self.action(name='Delete', icon_path=':icons/delete.ico')
        self.delete_all_action = self.action(name='Clear Records', icon_path=':icons/delete_all.ico')

        self.addActions([self.rename_action, self.export_action, self.delete_action, self.delete_all_action])

    @staticmethod
    def action(name, icon_path: str = None):
        action = QAction(text=name)
        if icon_path:
            action.setIcon(QIcon(icon_path))
        return action
