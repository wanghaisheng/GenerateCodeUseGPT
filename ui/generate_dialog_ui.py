# Form implementation generated from reading ui file 'C:\Users\vipno\Documents\projects\GenerateCodeUseGPT\ui\generate_dialog.ui'
#
# Created by: PyQt6 UI code generator 6.4.2
#
# WARNING: Any manual changes made to this file will be lost when pyuic6 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt6 import QtCore, QtGui, QtWidgets


class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(916, 770)
        self.horizontalLayout = QtWidgets.QHBoxLayout(Dialog)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.groupBoxExamples = QtWidgets.QGroupBox(parent=Dialog)
        self.groupBoxExamples.setObjectName("groupBoxExamples")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.groupBoxExamples)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.tabWidgetExamples = QtWidgets.QTabWidget(parent=self.groupBoxExamples)
        self.tabWidgetExamples.setObjectName("tabWidgetExamples")
        self.tabExample1 = QtWidgets.QWidget()
        self.tabExample1.setObjectName("tabExample1")
        self.tabWidgetExamples.addTab(self.tabExample1, "")
        self.tabExample2 = QtWidgets.QWidget()
        self.tabExample2.setEnabled(True)
        self.tabExample2.setObjectName("tabExample2")
        self.tabWidgetExamples.addTab(self.tabExample2, "")
        self.verticalLayout_2.addWidget(self.tabWidgetExamples)
        self.horizontalLayout_15 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_15.setObjectName("horizontalLayout_15")
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Policy.Expanding, QtWidgets.QSizePolicy.Policy.Minimum)
        self.horizontalLayout_15.addItem(spacerItem)
        self.pushButtonClearExample = QtWidgets.QPushButton(parent=self.groupBoxExamples)
        self.pushButtonClearExample.setObjectName("pushButtonClearExample")
        self.horizontalLayout_15.addWidget(self.pushButtonClearExample)
        spacerItem1 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Policy.Expanding, QtWidgets.QSizePolicy.Policy.Minimum)
        self.horizontalLayout_15.addItem(spacerItem1)
        self.pushButtonDeleteExample = QtWidgets.QPushButton(parent=self.groupBoxExamples)
        self.pushButtonDeleteExample.setObjectName("pushButtonDeleteExample")
        self.horizontalLayout_15.addWidget(self.pushButtonDeleteExample)
        spacerItem2 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Policy.Expanding, QtWidgets.QSizePolicy.Policy.Minimum)
        self.horizontalLayout_15.addItem(spacerItem2)
        self.pushButtonNewExample = QtWidgets.QPushButton(parent=self.groupBoxExamples)
        self.pushButtonNewExample.setObjectName("pushButtonNewExample")
        self.horizontalLayout_15.addWidget(self.pushButtonNewExample)
        spacerItem3 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Policy.Expanding, QtWidgets.QSizePolicy.Policy.Minimum)
        self.horizontalLayout_15.addItem(spacerItem3)
        self.verticalLayout_2.addLayout(self.horizontalLayout_15)
        self.verticalLayout.addWidget(self.groupBoxExamples)
        self.groupBox_Prompt = QtWidgets.QGroupBox(parent=Dialog)
        self.groupBox_Prompt.setObjectName("groupBox_Prompt")
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout(self.groupBox_Prompt)
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.plainTextEditPrompt = QtWidgets.QPlainTextEdit(parent=self.groupBox_Prompt)
        self.plainTextEditPrompt.setObjectName("plainTextEditPrompt")
        self.horizontalLayout_2.addWidget(self.plainTextEditPrompt)
        self.horizontalLayout_5 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        self.verticalLayout_4 = QtWidgets.QVBoxLayout()
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.groupBoxPromptFile = QtWidgets.QGroupBox(parent=self.groupBox_Prompt)
        self.groupBoxPromptFile.setObjectName("groupBoxPromptFile")
        self.horizontalLayout_6 = QtWidgets.QHBoxLayout(self.groupBoxPromptFile)
        self.horizontalLayout_6.setObjectName("horizontalLayout_6")
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.labelChoosePromptFile = QtWidgets.QLabel(parent=self.groupBoxPromptFile)
        self.labelChoosePromptFile.setObjectName("labelChoosePromptFile")
        self.horizontalLayout_4.addWidget(self.labelChoosePromptFile)
        self.lineEditPrompt = QtWidgets.QLineEdit(parent=self.groupBoxPromptFile)
        self.lineEditPrompt.setObjectName("lineEditPrompt")
        self.horizontalLayout_4.addWidget(self.lineEditPrompt)
        self.pushButtonOpenPromptFile = QtWidgets.QPushButton(parent=self.groupBoxPromptFile)
        self.pushButtonOpenPromptFile.setObjectName("pushButtonOpenPromptFile")
        self.horizontalLayout_4.addWidget(self.pushButtonOpenPromptFile)
        self.horizontalLayout_6.addLayout(self.horizontalLayout_4)
        self.verticalLayout_4.addWidget(self.groupBoxPromptFile)
        self.groupBoxPromptOperator = QtWidgets.QGroupBox(parent=self.groupBox_Prompt)
        self.groupBoxPromptOperator.setObjectName("groupBoxPromptOperator")
        self.horizontalLayout_7 = QtWidgets.QHBoxLayout(self.groupBoxPromptOperator)
        self.horizontalLayout_7.setObjectName("horizontalLayout_7")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout()
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.horizontalLayout_8 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_8.setObjectName("horizontalLayout_8")
        self.pushButtonRefreshPrompt = QtWidgets.QPushButton(parent=self.groupBoxPromptOperator)
        self.pushButtonRefreshPrompt.setObjectName("pushButtonRefreshPrompt")
        self.horizontalLayout_8.addWidget(self.pushButtonRefreshPrompt)
        spacerItem4 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Policy.Expanding, QtWidgets.QSizePolicy.Policy.Minimum)
        self.horizontalLayout_8.addItem(spacerItem4)
        self.verticalLayout_3.addLayout(self.horizontalLayout_8)
        self.horizontalLayout_9 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_9.setObjectName("horizontalLayout_9")
        self.horizontalLayout_10 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_10.setObjectName("horizontalLayout_10")
        self.pushButtonClearPrompt = QtWidgets.QPushButton(parent=self.groupBoxPromptOperator)
        self.pushButtonClearPrompt.setObjectName("pushButtonClearPrompt")
        self.horizontalLayout_10.addWidget(self.pushButtonClearPrompt)
        spacerItem5 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Policy.Expanding, QtWidgets.QSizePolicy.Policy.Minimum)
        self.horizontalLayout_10.addItem(spacerItem5)
        self.horizontalLayout_9.addLayout(self.horizontalLayout_10)
        self.verticalLayout_3.addLayout(self.horizontalLayout_9)
        self.horizontalLayout_7.addLayout(self.verticalLayout_3)
        self.verticalLayout_4.addWidget(self.groupBoxPromptOperator)
        self.horizontalLayout_5.addLayout(self.verticalLayout_4)
        self.horizontalLayout_2.addLayout(self.horizontalLayout_5)
        self.horizontalLayout_3.addLayout(self.horizontalLayout_2)
        self.verticalLayout.addWidget(self.groupBox_Prompt)
        self.groupBox_OutPut = QtWidgets.QGroupBox(parent=Dialog)
        self.groupBox_OutPut.setObjectName("groupBox_OutPut")
        self.horizontalLayout_12 = QtWidgets.QHBoxLayout(self.groupBox_OutPut)
        self.horizontalLayout_12.setObjectName("horizontalLayout_12")
        self.horizontalLayout_11 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_11.setObjectName("horizontalLayout_11")
        self.plainTextEditResult = QtWidgets.QPlainTextEdit(parent=self.groupBox_OutPut)
        self.plainTextEditResult.setObjectName("plainTextEditResult")
        self.horizontalLayout_11.addWidget(self.plainTextEditResult)
        self.horizontalLayout_13 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_13.setObjectName("horizontalLayout_13")
        self.groupBoxResult = QtWidgets.QGroupBox(parent=self.groupBox_OutPut)
        self.groupBoxResult.setObjectName("groupBoxResult")
        self.horizontalLayout_14 = QtWidgets.QHBoxLayout(self.groupBoxResult)
        self.horizontalLayout_14.setObjectName("horizontalLayout_14")
        self.verticalLayout_5 = QtWidgets.QVBoxLayout()
        self.verticalLayout_5.setObjectName("verticalLayout_5")
        self.comboBoxModel = QtWidgets.QComboBox(parent=self.groupBoxResult)
        self.comboBoxModel.setToolTip("")
        self.comboBoxModel.setToolTipDuration(1)
        self.comboBoxModel.setWhatsThis("")
        self.comboBoxModel.setObjectName("comboBoxModel")
        self.verticalLayout_5.addWidget(self.comboBoxModel)
        self.doubleSpinBoxTemperature = QtWidgets.QDoubleSpinBox(parent=self.groupBoxResult)
        self.doubleSpinBoxTemperature.setMaximum(1.0)
        self.doubleSpinBoxTemperature.setSingleStep(0.05)
        self.doubleSpinBoxTemperature.setObjectName("doubleSpinBoxTemperature")
        self.verticalLayout_5.addWidget(self.doubleSpinBoxTemperature)
        self.pushButtonGenerateResult = QtWidgets.QPushButton(parent=self.groupBoxResult)
        self.pushButtonGenerateResult.setObjectName("pushButtonGenerateResult")
        self.verticalLayout_5.addWidget(self.pushButtonGenerateResult)
        self.pushButtonLoadQueryInfo = QtWidgets.QPushButton(parent=self.groupBoxResult)
        self.pushButtonLoadQueryInfo.setObjectName("pushButtonLoadQueryInfo")
        self.verticalLayout_5.addWidget(self.pushButtonLoadQueryInfo)
        self.pushButtonSaveQueryInfo = QtWidgets.QPushButton(parent=self.groupBoxResult)
        self.pushButtonSaveQueryInfo.setObjectName("pushButtonSaveQueryInfo")
        self.verticalLayout_5.addWidget(self.pushButtonSaveQueryInfo)
        self.pushButtonCopyResult = QtWidgets.QPushButton(parent=self.groupBoxResult)
        self.pushButtonCopyResult.setObjectName("pushButtonCopyResult")
        self.verticalLayout_5.addWidget(self.pushButtonCopyResult)
        self.horizontalLayout_14.addLayout(self.verticalLayout_5)
        self.horizontalLayout_13.addWidget(self.groupBoxResult)
        self.horizontalLayout_11.addLayout(self.horizontalLayout_13)
        self.horizontalLayout_12.addLayout(self.horizontalLayout_11)
        self.verticalLayout.addWidget(self.groupBox_OutPut)
        self.horizontalLayout.addLayout(self.verticalLayout)

        self.retranslateUi(Dialog)
        self.tabWidgetExamples.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Generate Code from Examples"))
        self.groupBoxExamples.setTitle(_translate("Dialog", "Examples"))
        self.tabWidgetExamples.setTabText(self.tabWidgetExamples.indexOf(self.tabExample1), _translate("Dialog", "Tab 1"))
        self.tabWidgetExamples.setTabText(self.tabWidgetExamples.indexOf(self.tabExample2), _translate("Dialog", "Example 2"))
        self.pushButtonClearExample.setText(_translate("Dialog", "Clear Current"))
        self.pushButtonDeleteExample.setText(_translate("Dialog", "Delete Example"))
        self.pushButtonNewExample.setText(_translate("Dialog", "New Example"))
        self.groupBox_Prompt.setTitle(_translate("Dialog", "Prompt"))
        self.groupBoxPromptFile.setTitle(_translate("Dialog", "Prompt File Operation"))
        self.labelChoosePromptFile.setText(_translate("Dialog", "Open prompt file: "))
        self.pushButtonOpenPromptFile.setText(_translate("Dialog", "Open"))
        self.groupBoxPromptOperator.setTitle(_translate("Dialog", "Prompt Operation"))
        self.pushButtonRefreshPrompt.setText(_translate("Dialog", "Reload"))
        self.pushButtonClearPrompt.setText(_translate("Dialog", "Clear"))
        self.groupBox_OutPut.setTitle(_translate("Dialog", "Result"))
        self.groupBoxResult.setTitle(_translate("Dialog", "Result operation"))
        self.pushButtonGenerateResult.setText(_translate("Dialog", "Generate"))
        self.pushButtonLoadQueryInfo.setText(_translate("Dialog", "Load Data"))
        self.pushButtonSaveQueryInfo.setText(_translate("Dialog", "Save Data"))
        self.pushButtonCopyResult.setText(_translate("Dialog", "Copy result"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Dialog = QtWidgets.QDialog()
    ui = Ui_Dialog()
    ui.setupUi(Dialog)
    Dialog.show()
    sys.exit(app.exec())
