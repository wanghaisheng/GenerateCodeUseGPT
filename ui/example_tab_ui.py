# Form implementation generated from reading ui file 'C:\Users\vipno\Documents\projects\GenerateCodeUseGPT\ui\example_tab.ui'
#
# Created by: PyQt6 UI code generator 6.4.2
#
# WARNING: Any manual changes made to this file will be lost when pyuic6 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt6 import QtCore, QtGui, QtWidgets


class Ui_TabWidget(object):
    def setupUi(self, TabWidget):
        TabWidget.setObjectName("TabWidget")
        TabWidget.resize(915, 300)
        self.horizontalLayout = QtWidgets.QHBoxLayout(TabWidget)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.groupBoxExample = QtWidgets.QGroupBox(parent=TabWidget)
        self.groupBoxExample.setObjectName("groupBoxExample")
        self.horizontalLayout_5 = QtWidgets.QHBoxLayout(self.groupBoxExample)
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        self.plainTextEdit = QtWidgets.QPlainTextEdit(parent=self.groupBoxExample)
        self.plainTextEdit.setObjectName("plainTextEdit")
        self.horizontalLayout_5.addWidget(self.plainTextEdit)
        self.verticalLayout_3 = QtWidgets.QVBoxLayout()
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.groupBoxDesc = QtWidgets.QGroupBox(parent=self.groupBoxExample)
        self.groupBoxDesc.setObjectName("groupBoxDesc")
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout(self.groupBoxDesc)
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.plainTextEditExampleDesc = QtWidgets.QPlainTextEdit(parent=self.groupBoxDesc)
        self.plainTextEditExampleDesc.setObjectName("plainTextEditExampleDesc")
        self.horizontalLayout_4.addWidget(self.plainTextEditExampleDesc)
        self.verticalLayout_3.addWidget(self.groupBoxDesc)
        self.groupBoxResponse = QtWidgets.QGroupBox(parent=self.groupBoxExample)
        self.groupBoxResponse.setObjectName("groupBoxResponse")
        self.horizontalLayout_6 = QtWidgets.QHBoxLayout(self.groupBoxResponse)
        self.horizontalLayout_6.setObjectName("horizontalLayout_6")
        self.plainTextEditExampleResponse = QtWidgets.QPlainTextEdit(parent=self.groupBoxResponse)
        self.plainTextEditExampleResponse.setObjectName("plainTextEditExampleResponse")
        self.horizontalLayout_6.addWidget(self.plainTextEditExampleResponse)
        self.verticalLayout_3.addWidget(self.groupBoxResponse)
        self.horizontalLayout_5.addLayout(self.verticalLayout_3)
        self.verticalLayout.addWidget(self.groupBoxExample)
        self.groupBoxTabOperation = QtWidgets.QGroupBox(parent=TabWidget)
        self.groupBoxTabOperation.setObjectName("groupBoxTabOperation")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.groupBoxTabOperation)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout()
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.labelOPenExample = QtWidgets.QLabel(parent=self.groupBoxTabOperation)
        self.labelOPenExample.setObjectName("labelOPenExample")
        self.horizontalLayout_3.addWidget(self.labelOPenExample)
        self.lineEditExample = QtWidgets.QLineEdit(parent=self.groupBoxTabOperation)
        self.lineEditExample.setEnabled(False)
        self.lineEditExample.setObjectName("lineEditExample")
        self.horizontalLayout_3.addWidget(self.lineEditExample)
        self.pushButtonOpenExample = QtWidgets.QPushButton(parent=self.groupBoxTabOperation)
        self.pushButtonOpenExample.setObjectName("pushButtonOpenExample")
        self.horizontalLayout_3.addWidget(self.pushButtonOpenExample)
        self.pushButtonRefresh = QtWidgets.QPushButton(parent=self.groupBoxTabOperation)
        self.pushButtonRefresh.setObjectName("pushButtonRefresh")
        self.horizontalLayout_3.addWidget(self.pushButtonRefresh)
        self.verticalLayout_2.addLayout(self.horizontalLayout_3)
        self.horizontalLayout_2.addLayout(self.verticalLayout_2)
        self.verticalLayout.addWidget(self.groupBoxTabOperation)
        self.horizontalLayout.addLayout(self.verticalLayout)

        self.retranslateUi(TabWidget)
        QtCore.QMetaObject.connectSlotsByName(TabWidget)

    def retranslateUi(self, TabWidget):
        _translate = QtCore.QCoreApplication.translate
        TabWidget.setWindowTitle(_translate("TabWidget", "Form"))
        self.groupBoxExample.setTitle(_translate("TabWidget", "Content"))
        self.groupBoxDesc.setTitle(_translate("TabWidget", "Desc"))
        self.groupBoxResponse.setTitle(_translate("TabWidget", "Response"))
        self.groupBoxTabOperation.setTitle(_translate("TabWidget", "Operation"))
        self.labelOPenExample.setText(_translate("TabWidget", "File path : "))
        self.pushButtonOpenExample.setText(_translate("TabWidget", "Open"))
        self.pushButtonRefresh.setText(_translate("TabWidget", "Refresh"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    TabWidget = QtWidgets.QWidget()
    ui = Ui_TabWidget()
    ui.setupUi(TabWidget)
    TabWidget.show()
    sys.exit(app.exec())
