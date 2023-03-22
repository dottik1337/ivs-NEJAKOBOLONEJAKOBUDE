# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'kalkulacka1.ui'
#
# Created by: PyQt5 UI code generator 5.14.1
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets
import sys


buffer = ''
zatvorkaprava = 0
zatvorkalava = 0
zatvorka = False


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        def funkcia(cislo):
            global buffer
            buffer+=str(cislo)
            self.lineEdit.setText(buffer)
            self.buttoneq.setEnabled(True)
            self.buttonplus.setEnabled(True)
            self.buttonsub.setEnabled(True)
            self.buttonmul.setEnabled(True) 
            #print(buffer)
        
        def delete():
            global buffer
            buffer=buffer[:-1]
            self.lineEdit.setText(buffer)
            if len(buffer) > 0:
                lastChar = buffer[len(buffer) - 1]
                if lastChar in ['+', '-', '*', '/']:
                   self.buttoneq.setEnabled(False)
                   self.buttonplus.setEnabled(False)
                   self.buttonsub.setEnabled(False)
                   self.buttonmul.setEnabled(False)
                else: 
                    self.buttoneq.setEnabled(True)
                    self.buttonplus.setEnabled(True)
                    self.buttonsub.setEnabled(True)
                    self.buttonmul.setEnabled(True)                   
            
        def znamienko(znamienko):
            global buffer
            global zatvorka
            zatvorka = True
            buffer+=str(znamienko)
            self.lineEdit.setText(buffer)
            self.buttoneq.setEnabled(False)
            self.buttonplus.setEnabled(False)
            self.buttonsub.setEnabled(False)
            self.buttonmul.setEnabled(False)
            
            self.button4.setEnabled(True)
            self.button3.setEnabled(True)
            self.button2.setEnabled(True)
            self.button1.setEnabled(True)
            self.button5.setEnabled(True)
            self.button6.setEnabled(True)
            self.button7.setEnabled(True)
            self.button8.setEnabled(True)
            self.button9.setEnabled(True)
        
        def zatvorka():
            global buffer
            global zatvorka
            global zatvorkaprava
            global zatvorkalava
            kkt = 0
            lastChar = ''
            for num in range (len(buffer)):
                if buffer[num] in ['+', '-', '*', '/' ]:
                    kkt+=1
                elif buffer[num] in ['(']:
                    kkt=0
                if buffer[num] == '(':
                    zatvorkalava+=1
                elif buffer[num] == ')':
                    zatvorkaprava+=1
            
            print (zatvorkalava)
            print (zatvorkaprava)
            if len(buffer) != 0:
                lastChar = buffer[len(buffer) - 1]
            else: lastChar=''
            
            if  kkt == 0 and len(buffer) != 0:
                buffer=buffer
            
            elif lastChar == '' or lastChar in ['+', '-', '*', '/' '(']:
                buffer+='('
                self.buttoneq.setEnabled(False)
                self.buttonplus.setEnabled(False)
                self.buttonsub.setEnabled(False)
                self.buttonmul.setEnabled(False)
                
                
            elif zatvorkalava > zatvorkaprava and zatvorkalava != zatvorkaprava: 
                buffer+=')'
                self.button4.setEnabled(False)
                self.button3.setEnabled(False)
                self.button2.setEnabled(False)
                self.button1.setEnabled(False)
                self.button5.setEnabled(False)
                self.button6.setEnabled(False)
                self.button7.setEnabled(False)
                self.button8.setEnabled(False)
                self.button9.setEnabled(False)
           
            zatvorkaprava=0
            zatvorkalava=0
            self.lineEdit.setText(buffer)
            
            
            
            
            
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(860, 616)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        
        self.button1 = QtWidgets.QPushButton(self.centralwidget)
        self.button1.setGeometry(QtCore.QRect(50, 460, 101, 101))
        self.button1.setObjectName("button1")
        self.button4 = QtWidgets.QPushButton(self.centralwidget)
        self.button4.setGeometry(QtCore.QRect(50, 340, 101, 101))
        self.button4.setObjectName("button4")
        self.button7 = QtWidgets.QPushButton(self.centralwidget)
        self.button7.setGeometry(QtCore.QRect(50, 220, 101, 101))
        self.button7.setObjectName("button7")
        self.button8 = QtWidgets.QPushButton(self.centralwidget)
        self.button8.setGeometry(QtCore.QRect(170, 220, 101, 101))
        self.button8.setObjectName("button8")
        self.button5 = QtWidgets.QPushButton(self.centralwidget)
        self.button5.setGeometry(QtCore.QRect(170, 340, 101, 101))
        self.button5.setObjectName("button5")
        self.button2 = QtWidgets.QPushButton(self.centralwidget)
        self.button2.setGeometry(QtCore.QRect(170, 460, 101, 101))
        self.button2.setObjectName("button2")
        self.button9 = QtWidgets.QPushButton(self.centralwidget)
        self.button9.setGeometry(QtCore.QRect(290, 220, 101, 101))
        self.button9.setObjectName("button9")
        self.button6 = QtWidgets.QPushButton(self.centralwidget)
        self.button6.setGeometry(QtCore.QRect(290, 340, 101, 101))
        self.button6.setObjectName("button6")
        self.button3 = QtWidgets.QPushButton(self.centralwidget)
        self.button3.setGeometry(QtCore.QRect(290, 460, 101, 101))
        self.button3.setObjectName("button3")
        self.button0 = QtWidgets.QPushButton(self.centralwidget)
        self.button0.setGeometry(QtCore.QRect(410, 460, 101, 101))
        self.button0.setObjectName("button0")
        self.buttoneq = QtWidgets.QPushButton(self.centralwidget)
        self.buttoneq.setGeometry(QtCore.QRect(530, 460, 301, 101))
        self.buttoneq.setObjectName("buttoneq")
        self.buttonplus = QtWidgets.QPushButton(self.centralwidget)
        self.buttonplus.setGeometry(QtCore.QRect(530, 350, 101, 101))
        self.buttonplus.setObjectName("buttonplus")
        self.buttonsub = QtWidgets.QPushButton(self.centralwidget)
        self.buttonsub.setGeometry(QtCore.QRect(730, 350, 101, 101))
        self.buttonsub.setObjectName("buttonsub")
        self.buttonmul = QtWidgets.QPushButton(self.centralwidget)
        self.buttonmul.setGeometry(QtCore.QRect(530, 240, 101, 101))
        self.buttonmul.setObjectName("buttonmul")
        self.buttondiv = QtWidgets.QPushButton(self.centralwidget)
        self.buttondiv.setGeometry(QtCore.QRect(730, 240, 101, 101))
        self.buttondiv.setObjectName("buttondiv")
        
        self.lineEdit = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit.setGeometry(QtCore.QRect(10, 20, 831, 51))
        self.lineEdit.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.lineEdit.setObjectName("lineEdit")
        
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 860, 20))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.button0.clicked.connect(zatvorka) 
        self.button1.clicked.connect(lambda: funkcia (1))
        self.button2.clicked.connect(lambda: funkcia (2))
        self.button3.clicked.connect(lambda: funkcia (3))
        self.button4.clicked.connect(lambda: funkcia (4))
        self.button5.clicked.connect(lambda: funkcia (5))
        self.button6.clicked.connect(lambda: funkcia (6))
        self.button7.clicked.connect(lambda: funkcia (7))
        self.button8.clicked.connect(lambda: funkcia (8))
        self.button9.clicked.connect(lambda: funkcia (9))
        
        self.buttondiv.clicked.connect(delete)
        
        self.buttonmul.clicked.connect(lambda: znamienko ('*'))
        self.buttonplus.clicked.connect(lambda: znamienko ('+'))
        self.buttonsub.clicked.connect(lambda: znamienko ('-'))
        
        self.lineEdit.setText(str(buffer))
        
        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.button1.setText(_translate("MainWindow", "1"))
        self.button4.setText(_translate("MainWindow", "4"))
        self.button7.setText(_translate("MainWindow", "7"))
        self.button8.setText(_translate("MainWindow", "8"))
        self.button5.setText(_translate("MainWindow", "5"))
        self.button2.setText(_translate("MainWindow", "2"))
        self.button9.setText(_translate("MainWindow", "9"))
        self.button6.setText(_translate("MainWindow", "6"))
        self.button3.setText(_translate("MainWindow", "3"))
        self.button0.setText(_translate("MainWindow", "0"))
        self.buttoneq.setText(_translate("MainWindow", "="))
        self.buttonplus.setText(_translate("MainWindow", "+"))
        self.buttonsub.setText(_translate("MainWindow", "-"))
        self.buttonmul.setText(_translate("MainWindow", "*"))
        self.buttondiv.setText(_translate("MainWindow", "/"))
        
    
    



if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
