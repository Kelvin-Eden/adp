import os
from PySide6.QtGui import QIcon
from PySide6.QtWidgets import QDialog
import pickle
import ui_in_py.ui_about_dialog as uia

proj_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


class AboutDialog(QDialog, uia.Ui_Dialog):
    def __init__(self, parent=None):
        super(AboutDialog, self).__init__(parent=parent)
        self.setupUi(self)
        self.setFixedSize(773, 360)

        self.setWindowTitle('About')
        self.setWindowIcon(QIcon(':icons/icon.ico'))

        file_path = os.path.join(proj_dir, 'database/about_message.txt')
        _message = pickle.load(open(file_path, 'rb'))
        self.textEdit.setText(_message)
        self.textEdit.setReadOnly(True)
