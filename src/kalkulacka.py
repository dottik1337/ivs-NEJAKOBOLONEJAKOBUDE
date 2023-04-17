# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'finishcalc.ui'
#
# Created by: PyQt5 UI code generator 5.14.1
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets
from HelpWindov import Ui_HelpWindow


import sys
sys.path.append('/calculator')
#print(sys.path)
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


class Ui_Calculator(object):

    def openHelp(self):
        self.window = QtWidgets.QMainWindow()
        self.ui = Ui_HelpWindow()        
        self.ui.setupUi(self.window)
        self.window.show()

    def setupUi(self, Calculator):
        Calculator.setObjectName("Calculator")
        Calculator.resize(706, 325)
        #Calculator.setStyleSheet("background-color: rgb(242, 246, 255);\n"
#"\n"
#"\n"
#"")
        
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
                for i in range(len(buffer)-1, -1, -1):
                    
                    if buffer[i] in ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9", '⁺' , '⁻' , 'ˣ' , '÷', '⁽']:
                        if len(buffer)>i+1:
                            if buffer[i+1] == "⁰":
                                break
                            else:
                                print('aaaa')
                                buffer+=str(superscript(cislo))
                                lenpow+=1
                                break
                        else: 
                            buffer+=str(superscript(cislo))
                            lenpow+=1
                            break
                            print('bbb')
                
            elif pow == True and lastChar != '⁾' and cislo == 0 and lastChar != "⁰":
                buffer+=str(superscript(cislo))
                lenpow+=1
                print('cccc')
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
            
            if len(buffer) > 1:
                secondlast = buffer[len(buffer) - 2]
            else: secondlast=''
            
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
            elif lastChar == '(' and secondlast == 'n':
                buffer=buffer[:-1]
                buffer=buffer[:-1]
                buffer=buffer[:-1]
                buffer=buffer[:-1]
                self.label.setText(buffer)

            else:            
                buffer=buffer[:-1]
                self.label.setText(buffer)
                if len(buffer) > 0:
                    lastChar = buffer[len(buffer) - 1]
                    if lastChar in ['+', '-', 'x', '÷', '(', '.']:
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
            else:
                lastChar=""
                    
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
                if lastChar in ['+', '-', 'x', '÷', '√', '.', ''] and znamienko != '-':
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
                self.buttoneq.setEnabled(False)
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
            elif lastChar in ["⁰", "¹", "²", "³", "⁴", "⁵", "⁶", "⁷", "⁸", "⁹", '⁾'] and lava>prava:
                buffer+=')'
                pow = False
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
            global index
            ciarka = False
            for i in range (len(buffer)-1, -1, -1):
                
                if buffer[i] == '.' or buffer[len(buffer)-1] in ['+', '-', 'x', '÷', '(', ')', '!']:
                    ciarka = True
                elif buffer[i] not in ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9'] :
                    break 
            
            
            if ciarka == False and pow == False and len(buffer) != 0 and index == -2:
                buffer += '.'
                self.buttoneq.setEnabled(False)
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
                elif buffer[i] == 'n' or buffer[i] == 'i':
                    continue
                else:
                    newbuffer+=buffer[i]
            buffer = newbuffer
            newbuffer = ''
            zatvorka = False  
            print(buffer)      
            for i in range(0, len(buffer),1):
                print(zatvorka)
                if zatvorka == True and buffer[i] in ['+', '-', '*', '/']:
                    print("aaa")
                    newbuffer+=')'
                    zatvorka = False
                    newbuffer+=buffer[i]
                elif buffer[i] == 'e':   
                    
                    
                    newbuffer+='*10^('
                elif buffer[i] == '+':
                    
                    if buffer[i-1] == 'e':
                        zatvorka = True
                        continue
                    
                elif buffer[i] == '-' and i > 0:
                    if buffer[i-1] == 'e':
                        newbuffer+=buffer[i]
                        zatvorka=True
                        continue
                    
                else:
                    newbuffer+=buffer[i]
            print(newbuffer)        
            prava = 0
            lava = 0
            for i in range(0, len(newbuffer),1):
                if newbuffer[i]=='(':
                    lava+=1
                elif newbuffer[i]==')':
                    prava+=1
            
                   
            while(prava<lava):
                newbuffer+=')'
                prava+=1
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
            #print(buffer)
            buffer = ivsmath.evaluate_expression(buffer)
            buffer = str(buffer)
            self.label.setText(buffer)
            if buffer == "Math Error":
                buffer=''
        
        def sin():
            """
            @brief function adds sin( to the end of the buffer
            """
            global buffer
            global pow
            global index
            
            if len(buffer) > 0:
                lastChar = buffer[len(buffer) - 1]
            else: lastChar=''
            
            if lastChar in ['+', '-', 'x', '÷', '(', '' ] and pow == False and index == -2:
                buffer+='sin('
            else: buffer = buffer
            self.buttoneq.setEnabled(False)
            self.label.setText(buffer)
        
        self.centralwidget = QtWidgets.QWidget(Calculator)
        self.centralwidget.setObjectName("centralwidget")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(20, 10, 671, 61))
        font = QtGui.QFont()
        font.setFamily("URW Gothic [urw]")
        font.setPointSize(22)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        font.setStrikeOut(False)
        self.label.setFont(font)
        #self.label.setStyleSheet("background-color: rgb(242, 246, 255);\n"
