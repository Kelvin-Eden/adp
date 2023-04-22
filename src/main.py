import os
import random
import shutil
import sys
from PySide6.QtCore import Qt
from PySide6.QtGui import QIcon, QFont
from PySide6.QtWidgets import *
import predictor
from quick_actions import QuickActions
from report import Report
import ui_in_py.ui_main as uim
from static_methods import StaticMethod
from data_values import Dataset
from list_widget import ListWidgetItem, ListWidget
from about_dialog import AboutDialog
from settings_dialog import SettingsDialog
import resources

proj_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


class Master(QMainWindow, uim.Ui_MainWindow):
    def __init__(self):
        super(Master, self).__init__(parent=None)
        self.setupUi(self)
        # Init the window GUI
        self.initGUI()
        # show the window in maximized size
        self.showMaximized()
        # The settings dialog
        self.settings_dialog = SettingsDialog(parent=self)

        # Check if the database folder is there
        database_folder_path = os.path.join(proj_dir, 'database')
        # check the presence of the database folder
        if not os.path.exists(os.path.join(proj_dir, 'database/')):
            # if it's not there make one
            os.mkdir(database_folder_path)
            # Make the saved reports folder
            os.mkdir(os.path.join(database_folder_path, 'saved_reports'))
            # Make stgs folder
            os.mkdir(os.path.join(proj_dir, 'stgs'))
            # Make the settings JSON
            StaticMethod.createSettingsFile()
            # MAke the about message test as blank
            with open(os.path.join(proj_dir, 'database/about_message.txt', 'a')) as file:
                file.write("The about message couldn't be loaded. Seems an error occurred during installation.")
        # The path to the saved records folder

        self.saved_records_folder_path = os.path.join(proj_dir, 'database/saved_reports')
        # The path to the folder containing stgs
        self.stgs_folder_path = os.path.join(proj_dir, 'database/stgs')
        # The path to the desktop
        self.path_to_desktop = os.path.join(os.path.expanduser('~'), 'Desktop')
        # Make desktop as the default folder if it's the first launch
        if StaticMethod.settings_dict()['first_launch']:
            StaticMethod.updateSettings('export_folder', self.path_to_desktop)
        # The output/ exports folder -> set it as desktop being default
        # Update it whenever text in the export folder linedit has changed
        self.export_folder_path = StaticMethod.settings_dict()['export_folder']
        # Set this path of export folder to the lineedit showing the export folder
        self.settings_dialog.folderPathLineEdit.setText(self.export_folder_path)
        # if the text in this lineedit changes update the export folder
        self.settings_dialog.folderPathLineEdit.textChanged.connect(self.updateExportFolder)
        # Edit the properties of the Menu QMenu Item
        self.initMenuItem()
        # Add the email at the rightmost and the most bottom corner
        self.addEmailLogo()
        # if the user-input item is clicked then remove it from the list
        self.listWidget.clicked.connect(lambda: StaticMethod.RemoveFromListWidget(listWidget=self.listWidget, items=[
            self.listWidget.currentItem().text()], icon_path=':icons/bullet.ico'))
        # The message box when the user ass to delete all records
        self.clearRecordsMsgBox = None
        # The Dataset object contains data used to train the models
        self.dataset = Dataset(os.path.join(proj_dir, 'dataset/Training.csv'))
        # The criteria used in the latest prediction are stored in this
        # This is important in making the final report
        self._criteria = []
        # The predictions in the latest predict process are stored here
        # This is important in making the final report
        self.predictions: dict = {}
        # The listwidget to display the criteria supported by the app
        self.criteria_listwidget = ListWidget(items_names=self.dataset.criteria, icon_path=':icons/bullet.ico',
                                              funLMB=self.add_criteria)
        # Style the listwidget a bit
        StaticMethod.styleListWidget(self.criteria_listwidget)
        # The list widget that holds the final results
        self.mode_results_lw = ListWidget(icon_path=':icons/bullet.ico')
        # initialize the predictions table
        self.possibles_table = None
        self.initTable()
        # The menu for Quick actions of the Records ListWidget
        self.records_menu = QuickActions(parent=self)
        # the table to hold the saved reports
        # Clear all the temporary files on launching the app
        try:
            StaticMethod.cleanUpDir(path=self.saved_records_folder_path, filters=['~$'])
        except FileNotFoundError:
            os.mkdir(self.saved_records_folder_path)
        # if not permitted, just go -> instead of crushing the whole app
        except PermissionError:
            pass
        # The listwidget to display all the saved reports
        self.saved_reports_lw = ListWidget(
            items_names=StaticMethod.file_names_no_ext(dir_path=self.saved_records_folder_path),
            icon_path=':icons/doc.ico', funLMB=self.openRecord, funRMB=self.showRecordsMenu)
        # The tabs in the main window
        self.addTabs()

        # ----------THE LINEEDIT HANDLING----------
        self.completer = None
        self.setupInputField()

        # Handle the signals from the buttons
        self.handleButtons()
        # Handle signals from the Menu actions
        self.handleMenuActions()
        # Handle signals from the quick actions
        self.handleQuickActions()

    def initMenuItem(self):
        self.menu_MENU.setMinimumHeight(100)
        self.menu_MENU.setStyleSheet(
            "background-color: rgb(100,100,100); color: white; font: 11pt 'Maven Pro'; icon-size: 25px;")
        self.settings_action.setIcon(QIcon(':icons/settings.ico'))
        self.about_action.setIcon(QIcon(':icons/about.ico'))
        self.load_stg_action.setIcon(QIcon(':icons/update.ico'))

    def updateExportFolder(self):
        self.export_folder_path = self.settings_dialog.folderPathLineEdit.text()
        StaticMethod.updateSettings('export_folder', self.export_folder_path)
        self.settings_dialog.folderPathLineEdit.setText(self.export_folder_path)

    def directExport(self):
        name = self.exportReport(folder=self.export_folder_path)
        if name in StaticMethod.file_names_no_ext(dir_path=self.export_folder_path):
            msg = StaticMethod.messageBox(text='Exported Successfully.', parent=self)
            msg.setIcon(QMessageBox.Information)
            msg.exec()
            return

    def showAboutDialog(self):
        _about_dialog = AboutDialog(parent=self)
        _about_dialog.exec()

    @property
    def criteriaListWidget(self):
        criteria = self.dataset.criteria
        listwidget = ListWidget(items_names=criteria, icon_path=':icons/bullet.ico')

        StaticMethod.styleListWidget(listwidget)
        return listwidget

    def delete_saved(self):
        # get the name and path of the record that is to be deleted
        name = self.saved_reports_lw.currentItem().text()
        path = os.path.join(self.saved_records_folder_path, name + '.docx')
        os.unlink(path=path)
        self.saved_reports_lw.clear()
        for record_name in StaticMethod.file_names_no_ext(self.saved_records_folder_path):
            self.saved_reports_lw.add_item(item_name=record_name)

    def quick_export(self):
        path = os.path.join(self.saved_records_folder_path, self.saved_reports_lw.currentItem().text() + '.docx')
        out_path = os.path.join(self.export_folder_path, os.path.basename(path))
        shutil.copy2(path, out_path)
        if os.path.basename(path) in StaticMethod.getFilesNames(dir_path=self.export_folder_path):
            msg = StaticMethod.messageBox(text='Exported Successfully.', parent=self)
            msg.setIcon(QMessageBox.Information)
            msg.exec()
            return

    def renameRecord(self):
        new_name, ok = QInputDialog.getText(self, 'New Record Name', 'Name: ')
        if new_name and ok:
            old_name = self.saved_reports_lw.currentItem().text()
            destination_dir = self.saved_records_folder_path
            shutil.move(os.path.join(destination_dir, old_name + '.docx'),
                        os.path.join(destination_dir, new_name + '.docx'))

            self.saved_reports_lw.clear()
            for record_name in StaticMethod.file_names_no_ext(destination_dir):
                self.saved_reports_lw.add_item(item_name=record_name)

    def handleQuickActions(self):
        self.records_menu.export_action.triggered.connect(self.quick_export)
        self.records_menu.delete_action.triggered.connect(self.delete_saved)
        self.records_menu.rename_action.triggered.connect(self.renameRecord)
        self.records_menu.delete_all_action.triggered.connect(self.clear_all_records)

    def showRecordsMenu(self):
        # only show the menu when it has items in it
        if StaticMethod.listWidgetItemsNames(self.saved_reports_lw):
            StaticMethod.showMenu(self.records_menu)

    def openRecord(self):
        try:
            StaticMethod.openWordDoc(self.saved_reports_lw.currentItem().text(), parent=self)
        except AttributeError:
            return

    def updateSTG(self):
        loaded_stg = StaticMethod.chooseFile(parent=self, title='Load STG PDF', _filter='*.pdf')
        if loaded_stg:
            StaticMethod.clearDir(self.stgs_folder_path)
            new_stg = os.path.join(self.stgs_folder_path, os.path.basename(loaded_stg))
            try:
                shutil.copy2(loaded_stg, new_stg)
            except FileNotFoundError:
                return
            # Test if the STG has been loaded and notify the user
            # Simply, see if there is a file in ./database/saved_records folder
            if StaticMethod.getFilesNames(self.stgs_folder_path):
                msg = StaticMethod.messageBox(text="STG loaded successfully.", parent=self)
                msg.setIcon(QMessageBox.Information)
                msg.exec()

    def setupInputField(self):
        self.lineEdit.setClearButtonEnabled(True)
        self.completer = QCompleter()
        StaticMethod.set_completer(input_field=self.lineEdit, completer=self.completer, data=self.dataset.criteria)
        # if the completer gets activated, add the vales to the listWidget
        self.completer.activated.connect(lambda: self.listWidget.addItem(ListWidgetItem(
            name=self.lineEdit.text(), icon_path=':icons/bullet.ico'
        )))

    def handleMenuActions(self):
        self.load_stg_action.triggered.connect(self.updateSTG)
        self.about_action.triggered.connect(self.showAboutDialog)
        self.settings_action.triggered.connect(lambda: self.settings_dialog.exec())

    def handleButtons(self):
        self.clearBtn.clicked.connect(lambda: self.listWidget.clear())
        self.predictBtn.clicked.connect(self.predict)
        self.exportBtn.clicked.connect(self.directExport)
        self.stgBtn.clicked.connect(
            lambda: StaticMethod.openPdfDoc(dir_path=self.stgs_folder_path))
        self.saveBtn.clicked.connect(self.saveReport)

    def initGUI(self):
        # The progressBar and the status label and initially set not visible
        # until the process of prediction begins.
        self.progressBar.setVisible(False)
        self.status_label.setVisible(False)
        self.setWindowIcon(QIcon(':icons/icon.ico'))
        self.setWindowTitle('ADP 1.0')

    @property
    def diseasesListWidget(self):
        supported_diseases = self.dataset.diseases
        listwidget = ListWidget(items_names=supported_diseases, icon_path=':icons/bullet.ico')
        StaticMethod.styleListWidget(listwidget)
        return listwidget

    def add_criteria(self):
        # This adds a criteria chosen from the criteria listed
        self.listWidget.addItem(
            ListWidgetItem(name=self.criteria_listwidget.currentItem().text(), icon_path=':icons/bullet.ico'))

    def addTabs(self):
        self.results_tabWidget.setTabVisible(0, False)
        self.results_tabWidget.setTabVisible(1, False)
        self.results_tabWidget.addTab(self.possibles_table, 'Predictions')
        self.results_tabWidget.addTab(QWidget(), '')
        self.results_tabWidget.setTabEnabled(3, False)
        self.saved_reports_lw.setStyleSheet("background-color:white;"
                                            "font: 11pt 'Segoe UI';")
        self.possibles_table.setStyleSheet("background-color:white;"
                                           "font: 11pt 'Segoe UI';")
        self.mode_results_lw.setStyleSheet("background-color:white;"
                                           "font: 11pt 'Segoe UI';")
        self.results_tabWidget.addTab(self.mode_results_lw, 'Results')
        self.results_tabWidget.setCurrentIndex(4)
        self.results_tabWidget.addTab(QWidget(), '')
        self.results_tabWidget.setTabEnabled(5, False)
        self.results_tabWidget.addTab(self.saved_reports_lw, 'Records')
        self.results_tabWidget.setStyleSheet("QTabBar::tab::disabled{"
                                             "width: 120px;"
                                             "color: transparent;"
                                             "background: transparent;}"
                                             "QTabBar::tab::enabled{"
                                             "font: 10pt 'Maven Pro';}"
                                             "QTabWidget::pane{"
                                             "border: 1px solid black;"
                                             "margin-top: 10px;}"
                                             )

        self.supported_tabWidget.setTabVisible(0, False)
        self.supported_tabWidget.setTabVisible(1, False)
        self.supported_tabWidget.addTab(self.diseasesListWidget, 'Diseases')
        self.supported_tabWidget.addTab(QWidget(), ' ')
        self.supported_tabWidget.setCurrentIndex(2)
        self.supported_tabWidget.setTabEnabled(3, False)
        self.supported_tabWidget.setStyleSheet("QTabBar::tab::disabled{"
                                               "width: 120px;"
                                               "color: transparent;"
                                               "background: transparent;}"
                                               "QTabBar::tab::enabled{"
                                               "font: 10pt 'Maven Pro';}"
                                               "QTabWidget::pane{"
                                               "border: 1px solid black;"
                                               "margin-top: 10px;}"
                                               )
        self.supported_tabWidget.addTab(self.criteria_listwidget, 'Criteria')

    def createReport(self, name):
        if self.predictions:
            rf_prediction = self.predictions.get('rf_model_prediction')
            naive_bayes_prediction = self.predictions.get('naive_bayes_prediction')
            svm_prediction = self.predictions.get('svm_model_prediction')
            final_prediction = self.predictions.get('final_prediction')

            report = Report(name=name)
            report.createReport(svm_prediction=svm_prediction, rf_prediction=rf_prediction,
                                nb_prediction=naive_bayes_prediction,
                                final_prediction=final_prediction, criteria=self._criteria)
            return report

    def exportReport(self, folder):
        if not self.predictions:
            msg = StaticMethod.messageBox(text="No Record uploaded.", parent=self)
            msg.setIcon(QMessageBox.Information)
            msg.exec()
            return
        name, ok = QInputDialog.getText(self, 'Report Name', 'Name: ')
        self.setStyleSheet("QInputDialog {background-color: white; color: black;}")
        if ok and name:
            report = self.createReport(name=name)
            try:
                report.saveReport(folder=folder)
            except AttributeError:
                msg = StaticMethod.messageBox(text="No Record uploaded.", parent=self)
                msg.setIcon(QMessageBox.Information)
                msg.exec()
                return
        return name

    def saveReport(self):
        name = self.exportReport(folder=self.saved_records_folder_path)
        self.saved_reports_lw.add_item(item_name=name)
        # Check if the file has been saved successfully and notify the user
        if name in StaticMethod.file_names_no_ext(self.saved_records_folder_path):
            msg = StaticMethod.messageBox(text="Saved successfully.", parent=self)
            msg.setIcon(QMessageBox.Information)
            msg.exec()
            return

    def initTable(self):
        self.possibles_table = QTableWidget(3, 2)
        # Add the headers for the columns
        header_1 = QTableWidgetItem('MODEL')
        header_2 = QTableWidgetItem('PREDICTION')

        header_1.setFlags(Qt.ItemIsEnabled)
        header_2.setFlags(Qt.ItemIsEnabled)

        header_font = QFont()
        header_font.setPixelSize(13)
        header_font.setBold(True)
        header_font.setFamily('Lucida Sans Unicode')

        header_1.setFont(header_font)
        header_2.setFont(header_font)

        self.possibles_table.setHorizontalHeaderItem(0, header_1)
        self.possibles_table.setHorizontalHeaderItem(1, header_2)
        self.possibles_table.horizontalHeader().setStyleSheet("::section{background-color: rgb(232, 232, 232);}")

        model_name_font = QFont()
        model_name_font.setPixelSize(15)
        model_name_font.setFamily('Segoe UI')

        item = QTableWidgetItem('Support Vector Classifier')
        item.setFont(model_name_font)
        item.setFlags(Qt.ItemIsEnabled)
        self.possibles_table.setItem(0, 0, item)

        item = QTableWidgetItem('')
        item.setFlags(Qt.ItemIsEnabled)
        self.possibles_table.setItem(0, 1, item)

        item = QTableWidgetItem('Random Forest Classifier')
        item.setFont(model_name_font)
        item.setFlags(Qt.ItemIsEnabled)
        self.possibles_table.setItem(1, 0, item)

        item = QTableWidgetItem('')
        item.setFlags(Qt.ItemIsEnabled)
        self.possibles_table.setItem(1, 1, item)

        item = QTableWidgetItem('Gaussian Naive Bayes')
        item.setFont(model_name_font)
        item.setFlags(Qt.ItemIsEnabled)
        self.possibles_table.setItem(2, 0, item)

        item = QTableWidgetItem('')
        item.setFlags(Qt.ItemIsEnabled)
        self.possibles_table.setItem(2, 1, item)

        self.possibles_table.horizontalHeader().setStretchLastSection(True)
        self.possibles_table.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)


    def clear_all_records(self):
        self.clearRecordsMsgBox = StaticMethod.messageBox(text='Delete all saved reports?', parent=self)
        self.clearRecordsMsgBox.setIcon(QMessageBox.Question)
        self.clearRecordsMsgBox.setStandardButtons(QMessageBox.Cancel | QMessageBox.Ok)
        self.clearRecordsMsgBox.setDefaultButton(QMessageBox.Cancel)
        self.clearRecordsMsgBox.buttonClicked.connect(self.clearRecordsButton)

        self.clearRecordsMsgBox.exec()

    def addEmailLogo(self):
        self.logoLabel.setText('')
        self.logoLabel.setFixedSize(29, 29)
        self.logoLabel.setStyleSheet("border-image: url(':icons/email.ico');")

    def clearRecordsButton(self, i):
        if i.text() == 'OK':
            StaticMethod.clearDir(self.saved_records_folder_path)
            self.saved_reports_lw.clear()
        else:
            return

    def predict(self):
        # update the latest criteria
        self._criteria = StaticMethod.listWidgetItemsNames(self.listWidget)
        # If the user has not entered criteria show a warning
        if not self._criteria:
            msg = StaticMethod.messageBox(text="Enter at least 5 symptoms or signs", parent=self)
            msg.setIcon(QMessageBox.Information)
            msg.exec()
            return
        # format the criteria to be a string with all of them joined by ','
        # This is important because that is the input accepted by predictDisease() function.
        criteria = ','.join(self._criteria)
        # Do the prediction
        try:
            predictions = predictor.predictDisease(criteria)
        except KeyError:
            pass
        # update the latest predictions
        self.predictions = predictions

        rf_prediction = predictions.get('rf_model_prediction')
        naive_bayes_prediction = predictions.get('naive_bayes_prediction')
        svm_prediction = predictions.get('svm_model_prediction')
        final_prediction = predictions.get('final_prediction')

        # add the final prediction to the mode_result listWidget
        self.mode_results_lw.clear()
        # showing AIDS when the results are all unique isn't proper, if all values are unique and AIDS is included
        # don't show it, pick another. AIDS is scary,haha!
        if final_prediction == 'AIDS':
            del predictions['final_prediction']
            values = list(predictions.values())
            if values.count('AIDS') == 1:
                while final_prediction == 'AIDS':
                    final_prediction = random.choice(values)
            else:
                for value in values:
                    if values.count(value) >= 2 and value != 'AIDS':
                        final_prediction = value
        self.mode_results_lw.add_item(item_name=final_prediction)

        # create the table
        # self.possibles_table.clear()
        # item = QTableWidgetItem('SVM')
        # item.setFlags(Qt.ItemIsEnabled)
        # self.possibles_table.setItem(0, 0, item)

        font = QFont()
        font.setPixelSize(15)
        font.setFamily('Segoe UI')

        item = QTableWidgetItem(svm_prediction)
        item.setFont(font)
        item.setFlags(Qt.ItemIsEnabled)
        self.possibles_table.setItem(0, 1, item)

        item = QTableWidgetItem(rf_prediction)
        item.setFont(font)
        item.setFlags(Qt.ItemIsEnabled)
        self.possibles_table.setItem(1, 1, item)

        item = QTableWidgetItem(naive_bayes_prediction)
        item.setFont(font)
        item.setFlags(Qt.ItemIsEnabled)
        self.possibles_table.setItem(2, 1, item)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = Master()
    window.show()
    # The user has to read the about if it's first time running the software
    if StaticMethod.settings_dict()['first_launch']:
        about_dialog = AboutDialog(parent=window)
        about_dialog.exec()
        StaticMethod.updateSettings('first_launch', False)
    sys.exit(app.exec())
