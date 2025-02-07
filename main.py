# region header
# ---------------------------------------------------------------------------
# System    :
# Class Name   : Day2
# Overview    : Học python trên udemy
# Designer    : DuyHG＠SSV
# Programmer   : DuyHG＠SSV
# Created Date   : 2025/03/02
# -----------------< History >-----------------------------------------------
# ID     :
# Designer    :
# Programmer   :
# Updated Date   :
# Comment    :
# Version    :
# -----------------< History >-----------------------------------------------
# endregion header

# region import
# Python
import sys

from PySide6.QtWidgets import (
    QApplication,
    QMainWindow,
    QLineEdit,
    QComboBox,
    QTableWidgetItem,
    QMessageBox,
    QTableWidget,
    QDateEdit,
    QHeaderView,
    QDialog,
    QLabel,
    QVBoxLayout,
    QHBoxLayout,
    QPushButton,
    QButtonGroup,
)

from PySide6.QtGui import QIntValidator
import design
from Handlecsv import HandleFileCsv
from PySide6.QtCore import QDate
from UserModel import User
from InforEnum import StatusDiaLog, ColumnHeaders
from Helper import convert

# endregion import

COLUMN_HEADERS = (
    "Họ tên",
    "Địa chỉ",
    "Email",
    "Số điện thoại",
    "Trạng thái",
    "Giới tính",
    "Ngày Sinh",
)

CURRENT_POINTER = -1
DETECT_CHANGE = False


class CustomTableWidget(QTableWidget):
    def focusOutEvent(self, event):
        super().focusOutEvent(event)
        self.clearSelection()


