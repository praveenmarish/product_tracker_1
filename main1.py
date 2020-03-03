# main design


from PyQt5 import QtCore, QtGui, QtWidgets
from core1 import operations


class Ui_Dialog(object):
    
        
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(549, 445)
        self.lineEdit = QtWidgets.QLineEdit(Dialog)
        self.lineEdit.setGeometry(QtCore.QRect(180, 110, 181, 21))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(12)
        self.lineEdit.setFont(font)
        self.lineEdit.setObjectName("lineEdit")
        self.label1 = QtWidgets.QLabel(Dialog)
        self.label1.setGeometry(QtCore.QRect(40, 110, 111, 21))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.label1.setFont(font)
        self.label1.setTextFormat(QtCore.Qt.PlainText)
        self.label1.setObjectName("label1")
        self.label = QtWidgets.QLabel(Dialog)
        self.label.setGeometry(QtCore.QRect(10, 20, 531, 41))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(20)
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setTextFormat(QtCore.Qt.RichText)
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")
        self.pushButton = QtWidgets.QPushButton(Dialog)
        self.pushButton.setGeometry(QtCore.QRect(440, 110, 75, 23))
        self.pushButton.setObjectName("pushButton")
        self.label_2 = QtWidgets.QLabel(Dialog)
        self.label_2.setGeometry(QtCore.QRect(40, 160, 111, 21))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.comboBox = QtWidgets.QComboBox(Dialog)
        self.comboBox.setGeometry(QtCore.QRect(180, 160, 181, 23))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(12)
        self.comboBox.setFont(font)
        self.comboBox.setCurrentText("")
        self.comboBox.setMaxVisibleItems(3)
        self.comboBox.setObjectName("comboBox")
        self.pushButton_2 = QtWidgets.QPushButton(Dialog)
        self.pushButton_2.setGeometry(QtCore.QRect(440, 160, 75, 23))
        self.pushButton_2.setObjectName("pushButton_2")
        self.pushButton_3 = QtWidgets.QPushButton(Dialog)
        self.pushButton_3.setGeometry(QtCore.QRect(440, 210, 75, 23))
        self.pushButton_3.setObjectName("pushButton_3")
        self.label_3 = QtWidgets.QLabel(Dialog)
        self.label_3.setGeometry(QtCore.QRect(40, 210, 111, 21))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")
        self.label_4 = QtWidgets.QLabel(Dialog)
        self.label_4.setGeometry(QtCore.QRect(40, 260, 111, 21))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.label_4.setFont(font)
        self.label_4.setObjectName("label_4")
        self.lineEdit_2 = QtWidgets.QLineEdit(Dialog)
        self.lineEdit_2.setGeometry(QtCore.QRect(180, 210, 181, 21))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(12)
        self.lineEdit_2.setFont(font)
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.lineEdit_3 = QtWidgets.QLineEdit(Dialog)
        self.lineEdit_3.setGeometry(QtCore.QRect(180, 260, 181, 21))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(12)
        self.lineEdit_3.setFont(font)
        self.lineEdit_3.setObjectName("lineEdit_3")
        self.pushButton_4 = QtWidgets.QPushButton(Dialog)
        self.pushButton_4.setGeometry(QtCore.QRect(440, 260, 75, 23))
        self.pushButton_4.setObjectName("pushButton_4")
        self.pushButton_5 = QtWidgets.QPushButton(Dialog)
        self.pushButton_5.setGeometry(QtCore.QRect(440, 310, 75, 23))
        self.pushButton_5.setObjectName("pushButton_5")
        self.label_5 = QtWidgets.QLabel(Dialog)
        self.label_5.setGeometry(QtCore.QRect(40, 310, 111, 21))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.label_5.setFont(font)
        self.label_5.setObjectName("label_5")
        self.lineEdit_4 = QtWidgets.QLineEdit(Dialog)
        self.lineEdit_4.setGeometry(QtCore.QRect(180, 310, 181, 21))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(12)
        self.lineEdit_4.setFont(font)
        self.lineEdit_4.setObjectName("lineEdit_4")
        self.pushButton_6 = QtWidgets.QPushButton(Dialog)
        self.pushButton_6.setGeometry(QtCore.QRect(170, 380, 75, 23))
        self.pushButton_6.setObjectName("pushButton_6")
        self.pushButton_7 = QtWidgets.QPushButton(Dialog)
        self.pushButton_7.setGeometry(QtCore.QRect(300, 380, 75, 23))
        self.pushButton_7.setObjectName("pushButton_7")

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)
        

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.lineEdit.setPlaceholderText(_translate("Dialog", "Enter product name/URL"))
        self.label1.setText(_translate("Dialog", "Product name:"))
        self.label.setText(_translate("Dialog", "PRODUCT TRACKER"))
        self.pushButton.setText(_translate("Dialog", "search"))
        self.label_2.setText(_translate("Dialog", "Select browser:"))
        self.pushButton_2.setText(_translate("Dialog", "compare"))
        self.pushButton_3.setText(_translate("Dialog", "save link"))
        self.label_3.setText(_translate("Dialog", "Maill id:"))
        self.label_4.setText(_translate("Dialog", "Password:"))
        self.lineEdit_2.setPlaceholderText(_translate("Dialog", "Enter maill id "))
        self.lineEdit_3.setPlaceholderText(_translate("Dialog", "Enter password"))
        self.pushButton_4.setText(_translate("Dialog", "show links"))
        self.pushButton_5.setText(_translate("Dialog", "send mail"))
        self.label_5.setText(_translate("Dialog", "Maill id:"))
        self.lineEdit_4.setPlaceholderText(_translate("Dialog", "Enter target maill id "))
        self.pushButton_6.setText(_translate("Dialog", "clear data"))
        self.pushButton_7.setText(_translate("Dialog", "close"))
        
        self.comboBox.addItem("google crome")
        self.comboBox.addItem("microsoft edge")
        self.comboBox.addItem("mozilla firefox")
        
        self.url=""
        
        
        self.pushButton.clicked.connect(self.search)
        self.pushButton_2.clicked.connect(self.compare)
        self.pushButton_3.clicked.connect(self.save_link)
        self.pushButton_4.clicked.connect(self.show_link)
        self.pushButton_5.clicked.connect(self.send_mail)
        self.pushButton_6.clicked.connect(self.clear_data)
        self.pushButton_7.clicked.connect(self.close)
       
    
    def initiate(self):
        self.load=operations(str(self.comboBox.currentText()),self.lineEdit.text(),self.lineEdit_2.text(),self.lineEdit_3.text(),self.lineEdit_4.text())        
        
        
        
    
    
    
    def search(self):
        
        self.initiate()
        self.load.set_browser()
        self.load.product_search()
        
        
    
    def compare(self):
        
        self.initiate()
        self.load.set_browser()
        self.load.compare()
        
        
        
    
    def save_link(self):
        
        self.initiate()
        self.load.save_link()
        
        
    
    def show_link(self):
        self.initiate()
        self.load.show_link()
        
    
    def send_mail(self):
        
        self.initiate()
        self.load.send_mail()
        
    
    def clear_data(self):
        self.lineEdit.clear()
        self.lineEdit_2.clear()
        self.lineEdit_3.clear()
        self.lineEdit_4.clear()
        
    
    def close(self):
        QtCore.QCoreApplication.instance().quit()
        


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Dialog = QtWidgets.QDialog()
    ui = Ui_Dialog()
    ui.setupUi(Dialog)
    Dialog.show()
    sys.exit(app.exec_())