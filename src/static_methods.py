import json
import os
from PySide6.QtCore import QStringListModel, Qt
from PySide6.QtGui import QCursor, QIcon
from PySide6.QtWidgets import QListWidget, QFileDialog, QMenu, QMessageBox
import resources
from list_widget import ListWidgetItem

proj_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

class StaticMethod:
    def __init__(self):
        pass

    @staticmethod
    def createSettingsFile():
        file_path = os.path.join(proj_dir, 'database/settings.json')
        settings = {
            "export_folder": os.path.join(os.path.expanduser('~'), 'Desktop'),
            "first_launch": True,
        }

        json_object = json.dumps(settings, indent=4)
        with open(file_path, 'w') as file:
            file.write(json_object)

    @staticmethod
    def settings_dict():
        file_path = os.path.join(proj_dir, 'database/settings.json')
        with open(file_path, 'r') as file:
            data = json.load(file)
            return data

    @staticmethod
    def updateSettings(setting_name, new_value):
        file_path = os.path.join(proj_dir, 'database/settings.json')
        with open(file_path, 'r') as file:
            data = json.load(file)
            data[setting_name] = new_value
        with open(file_path, 'w') as file:
            json.dump(data, file, indent=4)

    @staticmethod
    def set_completer(input_field, completer, data):
        model = QStringListModel()
        model.setStringList(data)

        completer.setCaseSensitivity(Qt.CaseInsensitive)
        completer.setModel(model)

        input_field.setCompleter(completer)

    @staticmethod
    def openPdfDoc(pdf_path=None, dir_path=None, pdf_name=None):
        try:
            if pdf_path:
                os.startfile(path=pdf_path)
            elif dir_path:
                file_path = StaticMethod.getFilesPaths(dir_path)[0]
                os.startfile(file_path)
            elif pdf_name:
                dir_path = os.path.join(proj_dir, 'database/stgs')
                if pdf_name in StaticMethod.getFilesNames(dir_path):
                    os.startfile(os.path.join(dir_path, pdf_name + '.pdf'))
        except IndexError:
            msg = StaticMethod.messageBox(text='Upload the STG.')
            msg.setIcon(QMessageBox.Information)
            msg.exec()
            return

    @staticmethod
    def getFilesPaths(dir_path: str) -> list[str]:
        res = []
        for name in os.listdir(dir_path):
            path = os.path.join(dir_path, name)
            if os.path.isfile(path):
                res.append(path)
        return res

    @staticmethod
    def clearDir(path):
        for filename in os.listdir(path):
            try:
                os.unlink(os.path.join(path, filename))
            except OSError:
                return

    @staticmethod
    def cleanUpDir(path, filters: list):
        for filename in os.listdir(path):
            for _filter in filters:
                if filename.startswith(_filter) or filename.endswith(_filter):
                    os.unlink(os.path.join(path, filename))

    @staticmethod
    def showMenu(menu: QMenu):
        menu.exec(QCursor().pos())

    @staticmethod
    def messageBox(text, parent=None):
        msg = QMessageBox(parent=parent)
        msg.setText(text+'        ')
        msg.setStyleSheet("font: 10pt 'Lucida Sans Unicode';")
        msg.setWindowTitle(' ')
        msg.setWindowIcon(QIcon(':icons/zero_opacity.ico'))
        return msg

    @staticmethod
    def file_names_no_ext(dir_path):
        return [file.split('.')[0] for file in StaticMethod.getFilesNames(dir_path) if not file.split('.')[0].startswith('~$')]

    @staticmethod
    def openWordDoc(doc_name, parent=None):
        path = os.path.join(proj_dir, 'database/saved_reports', doc_name + '.docx')
        try:
            os.startfile(path)
        except FileNotFoundError:
            msg = StaticMethod.messageBox(text="File doesn't exist.", parent=parent)
            msg.setIcon(QMessageBox.Information)
            msg.exec()
            return

    @staticmethod
    def getFilesNames(dir_path):
        res = []
        for name in os.listdir(dir_path):
            path = os.path.join(dir_path, name)
            if os.path.isfile(path):
                res.append(name)
        return res

    @staticmethod
    def RemoveFromListWidget(listWidget: QListWidget, items: list[str], icon_path):
        items_names = StaticMethod.listWidgetItemsNames(listWidget)
        for item_name in items:
            if item_name in items_names:
                items_names.remove(item_name)
        listWidget.clear()
        for name in items_names:
            listWidget.addItem(ListWidgetItem(name=name, icon_path=icon_path))

    @staticmethod
    def listWidgetItemsNames(listWidget: QListWidget) -> list[str]:
        items = []
        row = 0
        while True:
            try:
                items.append(listWidget.item(row).text())
                row += 1
            except AttributeError:
                return items

    @staticmethod
    def chooseFolder(parent, title):
        folder = QFileDialog.getExistingDirectoryUrl(parent=parent, caption=title)
        folder = folder.path()[1:]
        return folder

    @staticmethod
    def chooseFile(parent, title, _filter=None):
        if not _filter:
            _filter = '*.pdf'
            file, _ = QFileDialog.getOpenFileUrl(filter=_filter, parent=parent, caption=title)
            return file.path()[1:]

        file, _ = QFileDialog.getOpenFileUrl(filter=_filter, parent=parent, caption=title)
        return file.path()[1:]

    @staticmethod
    def styleListWidget(listWidget: QListWidget):
        listWidget.sortItems()
        listWidget.setStyleSheet("QScrollBar:Handle {background-color: rgb(149, 149, 149);}"
                                 "QListWidget{background-color: white; font: 11pt 'Segoe UI';}")