class MainWindow(QMainWindow, design.Ui_MainWindow):
    # region Init
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.setUpTable()
        self.loadProduct()
        self.setStypeForPanel()
        self.styplesFrame()

    # region Method
    def setUpTable(self):
        # design
        self.tableWidget.setColumnCount(len(ColumnHeaders.list_name()))
        self.tableWidget.setHorizontalHeaderLabels(ColumnHeaders.list_value())
        self.tableWidget.horizontalHeader().setSectionResizeMode(0, QHeaderView.Stretch)
        self.tableWidget.horizontalHeader().setSectionResizeMode(
            1, QHeaderView.ResizeToContents
        )
        self.tableWidget.horizontalHeader().setSectionResizeMode(2, QHeaderView.Stretch)
        self.tableWidget.horizontalHeader().setSectionResizeMode(
            3, QHeaderView.ResizeToContents
        )
        self.tableWidget.horizontalHeader().setSectionResizeMode(
            4, QHeaderView.ResizeToContents
        )
        self.tableWidget.horizontalHeader().setSectionResizeMode(
            5, QHeaderView.ResizeToContents
        )
        self.tableWidget.horizontalHeader().setSectionResizeMode(
            6, QHeaderView.ResizeToContents
        )
        self.phonenumberText.setValidator(QIntValidator())

        self.button_group_status = QButtonGroup(self)
        self.button_group_status.addButton(self.statusOnlineButton)
        self.button_group_status.addButton(self.statusOfflineButton)
        self.statusOnlineButton.setChecked(True)

        self.button_group_gender = QButtonGroup(self)
        self.button_group_gender.addButton(self.genderMaleButton)
        self.button_group_gender.addButton(self.genderFemaleButton)
        self.genderMaleButton.setChecked(True)

        self.onTableFocusOut

        # region Clickbotton fill data when click Qtable
        self.tableWidget.clicked.connect(self.setupDataForm)

        # region Clickbotton delete data
        self.deleteButton.clicked.connect(self.deleteProduct)

        # region Clickbotton edit data
        self.saveButton.clicked.connect(self.saveProduct)

        # region Clickbotton refesh form data
        self.refeshButton.clicked.connect(self.resetFields)

        # region Clickbotton save data in file csv
        self.completeButton.clicked.connect(self.notificaWhenSave)

        # region Clickbotton out system
        self.quitButton.clicked.connect(self.handleLogicQuit)

        # Connect change events
        self.fullnameText.textChanged.connect(self.on_data_changed)
        self.addressText.textChanged.connect(self.on_data_changed)
        self.emailText.textChanged.connect(self.on_data_changed)
        self.phonenumberText.textChanged.connect(self.on_data_changed)
        self.button_group_gender.buttonClicked.connect(self.on_data_changed)
        self.button_group_status.buttonClicked.connect(self.on_data_changed)

    # region method
    def loadProduct(self):
        # region load data for Qtablewidget
        self.tableWidget.setItem(0, 0, QTableWidgetItem("data"))
        listData = HandleFileCsv.readfile()
        self.tableWidget.setRowCount(len(listData))
        for x, rowdata in enumerate(listData):
            for y, data in enumerate(rowdata):
                self.tableWidget.setItem(x, y, QTableWidgetItem(data))

    # Extracts all data from a QTableWidget
    def get_table_data(self):
        table_data = []
        for row in range(self.tableWidget.rowCount()):
            row_data = []
            for col in range(self.tableWidget.columnCount()):
                item = self.tableWidget.item(row, col)
                row_data.append(item.text() if item else "")
            table_data.append(row_data)
        return table_data

    # Compare Old Data and Current Data
    def compareData(self):
        listDataOld = HandleFileCsv.readfile()
        listDataCurrent = self.get_table_data()
        for i, (csv_row, table_row) in enumerate(zip(listDataOld, listDataCurrent)):
            if csv_row != table_row:
                return True
        if listDataOld == listDataCurrent:
            return False
        else:
            return True

    # region setup styple common for panel
    def setStypeForPanel(self):
        self.setVisibleDeleteButton()
        self.setStyleSheet(open("css/Qlineedit.css").read())

    # region setup styple for frame
    def styplesFrame(self):
        self.frameForm.setStyleSheet(open("css/frameform.css").read())
        self.frameForm.lower()

    def locationPoints(self):
        # region get row of points in Qtablewidget
        return self.tableWidget.currentRow()

    # region to get all data from QTableWidget
    def getAllData(self):
        rows = self.tableWidget.rowCount()
        columns = self.tableWidget.columnCount()
        data = []

        # Loop through each cell and get data
        for row in range(rows):
            row_data = []
            for col in range(columns):
                item = self.tableWidget.item(row, col)
                row_data.append(item.text() if item else "")
            data.append(row_data)
        return data

    # Catch clear selection in QtableWidget
    def onTableFocusOut(self, event):
        self.tableWidget.clearSelection()  # Clear all
        self.tableWidget.setCurrentItem(None)  # Delete current item
        super(QTableWidget, self.tableWidget).focusOutEvent(event)

    # Catch event close form
    def closeEvent(self, event):
        if DETECT_CHANGE is True or self.compareData() is True:
            if (
                DETECT_CHANGE is True
                and self.compareData() is True
                or DETECT_CHANGE is True
            ):
                reply = self.showDialogYesOrNo(
                    "Confirmation",
                    "There are some changes. Do you want to stay?",
                ).exec_()
                if reply == StatusDiaLog.Yes.value:
                    event.ignore()
                elif reply == StatusDiaLog.No.value:
                    event.accept()
                else:
                    event.ignore()
            else:
                reply = self.showDialogYesOrNo(
                    "Confirmation",
                    "There are some changes. Do you want to save?",
                ).exec_()
                if reply == StatusDiaLog.Yes.value:
                    self.saveData()
                    self.showDialogNotifications("Confirmation", "Saved!").exec()
        else:
            event.accept()

    # region insert data for Qtablewidget
    def writeProduct(self):
        try:
            user = User()
            user.full_name = self.fullnameText.displayText()
            user.address = self.addressText.displayText()
            user.email = self.emailText.displayText()
            user.phone_number = self.phonenumberText.displayText()
            user.status = self.button_group_status.checkedButton().text()
            user.gender = self.button_group_gender.checkedButton().text()
            user.birth_date = self.birthDateEdit.text()
            row_count = self.tableWidget.rowCount()
            self.tableWidget.insertRow(row_count)
            for col, value in enumerate(user.to_list()):
                self.tableWidget.setItem(row_count, col, QTableWidgetItem(value))
            self.resetFields()
        except ValueError as e:
            self.showDialogWhenInsert(str(e))

    # region delete data for Qtablewidget
    def deleteProduct(self):
        global CURRENT_POINTER
        column = CURRENT_POINTER

        replyDiaLog = self.showDialogYesOrNo(
            "Confirmation", "Do you want to delete?"
        ).exec()
        if replyDiaLog == StatusDiaLog.Yes.value:
            self.tableWidget.removeRow(column)
            self.resetFields()

    # region edit data for Qtablewidget
    def saveProduct(self):
        global DETECT_CHANGE, CURRENT_POINTER
        try:
            if CURRENT_POINTER == -1:
                self.writeProduct()
                self.showDialogNotifications("Confirmation", "Saved!")
            else:
                if DETECT_CHANGE is True:
                    replyDiaLog = self.showDialogYesOrNo(
                        "Confirmation", "Do you want to change data?"
                    ).exec()
                    if replyDiaLog == StatusDiaLog.Yes.value:
                        selected_row = CURRENT_POINTER
                        user = User()
                        user.full_name = self.fullnameText.displayText()
                        user.address = self.addressText.displayText()
                        user.email = self.emailText.displayText()
                        user.phone_number = self.phonenumberText.displayText()
                        user.status = self.button_group_status.checkedButton().text()
                        user.gender = self.button_group_gender.checkedButton().text()
                        user.birth_date = self.birthDateEdit.text()
                        # convert data use to list
                        newData = user.to_list()
                        if selected_row != -1:
                            for col in range(self.tableWidget.columnCount()):
                                self.tableWidget.setItem(
                                    selected_row, col, QTableWidgetItem(newData[col])
                                )
                        DETECT_CHANGE = False

            return True
        except ValueError as e:
            self.showDialogWhenInsert(str(e))
            self.tableWidget.selectRow(CURRENT_POINTER)
            return False

    # Catch change of form
    def on_data_changed(self):
        global DETECT_CHANGE
        DETECT_CHANGE = True

    # handle logic of event change
    def handleLogicChange(self):
        global CURRENT_POINTER, DETECT_CHANGE
        if DETECT_CHANGE is True:
            replyDiaLog = self.showDialogYesOrNo(
                "Confirmation", "There are some changes. Do you want to stay?"
            ).exec()
            if CURRENT_POINTER != -1:
                if replyDiaLog == StatusDiaLog.Yes.value:
                    result = self.saveProduct()
                    if result is False:
                        return False
            else:
                if replyDiaLog == StatusDiaLog.Yes.value:
                    self.tableWidget.clearSelection()
                    return False
            DETECT_CHANGE = False
        return True

    # handle logic of event Quit
    def handleLogicQuit(self):
        global DETECT_CHANGE

        if DETECT_CHANGE is True or self.compareData() is True:
            if (
                DETECT_CHANGE is True
                and self.compareData() is True
                or DETECT_CHANGE is True
            ):
                replyDiaLog = self.showDialogYesOrNo(
                    "Confirmation", "Do you want to save and stay?"
                ).exec()
                if replyDiaLog == StatusDiaLog.No.value:
                    DETECT_CHANGE = False
                    self.exitform()
            else:
                replyDiaLog = self.showDialogYesOrNo(
                    "Confirmation", "Do you want to save and quit?"
                ).exec()
                if replyDiaLog == StatusDiaLog.Yes.value:
                    self.saveData()
                    self.exitform()
        else:
            self.exitform()

    # fill data in row QTableWidget
    def setupDataForm(self):
        global CURRENT_POINTER
        fillData = self.handleLogicChange()
        if fillData is True:
            CURRENT_POINTER = self.tableWidget.currentRow()
            cols = self.tableWidget.columnCount()
            data = []

            for col in range(cols):
                item = self.tableWidget.item(CURRENT_POINTER, col)
                data.append(item.text() if item else "")

            # Block signals to prevent triggering change events
            self.fullnameText.blockSignals(True)
            self.addressText.blockSignals(True)
            self.emailText.blockSignals(True)
            self.phonenumberText.blockSignals(True)
            self.button_group_status.blockSignals(True)
            self.button_group_gender.blockSignals(True)

            # Set values
            self.fullnameText.setText(data[0])
            self.addressText.setText(data[1])
            self.emailText.setText(data[2])
            self.phonenumberText.setText(data[3])
            self.set_radio_button(self.button_group_status, data[4])
            self.set_radio_button(self.button_group_gender, data[5])
            self.birthDateEdit.setDate(convert(data[6]))

            # Unblock signals after setting values
            self.fullnameText.blockSignals(False)
            self.addressText.blockSignals(False)
            self.emailText.blockSignals(False)
            self.phonenumberText.blockSignals(False)
            self.button_group_status.blockSignals(False)
            self.button_group_gender.blockSignals(False)

            # Connect change events
            self.fullnameText.textChanged.connect(self.on_data_changed)
            self.addressText.textChanged.connect(self.on_data_changed)
            self.emailText.textChanged.connect(self.on_data_changed)
            self.phonenumberText.textChanged.connect(self.on_data_changed)
            self.button_group_status.buttonClicked.connect(self.on_data_changed)
            self.button_group_gender.buttonClicked.connect(self.on_data_changed)

        self.setVisibleDeleteButton()

    # reset form
    def resetFields(self):
        global DETECT_CHANGE, CURRENT_POINTER
        self.resetPoints()
        for widget in QApplication.allWidgets():
            if isinstance(widget, QLineEdit):
                widget.clear()  # delete context QLineEdit
            elif isinstance(widget, QComboBox):
                widget.setCurrentIndex(0)  # set default
            elif isinstance(widget, QDateEdit):
                widget.setDate(QDate(2000, 1, 1))
        DETECT_CHANGE = False
        CURRENT_POINTER = -1

        self.setVisibleDeleteButton()

    # logic hidden or non-hidden button delete
    def setVisibleDeleteButton(self):
        if CURRENT_POINTER == -1:
            self.deleteButton.setVisible(False)
        else:
            self.deleteButton.setVisible(True)

    # reset Current Point on QTableWidget
    def resetPoints(self):
        self.tableWidget.clearSelection()
        self.tableWidget.setCurrentItem(None)

    # set value for radio button
    def set_radio_button(self, group, value):
        for button in group.buttons():
            if button.text() == value:
                button.setChecked(True)
                break

    # save data to file csv
    def saveData(self):
        HandleFileCsv.writefile(self.getAllData())

    # event notifica of button save
    def notificaWhenSave(self):
        global DETECT_CHANGE
        if DETECT_CHANGE is True or self.compareData() is True:
            if (
                DETECT_CHANGE is True
                and self.compareData() is True
                or DETECT_CHANGE is True
            ):
                self.showDialogYesOrNo(
                    "Confirmation",
                    "There are some changes. Do you want to stay?",
                ).exec_()
                DETECT_CHANGE = False
            elif self.compareData() is True:
                replyDiaLog = self.showDialogYesOrNo(
                    "Confirmation", "Do you want to save change?"
                ).exec()
                if replyDiaLog == StatusDiaLog.Yes.value:
                    self.saveData()
                    self.showDialogNotifications("Confirmation", "Saved!").exec()
        else:
            self.showDialogNotifications("Confirmation", "No data is changed").exec()

    # quit systems
    def exitform(self):
        self.close()

    # form dialog yes or no
    def showDialogYesOrNo(self, titleDialog, contentDialog):
        dialog = QDialog(self)
        dialog.setWindowTitle(titleDialog)

        # Layout
        layout = QVBoxLayout()

        # Message label
        label = QLabel(contentDialog)
        layout.addWidget(label)

        # Buttons layout
        buttonLayout = QHBoxLayout()
        yesButton = QPushButton("Yes")
        noButton = QPushButton("No")

        buttonLayout.addWidget(yesButton)
        buttonLayout.addWidget(noButton)
        layout.addLayout(buttonLayout)

        dialog.setLayout(layout)

        # Default return value (if closed)
        result = "Close"

        # Button functionality
        yesButton.clicked.connect(lambda: dialog.done(StatusDiaLog.Yes.value))
        noButton.clicked.connect(lambda: dialog.done(StatusDiaLog.No.value))

        # Show dialog and return result
        result = dialog
        return result

    # form dialog notification
    def showDialogNotifications(self, titleDialog, contentDialog):
        dialog = QDialog(self)
        dialog.setWindowTitle(titleDialog)

        # Layout
        layout = QVBoxLayout()

        # Message label
        label = QLabel(contentDialog)
        layout.addWidget(label)

        # Buttons layout
        buttonLayout = QHBoxLayout()
        okButton = QPushButton("Ok")

        buttonLayout.addWidget(okButton)
        layout.addLayout(buttonLayout)

        dialog.setLayout(layout)

        okButton.clicked.connect(lambda: dialog.done(StatusDiaLog.Yes.value))
        # Show dialog and return result
        result = dialog
        return result

    # Create the message box
    def showDialogWhenInsert(self, errorText):
        msg_box = QMessageBox(self)
        msg_box.setWindowTitle("Notification Warning")
        msg_box.setText(errorText)
        msg_box.setStandardButtons(QMessageBox.Ok)
        msg_box.setIcon(QMessageBox.Question)

        response = msg_box.exec()

        # Create logic button oke
        if response == QMessageBox.Ok:
            msg_box.close()

    # endregion method


# region run main
if __name__ == "__main__":
    app = QApplication(sys.argv)
    main_window = MainWindow()
    main_window.show()
    sys.exit(app.exec_())
# endregion run main
