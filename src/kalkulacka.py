# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'calc2.ui'
#
# Created by: PyQt5 UI code generator 5.14.1
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets

import sys
sys.path.append('/calculator')
print(sys.path)
import ivsmath

"""
@ Global param buffer is used for storing the string that was written in the calculator
@ Global param buffer is used to indicate if the user is writing a power
@ Global param lenpow is used for storing the length of the power
@ Global param index is uesd for inidicataing where the root should be placed in the buffer
"""

buffer = ''
pow = False
lenpow = 0
index = -2

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        
        def superscript(p):
            """
                @ brief function converts a number to its superscript
                @ param intiger the number that wants to be converted to superscipt 
            """
            superscripts = ["⁰", "¹", "²", "³", "⁴", "⁵", "⁶", "⁷", "⁸", "⁹",]
            return ''.join([superscripts[int(char)] for char in str(p)])
        
        def funkcia(cislo):
            """
            @ brief function adds a number to the buffer and displays the new buffer in the calculator
            if the user is writing a power it adds the supercript of that number to the buffer
            @ param the number that wants to be added to the buffer
            """
            
            global buffer
            global pow
            global lenpow
            global index
            if len(buffer) > 0:
                lastChar = buffer[len(buffer) - 1]
            else: lastChar=''
            
            if len(buffer) > 1:
                secondlast = buffer[len(buffer) - 2]
            else: secondlast=''
            
            if pow == True and lastChar != '⁾' and (cislo != 0 or lastChar not in ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9", '⁺' , '⁻' , 'ˣ' , '÷', '⁽']):
                
                buffer+=str(superscript(cislo))
                lenpow+=1
            elif index != -2:
                
                if cislo == 0 and (buffer[index] in ['+', '-', 'x', '÷', '('] or index == -1):
                    
                    buffer=buffer
                else:
                    buffer+=' '
                    mylist = list(buffer)
                    for i in range (len(buffer)-2, index, -1):
                        mylist[i+1] = buffer[i]
                    mylist[index+1] = superscript(cislo)
                    index+=1
                    buffer = ''.join(mylist)
            elif lastChar not in [')',"⁰", "¹", "²", "³", "⁴", "⁵", "⁶", "⁷", "⁸", "⁹", '!'] and (lastChar != '0' or secondlast not in ['+', '-', 'x', '÷']  ) and pow == False:
                buffer+=str(cislo)
            
            self.label.setText(buffer)
            self.buttoneq.setEnabled(True)
        
        def delete():
            """
            @ brief function deletes the last value stored in the buffer or if the 
            last value in the buffer is the n root it deletes the root and the superscript of the root
            """
            global buffer
            global lenpow
            global pow
            global index
            index = -2
            if len(buffer) > 0:
                lastChar = buffer[len(buffer) - 1]
            else: lastChar= ''
            if lastChar == '√':
                buffer=buffer[:-1]
                while True:
                    if len(buffer) > 0:
                        lastChar = buffer[len(buffer) - 1]
                    else: break
                    if lastChar in ["⁰", "¹", "²", "³", "⁴", "⁵", "⁶", "⁷", "⁸", "⁹"]:
                        buffer=buffer[:-1]
                    else: break
                self.label.setText(buffer)
            else:            
                buffer=buffer[:-1]
                self.label.setText(buffer)
                if len(buffer) > 0:
                    lastChar = buffer[len(buffer) - 1]
                    if lastChar in ['+', '-', 'x', '÷']:
                        self.buttoneq.setEnabled(False)
                    else: 
                        self.buttoneq.setEnabled(True)
                if pow==True:
                    lenpow-=1
                    
                    
                if lenpow==0:
                    pow = False
            
                   
          
        def znamienko(znamienko):
            """
            @brief the function adds the sign to the end of the buffer or its superscript 
            @ param the sign that wants to be added
            """
            
            global buffer
            global pow
            global index
            global lenpow
            index = -2
            zatvotky = 0
            if len(buffer) > 0:
                    lastChar = buffer[len(buffer) - 1]
                    
            for i in range(len(buffer)):
                if buffer[i] == '⁽':
                    zatvotky+=1
                elif buffer[i] == '⁾':
                    zatvotky-=1
                elif buffer[i] in ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"] :
                    zatvotky = 0
                    
                    
            if zatvotky != 0:
                if lastChar in ['⁺' , '⁻' , 'ˣ' , '÷']:
                    buffer=buffer
                    
                elif lastChar == '⁽' and znamienko in ['+', 'x', '÷']:
                    buffer=buffer
                
                else:
                    supznamienka= { '+' : '⁺' ,'-' : '⁻' , 'x' : 'ˣ' , '÷' : '÷'}
                    znamienko=supznamienka[znamienko]
                    buffer+=znamienko
                    self.label.setText(buffer)
                    
            else:            
                pow = False
                lenpow = 0
                if lastChar in ['+', '-', 'x', '÷', '√']:
                        buffer=buffer
                        
                elif lastChar == '(' and znamienko in ['+', 'x', '÷']:
                    buffer=buffer
                
                else:
                    buffer+=str(znamienko)
                    self.label.setText(buffer)
                    self.buttoneq.setEnabled(False)
                    
                    
                        
        def pow():
            """
            @brief function sets global variable pow to true
            """
            global pow
            if len(buffer) > 0:
                lastChar = buffer[len(buffer) - 1]
            else: lastChar=''
            if lastChar in ['+', '-', 'x', '÷', '', '(', '!', '.'] or len(buffer) == 0:
                pow=False
            else:
                pow=True
            
        def clear():
            """
            @brief function clears buffer
            """
            global buffer
            global pow
            global index
            global lenpow
            pow = False
            buffer = ''
            
            lenpow = 0
            index = -2
            self.label.setText(buffer)
        
        def leftbracket():
            """
            @brief function adds left bracket or its superscipt to the end of the buffer
            """
            global buffer
            global pow
            global lenpow
            if len(buffer) > 0:
                lastChar = buffer[len(buffer) - 1]
            else: lastChar = ''
            if lastChar in ['+', '-', 'x', '÷', '', '(']:
                buffer+='('
            elif pow == True :
                if lastChar in ['⁺' , '⁻' , 'ˣ' , '÷', '⁽', '0', '1', '2', '3', '4', '5', '6', '7', '8', '9']:
                    buffer+='⁽'
                    lenpow+=1   
            else: buffer=buffer
            self.label.setText(buffer)
        
        def rightbracket():
            """
            @brief function adds right bracket or its superscipt to the end of the buffer
            """
            global buffer
            global pow
            global lenpow
            if len(buffer) > 0:
                lastChar = buffer[len(buffer) - 1]
            else: lastChar=''
            lava = 0
            prava = 0
            mlava = 0
            mprava = 0
            for i in range(len(buffer)):
                if buffer[i] == '(':
                    lava+=1
                elif buffer[i] == '⁽':
                    mlava+=1
                elif buffer[i] == ')':
                    prava+=1
                elif buffer[i] == '⁾':
                    mprava+=1
                    
            if lastChar in ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9', ')', '!'] and lava>prava and pow == False: 
                buffer += ')'
                self.label.setText(buffer)
            elif lastChar in ["⁰", "¹", "²", "³", "⁴", "⁵", "⁶", "⁷", "⁸", "⁹", '⁾'] and mlava>mprava and pow == True:
                buffer += '⁾'
                lenpow+=1
                self.label.setText(buffer)
            else: buffer = buffer
            
        def odmocnina():
            """
            @brief function adds square root and a left bracket to the end of the buffer
            """
            global buffer
            global pow
            if len(buffer) > 0:
                lastChar = buffer[len(buffer) - 1]
            else: lastChar=''
            if pow == False and lastChar in [ '+', '-', 'x', '÷', '']:
                buffer+='√'
                buffer+='('
                self.label.setText(buffer)
                
        def ntaodmocnina():
            """
            @brief funtion adds root to the first viable positon in the buffer or if 
            there is a right bracket it finds a left bracket so that the number of 
            left brackets = right brackets and adds the root to the first viable position 
            """
            global buffer
            global pow
            global index
            if len(buffer) > 0:
                lastChar = buffer[len(buffer) - 1]
            else: lastChar=''
            
            prava = 0
            lava = 0
            
            if lastChar in ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9', ')'] and pow == False:
                for i in range(len(buffer)-1, -1, -1):
                    if buffer[i] == ')':
                        prava+=1
                    elif buffer[i] == '(':
                        lava+=1
                    if lava == prava and buffer[i] in ['+', '-', 'x', '÷']:
                        index = i
                        break
                    elif lava == prava: index = -1
                        
                if index != -2:
                    buffer+=' '
                    mylist = list(buffer)
                    
                    for i in range(len(buffer)-2, index, -1):
                        
                        mylist[i+1]=buffer[i]
                    mylist[index+1] = '√'
                    buffer = ''.join(mylist)
            self.label.setText(buffer)
            
        def faktorial():
            """
            @brief function adds ! to the end of the buffer
            """
            
            global buffer
            global pow
            
            if len(buffer) > 0:
                lastChar = buffer[len(buffer) - 1]
            else: lastChar=''
            
            if lastChar in ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9', ')']:
                buffer+='!'
                self.label.setText(buffer)
            else: buffer=buffer
                    
        def dash():
            """
            @brief function adds . to the end of the buffer
            """
            global buffer
            global pow
            ciarka = False
            for i in range (len(buffer)-1, -1, -1):
                
                if buffer[i] == '.':
                    ciarka = True
                elif buffer[i] not in ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']:
                    break 
            
            
            if ciarka == False and pow == False and len(buffer) != 0:
                buffer += '.'
                self.label.setText(buffer)
            else: buffer = buffer
            
        def convert():
            """
            @brief function converts the buffer so it can be processed by the library
            """
            
            global buffer
            newbuffer = ''
            x = { '⁽' : '(', '⁾' : ')', '⁰' : '0', '¹' : '1', '²' : '2', '³' : '3', '⁴' : '4', '⁵' : '5', 
                 '⁶' : '6', '⁷' : '7', '⁸' : '8', '⁹' : '9',   '⁺' : '+' , '⁻' : '-', 'ˣ' : '*' , '÷' : '/', '√' : 'r', 'x' : '*'}
            
            for i in range(0, len(buffer), 1):
                
                if buffer[i] in x:
                    if i-1 >= 0 and buffer[i-1] in ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9', ')'] and buffer[i] in ["⁰", "¹", "²", "³", "⁴", "⁵", "⁶", "⁷", "⁸", "⁹", '⁽', '!']:
                        newbuffer+='^'
                    if buffer[i] == '√' and i == 0:
                        newbuffer+='2'
                    elif buffer[i] == '√' and buffer[i-1] not in ["⁰", "¹", "²", "³", "⁴", "⁵", "⁶", "⁷", "⁸", "⁹"]:
                        newbuffer+='2'
                    
                    newbuffer+=x[str(buffer[i])]
                else:
                    newbuffer+=buffer[i]    
            buffer = newbuffer 
            
        def equals():
            """
            @brief function converts the buffer so it can be used by the math library 
            and then stores the result inside the buffer
            """
            
            global buffer
            global pow
            global index
            global lenpow
            lenpow = 0
            index = -2
            pow = False
            convert()    
            print(buffer)
            buffer = ivsmath.evaluate_expression(buffer)
            buffer = str(buffer)
            self.label.setText(buffer)
                               
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(791, 589)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(10, 10, 771, 51))
        font = QtGui.QFont()
        font.setPointSize(17)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        font.setStrikeOut(False)
        self.label.setFont(font)
        self.label.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label.setObjectName("label")
        self.button1 = QtWidgets.QPushButton(self.centralwidget)
        self.button1.setGeometry(QtCore.QRect(20, 430, 91, 81))
        self.button1.setObjectName("button1")
        self.button4 = QtWidgets.QPushButton(self.centralwidget)
        self.button4.setGeometry(QtCore.QRect(20, 330, 91, 81))
        self.button4.setObjectName("button4")
        self.button7 = QtWidgets.QPushButton(self.centralwidget)
        self.button7.setGeometry(QtCore.QRect(20, 230, 91, 81))
        self.button7.setObjectName("button7")
        self.button8 = QtWidgets.QPushButton(self.centralwidget)
        self.button8.setGeometry(QtCore.QRect(130, 230, 91, 81))
        self.button8.setObjectName("button8")
        self.button5 = QtWidgets.QPushButton(self.centralwidget)
        self.button5.setGeometry(QtCore.QRect(130, 330, 91, 81))
        self.button5.setObjectName("button5")
        self.button2 = QtWidgets.QPushButton(self.centralwidget)
        self.button2.setGeometry(QtCore.QRect(130, 430, 91, 81))
        self.button2.setObjectName("button2")
        self.button3 = QtWidgets.QPushButton(self.centralwidget)
        self.button3.setGeometry(QtCore.QRect(240, 430, 91, 81))
        self.button3.setObjectName("button3")
        self.button6 = QtWidgets.QPushButton(self.centralwidget)
        self.button6.setGeometry(QtCore.QRect(240, 330, 91, 81))
        self.button6.setObjectName("button6")
        self.button9 = QtWidgets.QPushButton(self.centralwidget)
        self.button9.setGeometry(QtCore.QRect(240, 230, 91, 81))
        self.button9.setObjectName("button9")
        self.pushButton_0 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_0.setGeometry(QtCore.QRect(350, 420, 91, 81))
        self.pushButton_0.setObjectName("pushButton_0")
        self.buttoneq = QtWidgets.QPushButton(self.centralwidget)
        self.buttoneq.setGeometry(QtCore.QRect(460, 430, 311, 81))
        self.buttoneq.setObjectName("buttoneq")
        self.buttondel = QtWidgets.QPushButton(self.centralwidget)
        self.buttondel.setGeometry(QtCore.QRect(350, 230, 91, 81))
        self.buttondel.setObjectName("buttondel")
        self.buttonplus = QtWidgets.QPushButton(self.centralwidget)
        self.buttonplus.setGeometry(QtCore.QRect(460, 370, 151, 51))
        self.buttonplus.setObjectName("buttonplus")
        self.buttonsub = QtWidgets.QPushButton(self.centralwidget)
        self.buttonsub.setGeometry(QtCore.QRect(620, 370, 151, 51))
        self.buttonsub.setObjectName("buttonsub")
        self.buttonmul = QtWidgets.QPushButton(self.centralwidget)
        self.buttonmul.setGeometry(QtCore.QRect(460, 310, 151, 51))
        self.buttonmul.setObjectName("buttonmul")
        self.buttondiv = QtWidgets.QPushButton(self.centralwidget)
        self.buttondiv.setGeometry(QtCore.QRect(620, 310, 151, 51))
        self.buttondiv.setObjectName("buttondiv")
        self.buttonpow = QtWidgets.QPushButton(self.centralwidget)
        self.buttonpow.setGeometry(QtCore.QRect(460, 230, 71, 71))
        self.buttonpow.setObjectName("buttonpow")
        self.buttonodmocnina = QtWidgets.QPushButton(self.centralwidget)
        self.buttonodmocnina.setGeometry(QtCore.QRect(540, 230, 71, 71))
        self.buttonodmocnina.setObjectName("buttonodmocnina")
        self.buttofactorial = QtWidgets.QPushButton(self.centralwidget)
        self.buttofactorial.setGeometry(QtCore.QRect(620, 230, 71, 71))
        self.buttofactorial.setObjectName("buttofactorial")
        self.buttonsin = QtWidgets.QPushButton(self.centralwidget)
        self.buttonsin.setGeometry(QtCore.QRect(700, 230, 71, 71))
        self.buttonsin.setObjectName("buttonsin")
        self.buttonclear = QtWidgets.QPushButton(self.centralwidget)
        self.buttonclear.setGeometry(QtCore.QRect(350, 330, 91, 81))
        self.buttonclear.setObjectName("buttonclear")
        self.buttonlb = QtWidgets.QPushButton(self.centralwidget)
        self.buttonlb.setGeometry(QtCore.QRect(350, 140, 41, 81))
        self.buttonlb.setObjectName("buttonlb")
        self.buttonrb = QtWidgets.QPushButton(self.centralwidget)
        self.buttonrb.setGeometry(QtCore.QRect(400, 140, 41, 81))
        self.buttonrb.setObjectName("buttonrb")
        self.pushciarka = QtWidgets.QPushButton(self.centralwidget)
        self.pushciarka.setGeometry(QtCore.QRect(350, 510, 91, 31))
        self.pushciarka.setObjectName("pushciarka")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 791, 20))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.pushButton_0.clicked.connect(lambda: funkcia (0)) 
        self.button1.clicked.connect(lambda: funkcia (1))
        self.button2.clicked.connect(lambda: funkcia (2))
        self.button3.clicked.connect(lambda: funkcia (3))
        self.button4.clicked.connect(lambda: funkcia (4))
        self.button5.clicked.connect(lambda: funkcia (5))
        self.button6.clicked.connect(lambda: funkcia (6))
        self.button7.clicked.connect(lambda: funkcia (7))
        self.button8.clicked.connect(lambda: funkcia (8))
        self.button9.clicked.connect(lambda: funkcia (9))
        
        self.buttonmul.clicked.connect(lambda: znamienko ('x'))
        self.buttonplus.clicked.connect(lambda: znamienko ('+'))
        self.buttonsub.clicked.connect(lambda: znamienko ('-'))
        self.buttondiv.clicked.connect(lambda: znamienko ('÷'))
        
        self.buttonpow.clicked.connect(pow)

        self.buttondel.clicked.connect(delete)
        self.buttonclear.clicked.connect(clear)
        
        self.buttonlb.clicked.connect(leftbracket)
        self.buttonrb.clicked.connect(rightbracket)
        self.buttonodmocnina.clicked.connect(odmocnina)
        self.buttonsin.clicked.connect(ntaodmocnina)
        self.buttofactorial.clicked.connect(faktorial)
        self.pushciarka.clicked.connect(dash)
        
        self.buttoneq.clicked.connect(equals)
        
        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label.setText(_translate("MainWindow", ""))
        self.button1.setText(_translate("MainWindow", "1"))
        self.button4.setText(_translate("MainWindow", "4"))
        self.button7.setText(_translate("MainWindow", "7"))
        self.button8.setText(_translate("MainWindow", "8"))
        self.button5.setText(_translate("MainWindow", "5"))
        self.button2.setText(_translate("MainWindow", "2"))
        self.button3.setText(_translate("MainWindow", "3"))
        self.button6.setText(_translate("MainWindow", "6"))
        self.button9.setText(_translate("MainWindow", "9"))
        self.pushButton_0.setText(_translate("MainWindow", "0"))
        self.buttoneq.setText(_translate("MainWindow", "="))
        self.buttondel.setText(_translate("MainWindow", "CE"))
        self.buttonplus.setText(_translate("MainWindow", "+"))
        self.buttonsub.setText(_translate("MainWindow", "-"))
        self.buttonmul.setText(_translate("MainWindow", "x"))
        self.buttondiv.setText(_translate("MainWindow", " ÷"))
        self.buttonpow.setText(_translate("MainWindow", "x^y"))
        self.buttonodmocnina.setText(_translate("MainWindow", "√x"))
        self.buttofactorial.setText(_translate("MainWindow", "x!"))
        self.buttonsin.setText(_translate("MainWindow", "sin(x)"))
        self.buttonclear.setText(_translate("MainWindow", "AC"))
        self.buttonlb.setText(_translate("MainWindow", "("))
        self.buttonrb.setText(_translate("MainWindow", ")"))
        self.pushciarka.setText(_translate("MainWindow", "."))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
