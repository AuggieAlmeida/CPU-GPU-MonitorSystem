# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'StartMenu.ui'
#
# Created by: PyQt5 UI code generator 5.15.7
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(824, 480)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(MainWindow.sizePolicy().hasHeightForWidth())
        MainWindow.setSizePolicy(sizePolicy)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.centralwidget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.menubar_2 = QtWidgets.QFrame(self.centralwidget)
        self.menubar_2.setMaximumSize(QtCore.QSize(16777215, 40))
        self.menubar_2.setStyleSheet("background-color: rgb(173, 52, 143);\n"
                                     "border-radius: 4px 4px;")
        self.menubar_2.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.menubar_2.setFrameShadow(QtWidgets.QFrame.Raised)
        self.menubar_2.setObjectName("menubar_2")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.menubar_2)
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_2.setSpacing(0)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.frame_erro = QtWidgets.QFrame(self.menubar_2)
        self.frame_erro.setMinimumSize(QtCore.QSize(0, 0))
        self.frame_erro.setMaximumSize(QtCore.QSize(370, 32))
        self.frame_erro.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.frame_erro.setStyleSheet("background-color: rgb(226, 67, 189);\n"
                                      "border-radius: 8px;\n"
                                      "")
        self.frame_erro.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.frame_erro.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_erro.setObjectName("frame_erro")
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout(self.frame_erro)
        self.horizontalLayout_3.setContentsMargins(10, 0, 10, 0)
        self.horizontalLayout_3.setSpacing(0)
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.label = QtWidgets.QLabel(self.frame_erro)
        self.label.setStyleSheet("\n"
                                 "font: 25 20pt \"Yu Gothic Light\";")
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")
        self.horizontalLayout_3.addWidget(self.label)
        self.pushButton = QtWidgets.QPushButton(self.frame_erro)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pushButton.sizePolicy().hasHeightForWidth())
        self.pushButton.setSizePolicy(sizePolicy)
        self.pushButton.setMaximumSize(QtCore.QSize(26, 26))
        font = QtGui.QFont()
        font.setFamily("Sitka Small Semibold")
        font.setPointSize(20)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(7)
        self.pushButton.setFont(font)
        self.pushButton.setStyleSheet("QPushButton {\n"
                                      "    font: 63 20pt \"Sitka Small Semibold\";\n"
                                      "    background-image: url(:/close_image/cls.png);\n"
                                      "    background-position: center;\n"
                                      "    background-size: contain;\n"
                                      "    border: 2px solid;\n"
                                      "    border-color: rgb(153, 92, 138);\n"
                                      "    background-color: #d47fc0;\n"
                                      "}\n"
                                      "\n"
                                      "QPushButton:hover {\n"
                                      "    background-color: rgb(175, 51, 148);    \n"
                                      "    color: rgb(255, 255, 255);\n"
                                      "}\n"
                                      "\n"
                                      "QPushButton:pressed {\n"
                                      "    background-color: rgb(175, 51, 148);    \n"
                                      "    color: rgb(255, 153, 230);\n"
                                      "}")
        self.pushButton.setText("")
        self.pushButton.setObjectName("pushButton")
        self.horizontalLayout_3.addWidget(self.pushButton)
        self.horizontalLayout_2.addWidget(self.frame_erro)
        self.verticalLayout.addWidget(self.menubar_2)
        self.start = QtWidgets.QFrame(self.centralwidget)
        self.start.setStyleSheet("background-color: rgb(255, 170, 255);")
        self.start.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.start.setFrameShadow(QtWidgets.QFrame.Raised)
        self.start.setObjectName("start")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.start)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.frame_5 = QtWidgets.QFrame(self.start)
        self.frame_5.setMaximumSize(QtCore.QSize(300, 350))
        self.frame_5.setStyleSheet("background-color: rgb(214, 128, 193);\n"
                                   "border-radius:15px;")
        self.frame_5.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.frame_5.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_5.setObjectName("frame_5")
        self.frame = QtWidgets.QFrame(self.frame_5)
        self.frame.setGeometry(QtCore.QRect(30, -50, 251, 281))
        self.frame.setAutoFillBackground(False)
        self.frame.setStyleSheet("background-image: url(:/icons/LOGO.png.png);\n"
                                 "background-repeat: no-repeat;\n"
                                 "background-position: top;\n"
                                 "background-size: contain;\n"
                                 "\n"
                                 "\n"
                                 "")
        self.frame.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.btn_Login = QtWidgets.QPushButton(self.frame_5)
        self.btn_Login.setGeometry(QtCore.QRect(70, 280, 160, 40))
        self.btn_Login.setMinimumSize(QtCore.QSize(160, 40))
        self.btn_Login.setMaximumSize(QtCore.QSize(0, 0))
        self.btn_Login.setStyleSheet("QPushButton {\n"
                                     "    font: 16pt \"MS Shell Dlg 2\";\n"
                                     "    background-color: #AD348F;\n"
                                     "    border: 2px solid  rgb(255, 170, 255);\n"
                                     "    color: rgb(255, 255, 255);\n"
                                     "}\n"
                                     "\n"
                                     "\n"
                                     "QPushButton:hover {\n"
                                     "      transform: scale(1.1);\n"
                                     "    background-color: #E68ACF\n"
                                     "}\n"
                                     "\n"
                                     "QPushButton:pressed {\n"
                                     "    background-color: rgb(226, 67, 189);\n"
                                     "}\n"
                                     "")
        self.btn_Login.setObjectName("btn_Login")
        self.horizontalLayout.addWidget(self.frame_5)
        self.verticalLayout.addWidget(self.start)
        self.bottom = QtWidgets.QFrame(self.centralwidget)
        self.bottom.setMaximumSize(QtCore.QSize(16777215, 40))
        self.bottom.setStyleSheet("background-color: rgb(173, 52, 143);")
        self.bottom.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.bottom.setFrameShadow(QtWidgets.QFrame.Raised)
        self.bottom.setObjectName("bottom")
        self.verticalLayout.addWidget(self.bottom)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 824, 21))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label.setText(_translate("MainWindow", "Seja bem vindo!!"))
        self.btn_Login.setText(_translate("MainWindow", "ENTRAR"))

from assets.img import files_rc

if __name__ == "__main__":
    import sys

    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())