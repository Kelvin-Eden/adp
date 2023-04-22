from PySide6.QtGui import QIcon
from PySide6.QtWidgets import QDialog
from static_methods import StaticMethod
import ui_in_py.ui_settings_dialog as uid
import resources


class SettingsDialog(QDialog, uid.Ui_Dialog):
    def __init__(self, parent=None):
        super(SettingsDialog, self).__init__(parent=parent)
        self.setupUi(self)

        self.setWindowIcon(QIcon(':/icons/icon.ico'))
        self.setWindowTitle('Settings')

        self.setMinimumSize(507, 300)

        self.folderPathLineEdit.setReadOnly(True)

        self.chooseFolderBtn.clicked.connect(self.updateExportFolder)

    def updateExportFolder(self):
        chosen_folder = StaticMethod.chooseFolder(self, 'Choose Folder')
        if chosen_folder:
            self.folderPathLineEdit.setText(chosen_folder)
