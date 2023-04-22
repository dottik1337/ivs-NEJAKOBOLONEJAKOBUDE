""" HelpWindow.py created by: PyQt5 UI code generator 5.14.1 """

# -*- coding: utf-8 -*-

from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtGui import QIcon

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1106, 863)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.textBrowser = QtWidgets.QTextBrowser(self.centralwidget)
        self.textBrowser.setGeometry(QtCore.QRect(0, 0, 1111, 841))
        self.textBrowser.setObjectName("textBrowser")
        MainWindow.setCentralWidget(self.centralwidget)
        self.textBrowser.setOpenExternalLinks(True)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1106, 20))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Help"))
        MainWindow.setWindowIcon(QtGui.QIcon('../icon.png'))
        self.textBrowser.setHtml(_translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'Sans Serif\'; font-size:9pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'URW Gothic [urw]\'; font-size:14pt; font-weight:600; color:#55aa00;\">1.Úvod</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'URW Gothic [urw]\'; font-size:12pt;\">Vitajte v našej kalkulačke! Naša aplikácia vám uľahčí život pri každodenných úlohách</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'URW Gothic [urw]\'; font-size:12pt;\">či už v škole, alebo v práci. Kalkulačka ovláda základné matematické operácie (sčítanie,</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'URW Gothic [urw]\'; font-size:12pt;\">odčítanie, násobenie, delenie) ale aj náročnejšie (n-tá mocnina, 2. a n-tá odmocnina, </span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'URW Gothic [urw]\'; font-size:12pt;\">faktoriál, sin(x)).</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'URW Gothic [urw]\'; font-size:14pt; font-weight:600; color:#55aa00;\">2. Popis matematických symbolov</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'URW Gothic [urw]\'; font-size:12pt; font-weight:600;\">1 Sčítanie a odčítanie</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'URW Gothic [urw]\'; font-size:12pt;\">Vypočíta súčet/rozdiel 2 a viacerých hodnôt. Nie je možné 2 alebo viackrát za sebou kliknúť</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'URW Gothic [urw]\'; font-size:12pt;\">na symbol “+” alebo “-“.</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'URW Gothic [urw]\'; font-size:12pt;\">1.5 – 4 + 47 = 44.5</span></p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-family:\'URW Gothic [urw]\'; font-size:12pt;\"><br /></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'URW Gothic [urw]\'; font-size:12pt; font-weight:600;\">2 Násobenie a delenie</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'URW Gothic [urw]\'; font-size:12pt;\">Vypočíta súčet/rozdiel 2 a viacerých hodnôt. Nie je možné 2 alebo viackrát za sebou kliknúť</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'URW Gothic [urw]\'; font-size:12pt;\">na symbol “×” alebo “÷”. Má prednosť pred sčítaním a odčítaním.</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'URW Gothic [urw]\'; font-size:12pt;\">52 ÷ 4 × 2.5 = 32.5</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'URW Gothic [urw]\'; font-size:12pt;\">5 ÷ 0 = Math Error</span></p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-family:\'URW Gothic [urw]\'; font-size:12pt;\"><br /></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'URW Gothic [urw]\'; font-size:12pt; font-weight:600;\">3 Druhá odmocnina</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'URW Gothic [urw]\'; font-size:12pt;\">Vypočíta druhú odmocninu z daného čísla. Pre jej zápis je potrebné kliknúť na symbol “√”,</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'URW Gothic [urw]\'; font-size:12pt;\">zadať výraz, ktorého 2. mocninu chceme vyrátať a následne výraz ukončiť zátvorkou.</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'URW Gothic [urw]\'; font-size:12pt;\">45 ÷ √(9) = 15</span></p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-family:\'URW Gothic [urw]\'; font-size:12pt;\"><br /></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'URW Gothic [urw]\'; font-size:12pt; font-weight:600;\">4 N-tá odmocnina</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'URW Gothic [urw]\'; font-size:12pt;\">Vypočíta n-tú odmocninu z daného čísla. Pre jej zápis je potrebné do zátvoriek zadať výraz</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'URW Gothic [urw]\'; font-size:12pt;\">ktorý chcete odmocniť, kliknúť na symbol “√𝑥”, zadať výraz ktorým odmocňujeme (ak v</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'URW Gothic [urw]\'; font-size:12pt;\">ňom chcete použiť iné matematické operácie, je potrebné ho zapísať v zátvorkách), a</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'URW Gothic [urw]\'; font-size:12pt;\">následne použitím jedným zo symbolov “+”, “-“, “×”, “÷”, “=” vyskočíte z daného výrazu.</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'URW Gothic [urw]\'; font-size:12pt; vertical-align:super;\">(2×2)</span><span style=\" font-family:\'URW Gothic [urw]\'; font-size:12pt;\">√64 = 4</span></p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-family:\'URW Gothic [urw]\'; font-size:12pt;\"><br /></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'URW Gothic [urw]\'; font-size:12pt; font-weight:600;\">5 N-tá mocnina</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'URW Gothic [urw]\'; font-size:12pt;\">Vypočíta n-tú mocninu z daného čísla. Pre jej zápis je potrebné zadať výraz, ktorý</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'URW Gothic [urw]\'; font-size:12pt;\">umocňujeme, kliknúť na symbol “𝑥</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'URW Gothic [urw]\'; font-size:12pt;\">𝑦”, zadať výraz, ktorým chcete umocniť (ak v ňom chcete</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'URW Gothic [urw]\'; font-size:12pt;\">použiť iné matematické operácie, je potrebné ho zapísať v zátvorkách) a následne použitím</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'URW Gothic [urw]\'; font-size:12pt;\">jedným zo symbolov “+”, “-“, “×”, “÷”, “=” vyskočíte z daného výrazu.</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'URW Gothic [urw]\'; font-size:12pt;\">(8 × 7)</span><span style=\" font-family:\'URW Gothic [urw]\'; font-size:12pt; vertical-align:super;\">(8−7)</span><span style=\" font-family:\'URW Gothic [urw]\'; font-size:12pt;\"> = 56</span></p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-family:\'URW Gothic [urw]\'; font-size:12pt;\"><br /></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'URW Gothic [urw]\'; font-size:12pt; font-weight:600;\">6 sin(x)</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'URW Gothic [urw]\'; font-size:12pt;\">Vypočíta sínus daného výrazu (zadaný v stupňoch!). Pre jeho zápis je potrebné kliknúť na</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'URW Gothic [urw]\'; font-size:12pt;\">symbol ”sin(𝑥)”a v zátvorkách zadať výraz. Použitím pravej zátvorky vyskočíte z daného</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'URW Gothic [urw]\'; font-size:12pt;\">výrazu.</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'URW Gothic [urw]\'; font-size:12pt;\">sin(−180) + sin(−90) = −1</span></p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-family:\'URW Gothic [urw]\'; font-size:12pt;\"><br /></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'URW Gothic [urw]\'; font-size:12pt; font-weight:600;\">7 Faktoriál</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'URW Gothic [urw]\'; font-size:12pt;\">Vypočíta faktoriál daného výrazu. Pre jeho zápis je potrebné zadať výraz, ktorého faktoriál</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'URW Gothic [urw]\'; font-size:12pt;\">chcete vypočítať (ak v ňom chcete použiť iné matematické operácie, je potrebné ho zapísať</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'URW Gothic [urw]\'; font-size:12pt;\">v zátvorkách) a kliknúť na symbol “𝑥!”.</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'URW Gothic [urw]\'; font-size:12pt;\">Poznámka: najvyššia možná hodnota faktoriálu, ktorú vie kalkulačka vypočítať = 170!</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'URW Gothic [urw]\'; font-size:12pt;\">(25 ÷ 5)! = 120</span></p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-family:\'URW Gothic [urw]\'; font-size:12pt;\"><br /></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'URW Gothic [urw]\'; font-size:14pt; font-weight:600; color:#55aa00;\">3. Ďalšie symboly</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'URW Gothic [urw]\'; font-size:12pt; font-weight:600;\">1 Zátvorky</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'URW Gothic [urw]\'; font-size:12pt;\">Majú prednosť pred násobením a delením.</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'URW Gothic [urw]\'; font-size:12pt;\">(99 − √(81)) ÷ 10 = 9</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'URW Gothic [urw]\'; font-size:12pt;\">Poznámka: pokiaľ váš výraz nemá rovnaký počet ľavých a pravých zátvoriek, stlačením symbolu</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'URW Gothic [urw]\'; font-size:12pt;\">“=” sa automaticky doplnia a vyráta výsledok.</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'URW Gothic [urw]\'; font-size:12pt;\">napr. ak zadáte ”(1120 × (154” a následne stlačíte symbol “=”, kalkulačka vypočíta</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'URW Gothic [urw]\'; font-size:12pt;\">výsledok výrazu (120 × (54)) = 6480</span></p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-family:\'URW Gothic [urw]\'; font-size:12pt;\"><br /></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'URW Gothic [urw]\'; font-size:12pt; font-weight:600;\">2 Clear Entry</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'URW Gothic [urw]\'; font-size:12pt;\">Vymaže posledný znak – znak najviac vpravo.</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'URW Gothic [urw]\'; font-size:12pt;\">Poznámka: pokiaľ ste napr. v procese písania n-tej odmocniny a zadáte nesprávne výraz ktorým</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'URW Gothic [urw]\'; font-size:12pt;\">chcete odmocniť, stlačením “CE” sa zmaže znak najviac vpravo. Ak výraz chcete opraviť, je</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'URW Gothic [urw]\'; font-size:12pt;\">potrebné celý výraz vymazať a zápis n-tej odmocniny začať odznovu.</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'URW Gothic [urw]\'; font-size:12pt; vertical-align:super;\">98</span><span style=\" font-family:\'URW Gothic [urw]\'; font-size:12pt;\">√65  ---&gt;  </span><span style=\" font-family:\'URW Gothic [urw]\'; font-size:12pt; vertical-align:super;\">98</span><span style=\" font-family:\'URW Gothic [urw]\'; font-size:12pt;\">√6</span></p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-family:\'URW Gothic [urw]\'; font-size:12pt;\"><br /></p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-family:\'URW Gothic [urw]\'; font-size:12pt;\"><br /></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'URW Gothic [urw]\'; font-size:12pt; font-weight:600;\">3 All Clear</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'URW Gothic [urw]\'; font-size:12pt;\">Vymaže celý zadaný vstup.</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'URW Gothic [urw]\'; font-size:12pt; vertical-align:super;\">98</span><span style=\" font-family:\'URW Gothic [urw]\'; font-size:12pt;\"> √(65 − 158)  ----&gt;</span></p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-family:\'URW Gothic [urw]\'; font-size:12pt;\"><br /></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'URW Gothic [urw]\'; font-size:12pt; font-weight:600;\">4 Rovná sa</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'URW Gothic [urw]\'; font-size:12pt;\">Vypíše výsledok.</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'URW Gothic [urw]\'; font-size:12pt;\">Poznámka: pokiaľ ste zadali výraz, ktorého zápis je neúplný, funkcia symbolu “=” je</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'URW Gothic [urw]\'; font-size:12pt;\">deaktivovaná, nie je možné ju stlačiť, kým výraz nie je zapísaný správne.</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'URW Gothic [urw]\'; font-size:12pt;\">napr. ak kliknete na “sin(x)” a následne by ste chceli kliknúť na symbol “=”, táto funkcia vám</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'URW Gothic [urw]\'; font-size:12pt;\">nebude umožnená. Pred kliknutím na symbol “=”musíte zadať výraz, ktorého sinus chcete vypočítať.</span></p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-family:\'URW Gothic [urw]\'; font-size:12pt;\"><br /></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'URW Gothic [urw]\'; font-size:12pt; font-weight:600;\">5 Desatinná čiarka</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'URW Gothic [urw]\'; font-size:12pt;\">Umožňuje zápis desatiného čísla.</span></p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-family:\'URW Gothic [urw]\'; font-size:12pt;\"><br /></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'URW Gothic [urw]\'; font-size:14pt; font-weight:600; color:#55aa00;\">4. Chybové hlásenie</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'URW Gothic [urw]\'; font-size:12pt;\">Pri matematicky nesprávnych zápisoch kalkulačka vypisuje chybové hlásenie Math Error.</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'URW Gothic [urw]\'; font-size:12pt;\">Zápis výrazu môžte začat odznovu, nie je potrebné nič mazať.</span></p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-family:\'URW Gothic [urw]\'; font-size:12pt;\"><br /></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'URW Gothic [urw]\'; font-size:14pt; font-weight:600; color:#55aa00;\">5. Klávesové ovládanie</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'URW Gothic [urw]\'; font-size:12pt; font-weight:600;\">Funkcie </span><span style=\" font-family:\'URW Gothic [urw]\'; font-size:12pt;\">                 </span><span style=\" font-family:\'URW Gothic [urw]\'; font-size:12pt; font-weight:600;\">Symboly klávesy</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'URW Gothic [urw]\'; font-size:12pt; color:#000000;\">číslice</span><span style=\" font-family:\'URW Gothic [urw]\'; font-size:12pt; color:#00ff00;\"> </span><span style=\" font-family:\'URW Gothic [urw]\'; font-size:12pt;\">                 1, 2, 3, 4, 5, 6, 7, 8, 9, 0</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'URW Gothic [urw]\'; font-size:12pt;\">zátvorky                              (, )</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'URW Gothic [urw]\'; font-size:12pt;\">rovná sa                               =</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'URW Gothic [urw]\'; font-size:12pt;\">sčítanie                                +</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'URW Gothic [urw]\'; font-size:12pt;\">odčítanie                             -</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'URW Gothic [urw]\'; font-size:12pt;\">násobenie                           *</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'URW Gothic [urw]\'; font-size:12pt;\">delenie                                 /</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'URW Gothic [urw]\'; font-size:12pt;\">sin(x)                                     s</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'URW Gothic [urw]\'; font-size:12pt;\">faktoriál                                f</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'URW Gothic [urw]\'; font-size:12pt;\">druhá odmocnina             o</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'URW Gothic [urw]\'; font-size:12pt;\">n-tá odmocnina                 y</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'URW Gothic [urw]\'; font-size:12pt;\">n-tá mocnina                      p</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'URW Gothic [urw]\'; font-size:12pt;\">Clear Entry                  backspace</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'URW Gothic [urw]\'; font-size:12pt;\">All Clear                               c</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'URW Gothic [urw]\'; font-size:12pt;\">manuál                           Ctrl+M</span></p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-family:\'URW Gothic [urw]\'; font-size:12pt;\"><br /></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'URW Gothic [urw]\'; font-size:14pt; font-weight:600; color:#55aa00;\">6. Odinštalácia</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'URW Gothic [urw]\'; font-size:12pt;\">Návod na inštaláciu a odinštaláciu nájdete </span><a href=\"http://www.stud.fit.vutbr.cz/~xgallo06/\"><span style=\" font-size:12pt; text-decoration: underline; color:#0000ff;\">tu.</span></a></p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-family:\'URW Gothic [urw]\'; font-size:12pt;\"><br /></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'URW Gothic [urw]\'; font-size:14pt; font-weight:600; color:#55aa00;\">7. Kontaktné údaje</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'URW Gothic [urw]\'; font-size:12pt;\">Pri odhalení chyby v našej aplikácii alebo problémoch s prevádzkou program nás neváhajte kontaktovať.</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'URW Gothic [urw]\'; font-size:12pt;\">xgallo06@stud.fit.vutbr.cz</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'URW Gothic [urw]\'; font-size:12pt;\">xpaska05@stud.fit.vutbr.cz</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'URW Gothic [urw]\'; font-size:12pt;\">xhalas14@stud.fit.vutbr.cz</span></p></body></html>"))



if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
