# Здесь импорты
import sys
from PyQt5 import uic
from PyQt5.QtWidgets import *
from PyQt5 import QtCore
from PyQt5 import QtGui


class Title(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi('Ui/theory/title.ui', self)
        self.p2.clicked.connect(self.Napravlenie)
        self.p3.clicked.connect(self.Napravlenie)
        self.p4.clicked.connect(self.Napravlenie)
        self.p5.clicked.connect(self.Napravlenie)
        self.p6.clicked.connect(self.Napravlenie)
        self.p7.clicked.connect(self.Napravlenie)
        self.p8.clicked.connect(self.Napravlenie)
        self.p9.clicked.connect(self.Napravlenie)
        self.p10.clicked.connect(self.Napravlenie)
        self.p11.clicked.connect(self.Napravlenie)
        self.p12.clicked.connect(self.Napravlenie)
        self.p13.clicked.connect(self.Napravlenie)
        self.p14.clicked.connect(self.Napravlenie)
        self.p15.clicked.connect(self.Napravlenie)
        self.p16.clicked.connect(self.Napravlenie)

        self.show()

    def Napravlenie(self):
        if self.sender().text() == 'Урок 1':
            self.anotherwindow = MyWidget()
            self.anotherwindow.show()
            self.close()
        elif self.sender().text() == 'Урок 2':
            self.anotherwindow = Info2()
            self.anotherwindow.show()
            self.close()
        elif self.sender().text() == 'Урок 3':
            self.anotherwindow = Info3()
            self.anotherwindow.show()
            self.close()
        elif self.sender().text() == 'Урок 4':
            self.anotherwindow = Info4()
            self.anotherwindow.show()
            self.close()
        elif self.sender().text() == 'Урок 5':
            self.anotherwindow = Info5()
            self.anotherwindow.show()
            self.close()
        elif self.sender().text() == 'Урок 6':
            self.anotherwindow = Info6()
            self.anotherwindow.show()
            self.close()
        elif self.sender().text() == 'Урок 7':
            self.anotherwindow = Info7()
            self.anotherwindow.show()
            self.close()
        elif self.sender().text() == 'Урок 8':
            self.anotherwindow = Info8()
            self.anotherwindow.show()
            self.close()
        elif self.sender().text() == 'Урок 9':
            self.anotherwindow = Info9()
            self.anotherwindow.show()
            self.close()
        elif self.sender().text() == 'Урок 10':
            self.anotherwindow = Info10()
            self.anotherwindow.show()
            self.close()
        elif self.sender().text() == 'Урок 11':
            self.anotherwindow = Info11()
            self.anotherwindow.show()
            self.close()
        elif self.sender().text() == 'Урок 12':
            self.anotherwindow = Info12()
            self.anotherwindow.show()
            self.close()
        elif self.sender().text() == 'Урок 13':
            self.anotherwindow = Info13()
            self.anotherwindow.show()
            self.close()
        elif self.sender().text() == 'Урок 14':
            self.anotherwindow = Info14()
            self.anotherwindow.show()
            self.close()
        elif self.sender().text() == 'Урок 15':
            self.anotherwindow = Info15()
            self.anotherwindow.show()
            self.close()


class MyWidget(QMainWindow):
    # Здесь создание главного окна и кнопки теста, можно использовать для других окон
    def __init__(self, *lyek):
        super().__init__()
        uic.loadUi('Ui/theory/main.ui', self)
        self.pushButton.setStyleSheet("""
            QPushButton:hover { background-color: red }
            QPushButton:!hover { background-color: white }
        
            QPushButton:pressed { background-color: rgb(0, 255, 0); }
        """)
        if lyek :
            self.label = QLabel(self)
            self.label.setText("Неправильно!")
            self.label.move(710, 350)
            self.label.setFont(QtGui.QFont("Times", 22, QtGui.QFont.Bold))
            self.label.adjustSize()
            self.label2 = QLabel(self)
            self.label2.setText("Попробуй ещё раз")
            self.label2.move(710, 400)
            self.label2.setFont(QtGui.QFont("Times", 17, QtGui.QFont.Bold))
            self.label2.adjustSize()
        self.l1.display(1)
        self.pushButton.clicked.connect(self.test)
        self.p2.clicked.connect(self.Napravlenie)
        self.p3.clicked.connect(self.Napravlenie)
        self.p4.clicked.connect(self.Napravlenie)
        self.p5.clicked.connect(self.Napravlenie)
        self.p6.clicked.connect(self.Napravlenie)
        self.p7.clicked.connect(self.Napravlenie)
        self.p8.clicked.connect(self.Napravlenie)
        self.p9.clicked.connect(self.Napravlenie)
        self.p10.clicked.connect(self.Napravlenie)
        self.p11.clicked.connect(self.Napravlenie)
        self.p12.clicked.connect(self.Napravlenie)
        self.p13.clicked.connect(self.Napravlenie)
        self.p14.clicked.connect(self.Napravlenie)
        self.p15.clicked.connect(self.Napravlenie)
        self.p16.clicked.connect(self.Napravlenie)

        self.show()

    def Napravlenie(self):
        if self.sender().text() == '1 урок':
            self.anotherwindow = MyWidget()
            self.anotherwindow.show()
            self.close()
        elif self.sender().text() == '2 урок':
            self.anotherwindow = Info2()
            self.anotherwindow.show()
            self.close()
        elif self.sender().text() == '3 урок':
            self.anotherwindow = Info3()
            self.anotherwindow.show()
            self.close()
        elif self.sender().text() == '4 урок':
            self.anotherwindow = Info4()
            self.anotherwindow.show()
            self.close()
        elif self.sender().text() == '5 урок':
            self.anotherwindow = Info5()
            self.anotherwindow.show()
            self.close()
        elif self.sender().text() == '6 урок':
            self.anotherwindow = Info6()
            self.anotherwindow.show()
            self.close()
        elif self.sender().text() == '7 урок':
            self.anotherwindow = Info7()
            self.anotherwindow.show()
            self.close()
        elif self.sender().text() == '8 урок':
            self.anotherwindow = Info8()
            self.anotherwindow.show()
            self.close()
        elif self.sender().text() == '9 урок':
            self.anotherwindow = Info9()
            self.anotherwindow.show()
            self.close()
        elif self.sender().text() == '10 урок':
            self.anotherwindow = Info10()
            self.anotherwindow.show()
            self.close()
        elif self.sender().text() == '11 урок':
            self.anotherwindow = Info11()
            self.anotherwindow.show()
            self.close()
        elif self.sender().text() == '12 урок':
            self.anotherwindow = Info12()
            self.anotherwindow.show()
            self.close()
        elif self.sender().text() == '13 урок':
            self.anotherwindow = Info13()
            self.anotherwindow.show()
            self.close()
        elif self.sender().text() == '14 урок':
            self.anotherwindow = Info14()
            self.anotherwindow.show()
            self.close()
        elif self.sender().text() == '15 урок':
            self.anotherwindow = Info15()
            self.anotherwindow.show()
            self.close()

    # def OpenWindowIntro(self):
    # self.anotherwindow = Wind2()
    # self.anotherwindow.show()

    def test(self):
        self.anotherwindow = TestingWindow('Ui/tests/test.ui')
        self.anotherwindow.show()
        self.close()


class TestingWindow(QMainWindow):

    def __init__(self, file):
        super().__init__()
        self.file = file
        uic.loadUi(file, self)
        self.show()

        self.pushButton.clicked.connect(lambda: self.opennext())

    def opennext(self):
        # radiobutton = self.sender()
        if self.file == 'Ui/tests/test.ui':
            if self.rb1.isChecked() and self.rb5.isChecked() and self.rb9.isChecked():
                self.anotherwindow = Info2()
                self.anotherwindow.show()
                self.close()
            else:
                self.anotherwindow = MyWidget(True)
                self.anotherwindow.show()
                self.close()
        elif self.file == 'Ui/tests/test2.ui':
            if self.rb2.isChecked() and self.rb7.isChecked() and self.rb10.isChecked():
                self.anotherwindow = Info3()
                self.anotherwindow.show()
                self.close()
            else:
                self.anotherwindow = Info2(True)
                self.anotherwindow.show()
                self.close()
        elif self.file == 'Ui/tests/test3.ui':
            if self.rb1.isChecked() and self.rb7.isChecked() and self.rb12.isChecked():
                self.anotherwindow = Info4()
                self.anotherwindow.show()
                self.close()
            else:
                self.anotherwindow = Info3(True)
                self.anotherwindow.show()
                self.close()

        elif self.file == 'Ui/tests/test5.ui':
            if self.rb1.isChecked() and self.rb7.isChecked():
                self.anotherwindow = Info6()
                self.anotherwindow.show()
                self.close()
            else:
                self.anotherwindow = Info5(True)
                self.anotherwindow.show()
                self.close()

        elif self.file == 'Ui/tests/test7.ui':
            if self.rb2.isChecked() and self.rb7.isChecked() and self.rb10.isChecked():
                self.anotherwindow = Info8()
                self.anotherwindow.show()
                self.close()
            else:
                self.anotherwindow = Info7(True)
                self.anotherwindow.show()
                self.close()
        elif self.file == 'Ui/tests/test8.ui':
            if self.rb2.isChecked() and self.rb6.isChecked() and self.rb9.isChecked():
                self.anotherwindow = Info9()
                self.anotherwindow.show()
                self.close()
            else:
                self.anotherwindow = Info8(True)
                self.anotherwindow.show()
                self.close()

        elif self.file == 'Ui/tests/test10.ui':
            if self.rb4.isChecked() and self.rb6.isChecked() and self.rb11.isChecked():
                self.anotherwindow = Info11()
                self.anotherwindow.show()
                self.close()
            else:
                self.anotherwindow = Info10(True)
                self.anotherwindow.show()
                self.close()
        elif self.file == 'Ui/tests/test11.ui':
            if self.rb4.isChecked() and self.rb4_2.isChecked():
                self.anotherwindow = Info12()
                self.anotherwindow.show()
                self.close()
            else:
                self.anotherwindow = Info11(True)
                self.anotherwindow.show()
                self.close()
        elif self.file == 'Ui/tests/test12.ui':
            if self.rb3.isChecked() and self.rb7.isChecked() and self.rb11.isChecked():
                self.anotherwindow = Info13()
                self.anotherwindow.show()
                self.close()
            else:
                self.anotherwindow = Info12(True)
                self.anotherwindow.show()
                self.close()
        elif self.file == 'Ui/tests/test13.ui':
            if self.rb4.isChecked() and self.rb6.isChecked() and self.rb9.isChecked():
                self.anotherwindow = Info14()
                self.anotherwindow.show()
                self.close()
            else:
                self.anotherwindow = Info13(True)
                self.anotherwindow.show()
                self.close()
        elif self.file == 'Ui/tests/test14.ui':
            if self.rb1.isChecked() and self.rb7.isChecked():
                self.anotherwindow = Info15()
                self.anotherwindow.show()
                self.close()
            else:
                self.anotherwindow = Info14(True)
                self.anotherwindow.show()
                self.close()
        elif self.file == 'Ui/tests/test15.ui':
            if self.rb5.isChecked():
                self.close()
            else:
                self.anotherwindow = Info15(True)
                self.anotherwindow.show()
                self.close()


class Info2(QMainWindow):
    # Здесь создание главного окна и кнопки теста, можно использовать для других окон
    def __init__(self, *lyek):
        super().__init__()
        uic.loadUi('Ui/theory/theory2.ui', self)
        self.pushButton.setStyleSheet("""
            QPushButton:hover { background-color: red }
            QPushButton:!hover { background-color: white }

            QPushButton:pressed { background-color: rgb(0, 255, 0); }
        """)
        if lyek :
            self.label = QLabel(self)
            self.label.setText("Неправильно!")
            self.label.move(710, 350)
            self.label.setFont(QtGui.QFont("Times", 22, QtGui.QFont.Bold))
            self.label.adjustSize()
            self.label2 = QLabel(self)
            self.label2.setText("Попробуй ещё раз")
            self.label2.move(710, 400)
            self.label2.setFont(QtGui.QFont("Times", 17, QtGui.QFont.Bold))
            self.label2.adjustSize()

        self.pushButton.clicked.connect(self.test)
        self.show()

        self.l1.display(2)
        self.pushButton.clicked.connect(self.test)
        self.p2.clicked.connect(self.Napravlenie)
        self.p3.clicked.connect(self.Napravlenie)
        self.p4.clicked.connect(self.Napravlenie)
        self.p5.clicked.connect(self.Napravlenie)
        self.p6.clicked.connect(self.Napravlenie)
        self.p7.clicked.connect(self.Napravlenie)
        self.p8.clicked.connect(self.Napravlenie)
        self.p9.clicked.connect(self.Napravlenie)
        self.p10.clicked.connect(self.Napravlenie)
        self.p11.clicked.connect(self.Napravlenie)
        self.p12.clicked.connect(self.Napravlenie)
        self.p13.clicked.connect(self.Napravlenie)
        self.p14.clicked.connect(self.Napravlenie)
        self.p15.clicked.connect(self.Napravlenie)
        self.p16.clicked.connect(self.Napravlenie)

        self.show()

    def Napravlenie(self):
        if self.sender().text() == '1 урок':
            self.anotherwindow = MyWidget()
            self.anotherwindow.show()
            self.close()
        elif self.sender().text() == '2 урок':
            self.anotherwindow = Info2()
            self.anotherwindow.show()
            self.close()
        elif self.sender().text() == '3 урок':
            self.anotherwindow = Info3()
            self.anotherwindow.show()
            self.close()
        elif self.sender().text() == '4 урок':
            self.anotherwindow = Info4()
            self.anotherwindow.show()
            self.close()
        elif self.sender().text() == '5 урок':
            self.anotherwindow = Info5()
            self.anotherwindow.show()
            self.close()
        elif self.sender().text() == '6 урок':
            self.anotherwindow = Info6()
            self.anotherwindow.show()
            self.close()
        elif self.sender().text() == '7 урок':
            self.anotherwindow = Info7()
            self.anotherwindow.show()
            self.close()
        elif self.sender().text() == '8 урок':
            self.anotherwindow = Info8()
            self.anotherwindow.show()
            self.close()
        elif self.sender().text() == '9 урок':
            self.anotherwindow = Info9()
            self.anotherwindow.show()
            self.close()
        elif self.sender().text() == '10 урок':
            self.anotherwindow = Info10()
            self.anotherwindow.show()
            self.close()
        elif self.sender().text() == '11 урок':
            self.anotherwindow = Info11()
            self.anotherwindow.show()
            self.close()
        elif self.sender().text() == '12 урок':
            self.anotherwindow = Info12()
            self.anotherwindow.show()
            self.close()
        elif self.sender().text() == '13 урок':
            self.anotherwindow = Info13()
            self.anotherwindow.show()
            self.close()
        elif self.sender().text() == '14 урок':
            self.anotherwindow = Info14()
            self.anotherwindow.show()
            self.close()
        elif self.sender().text() == '15 урок':
            self.anotherwindow = Info15()
            self.anotherwindow.show()
            self.close()

    # def OpenWindowIntro(self):
    # self.anotherwindow = Wind2()
    # self.anotherwindow.show()

    def test(self):
        self.anotherwindow = TestingWindow('Ui/tests/test2.ui')
        self.anotherwindow.show()
        self.close()


class Info3(QMainWindow):
    def __init__(self, *lyek):
        super().__init__()
        uic.loadUi('Ui/theory/theory3.ui', self)
        self.pushButton.setStyleSheet("""
            QPushButton:hover { background-color: red }
            QPushButton:!hover { background-color: white }

            QPushButton:pressed { background-color: rgb(0, 255, 0); }
        """)
        if lyek :
            self.label = QLabel(self)
            self.label.setText("Неправильно!")
            self.label.move(710, 350)
            self.label.setFont(QtGui.QFont("Times", 22, QtGui.QFont.Bold))
            self.label.adjustSize()
            self.label2 = QLabel(self)
            self.label2.setText("Попробуй ещё раз")
            self.label2.move(710, 400)
            self.label2.setFont(QtGui.QFont("Times", 17, QtGui.QFont.Bold))
            self.label2.adjustSize()
        self.l1.display(3)
        self.pushButton.clicked.connect(self.test)
        self.show()
        self.pushButton.clicked.connect(self.test)
        self.p2.clicked.connect(self.Napravlenie)
        self.p3.clicked.connect(self.Napravlenie)
        self.p4.clicked.connect(self.Napravlenie)
        self.p5.clicked.connect(self.Napravlenie)
        self.p6.clicked.connect(self.Napravlenie)
        self.p7.clicked.connect(self.Napravlenie)
        self.p8.clicked.connect(self.Napravlenie)
        self.p9.clicked.connect(self.Napravlenie)
        self.p10.clicked.connect(self.Napravlenie)
        self.p11.clicked.connect(self.Napravlenie)
        self.p12.clicked.connect(self.Napravlenie)
        self.p13.clicked.connect(self.Napravlenie)
        self.p14.clicked.connect(self.Napravlenie)
        self.p15.clicked.connect(self.Napravlenie)
        self.p16.clicked.connect(self.Napravlenie)

        self.show()

    def Napravlenie(self):
        if self.sender().text() == '1 урок':
            self.anotherwindow = MyWidget()
            self.anotherwindow.show()
            self.close()
        elif self.sender().text() == '2 урок':
            self.anotherwindow = Info2()
            self.anotherwindow.show()
            self.close()
        elif self.sender().text() == '3 урок':
            self.anotherwindow = Info3()
            self.anotherwindow.show()
            self.close()
        elif self.sender().text() == '4 урок':
            self.anotherwindow = Info4()
            self.anotherwindow.show()
            self.close()
        elif self.sender().text() == '5 урок':
            self.anotherwindow = Info5()
            self.anotherwindow.show()
            self.close()
        elif self.sender().text() == '6 урок':
            self.anotherwindow = Info6()
            self.anotherwindow.show()
            self.close()
        elif self.sender().text() == '7 урок':
            self.anotherwindow = Info7()
            self.anotherwindow.show()
            self.close()
        elif self.sender().text() == '8 урок':
            self.anotherwindow = Info8()
            self.anotherwindow.show()
            self.close()
        elif self.sender().text() == '9 урок':
            self.anotherwindow = Info9()
            self.anotherwindow.show()
            self.close()
        elif self.sender().text() == '10 урок':
            self.anotherwindow = Info10()
            self.anotherwindow.show()
            self.close()
        elif self.sender().text() == '11 урок':
            self.anotherwindow = Info11()
            self.anotherwindow.show()
            self.close()
        elif self.sender().text() == '12 урок':
            self.anotherwindow = Info12()
            self.anotherwindow.show()
            self.close()
        elif self.sender().text() == '13 урок':
            self.anotherwindow = Info13()
            self.anotherwindow.show()
            self.close()
        elif self.sender().text() == '14 урок':
            self.anotherwindow = Info14()
            self.anotherwindow.show()
            self.close()
        elif self.sender().text() == '15 урок':
            self.anotherwindow = Info15()
            self.anotherwindow.show()
            self.close()

    # def OpenWindowIntro(self):
    # self.anotherwindow = Wind2()
    # self.anotherwindow.show()

    def test(self):
        self.anotherwindow = TestingWindow('Ui/tests/test3.ui')
        self.anotherwindow.show()
        self.close()


class Info4(QMainWindow):
    def __init__(self, *lyek):
        super().__init__()
        uic.loadUi('Ui/theory/theory4.ui', self)
        self.pushButton.setStyleSheet("""
            QPushButton:hover { background-color: red }
            QPushButton:!hover { background-color: white }

            QPushButton:pressed { background-color: rgb(0, 255, 0); }
        """)
        if lyek :
            self.label = QLabel(self)
            self.label.setText("Неправильно!")
            self.label.move(710, 350)
            self.label.setFont(QtGui.QFont("Times", 22, QtGui.QFont.Bold))
            self.label.adjustSize()
            self.label2 = QLabel(self)
            self.label2.setText("Попробуй ещё раз")
            self.label2.move(710, 400)
            self.label2.setFont(QtGui.QFont("Times", 17, QtGui.QFont.Bold))
            self.label2.adjustSize()
        self.l1.display(4)
        self.pushButton.clicked.connect(self.test)
        self.show()
        self.pushButton.clicked.connect(self.test)
        self.p2.clicked.connect(self.Napravlenie)
        self.p3.clicked.connect(self.Napravlenie)
        self.p4.clicked.connect(self.Napravlenie)
        self.p5.clicked.connect(self.Napravlenie)
        self.p6.clicked.connect(self.Napravlenie)
        self.p7.clicked.connect(self.Napravlenie)
        self.p8.clicked.connect(self.Napravlenie)
        self.p9.clicked.connect(self.Napravlenie)
        self.p10.clicked.connect(self.Napravlenie)
        self.p11.clicked.connect(self.Napravlenie)
        self.p12.clicked.connect(self.Napravlenie)
        self.p13.clicked.connect(self.Napravlenie)
        self.p14.clicked.connect(self.Napravlenie)
        self.p15.clicked.connect(self.Napravlenie)
        self.p16.clicked.connect(self.Napravlenie)

        self.show()

    def Napravlenie(self):
        if self.sender().text() == '1 урок':
            self.anotherwindow = MyWidget()
            self.anotherwindow.show()
            self.close()
        elif self.sender().text() == '2 урок':
            self.anotherwindow = Info2()
            self.anotherwindow.show()
            self.close()
        elif self.sender().text() == '3 урок':
            self.anotherwindow = Info3()
            self.anotherwindow.show()
            self.close()
        elif self.sender().text() == '4 урок':
            self.anotherwindow = Info4()
            self.anotherwindow.show()
            self.close()
        elif self.sender().text() == '5 урок':
            self.anotherwindow = Info5()
            self.anotherwindow.show()
            self.close()
        elif self.sender().text() == '6 урок':
            self.anotherwindow = Info6()
            self.anotherwindow.show()
            self.close()
        elif self.sender().text() == '7 урок':
            self.anotherwindow = Info7()
            self.anotherwindow.show()
            self.close()
        elif self.sender().text() == '8 урок':
            self.anotherwindow = Info8()
            self.anotherwindow.show()
            self.close()
        elif self.sender().text() == '9 урок':
            self.anotherwindow = Info9()
            self.anotherwindow.show()
            self.close()
        elif self.sender().text() == '10 урок':
            self.anotherwindow = Info10()
            self.anotherwindow.show()
            self.close()
        elif self.sender().text() == '11 урок':
            self.anotherwindow = Info11()
            self.anotherwindow.show()
            self.close()
        elif self.sender().text() == '12 урок':
            self.anotherwindow = Info12()
            self.anotherwindow.show()
            self.close()
        elif self.sender().text() == '13 урок':
            self.anotherwindow = Info13()
            self.anotherwindow.show()
            self.close()
        elif self.sender().text() == '14 урок':
            self.anotherwindow = Info14()
            self.anotherwindow.show()
            self.close()
        elif self.sender().text() == '15 урок':
            self.anotherwindow = Info15()
            self.anotherwindow.show()
            self.close()

    # def OpenWindowIntro(self):
    # self.anotherwindow = Wind2()
    # self.anotherwindow.show()

    def test(self):
        self.anotherwindow = Info5()
        self.anotherwindow.show()
        self.close()


class Info5(QMainWindow):
    def __init__(self, *lyek):
        super().__init__()
        uic.loadUi('Ui/theory/theory5.ui', self)
        self.pushButton.setStyleSheet("""
            QPushButton:hover { background-color: red }
            QPushButton:!hover { background-color: white }

            QPushButton:pressed { background-color: rgb(0, 255, 0); }
        """)
        if lyek :
            self.label = QLabel(self)
            self.label.setText("Неправильно!")
            self.label.move(710, 350)
            self.label.setFont(QtGui.QFont("Times", 22, QtGui.QFont.Bold))
            self.label.adjustSize()
            self.label2 = QLabel(self)
            self.label2.setText("Попробуй ещё раз")
            self.label2.move(710, 400)
            self.label2.setFont(QtGui.QFont("Times", 17, QtGui.QFont.Bold))
            self.label2.adjustSize()
        self.l1.display(5)
        self.pushButton.clicked.connect(self.test)
        self.show()
        self.pushButton.clicked.connect(self.test)
        self.p2.clicked.connect(self.Napravlenie)
        self.p3.clicked.connect(self.Napravlenie)
        self.p4.clicked.connect(self.Napravlenie)
        self.p5.clicked.connect(self.Napravlenie)
        self.p6.clicked.connect(self.Napravlenie)
        self.p7.clicked.connect(self.Napravlenie)
        self.p8.clicked.connect(self.Napravlenie)
        self.p9.clicked.connect(self.Napravlenie)
        self.p10.clicked.connect(self.Napravlenie)
        self.p11.clicked.connect(self.Napravlenie)
        self.p12.clicked.connect(self.Napravlenie)
        self.p13.clicked.connect(self.Napravlenie)
        self.p14.clicked.connect(self.Napravlenie)
        self.p15.clicked.connect(self.Napravlenie)
        self.p16.clicked.connect(self.Napravlenie)

        self.show()

    def Napravlenie(self):
        if self.sender().text() == '1 урок':
            self.anotherwindow = MyWidget()
            self.anotherwindow.show()
            self.close()
        elif self.sender().text() == '2 урок':
            self.anotherwindow = Info2()
            self.anotherwindow.show()
            self.close()
        elif self.sender().text() == '3 урок':
            self.anotherwindow = Info3()
            self.anotherwindow.show()
            self.close()
        elif self.sender().text() == '4 урок':
            self.anotherwindow = Info4()
            self.anotherwindow.show()
            self.close()
        elif self.sender().text() == '5 урок':
            self.anotherwindow = Info5()
            self.anotherwindow.show()
            self.close()
        elif self.sender().text() == '6 урок':
            self.anotherwindow = Info6()
            self.anotherwindow.show()
            self.close()
        elif self.sender().text() == '7 урок':
            self.anotherwindow = Info7()
            self.anotherwindow.show()
            self.close()
        elif self.sender().text() == '8 урок':
            self.anotherwindow = Info8()
            self.anotherwindow.show()
            self.close()
        elif self.sender().text() == '9 урок':
            self.anotherwindow = Info9()
            self.anotherwindow.show()
            self.close()
        elif self.sender().text() == '10 урок':
            self.anotherwindow = Info10()
            self.anotherwindow.show()
            self.close()
        elif self.sender().text() == '11 урок':
            self.anotherwindow = Info11()
            self.anotherwindow.show()
            self.close()
        elif self.sender().text() == '12 урок':
            self.anotherwindow = Info12()
            self.anotherwindow.show()
            self.close()
        elif self.sender().text() == '13 урок':
            self.anotherwindow = Info13()
            self.anotherwindow.show()
            self.close()
        elif self.sender().text() == '14 урок':
            self.anotherwindow = Info14()
            self.anotherwindow.show()
            self.close()
        elif self.sender().text() == '15 урок':
            self.anotherwindow = Info15()
            self.anotherwindow.show()
            self.close()

    # def OpenWindowIntro(self):
    # self.anotherwindow = Wind2()
    # self.anotherwindow.show()

    def test(self):
        self.anotherwindow = TestingWindow('Ui/tests/test5.ui')
        self.anotherwindow.show()
        self.close()


class Info6(QMainWindow):
    def __init__(self, *lyek):
        super().__init__()
        uic.loadUi('Ui/theory/theory6.ui', self)
        self.pushButton.setStyleSheet("""
            QPushButton:hover { background-color: red }
            QPushButton:!hover { background-color: white }

            QPushButton:pressed { background-color: rgb(0, 255, 0); }
        """)
        if lyek :
            self.label = QLabel(self)
            self.label.setText("Неправильно!")
            self.label.move(710, 350)
            self.label.setFont(QtGui.QFont("Times", 22, QtGui.QFont.Bold))
            self.label.adjustSize()
            self.label2 = QLabel(self)
            self.label2.setText("Попробуй ещё раз")
            self.label2.move(710, 400)
            self.label2.setFont(QtGui.QFont("Times", 17, QtGui.QFont.Bold))
            self.label2.adjustSize()
        self.l1.display(6)
        self.pushButton.clicked.connect(self.test)
        self.show()
        self.pushButton.clicked.connect(self.test)
        self.p2.clicked.connect(self.Napravlenie)
        self.p3.clicked.connect(self.Napravlenie)
        self.p4.clicked.connect(self.Napravlenie)
        self.p5.clicked.connect(self.Napravlenie)
        self.p6.clicked.connect(self.Napravlenie)
        self.p7.clicked.connect(self.Napravlenie)
        self.p8.clicked.connect(self.Napravlenie)
        self.p9.clicked.connect(self.Napravlenie)
        self.p10.clicked.connect(self.Napravlenie)
        self.p11.clicked.connect(self.Napravlenie)
        self.p12.clicked.connect(self.Napravlenie)
        self.p13.clicked.connect(self.Napravlenie)
        self.p14.clicked.connect(self.Napravlenie)
        self.p15.clicked.connect(self.Napravlenie)
        self.p16.clicked.connect(self.Napravlenie)

        self.show()

    def Napravlenie(self):
        if self.sender().text() == '1 урок':
            self.anotherwindow = MyWidget()
            self.anotherwindow.show()
            self.close()
        elif self.sender().text() == '2 урок':
            self.anotherwindow = Info2()
            self.anotherwindow.show()
            self.close()
        elif self.sender().text() == '3 урок':
            self.anotherwindow = Info3()
            self.anotherwindow.show()
            self.close()
        elif self.sender().text() == '4 урок':
            self.anotherwindow = Info4()
            self.anotherwindow.show()
            self.close()
        elif self.sender().text() == '5 урок':
            self.anotherwindow = Info5()
            self.anotherwindow.show()
            self.close()
        elif self.sender().text() == '6 урок':
            self.anotherwindow = Info6()
            self.anotherwindow.show()
            self.close()
        elif self.sender().text() == '7 урок':
            self.anotherwindow = Info7()
            self.anotherwindow.show()
            self.close()
        elif self.sender().text() == '8 урок':
            self.anotherwindow = Info8()
            self.anotherwindow.show()
            self.close()
        elif self.sender().text() == '9 урок':
            self.anotherwindow = Info9()
            self.anotherwindow.show()
            self.close()
        elif self.sender().text() == '10 урок':
            self.anotherwindow = Info10()
            self.anotherwindow.show()
            self.close()
        elif self.sender().text() == '11 урок':
            self.anotherwindow = Info11()
            self.anotherwindow.show()
            self.close()
        elif self.sender().text() == '12 урок':
            self.anotherwindow = Info12()
            self.anotherwindow.show()
            self.close()
        elif self.sender().text() == '13 урок':
            self.anotherwindow = Info13()
            self.anotherwindow.show()
            self.close()
        elif self.sender().text() == '14 урок':
            self.anotherwindow = Info14()
            self.anotherwindow.show()
            self.close()
        elif self.sender().text() == '15 урок':
            self.anotherwindow = Info15()
            self.anotherwindow.show()
            self.close()

    # def OpenWindowIntro(self):
    # self.anotherwindow = Wind2()
    # self.anotherwindow.show()

    def test(self):
        self.anotherwindow = Info7()
        self.anotherwindow.show()
        self.close()


class Info7(QMainWindow):
    def __init__(self, *lyek):
        super().__init__()
        uic.loadUi('Ui/theory/theory7.ui', self)
        self.pushButton.setStyleSheet("""
            QPushButton:hover { background-color: red }
            QPushButton:!hover { background-color: white }

            QPushButton:pressed { background-color: rgb(0, 255, 0); }
        """)
        if lyek :
            self.label = QLabel(self)
            self.label.setText("Неправильно!")
            self.label.move(710, 350)
            self.label.setFont(QtGui.QFont("Times", 22, QtGui.QFont.Bold))
            self.label.adjustSize()
            self.label2 = QLabel(self)
            self.label2.setText("Попробуй ещё раз")
            self.label2.move(710, 400)
            self.label2.setFont(QtGui.QFont("Times", 17, QtGui.QFont.Bold))
            self.label2.adjustSize()
        self.l1.display(7)
        self.pushButton.clicked.connect(self.test)
        self.show()
        self.pushButton.clicked.connect(self.test)
        self.p2.clicked.connect(self.Napravlenie)
        self.p3.clicked.connect(self.Napravlenie)
        self.p4.clicked.connect(self.Napravlenie)
        self.p5.clicked.connect(self.Napravlenie)
        self.p6.clicked.connect(self.Napravlenie)
        self.p7.clicked.connect(self.Napravlenie)
        self.p8.clicked.connect(self.Napravlenie)
        self.p9.clicked.connect(self.Napravlenie)
        self.p10.clicked.connect(self.Napravlenie)
        self.p11.clicked.connect(self.Napravlenie)
        self.p12.clicked.connect(self.Napravlenie)
        self.p13.clicked.connect(self.Napravlenie)
        self.p14.clicked.connect(self.Napravlenie)
        self.p15.clicked.connect(self.Napravlenie)
        self.p16.clicked.connect(self.Napravlenie)

        self.show()

    def Napravlenie(self):
        if self.sender().text() == '1 урок':
            self.anotherwindow = MyWidget()
            self.anotherwindow.show()
            self.close()
        elif self.sender().text() == '2 урок':
            self.anotherwindow = Info2()
            self.anotherwindow.show()
            self.close()
        elif self.sender().text() == '3 урок':
            self.anotherwindow = Info3()
            self.anotherwindow.show()
            self.close()
        elif self.sender().text() == '4 урок':
            self.anotherwindow = Info4()
            self.anotherwindow.show()
            self.close()
        elif self.sender().text() == '5 урок':
            self.anotherwindow = Info5()
            self.anotherwindow.show()
            self.close()
        elif self.sender().text() == '6 урок':
            self.anotherwindow = Info6()
            self.anotherwindow.show()
            self.close()
        elif self.sender().text() == '7 урок':
            self.anotherwindow = Info7()
            self.anotherwindow.show()
            self.close()
        elif self.sender().text() == '8 урок':
            self.anotherwindow = Info8()
            self.anotherwindow.show()
            self.close()
        elif self.sender().text() == '9 урок':
            self.anotherwindow = Info9()
            self.anotherwindow.show()
            self.close()
        elif self.sender().text() == '10 урок':
            self.anotherwindow = Info10()
            self.anotherwindow.show()
            self.close()
        elif self.sender().text() == '11 урок':
            self.anotherwindow = Info11()
            self.anotherwindow.show()
            self.close()
        elif self.sender().text() == '12 урок':
            self.anotherwindow = Info12()
            self.anotherwindow.show()
            self.close()
        elif self.sender().text() == '13 урок':
            self.anotherwindow = Info13()
            self.anotherwindow.show()
            self.close()
        elif self.sender().text() == '14 урок':
            self.anotherwindow = Info14()
            self.anotherwindow.show()
            self.close()
        elif self.sender().text() == '15 урок':
            self.anotherwindow = Info15()
            self.anotherwindow.show()
            self.close()

    # def OpenWindowIntro(self):
    # self.anotherwindow = Wind2()
    # self.anotherwindow.show()

    def test(self):
        self.anotherwindow = TestingWindow('Ui/tests/test7.ui')
        self.anotherwindow.show()
        self.close()


class Info8(QMainWindow):
    def __init__(self, *lyek):
        super().__init__()
        uic.loadUi('Ui/theory/theory8.ui', self)
        self.pushButton.setStyleSheet("""
            QPushButton:hover { background-color: red }
            QPushButton:!hover { background-color: white }

            QPushButton:pressed { background-color: rgb(0, 255, 0); }
        """)
        if lyek:
            self.label = QLabel(self)
            self.label.setText("Неправильно!")
            self.label.move(710, 300)
            self.label.setFont(QtGui.QFont("Times", 22, QtGui.QFont.Bold))
            self.label.adjustSize()
            self.label2 = QLabel(self)
            self.label2.setText("Попробуй ещё раз")
            self.label2.move(710, 350)
            self.label2.setFont(QtGui.QFont("Times", 17, QtGui.QFont.Bold))
            self.label2.adjustSize()
        self.pushButton.clicked.connect(self.test)
        self.show()
        self.l1.display(8)

        # def OpenWindowIntro(self):
        # self.anotherwindow = Wind2()
        # self.anotherwindow.show()
        self.pushButton.clicked.connect(self.test)
        self.p2.clicked.connect(self.Napravlenie)
        self.p3.clicked.connect(self.Napravlenie)
        self.p4.clicked.connect(self.Napravlenie)
        self.p5.clicked.connect(self.Napravlenie)
        self.p6.clicked.connect(self.Napravlenie)
        self.p7.clicked.connect(self.Napravlenie)
        self.p8.clicked.connect(self.Napravlenie)
        self.p9.clicked.connect(self.Napravlenie)
        self.p10.clicked.connect(self.Napravlenie)
        self.p11.clicked.connect(self.Napravlenie)
        self.p12.clicked.connect(self.Napravlenie)
        self.p13.clicked.connect(self.Napravlenie)
        self.p14.clicked.connect(self.Napravlenie)
        self.p15.clicked.connect(self.Napravlenie)
        self.p16.clicked.connect(self.Napravlenie)

        self.show()

    def Napravlenie(self):
        if self.sender().text() == '1 урок':
            self.anotherwindow = MyWidget()
            self.anotherwindow.show()
            self.close()
        elif self.sender().text() == '2 урок':
            self.anotherwindow = Info2()
            self.anotherwindow.show()
            self.close()
        elif self.sender().text() == '3 урок':
            self.anotherwindow = Info3()
            self.anotherwindow.show()
            self.close()
        elif self.sender().text() == '4 урок':
            self.anotherwindow = Info4()
            self.anotherwindow.show()
            self.close()
        elif self.sender().text() == '5 урок':
            self.anotherwindow = Info5()
            self.anotherwindow.show()
            self.close()
        elif self.sender().text() == '6 урок':
            self.anotherwindow = Info6()
            self.anotherwindow.show()
            self.close()
        elif self.sender().text() == '7 урок':
            self.anotherwindow = Info7()
            self.anotherwindow.show()
            self.close()
        elif self.sender().text() == '8 урок':
            self.anotherwindow = Info8()
            self.anotherwindow.show()
            self.close()
        elif self.sender().text() == '9 урок':
            self.anotherwindow = Info9()
            self.anotherwindow.show()
            self.close()
        elif self.sender().text() == '10 урок':
            self.anotherwindow = Info10()
            self.anotherwindow.show()
            self.close()
        elif self.sender().text() == '11 урок':
            self.anotherwindow = Info11()
            self.anotherwindow.show()
            self.close()
        elif self.sender().text() == '12 урок':
            self.anotherwindow = Info12()
            self.anotherwindow.show()
            self.close()
        elif self.sender().text() == '13 урок':
            self.anotherwindow = Info13()
            self.anotherwindow.show()
            self.close()
        elif self.sender().text() == '14 урок':
            self.anotherwindow = Info14()
            self.anotherwindow.show()
            self.close()
        elif self.sender().text() == '15 урок':
            self.anotherwindow = Info15()
            self.anotherwindow.show()
            self.close()

    def test(self):
        self.anotherwindow = TestingWindow('Ui/tests/test8.ui')
        self.anotherwindow.show()
        self.close()


class Info9(QMainWindow):
    def __init__(self, *lyek):
        super().__init__()
        uic.loadUi('Ui/theory/theory9.ui', self)
        self.pushButton.setStyleSheet("""
            QPushButton:hover { background-color: red }
            QPushButton:!hover { background-color: white }

            QPushButton:pressed { background-color: rgb(0, 255, 0); }
        """)
        if lyek:
            self.label = QLabel(self)
            self.label.setText("Неправильно!")
            self.label.move(710, 300)
            self.label.setFont(QtGui.QFont("Times", 22, QtGui.QFont.Bold))
            self.label.adjustSize()
            self.label2 = QLabel(self)
            self.label2.setText("Попробуй ещё раз")
            self.label2.move(710, 350)
            self.label2.setFont(QtGui.QFont("Times", 17, QtGui.QFont.Bold))
            self.label2.adjustSize()
        self.l1.display(9)
        self.pushButton.clicked.connect(self.test)
        self.show()
        self.pushButton.clicked.connect(self.test)
        self.p2.clicked.connect(self.Napravlenie)
        self.p3.clicked.connect(self.Napravlenie)
        self.p4.clicked.connect(self.Napravlenie)
        self.p5.clicked.connect(self.Napravlenie)
        self.p6.clicked.connect(self.Napravlenie)
        self.p7.clicked.connect(self.Napravlenie)
        self.p8.clicked.connect(self.Napravlenie)
        self.p9.clicked.connect(self.Napravlenie)
        self.p10.clicked.connect(self.Napravlenie)
        self.p11.clicked.connect(self.Napravlenie)
        self.p12.clicked.connect(self.Napravlenie)
        self.p13.clicked.connect(self.Napravlenie)
        self.p14.clicked.connect(self.Napravlenie)
        self.p15.clicked.connect(self.Napravlenie)
        self.p16.clicked.connect(self.Napravlenie)

        self.show()

    def Napravlenie(self):
        if self.sender().text() == '1 урок':
            self.anotherwindow = MyWidget()
            self.anotherwindow.show()
            self.close()
        elif self.sender().text() == '2 урок':
            self.anotherwindow = Info2()
            self.anotherwindow.show()
            self.close()
        elif self.sender().text() == '3 урок':
            self.anotherwindow = Info3()
            self.anotherwindow.show()
            self.close()
        elif self.sender().text() == '4 урок':
            self.anotherwindow = Info4()
            self.anotherwindow.show()
            self.close()
        elif self.sender().text() == '5 урок':
            self.anotherwindow = Info5()
            self.anotherwindow.show()
            self.close()
        elif self.sender().text() == '6 урок':
            self.anotherwindow = Info6()
            self.anotherwindow.show()
            self.close()
        elif self.sender().text() == '7 урок':
            self.anotherwindow = Info7()
            self.anotherwindow.show()
            self.close()
        elif self.sender().text() == '8 урок':
            self.anotherwindow = Info8()
            self.anotherwindow.show()
            self.close()
        elif self.sender().text() == '9 урок':
            self.anotherwindow = Info9()
            self.anotherwindow.show()
            self.close()
        elif self.sender().text() == '10 урок':
            self.anotherwindow = Info10()
            self.anotherwindow.show()
            self.close()
        elif self.sender().text() == '11 урок':
            self.anotherwindow = Info11()
            self.anotherwindow.show()
            self.close()
        elif self.sender().text() == '12 урок':
            self.anotherwindow = Info12()
            self.anotherwindow.show()
            self.close()
        elif self.sender().text() == '13 урок':
            self.anotherwindow = Info13()
            self.anotherwindow.show()
            self.close()
        elif self.sender().text() == '14 урок':
            self.anotherwindow = Info14()
            self.anotherwindow.show()
            self.close()
        elif self.sender().text() == '15 урок':
            self.anotherwindow = Info15()
            self.anotherwindow.show()
            self.close()

    # def OpenWindowIntro(self):
    # self.anotherwindow = Wind2()
    # self.anotherwindow.show()

    def test(self):
        self.anotherwindow = Info10()
        self.anotherwindow.show()
        self.close()


class Info10(QMainWindow):
    def __init__(self, *lyek):
        super().__init__()
        uic.loadUi('Ui/theory/theory10.ui', self)
        self.pushButton.setStyleSheet("""
            QPushButton:hover { background-color: red }
            QPushButton:!hover { background-color: white }

            QPushButton:pressed { background-color: rgb(0, 255, 0); }
        """)
        if lyek:
            self.label = QLabel(self)
            self.label.setText("Неправильно!")
            self.label.move(710, 300)
            self.label.setFont(QtGui.QFont("Times", 22, QtGui.QFont.Bold))
            self.label.adjustSize()
            self.label2 = QLabel(self)
            self.label2.setText("Попробуй ещё раз")
            self.label2.move(710, 350)
            self.label2.setFont(QtGui.QFont("Times", 17, QtGui.QFont.Bold))
            self.label2.adjustSize()
        self.l1.display(10)
        self.pushButton.clicked.connect(self.test)
        self.show()
        self.pushButton.clicked.connect(self.test)
        self.p2.clicked.connect(self.Napravlenie)
        self.p3.clicked.connect(self.Napravlenie)
        self.p4.clicked.connect(self.Napravlenie)
        self.p5.clicked.connect(self.Napravlenie)
        self.p6.clicked.connect(self.Napravlenie)
        self.p7.clicked.connect(self.Napravlenie)
        self.p8.clicked.connect(self.Napravlenie)
        self.p9.clicked.connect(self.Napravlenie)
        self.p10.clicked.connect(self.Napravlenie)
        self.p11.clicked.connect(self.Napravlenie)
        self.p12.clicked.connect(self.Napravlenie)
        self.p13.clicked.connect(self.Napravlenie)
        self.p14.clicked.connect(self.Napravlenie)
        self.p15.clicked.connect(self.Napravlenie)
        self.p16.clicked.connect(self.Napravlenie)

        self.show()

    def Napravlenie(self):
        if self.sender().text() == '1 урок':
            self.anotherwindow = MyWidget()
            self.anotherwindow.show()
            self.close()
        elif self.sender().text() == '2 урок':
            self.anotherwindow = Info2()
            self.anotherwindow.show()
            self.close()
        elif self.sender().text() == '3 урок':
            self.anotherwindow = Info3()
            self.anotherwindow.show()
            self.close()
        elif self.sender().text() == '4 урок':
            self.anotherwindow = Info4()
            self.anotherwindow.show()
            self.close()
        elif self.sender().text() == '5 урок':
            self.anotherwindow = Info5()
            self.anotherwindow.show()
            self.close()
        elif self.sender().text() == '6 урок':
            self.anotherwindow = Info6()
            self.anotherwindow.show()
            self.close()
        elif self.sender().text() == '7 урок':
            self.anotherwindow = Info7()
            self.anotherwindow.show()
            self.close()
        elif self.sender().text() == '8 урок':
            self.anotherwindow = Info8()
            self.anotherwindow.show()
            self.close()
        elif self.sender().text() == '9 урок':
            self.anotherwindow = Info9()
            self.anotherwindow.show()
            self.close()
        elif self.sender().text() == '10 урок':
            self.anotherwindow = Info10()
            self.anotherwindow.show()
            self.close()
        elif self.sender().text() == '11 урок':
            self.anotherwindow = Info11()
            self.anotherwindow.show()
            self.close()
        elif self.sender().text() == '12 урок':
            self.anotherwindow = Info12()
            self.anotherwindow.show()
            self.close()
        elif self.sender().text() == '13 урок':
            self.anotherwindow = Info13()
            self.anotherwindow.show()
            self.close()
        elif self.sender().text() == '14 урок':
            self.anotherwindow = Info14()
            self.anotherwindow.show()
            self.close()
        elif self.sender().text() == '15 урок':
            self.anotherwindow = Info15()
            self.anotherwindow.show()
            self.close()

    # def OpenWindowIntro(self):
    # self.anotherwindow = Wind2()
    # self.anotherwindow.show()

    def test(self):
        self.anotherwindow = TestingWindow('Ui/tests/test10.ui')
        self.anotherwindow.show()
        self.close()


class Info11(QMainWindow):
    def __init__(self, *lyek):
        super().__init__()
        uic.loadUi('Ui/theory/theory11.ui', self)
        self.pushButton.setStyleSheet("""
            QPushButton:hover { background-color: red }
            QPushButton:!hover { background-color: white }

            QPushButton:pressed { background-color: rgb(0, 255, 0); }
        """)
        if lyek:
            self.label = QLabel(self)
            self.label.setText("Неправильно!")
            self.label.move(710, 300)
            self.label.setFont(QtGui.QFont("Times", 22, QtGui.QFont.Bold))
            self.label.adjustSize()
            self.label2 = QLabel(self)
            self.label2.setText("Попробуй ещё раз")
            self.label2.move(710, 350)
            self.label2.setFont(QtGui.QFont("Times", 17, QtGui.QFont.Bold))
            self.label2.adjustSize()
        self.l1.display(11)
        self.pushButton.clicked.connect(self.test)
        self.show()
        self.pushButton.clicked.connect(self.test)
        self.p2.clicked.connect(self.Napravlenie)
        self.p3.clicked.connect(self.Napravlenie)
        self.p4.clicked.connect(self.Napravlenie)
        self.p5.clicked.connect(self.Napravlenie)
        self.p6.clicked.connect(self.Napravlenie)
        self.p7.clicked.connect(self.Napravlenie)
        self.p8.clicked.connect(self.Napravlenie)
        self.p9.clicked.connect(self.Napravlenie)
        self.p10.clicked.connect(self.Napravlenie)
        self.p11.clicked.connect(self.Napravlenie)
        self.p12.clicked.connect(self.Napravlenie)
        self.p13.clicked.connect(self.Napravlenie)
        self.p14.clicked.connect(self.Napravlenie)
        self.p15.clicked.connect(self.Napravlenie)
        self.p16.clicked.connect(self.Napravlenie)

        self.show()

    def Napravlenie(self):
        if self.sender().text() == '1 урок':
            self.anotherwindow = MyWidget()
            self.anotherwindow.show()
            self.close()
        elif self.sender().text() == '2 урок':
            self.anotherwindow = Info2()
            self.anotherwindow.show()
            self.close()
        elif self.sender().text() == '3 урок':
            self.anotherwindow = Info3()
            self.anotherwindow.show()
            self.close()
        elif self.sender().text() == '4 урок':
            self.anotherwindow = Info4()
            self.anotherwindow.show()
            self.close()
        elif self.sender().text() == '5 урок':
            self.anotherwindow = Info5()
            self.anotherwindow.show()
            self.close()
        elif self.sender().text() == '6 урок':
            self.anotherwindow = Info6()
            self.anotherwindow.show()
            self.close()
        elif self.sender().text() == '7 урок':
            self.anotherwindow = Info7()
            self.anotherwindow.show()
            self.close()
        elif self.sender().text() == '8 урок':
            self.anotherwindow = Info8()
            self.anotherwindow.show()
            self.close()
        elif self.sender().text() == '9 урок':
            self.anotherwindow = Info9()
            self.anotherwindow.show()
            self.close()
        elif self.sender().text() == '10 урок':
            self.anotherwindow = Info10()
            self.anotherwindow.show()
            self.close()
        elif self.sender().text() == '11 урок':
            self.anotherwindow = Info11()
            self.anotherwindow.show()
            self.close()
        elif self.sender().text() == '12 урок':
            self.anotherwindow = Info12()
            self.anotherwindow.show()
            self.close()
        elif self.sender().text() == '13 урок':
            self.anotherwindow = Info13()
            self.anotherwindow.show()
            self.close()
        elif self.sender().text() == '14 урок':
            self.anotherwindow = Info14()
            self.anotherwindow.show()
            self.close()
        elif self.sender().text() == '15 урок':
            self.anotherwindow = Info15()
            self.anotherwindow.show()
            self.close()

    # def OpenWindowIntro(self):
    # self.anotherwindow = Wind2()
    # self.anotherwindow.show()

    def test(self):
        self.anotherwindow = TestingWindow('Ui/tests/test11.ui')
        self.anotherwindow.show()
        self.close()


class Info12(QMainWindow):
    def __init__(self, *lyek):
        super().__init__()
        uic.loadUi('Ui/theory/theory12.ui', self)
        self.pushButton.setStyleSheet("""
            QPushButton:hover { background-color: red }
            QPushButton:!hover { background-color: white }

            QPushButton:pressed { background-color: rgb(0, 255, 0); }
        """)
        if lyek:
            self.label = QLabel(self)
            self.label.setText("Неправильно!")
            self.label.move(710, 300)
            self.label.setFont(QtGui.QFont("Times", 22, QtGui.QFont.Bold))
            self.label.adjustSize()
            self.label2 = QLabel(self)
            self.label2.setText("Попробуй ещё раз")
            self.label2.move(710, 350)
            self.label2.setFont(QtGui.QFont("Times", 17, QtGui.QFont.Bold))
            self.label2.adjustSize()
        self.l1.display(12)
        self.pushButton.clicked.connect(self.test)
        self.show()
        self.pushButton.clicked.connect(self.test)
        self.p2.clicked.connect(self.Napravlenie)
        self.p3.clicked.connect(self.Napravlenie)
        self.p4.clicked.connect(self.Napravlenie)
        self.p5.clicked.connect(self.Napravlenie)
        self.p6.clicked.connect(self.Napravlenie)
        self.p7.clicked.connect(self.Napravlenie)
        self.p8.clicked.connect(self.Napravlenie)
        self.p9.clicked.connect(self.Napravlenie)
        self.p10.clicked.connect(self.Napravlenie)
        self.p11.clicked.connect(self.Napravlenie)
        self.p12.clicked.connect(self.Napravlenie)
        self.p13.clicked.connect(self.Napravlenie)
        self.p14.clicked.connect(self.Napravlenie)
        self.p15.clicked.connect(self.Napravlenie)
        self.p16.clicked.connect(self.Napravlenie)

        self.show()

    def Napravlenie(self):
        if self.sender().text() == '1 урок':
            self.anotherwindow = MyWidget()
            self.anotherwindow.show()
            self.close()
        elif self.sender().text() == '2 урок':
            self.anotherwindow = Info2()
            self.anotherwindow.show()
            self.close()
        elif self.sender().text() == '3 урок':
            self.anotherwindow = Info3()
            self.anotherwindow.show()
            self.close()
        elif self.sender().text() == '4 урок':
            self.anotherwindow = Info4()
            self.anotherwindow.show()
            self.close()
        elif self.sender().text() == '5 урок':
            self.anotherwindow = Info5()
            self.anotherwindow.show()
            self.close()
        elif self.sender().text() == '6 урок':
            self.anotherwindow = Info6()
            self.anotherwindow.show()
            self.close()
        elif self.sender().text() == '7 урок':
            self.anotherwindow = Info7()
            self.anotherwindow.show()
            self.close()
        elif self.sender().text() == '8 урок':
            self.anotherwindow = Info8()
            self.anotherwindow.show()
            self.close()
        elif self.sender().text() == '9 урок':
            self.anotherwindow = Info9()
            self.anotherwindow.show()
            self.close()
        elif self.sender().text() == '10 урок':
            self.anotherwindow = Info10()
            self.anotherwindow.show()
            self.close()
        elif self.sender().text() == '11 урок':
            self.anotherwindow = Info11()
            self.anotherwindow.show()
            self.close()
        elif self.sender().text() == '12 урок':
            self.anotherwindow = Info12()
            self.anotherwindow.show()
            self.close()
        elif self.sender().text() == '13 урок':
            self.anotherwindow = Info13()
            self.anotherwindow.show()
            self.close()
        elif self.sender().text() == '14 урок':
            self.anotherwindow = Info14()
            self.anotherwindow.show()
            self.close()
        elif self.sender().text() == '15 урок':
            self.anotherwindow = Info15()
            self.anotherwindow.show()
            self.close()

    # def OpenWindowIntro(self):
    # self.anotherwindow = Wind2()
    # self.anotherwindow.show()

    def test(self):
        self.anotherwindow = TestingWindow('Ui/tests/test12.ui')
        self.anotherwindow.show()
        self.close()


class Info13(QMainWindow):
    def __init__(self, *lyek):
        super().__init__()
        uic.loadUi('Ui/theory/theory13.ui', self)
        self.pushButton.setStyleSheet("""
            QPushButton:hover { background-color: red }
            QPushButton:!hover { background-color: white }

            QPushButton:pressed { background-color: rgb(0, 255, 0); }
        """)
        if lyek:
            self.label = QLabel(self)
            self.label.setText("Неправильно!")
            self.label.move(710, 300)
            self.label.setFont(QtGui.QFont("Times", 22, QtGui.QFont.Bold))
            self.label.adjustSize()
            self.label2 = QLabel(self)
            self.label2.setText("Попробуй ещё раз")
            self.label2.move(710, 350)
            self.label2.setFont(QtGui.QFont("Times", 17, QtGui.QFont.Bold))
            self.label2.adjustSize()
        self.l1.display(13)
        self.pushButton.clicked.connect(self.test)
        self.show()
        self.pushButton.clicked.connect(self.test)
        self.p2.clicked.connect(self.Napravlenie)
        self.p3.clicked.connect(self.Napravlenie)
        self.p4.clicked.connect(self.Napravlenie)
        self.p5.clicked.connect(self.Napravlenie)
        self.p6.clicked.connect(self.Napravlenie)
        self.p7.clicked.connect(self.Napravlenie)
        self.p8.clicked.connect(self.Napravlenie)
        self.p9.clicked.connect(self.Napravlenie)
        self.p10.clicked.connect(self.Napravlenie)
        self.p11.clicked.connect(self.Napravlenie)
        self.p12.clicked.connect(self.Napravlenie)
        self.p13.clicked.connect(self.Napravlenie)
        self.p14.clicked.connect(self.Napravlenie)
        self.p15.clicked.connect(self.Napravlenie)
        self.p16.clicked.connect(self.Napravlenie)

        self.show()

    def Napravlenie(self):
        if self.sender().text() == '1 урок':
            self.anotherwindow = MyWidget()
            self.anotherwindow.show()
            self.close()
        elif self.sender().text() == '2 урок':
            self.anotherwindow = Info2()
            self.anotherwindow.show()
            self.close()
        elif self.sender().text() == '3 урок':
            self.anotherwindow = Info3()
            self.anotherwindow.show()
            self.close()
        elif self.sender().text() == '4 урок':
            self.anotherwindow = Info4()
            self.anotherwindow.show()
            self.close()
        elif self.sender().text() == '5 урок':
            self.anotherwindow = Info5()
            self.anotherwindow.show()
            self.close()
        elif self.sender().text() == '6 урок':
            self.anotherwindow = Info6()
            self.anotherwindow.show()
            self.close()
        elif self.sender().text() == '7 урок':
            self.anotherwindow = Info7()
            self.anotherwindow.show()
            self.close()
        elif self.sender().text() == '8 урок':
            self.anotherwindow = Info8()
            self.anotherwindow.show()
            self.close()
        elif self.sender().text() == '9 урок':
            self.anotherwindow = Info9()
            self.anotherwindow.show()
            self.close()
        elif self.sender().text() == '10 урок':
            self.anotherwindow = Info10()
            self.anotherwindow.show()
            self.close()
        elif self.sender().text() == '11 урок':
            self.anotherwindow = Info11()
            self.anotherwindow.show()
            self.close()
        elif self.sender().text() == '12 урок':
            self.anotherwindow = Info12()
            self.anotherwindow.show()
            self.close()
        elif self.sender().text() == '13 урок':
            self.anotherwindow = Info13()
            self.anotherwindow.show()
            self.close()
        elif self.sender().text() == '14 урок':
            self.anotherwindow = Info14()
            self.anotherwindow.show()
            self.close()
        elif self.sender().text() == '15 урок':
            self.anotherwindow = Info15()
            self.anotherwindow.show()
            self.close()

    # def OpenWindowIntro(self):
    # self.anotherwindow = Wind2()
    # self.anotherwindow.show()

    def test(self):
        self.anotherwindow = TestingWindow('Ui/tests/test13.ui')
        self.anotherwindow.show()
        self.close()


class Info14(QMainWindow):
    def __init__(self, *lyek):
        super().__init__()
        uic.loadUi('Ui/theory/theory14.ui', self)
        self.pushButton.setStyleSheet("""
            QPushButton:hover { background-color: red }
            QPushButton:!hover { background-color: white }

            QPushButton:pressed { background-color: rgb(0, 255, 0); }
        """)
        if lyek:
            self.label = QLabel(self)
            self.label.setText("Неправильно!")
            self.label.move(710, 300)
            self.label.setFont(QtGui.QFont("Times", 22, QtGui.QFont.Bold))
            self.label.adjustSize()
            self.label2 = QLabel(self)
            self.label2.setText("Попробуй ещё раз")
            self.label2.move(710, 350)
            self.label2.setFont(QtGui.QFont("Times", 17, QtGui.QFont.Bold))
            self.label2.adjustSize()
        self.l1.display(14)
        self.pushButton.clicked.connect(self.test)
        self.show()
        self.pushButton.clicked.connect(self.test)
        self.p2.clicked.connect(self.Napravlenie)
        self.p3.clicked.connect(self.Napravlenie)
        self.p4.clicked.connect(self.Napravlenie)
        self.p5.clicked.connect(self.Napravlenie)
        self.p6.clicked.connect(self.Napravlenie)
        self.p7.clicked.connect(self.Napravlenie)
        self.p8.clicked.connect(self.Napravlenie)
        self.p9.clicked.connect(self.Napravlenie)
        self.p10.clicked.connect(self.Napravlenie)
        self.p11.clicked.connect(self.Napravlenie)
        self.p12.clicked.connect(self.Napravlenie)
        self.p13.clicked.connect(self.Napravlenie)
        self.p14.clicked.connect(self.Napravlenie)
        self.p15.clicked.connect(self.Napravlenie)
        self.p16.clicked.connect(self.Napravlenie)

        self.show()

    def Napravlenie(self):
        if self.sender().text() == '1 урок':
            self.anotherwindow = MyWidget()
            self.anotherwindow.show()
            self.close()
        elif self.sender().text() == '2 урок':
            self.anotherwindow = Info2()
            self.anotherwindow.show()
            self.close()
        elif self.sender().text() == '3 урок':
            self.anotherwindow = Info3()
            self.anotherwindow.show()
            self.close()
        elif self.sender().text() == '4 урок':
            self.anotherwindow = Info4()
            self.anotherwindow.show()
            self.close()
        elif self.sender().text() == '5 урок':
            self.anotherwindow = Info5()
            self.anotherwindow.show()
            self.close()
        elif self.sender().text() == '6 урок':
            self.anotherwindow = Info6()
            self.anotherwindow.show()
            self.close()
        elif self.sender().text() == '7 урок':
            self.anotherwindow = Info7()
            self.anotherwindow.show()
            self.close()
        elif self.sender().text() == '8 урок':
            self.anotherwindow = Info8()
            self.anotherwindow.show()
            self.close()
        elif self.sender().text() == '9 урок':
            self.anotherwindow = Info9()
            self.anotherwindow.show()
            self.close()
        elif self.sender().text() == '10 урок':
            self.anotherwindow = Info10()
            self.anotherwindow.show()
            self.close()
        elif self.sender().text() == '11 урок':
            self.anotherwindow = Info11()
            self.anotherwindow.show()
            self.close()
        elif self.sender().text() == '12 урок':
            self.anotherwindow = Info12()
            self.anotherwindow.show()
            self.close()
        elif self.sender().text() == '13 урок':
            self.anotherwindow = Info13()
            self.anotherwindow.show()
            self.close()
        elif self.sender().text() == '14 урок':
            self.anotherwindow = Info14()
            self.anotherwindow.show()
            self.close()
        elif self.sender().text() == '15 урок':
            self.anotherwindow = Info15()
            self.anotherwindow.show()
            self.close()

    # def OpenWindowIntro(self):
    # self.anotherwindow = Wind2()
    # self.anotherwindow.show()

    def test(self):
        self.anotherwindow = TestingWindow('Ui/tests/test14.ui')
        self.anotherwindow.show()
        self.close()


class Info15(QMainWindow):
    def __init__(self, *lyek):
        super().__init__()
        uic.loadUi('Ui/theory/theory15.ui', self)
        self.pushButton.setStyleSheet("""
            QPushButton:hover { background-color: red }
            QPushButton:!hover { background-color: white }

            QPushButton:pressed { background-color: rgb(0, 255, 0); }
        """)
        if lyek:
            self.label = QLabel(self)
            self.label.setText("Неправильно!")
            self.label.move(710, 300)
            self.label.setFont(QtGui.QFont("Times", 22, QtGui.QFont.Bold))
            self.label.adjustSize()
            self.label2 = QLabel(self)
            self.label2.setText("Попробуй ещё раз")
            self.label2.move(710, 350)
            self.label2.setFont(QtGui.QFont("Times", 17, QtGui.QFont.Bold))
            self.label2.adjustSize()
        self.l1.display(15)
        self.pushButton.clicked.connect(self.test)
        self.show()
        self.pushButton.clicked.connect(self.test)
        self.p2.clicked.connect(self.Napravlenie)
        self.p3.clicked.connect(self.Napravlenie)
        self.p4.clicked.connect(self.Napravlenie)
        self.p5.clicked.connect(self.Napravlenie)
        self.p6.clicked.connect(self.Napravlenie)
        self.p7.clicked.connect(self.Napravlenie)
        self.p8.clicked.connect(self.Napravlenie)
        self.p9.clicked.connect(self.Napravlenie)
        self.p10.clicked.connect(self.Napravlenie)
        self.p11.clicked.connect(self.Napravlenie)
        self.p12.clicked.connect(self.Napravlenie)
        self.p13.clicked.connect(self.Napravlenie)
        self.p14.clicked.connect(self.Napravlenie)
        self.p15.clicked.connect(self.Napravlenie)
        self.p16.clicked.connect(self.Napravlenie)

        self.show()

    def Napravlenie(self):
        if self.sender().text() == '1 урок':
            self.anotherwindow = MyWidget()
            self.anotherwindow.show()
            self.close()
        elif self.sender().text() == '2 урок':
            self.anotherwindow = Info2()
            self.anotherwindow.show()
            self.close()
        elif self.sender().text() == '3 урок':
            self.anotherwindow = Info3()
            self.anotherwindow.show()
            self.close()
        elif self.sender().text() == '4 урок':
            self.anotherwindow = Info4()
            self.anotherwindow.show()
            self.close()
        elif self.sender().text() == '5 урок':
            self.anotherwindow = Info5()
            self.anotherwindow.show()
            self.close()
        elif self.sender().text() == '6 урок':
            self.anotherwindow = Info6()
            self.anotherwindow.show()
            self.close()
        elif self.sender().text() == '7 урок':
            self.anotherwindow = Info7()
            self.anotherwindow.show()
            self.close()
        elif self.sender().text() == '8 урок':
            self.anotherwindow = Info8()
            self.anotherwindow.show()
            self.close()
        elif self.sender().text() == '9 урок':
            self.anotherwindow = Info9()
            self.anotherwindow.show()
            self.close()
        elif self.sender().text() == '10 урок':
            self.anotherwindow = Info10()
            self.anotherwindow.show()
            self.close()
        elif self.sender().text() == '11 урок':
            self.anotherwindow = Info11()
            self.anotherwindow.show()
            self.close()
        elif self.sender().text() == '12 урок':
            self.anotherwindow = Info12()
            self.anotherwindow.show()
            self.close()
        elif self.sender().text() == '13 урок':
            self.anotherwindow = Info13()
            self.anotherwindow.show()
            self.close()
        elif self.sender().text() == '14 урок':
            self.anotherwindow = Info14()
            self.anotherwindow.show()
            self.close()
        elif self.sender().text() == '15 урок':
            self.anotherwindow = Info15()
            self.anotherwindow.show()
            self.close()

    # def OpenWindowIntro(self):
    # self.anotherwindow = Wind2()
    # self.anotherwindow.show()

    def test(self):
        self.anotherwindow = TestingWindow('Ui/tests/test15.ui')
        self.anotherwindow.show()
        self.close()


app = QApplication(sys.argv)
ex = Title()
ex.show()
sys.exit(app.exec_())