#"border-color: black;\n"
#"border-width: 3px;")
        self.label.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label.setObjectName("label")
        self.button1 = QtWidgets.QPushButton(self.centralwidget)
        self.button1.setGeometry(QtCore.QRect(140, 190, 91, 31))
        font = QtGui.QFont()
        font.setFamily("URW Gothic [urw]")
        font.setPointSize(12)
        self.button1.setFont(font)
        self.button1.setStyleSheet("background-color: rgb(200, 185, 214);")
        self.button1.setObjectName("button1")
        self.button4 = QtWidgets.QPushButton(self.centralwidget)
        self.button4.setGeometry(QtCore.QRect(140, 140, 91, 31))
        font = QtGui.QFont()
        font.setFamily("URW Gothic [urw]")
        font.setPointSize(12)
        self.button4.setFont(font)
        self.button4.setStyleSheet("background-color: rgb(200, 185, 214);")
        self.button4.setObjectName("button4")
        self.button7 = QtWidgets.QPushButton(self.centralwidget)
        self.button7.setGeometry(QtCore.QRect(140, 90, 91, 31))
        font = QtGui.QFont()
        font.setFamily("URW Gothic [urw]")
        font.setPointSize(12)
        self.button7.setFont(font)
        self.button7.setStyleSheet("background-color: rgb(200, 185, 214);\n"
"borde-color: transparent;")
        self.button7.setObjectName("button7")
        self.button8 = QtWidgets.QPushButton(self.centralwidget)
        self.button8.setGeometry(QtCore.QRect(240, 90, 91, 31))
        font = QtGui.QFont()
        font.setFamily("URW Gothic [urw]")
        font.setPointSize(12)
        self.button8.setFont(font)
        self.button8.setStyleSheet("background-color: rgb(200, 185, 214);")
        self.button8.setObjectName("button8")
        self.button5 = QtWidgets.QPushButton(self.centralwidget)
        self.button5.setGeometry(QtCore.QRect(240, 140, 91, 31))
        font = QtGui.QFont()
        font.setFamily("URW Gothic [urw]")
        font.setPointSize(12)
        self.button5.setFont(font)
        self.button5.setStyleSheet("background-color: rgb(200, 185, 214);")
        self.button5.setObjectName("button5")
        self.button2 = QtWidgets.QPushButton(self.centralwidget)
        self.button2.setGeometry(QtCore.QRect(240, 190, 91, 31))
        font = QtGui.QFont()
        font.setFamily("URW Gothic [urw]")
        font.setPointSize(12)
        self.button2.setFont(font)
        self.button2.setStyleSheet("background-color: rgb(200, 185, 214);")
        self.button2.setObjectName("button2")
        self.button3 = QtWidgets.QPushButton(self.centralwidget)
        self.button3.setGeometry(QtCore.QRect(340, 190, 91, 31))
        font = QtGui.QFont()
        font.setFamily("URW Gothic [urw]")
        font.setPointSize(12)
        self.button3.setFont(font)
        self.button3.setStyleSheet("background-color: rgb(200, 185, 214);")
        self.button3.setObjectName("button3")
        self.button6 = QtWidgets.QPushButton(self.centralwidget)
        self.button6.setGeometry(QtCore.QRect(340, 140, 91, 31))
        font = QtGui.QFont()
        font.setFamily("URW Gothic [urw]")
        font.setPointSize(12)
        self.button6.setFont(font)
        self.button6.setStyleSheet("background-color: rgb(200, 185, 214);")
        self.button6.setObjectName("button6")
        self.button9 = QtWidgets.QPushButton(self.centralwidget)
        self.button9.setGeometry(QtCore.QRect(340, 90, 91, 31))
        font = QtGui.QFont()
        font.setFamily("URW Gothic [urw]")
        font.setPointSize(12)
        self.button9.setFont(font)
        self.button9.setStyleSheet("background-color: rgb(200, 185, 214);")
        self.button9.setObjectName("button9")
        self.pushButton_0 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_0.setGeometry(QtCore.QRect(140, 240, 191, 31))
        font = QtGui.QFont()
        font.setFamily("URW Gothic [urw]")
        font.setPointSize(12)
        self.pushButton_0.setFont(font)
        self.pushButton_0.setStyleSheet("background-color: rgb(200, 185, 214);")
        self.pushButton_0.setObjectName("pushButton_0")
        self.buttoneq = QtWidgets.QPushButton(self.centralwidget)
        self.buttoneq.setGeometry(QtCore.QRect(450, 240, 231, 31))
        font = QtGui.QFont()
        font.setFamily("URW Gothic [urw]")
        font.setPointSize(15)
        self.buttoneq.setFont(font)
        self.buttoneq.setStyleSheet("background-color: rgb(103, 105, 255);\n"
        "color: rgb(255, 255, 255);")
        self.buttoneq.setObjectName("buttoneq")
        self.buttondel = QtWidgets.QPushButton(self.centralwidget)
        self.buttondel.setGeometry(QtCore.QRect(450, 140, 71, 31))
        font = QtGui.QFont()
        font.setFamily("URW Gothic [urw]")
        font.setPointSize(12)
        self.buttondel.setFont(font)
        self.buttondel.setStyleSheet("background-color: rgb(180, 180, 180);")
        self.buttondel.setObjectName("buttondel")
        self.buttonplus = QtWidgets.QPushButton(self.centralwidget)
        self.buttonplus.setGeometry(QtCore.QRect(20, 90, 111, 31))
        font = QtGui.QFont()
        font.setFamily("URW Gothic [urw]")
        font.setPointSize(12)
        font.setBold(False)
        font.setWeight(50)
        self.buttonplus.setFont(font)
        self.buttonplus.setToolTip("")
        self.buttonplus.setStyleSheet("background-color: rgb(180, 180, 180);")
        self.buttonplus.setShortcut("")
        self.buttonplus.setObjectName("buttonplus")
        self.buttonsub = QtWidgets.QPushButton(self.centralwidget)
        self.buttonsub.setGeometry(QtCore.QRect(20, 140, 111, 31))
        font = QtGui.QFont()
        font.setFamily("URW Gothic [urw]")
        font.setPointSize(12)
        self.buttonsub.setFont(font)
        self.buttonsub.setStyleSheet("background-color: rgb(180, 180, 180);")
        self.buttonsub.setObjectName("buttonsub")
        self.buttonmul = QtWidgets.QPushButton(self.centralwidget)
        self.buttonmul.setGeometry(QtCore.QRect(20, 240, 111, 31))
        font = QtGui.QFont()
        font.setFamily("URW Gothic [urw]")
        font.setPointSize(12)
        self.buttonmul.setFont(font)
        self.buttonmul.setStyleSheet("background-color: rgb(180, 180, 180);")
        self.buttonmul.setObjectName("buttonmul")
        self.buttondiv = QtWidgets.QPushButton(self.centralwidget)
        self.buttondiv.setGeometry(QtCore.QRect(20, 190, 111, 31))
        font = QtGui.QFont()
        font.setFamily("URW Gothic [urw]")
        font.setPointSize(12)
        self.buttondiv.setFont(font)
        self.buttondiv.setStyleSheet("background-color: rgb(180, 180, 180);")
        self.buttondiv.setObjectName("buttondiv")
        self.buttonpow = QtWidgets.QPushButton(self.centralwidget)
        self.buttonpow.setGeometry(QtCore.QRect(530, 190, 71, 31))
        font = QtGui.QFont()
        font.setFamily("URW Gothic [urw]")
        font.setPointSize(12)
        self.buttonpow.setFont(font)
        self.buttonpow.setStyleSheet("background-color: rgb(180, 180, 180);")
        self.buttonpow.setObjectName("buttonpow")
        self.buttonodmocnina = QtWidgets.QPushButton(self.centralwidget)
        self.buttonodmocnina.setGeometry(QtCore.QRect(530, 140, 71, 31))
        font = QtGui.QFont()
        font.setFamily("URW Gothic [urw]")
        font.setPointSize(12)
        self.buttonodmocnina.setFont(font)
        self.buttonodmocnina.setStyleSheet("background-color: rgb(180, 180, 180);")
        self.buttonodmocnina.setObjectName("buttonodmocnina")
        self.buttofactorial = QtWidgets.QPushButton(self.centralwidget)
        self.buttofactorial.setGeometry(QtCore.QRect(610, 190, 71, 31))
        font = QtGui.QFont()
        font.setFamily("URW Gothic [urw]")
        font.setPointSize(12)
        self.buttofactorial.setFont(font)
        self.buttofactorial.setStyleSheet("background-color: rgb(180, 180, 180);")
        self.buttofactorial.setObjectName("buttofactorial")
        self.buttonsin = QtWidgets.QPushButton(self.centralwidget)
        self.buttonsin.setGeometry(QtCore.QRect(610, 90, 71, 31))
        font = QtGui.QFont()
        font.setFamily("URW Gothic [urw]")
        font.setPointSize(12)
        self.buttonsin.setFont(font)
        self.buttonsin.setStyleSheet("background-color: rgb(180, 180, 180);")
        self.buttonsin.setObjectName("buttonsin")
        self.buttonclear = QtWidgets.QPushButton(self.centralwidget)
        self.buttonclear.setGeometry(QtCore.QRect(450, 190, 71, 31))
        font = QtGui.QFont()
        font.setFamily("URW Gothic [urw]")
        font.setPointSize(12)
        self.buttonclear.setFont(font)
        self.buttonclear.setStyleSheet("background-color: rgb(180, 180, 180);")
        self.buttonclear.setObjectName("buttonclear")
        self.buttonlb = QtWidgets.QPushButton(self.centralwidget)
        self.buttonlb.setGeometry(QtCore.QRect(450, 90, 71, 31))
        font = QtGui.QFont()
        font.setFamily("URW Gothic [urw]")
        font.setPointSize(12)
        self.buttonlb.setFont(font)
        self.buttonlb.setStyleSheet("background-color: rgb(180, 180, 180);")
        self.buttonlb.setObjectName("buttonlb")
        self.buttonrb = QtWidgets.QPushButton(self.centralwidget)
        self.buttonrb.setGeometry(QtCore.QRect(530, 90, 71, 31))
        font = QtGui.QFont()
        font.setFamily("URW Gothic [urw]")
        font.setPointSize(12)
        self.buttonrb.setFont(font)
        self.buttonrb.setStyleSheet("background-color: rgb(180, 180, 180);")
        self.buttonrb.setObjectName("buttonrb")
        self.pushciarka = QtWidgets.QPushButton(self.centralwidget)
        self.pushciarka.setGeometry(QtCore.QRect(340, 240, 91, 31))
        font = QtGui.QFont()
        font.setFamily("URW Gothic [urw]")
        font.setPointSize(12)
        self.pushciarka.setFont(font)
        self.pushciarka.setStyleSheet("background-color: rgb(180, 180, 180);")
        self.pushciarka.setObjectName("pushciarka")
        self.ytaodmocnia = QtWidgets.QPushButton(self.centralwidget)
        self.ytaodmocnia.setEnabled(True)
        self.ytaodmocnia.setGeometry(QtCore.QRect(610, 140, 71, 31))
        font = QtGui.QFont()
        font.setFamily("URW Gothic [urw]")
        font.setPointSize(12)
        self.ytaodmocnia.setFont(font)
        self.ytaodmocnia.setStyleSheet("background-color: rgb(180, 180, 180);")
        self.ytaodmocnia.setObjectName("ytaodmocnia")
        Calculator.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(Calculator)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 706, 20))
        self.menubar.setObjectName("menubar")
        self.menuHelp = QtWidgets.QMenu(self.menubar)
        palette = QtGui.QPalette()
        brush = QtGui.QBrush(QtGui.QColor(242, 246, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Light, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.BrightText, brush)
        brush = QtGui.QBrush(QtGui.QColor(242, 246, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(242, 246, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Window, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 115, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.HighlightedText, brush)
        brush = QtGui.QBrush(QtGui.QColor(242, 246, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Light, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.BrightText, brush)
        brush = QtGui.QBrush(QtGui.QColor(242, 246, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(242, 246, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Window, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 115, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.HighlightedText, brush)
        brush = QtGui.QBrush(QtGui.QColor(242, 246, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Light, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.BrightText, brush)
        brush = QtGui.QBrush(QtGui.QColor(242, 246, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(242, 246, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Window, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 115, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.HighlightedText, brush)
        self.menuHelp.setPalette(palette)
        self.menuHelp.setToolTipsVisible(False)
        self.menuHelp.setObjectName("menuHelp")
        Calculator.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(Calculator)
        self.statusbar.setObjectName("statusbar")
        Calculator.setStatusBar(self.statusbar)
        self.actionOpen_Manual = QtWidgets.QAction(Calculator)
        self.actionOpen_Manual.setCheckable(False)
        self.actionOpen_Manual.setIconVisibleInMenu(True)
        self.actionOpen_Manual.setObjectName("actionOpen_Manual")
        self.menuHelp.addSeparator()
        self.menuHelp.addAction(self.actionOpen_Manual)
        self.menubar.addAction(self.menuHelp.menuAction())

        self.actionOpen_Manual.triggered.connect(lambda: self.openHelp())
        
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
        self.ytaodmocnia.clicked.connect(ntaodmocnina)
        self.buttofactorial.clicked.connect(faktorial)
        self.pushciarka.clicked.connect(dash)
        
        self.buttoneq.clicked.connect(equals)
        
        self.buttonsin.clicked.connect(sin)
        
        
        self.retranslateUi(Calculator)
        QtCore.QMetaObject.connectSlotsByName(Calculator)

    def retranslateUi(self, Calculator):
        _translate = QtCore.QCoreApplication.translate
        Calculator.setWindowTitle(_translate("Calculator", "Calculator"))
        Calculator.setWindowIcon(QtGui.QIcon('../icon.png'))
        self.label.setText(_translate("Calculator", ""))
        self.button1.setText(_translate("Calculator", "1"))
        self.button1.setShortcut("1")
        self.button4.setText(_translate("Calculator", "4"))
        self.button4.setShortcut("4")
        self.button7.setText(_translate("Calculator", "7"))
        self.button7.setShortcut("7")
        self.button8.setText(_translate("Calculator", "8"))
        self.button8.setShortcut("8")
        self.button5.setText(_translate("Calculator", "5"))
        self.button5.setShortcut("5")
        self.button2.setText(_translate("Calculator", "2"))
        self.button2.setShortcut("2")
        self.button3.setText(_translate("Calculator", "3"))
        self.button3.setShortcut("3")
        self.button6.setText(_translate("Calculator", "6"))
        self.button6.setShortcut("6")
        self.button9.setText(_translate("Calculator", "9"))
        self.button9.setShortcut("9")
        self.pushButton_0.setText(_translate("Calculator", "0"))
        self.pushButton_0.setShortcut("0")
        self.buttoneq.setText(_translate("Calculator", "="))
        self.buttoneq.setShortcut("Return")
        self.buttondel.setText(_translate("Calculator", "CE"))
        self.buttondel.setShortcut("Backspace")
        self.buttonplus.setText(_translate("Calculator", "+"))
        self.buttonplus.setShortcut("+")
        self.buttonsub.setText(_translate("Calculator", "-"))
        self.buttonsub.setShortcut("-")
        self.buttonmul.setText(_translate("Calculator", "x"))
        self.buttonmul.setShortcut("*")
        self.buttondiv.setText(_translate("Calculator", " ÷"))
        self.buttondiv.setShortcut("/")
        self.buttonpow.setText(_translate("Calculator", "xʸ"))
        self.buttonpow.setShortcut("p")
        self.buttonodmocnina.setText(_translate("Calculator", "√x"))
        self.buttonodmocnina.setShortcut("o")
        self.buttofactorial.setText(_translate("Calculator", "x!"))
        self.buttofactorial.setShortcut("f")
        self.buttonsin.setText(_translate("Calculator", "sin(x)"))
        self.buttonsin.setShortcut("s")
        self.buttonclear.setText(_translate("Calculator", "AC"))
        self.buttonclear.setShortcut("c")
        self.buttonlb.setText(_translate("Calculator", "("))
        self.buttonlb.setShortcut("(")
        self.buttonrb.setText(_translate("Calculator", ")"))
        self.buttonrb.setShortcut(")")
        self.pushciarka.setText(_translate("Calculator", "."))
        self.pushciarka.setShortcut(".")
        self.ytaodmocnia.setText(_translate("Calculator", "ʸ√x"))
        self.ytaodmocnia.setShortcut("y")
        self.menuHelp.setTitle(_translate("Calculator", "Help"))
        self.actionOpen_Manual.setText(_translate("Calculator", "Open Manual"))
        self.actionOpen_Manual.setStatusTip(_translate("Calculator", "Manual"))
        self.actionOpen_Manual.setShortcut(_translate("Calculator", "Ctrl+M"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Calculator = QtWidgets.QMainWindow()
    ui = Ui_Calculator()
    ui.setupUi(Calculator)
    Calculator.show()
    sys.exit(app.exec_())

