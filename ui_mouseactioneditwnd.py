# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'mouseactioneditwnd.ui'
#
# Created by: PyQt5 UI code generator 5.12.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MouseActionEditDialog(object):
    def setupUi(self, MouseActionEditDialog):
        MouseActionEditDialog.setObjectName("MouseActionEditDialog")
        MouseActionEditDialog.resize(651, 268)
        font = QtGui.QFont()
        font.setPointSize(10)
        MouseActionEditDialog.setFont(font)
        self.gridLayout = QtWidgets.QGridLayout(MouseActionEditDialog)
        self.gridLayout.setVerticalSpacing(20)
        self.gridLayout.setObjectName("gridLayout")
        self.mouseActionTabWidget = QtWidgets.QTabWidget(MouseActionEditDialog)
        self.mouseActionTabWidget.setObjectName("mouseActionTabWidget")
        self.clickActionTab = QtWidgets.QWidget()
        self.clickActionTab.setObjectName("clickActionTab")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.clickActionTab)
        self.gridLayout_2.setContentsMargins(-1, 20, -1, 9)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.leftClick = QtWidgets.QRadioButton(self.clickActionTab)
        self.leftClick.setObjectName("leftClick")
        self.gridLayout_2.addWidget(self.leftClick, 0, 0, 1, 1)
        self.rightClick = QtWidgets.QRadioButton(self.clickActionTab)
        self.rightClick.setObjectName("rightClick")
        self.gridLayout_2.addWidget(self.rightClick, 0, 1, 1, 1)
        self.middleClick = QtWidgets.QRadioButton(self.clickActionTab)
        self.middleClick.setObjectName("middleClick")
        self.gridLayout_2.addWidget(self.middleClick, 0, 2, 1, 1)
        self.leftDclick = QtWidgets.QRadioButton(self.clickActionTab)
        self.leftDclick.setObjectName("leftDclick")
        self.gridLayout_2.addWidget(self.leftDclick, 1, 0, 1, 1)
        self.rightDclick = QtWidgets.QRadioButton(self.clickActionTab)
        self.rightDclick.setObjectName("rightDclick")
        self.gridLayout_2.addWidget(self.rightDclick, 1, 1, 1, 1)
        self.middleDclick = QtWidgets.QRadioButton(self.clickActionTab)
        self.middleDclick.setObjectName("middleDclick")
        self.gridLayout_2.addWidget(self.middleDclick, 1, 2, 1, 1)
        self.leftDown = QtWidgets.QRadioButton(self.clickActionTab)
        self.leftDown.setObjectName("leftDown")
        self.gridLayout_2.addWidget(self.leftDown, 2, 0, 1, 1)
        self.rightDown = QtWidgets.QRadioButton(self.clickActionTab)
        self.rightDown.setObjectName("rightDown")
        self.gridLayout_2.addWidget(self.rightDown, 2, 1, 1, 1)
        self.middleDown = QtWidgets.QRadioButton(self.clickActionTab)
        self.middleDown.setObjectName("middleDown")
        self.gridLayout_2.addWidget(self.middleDown, 2, 2, 1, 1)
        self.leftUp = QtWidgets.QRadioButton(self.clickActionTab)
        self.leftUp.setObjectName("leftUp")
        self.gridLayout_2.addWidget(self.leftUp, 3, 0, 1, 1)
        self.rightUp = QtWidgets.QRadioButton(self.clickActionTab)
        self.rightUp.setObjectName("rightUp")
        self.gridLayout_2.addWidget(self.rightUp, 3, 1, 1, 1)
        self.middleUp = QtWidgets.QRadioButton(self.clickActionTab)
        self.middleUp.setObjectName("middleUp")
        self.gridLayout_2.addWidget(self.middleUp, 3, 2, 1, 1)
        self.mouseActionTabWidget.addTab(self.clickActionTab, "")
        self.moveActionTab = QtWidgets.QWidget()
        self.moveActionTab.setObjectName("moveActionTab")
        self.gridLayout_3 = QtWidgets.QGridLayout(self.moveActionTab)
        self.gridLayout_3.setContentsMargins(-1, 20, -1, -1)
        self.gridLayout_3.setObjectName("gridLayout_3")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.moveTo = QtWidgets.QRadioButton(self.moveActionTab)
        self.moveTo.setMinimumSize(QtCore.QSize(100, 0))
        self.moveTo.setObjectName("moveTo")
        self.horizontalLayout_2.addWidget(self.moveTo)
        self.label_2 = QtWidgets.QLabel(self.moveActionTab)
        self.label_2.setMinimumSize(QtCore.QSize(25, 0))
        self.label_2.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_2.setObjectName("label_2")
        self.horizontalLayout_2.addWidget(self.label_2)
        self.xEdit = QtWidgets.QLineEdit(self.moveActionTab)
        self.xEdit.setObjectName("xEdit")
        self.horizontalLayout_2.addWidget(self.xEdit)
        self.label_3 = QtWidgets.QLabel(self.moveActionTab)
        self.label_3.setMinimumSize(QtCore.QSize(25, 0))
        self.label_3.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_3.setObjectName("label_3")
        self.horizontalLayout_2.addWidget(self.label_3)
        self.yEdit = QtWidgets.QLineEdit(self.moveActionTab)
        self.yEdit.setObjectName("yEdit")
        self.horizontalLayout_2.addWidget(self.yEdit)
        self.gridLayout_3.addLayout(self.horizontalLayout_2, 1, 0, 1, 3)
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.moveOffset = QtWidgets.QRadioButton(self.moveActionTab)
        self.moveOffset.setMinimumSize(QtCore.QSize(100, 0))
        self.moveOffset.setAutoExclusive(True)
        self.moveOffset.setObjectName("moveOffset")
        self.horizontalLayout_3.addWidget(self.moveOffset)
        self.label_5 = QtWidgets.QLabel(self.moveActionTab)
        self.label_5.setMinimumSize(QtCore.QSize(25, 0))
        self.label_5.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_5.setObjectName("label_5")
        self.horizontalLayout_3.addWidget(self.label_5)
        self.xOffsetEdit = QtWidgets.QLineEdit(self.moveActionTab)
        self.xOffsetEdit.setObjectName("xOffsetEdit")
        self.horizontalLayout_3.addWidget(self.xOffsetEdit)
        self.label_4 = QtWidgets.QLabel(self.moveActionTab)
        self.label_4.setMinimumSize(QtCore.QSize(70, 0))
        self.label_4.setObjectName("label_4")
        self.horizontalLayout_3.addWidget(self.label_4)
        self.label_6 = QtWidgets.QLabel(self.moveActionTab)
        self.label_6.setMinimumSize(QtCore.QSize(25, 0))
        self.label_6.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_6.setObjectName("label_6")
        self.horizontalLayout_3.addWidget(self.label_6)
        self.yOffsetEdit = QtWidgets.QLineEdit(self.moveActionTab)
        self.yOffsetEdit.setObjectName("yOffsetEdit")
        self.horizontalLayout_3.addWidget(self.yOffsetEdit)
        self.label_7 = QtWidgets.QLabel(self.moveActionTab)
        self.label_7.setMinimumSize(QtCore.QSize(70, 0))
        self.label_7.setObjectName("label_7")
        self.horizontalLayout_3.addWidget(self.label_7)
        self.gridLayout_3.addLayout(self.horizontalLayout_3, 2, 0, 1, 6)
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.scrollUp = QtWidgets.QRadioButton(self.moveActionTab)
        self.scrollUp.setMinimumSize(QtCore.QSize(100, 0))
        self.scrollUp.setAutoExclusive(True)
        self.scrollUp.setObjectName("scrollUp")
        self.horizontalLayout_4.addWidget(self.scrollUp)
        self.scrollUpEdit = QtWidgets.QLineEdit(self.moveActionTab)
        self.scrollUpEdit.setObjectName("scrollUpEdit")
        self.horizontalLayout_4.addWidget(self.scrollUpEdit)
        self.label_8 = QtWidgets.QLabel(self.moveActionTab)
        self.label_8.setMinimumSize(QtCore.QSize(80, 0))
        self.label_8.setObjectName("label_8")
        self.horizontalLayout_4.addWidget(self.label_8)
        self.scrollDown = QtWidgets.QRadioButton(self.moveActionTab)
        self.scrollDown.setMinimumSize(QtCore.QSize(110, 0))
        self.scrollDown.setAutoExclusive(True)
        self.scrollDown.setObjectName("scrollDown")
        self.horizontalLayout_4.addWidget(self.scrollDown)
        self.scrollDownEdit = QtWidgets.QLineEdit(self.moveActionTab)
        self.scrollDownEdit.setObjectName("scrollDownEdit")
        self.horizontalLayout_4.addWidget(self.scrollDownEdit)
        self.label_9 = QtWidgets.QLabel(self.moveActionTab)
        self.label_9.setMinimumSize(QtCore.QSize(80, 0))
        self.label_9.setObjectName("label_9")
        self.horizontalLayout_4.addWidget(self.label_9)
        self.gridLayout_3.addLayout(self.horizontalLayout_4, 3, 0, 1, 1)
        self.mouseActionTabWidget.addTab(self.moveActionTab, "")
        self.gridLayout.addWidget(self.mouseActionTabWidget, 0, 0, 1, 1)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setSpacing(20)
        self.horizontalLayout.setObjectName("horizontalLayout")
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem)
        self.ok = QtWidgets.QPushButton(MouseActionEditDialog)
        self.ok.setMinimumSize(QtCore.QSize(130, 0))
        self.ok.setAutoDefault(False)
        self.ok.setObjectName("ok")
        self.horizontalLayout.addWidget(self.ok)
        self.cancel = QtWidgets.QPushButton(MouseActionEditDialog)
        self.cancel.setMinimumSize(QtCore.QSize(130, 0))
        self.cancel.setAutoDefault(False)
        self.cancel.setObjectName("cancel")
        self.horizontalLayout.addWidget(self.cancel)
        self.gridLayout.addLayout(self.horizontalLayout, 3, 0, 1, 1)

        self.retranslateUi(MouseActionEditDialog)
        self.mouseActionTabWidget.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(MouseActionEditDialog)

    def retranslateUi(self, MouseActionEditDialog):
        _translate = QtCore.QCoreApplication.translate
        MouseActionEditDialog.setWindowTitle(_translate("MouseActionEditDialog", "Dialog"))
        self.leftClick.setText(_translate("MouseActionEditDialog", "Click left button"))
        self.rightClick.setText(_translate("MouseActionEditDialog", "Click right button"))
        self.middleClick.setText(_translate("MouseActionEditDialog", "Click middle button"))
        self.leftDclick.setText(_translate("MouseActionEditDialog", "Double-click left button"))
        self.rightDclick.setText(_translate("MouseActionEditDialog", "Double-click right button"))
        self.middleDclick.setText(_translate("MouseActionEditDialog", "Double-click middle button"))
        self.leftDown.setText(_translate("MouseActionEditDialog", "left button down"))
        self.rightDown.setText(_translate("MouseActionEditDialog", "right button down"))
        self.middleDown.setText(_translate("MouseActionEditDialog", "middle button down"))
        self.leftUp.setText(_translate("MouseActionEditDialog", "left button up"))
        self.rightUp.setText(_translate("MouseActionEditDialog", "right button up"))
        self.middleUp.setText(_translate("MouseActionEditDialog", "middle button up"))
        self.mouseActionTabWidget.setTabText(self.mouseActionTabWidget.indexOf(self.clickActionTab), _translate("MouseActionEditDialog", "Click"))
        self.moveTo.setText(_translate("MouseActionEditDialog", "Move to:"))
        self.label_2.setText(_translate("MouseActionEditDialog", "X"))
        self.label_3.setText(_translate("MouseActionEditDialog", "Y"))
        self.moveOffset.setText(_translate("MouseActionEditDialog", "Move offset"))
        self.label_5.setText(_translate("MouseActionEditDialog", "X"))
        self.label_4.setText(_translate("MouseActionEditDialog", "pixels"))
        self.label_6.setText(_translate("MouseActionEditDialog", "Y"))
        self.label_7.setText(_translate("MouseActionEditDialog", "pixels"))
        self.scrollUp.setText(_translate("MouseActionEditDialog", "Scroll up"))
        self.label_8.setText(_translate("MouseActionEditDialog", "pixels"))
        self.scrollDown.setText(_translate("MouseActionEditDialog", "Scroll down"))
        self.label_9.setText(_translate("MouseActionEditDialog", "pixels"))
        self.mouseActionTabWidget.setTabText(self.mouseActionTabWidget.indexOf(self.moveActionTab), _translate("MouseActionEditDialog", "Move"))
        self.ok.setText(_translate("MouseActionEditDialog", "OK"))
        self.cancel.setText(_translate("MouseActionEditDialog", "Cancel"))




if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MouseActionEditDialog = QtWidgets.QDialog()
    ui = Ui_MouseActionEditDialog()
    ui.setupUi(MouseActionEditDialog)
    MouseActionEditDialog.show()
    sys.exit(app.exec_())