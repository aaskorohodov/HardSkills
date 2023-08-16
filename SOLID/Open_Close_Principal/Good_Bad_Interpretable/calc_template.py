from PyQt5 import QtCore, QtGui, QtWidgets
from Open_Close_Principal.Good_Bad_Interpretable.calc_engine import *


class CalcTemplate:
    """Represents calculators window, it's widgets and general widget's logic."""

    def __init__(self):
        self.statusbar = QtWidgets.QStatusBar()
        self.menubar = QtWidgets.QMenuBar()

        self.label_screen = QtWidgets.QLabel()

        self.btn_0 = QtWidgets.QPushButton()
        self.btn_1 = QtWidgets.QPushButton()
        self.btn_2 = QtWidgets.QPushButton()
        self.btn_3 = QtWidgets.QPushButton()
        self.btn_4 = QtWidgets.QPushButton()
        self.btn_5 = QtWidgets.QPushButton()
        self.btn_6 = QtWidgets.QPushButton()
        self.btn_7 = QtWidgets.QPushButton()
        self.btn_8 = QtWidgets.QPushButton()
        self.btn_9 = QtWidgets.QPushButton()

        self.btn_equal = QtWidgets.QPushButton()
        self.btn_dot = QtWidgets.QPushButton()
        self.btn_pm = QtWidgets.QPushButton()
        self.btn_percent = QtWidgets.QPushButton()
        self.btn_square = QtWidgets.QPushButton()
        self.btn_mult = QtWidgets.QPushButton()
        self.btn_div = QtWidgets.QPushButton()
        self.btn_min = QtWidgets.QPushButton()
        self.btn_plus = QtWidgets.QPushButton()
        self.btn_del = QtWidgets.QPushButton()

        self.btns_layout = QtWidgets.QGridLayout()
        self.vertical_layout = QtWidgets.QVBoxLayout()
        self.central_widget = QtWidgets.QWidget()

    def setup_ui(self, main_window: QtWidgets.QMainWindow):
        """Builds layers and widgets (buttons and calculator's screen)
        
        Args:
            main_window: link to PyQt window instance, inside which widgets are placed"""

        main_window.setObjectName("MainWindow")
        main_window.resize(450, 550)
        main_window.setMaximumSize(QtCore.QSize(450, 550))
        self.central_widget = QtWidgets.QWidget(main_window)
        self.central_widget.setObjectName("centralwidget")
        self.vertical_layout = QtWidgets.QVBoxLayout(self.central_widget)
        self.vertical_layout.setObjectName("verticalLayout")

        self.label_screen = QtWidgets.QLabel(self.central_widget)
        size_policy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        size_policy.setHorizontalStretch(0)
        size_policy.setVerticalStretch(0)
        size_policy.setHeightForWidth(self.label_screen.sizePolicy().hasHeightForWidth())
        self.label_screen.setSizePolicy(size_policy)
        self.label_screen.setMaximumSize(QtCore.QSize(16777215, 100))
        font = QtGui.QFont()
        font.setPointSize(35)
        font.setUnderline(False)
        font.setStrikeOut(False)
        self.label_screen.setFont(font)
        self.label_screen.setAlignment(QtCore.Qt.AlignRight | QtCore.Qt.AlignTrailing | QtCore.Qt.AlignVCenter)
        self.label_screen.setObjectName("label")
        self.vertical_layout.addWidget(self.label_screen)

        self.btns_layout = QtWidgets.QGridLayout()
        self.btns_layout.setObjectName("btns_layout")

        self.btn_0 = QtWidgets.QPushButton(self.central_widget)
        self.btn_0.setMinimumSize(QtCore.QSize(0, 50))
        font = QtGui.QFont()
        font.setPointSize(15)
        self.btn_0.setFont(font)
        self.btn_0.setObjectName("btn_0")
        self.btn_0.clicked.connect(lambda: self.show_equation('0'))
        self.btns_layout.addWidget(self.btn_0, 4, 2, 1, 1)

        self.btn_1 = QtWidgets.QPushButton(self.central_widget)
        self.btn_1.setMinimumSize(QtCore.QSize(0, 50))
        font = QtGui.QFont()
        font.setPointSize(15)
        self.btn_1.setFont(font)
        self.btn_1.setObjectName("btn_1")
        self.btn_1.clicked.connect(lambda: self.show_equation('1'))
        self.btns_layout.addWidget(self.btn_1, 3, 0, 1, 1)

        self.btn_2 = QtWidgets.QPushButton(self.central_widget)
        self.btn_2.setMinimumSize(QtCore.QSize(0, 50))
        font = QtGui.QFont()
        font.setPointSize(15)
        self.btn_2.setFont(font)
        self.btn_2.setObjectName("btn_2")
        self.btn_2.clicked.connect(lambda: self.show_equation('2'))
        self.btns_layout.addWidget(self.btn_2, 3, 2, 1, 1)

        self.btn_3 = QtWidgets.QPushButton(self.central_widget)
        self.btn_3.setMinimumSize(QtCore.QSize(0, 50))
        font = QtGui.QFont()
        font.setPointSize(15)
        self.btn_3.setFont(font)
        self.btn_3.setObjectName("btn_3")
        self.btn_3.clicked.connect(lambda: self.show_equation('3'))
        self.btns_layout.addWidget(self.btn_3, 3, 3, 1, 1)

        self.btn_4 = QtWidgets.QPushButton(self.central_widget)
        self.btn_4.setMinimumSize(QtCore.QSize(0, 50))
        font = QtGui.QFont()
        font.setPointSize(15)
        self.btn_4.setFont(font)
        self.btn_4.setObjectName("btn_4")
        self.btn_4.clicked.connect(lambda: self.show_equation('4'))
        self.btns_layout.addWidget(self.btn_4, 2, 0, 1, 1)

        self.btn_5 = QtWidgets.QPushButton(self.central_widget)
        self.btn_5.setMinimumSize(QtCore.QSize(0, 50))
        font = QtGui.QFont()
        font.setPointSize(15)
        self.btn_5.setFont(font)
        self.btn_5.setObjectName("btn_5")
        self.btn_5.clicked.connect(lambda: self.show_equation('5'))
        self.btns_layout.addWidget(self.btn_5, 2, 2, 1, 1)

        self.btn_6 = QtWidgets.QPushButton(self.central_widget)
        self.btn_6.setMinimumSize(QtCore.QSize(0, 50))
        font = QtGui.QFont()
        font.setPointSize(15)
        self.btn_6.setFont(font)
        self.btn_6.setObjectName("btn_6")
        self.btn_6.clicked.connect(lambda: self.show_equation('6'))
        self.btns_layout.addWidget(self.btn_6, 2, 3, 1, 1)

        self.btn_7 = QtWidgets.QPushButton(self.central_widget)
        self.btn_7.setMinimumSize(QtCore.QSize(0, 50))
        font = QtGui.QFont()
        font.setPointSize(15)
        font.setWeight(50)
        self.btn_7.setFont(font)
        self.btn_7.setObjectName("btn_7")
        self.btn_7.clicked.connect(lambda: self.show_equation('7'))
        self.btns_layout.addWidget(self.btn_7, 1, 0, 1, 1)

        self.btn_8 = QtWidgets.QPushButton(self.central_widget)
        self.btn_8.setMinimumSize(QtCore.QSize(0, 50))
        font = QtGui.QFont()
        font.setPointSize(15)
        self.btn_8.setFont(font)
        self.btn_8.setObjectName("btn_8")
        self.btn_8.clicked.connect(lambda: self.show_equation('8'))
        self.btns_layout.addWidget(self.btn_8, 1, 2, 1, 1)

        self.btn_9 = QtWidgets.QPushButton(self.central_widget)
        self.btn_9.setMinimumSize(QtCore.QSize(0, 50))
        font = QtGui.QFont()
        font.setPointSize(15)
        self.btn_9.setFont(font)
        self.btn_9.setObjectName("btn_9")
        self.btn_9.clicked.connect(lambda: self.show_equation('9'))
        self.btns_layout.addWidget(self.btn_9, 1, 3, 1, 1)

        self.btn_plus = QtWidgets.QPushButton(self.central_widget)
        self.btn_plus.setMinimumSize(QtCore.QSize(0, 50))
        font = QtGui.QFont()
        font.setPointSize(15)
        self.btn_plus.setFont(font)
        self.btn_plus.setObjectName("btn_plus")
        self.btn_plus.clicked.connect(lambda:
                                      self.label_screen.setText(
                                          BasicOperations(self.label_screen.text(), '+').calculate())
                                      )
        self.btns_layout.addWidget(self.btn_plus, 3, 4, 1, 1)

        self.btn_min = QtWidgets.QPushButton(self.central_widget)
        self.btn_min.setMinimumSize(QtCore.QSize(0, 50))
        font = QtGui.QFont()
        font.setPointSize(15)
        self.btn_min.setFont(font)
        self.btn_min.setObjectName("btn_min")
        self.btn_min.clicked.connect(lambda:
                                     self.label_screen.setText(
                                         BasicOperations(self.label_screen.text(), '-').calculate())
                                     )
        self.btns_layout.addWidget(self.btn_min, 2, 4, 1, 1)

        self.btn_div = QtWidgets.QPushButton(self.central_widget)
        self.btn_div.setMinimumSize(QtCore.QSize(0, 50))
        font = QtGui.QFont()
        font.setPointSize(15)
        self.btn_div.setFont(font)
        self.btn_div.setObjectName("btn_div")
        self.btn_div.clicked.connect(lambda:
                                     self.label_screen.setText(
                                         BasicOperations(self.label_screen.text(), '/').calculate())
                                     )
        self.btns_layout.addWidget(self.btn_div, 0, 4, 1, 1)

        self.btn_mult = QtWidgets.QPushButton(self.central_widget)
        self.btn_mult.setMinimumSize(QtCore.QSize(0, 50))
        font = QtGui.QFont()
        font.setPointSize(15)
        self.btn_mult.setFont(font)
        self.btn_mult.setObjectName("btn_mult")
        self.btn_mult.clicked.connect(lambda:
                                      self.label_screen.setText(
                                          BasicOperations(self.label_screen.text(), '*').calculate())
                                      )
        self.btns_layout.addWidget(self.btn_mult, 1, 4, 1, 1)

        self.btn_square = QtWidgets.QPushButton(self.central_widget)
        self.btn_square.setMinimumSize(QtCore.QSize(0, 50))
        font = QtGui.QFont()
        font.setPointSize(15)
        self.btn_square.setFont(font)
        self.btn_square.setObjectName("btn_square")
        self.btn_square.clicked.connect(lambda:
                                        self.label_screen.setText(Square(self.label_screen.text(), 'sq').calculate()))
        self.btns_layout.addWidget(self.btn_square, 0, 2, 1, 1)

        self.btn_del = QtWidgets.QPushButton(self.central_widget)
        self.btn_del.setMinimumSize(QtCore.QSize(0, 50))
        font = QtGui.QFont()
        font.setPointSize(15)
        self.btn_del.setFont(font)
        self.btn_del.setObjectName("btn_del")
        self.btn_del.clicked.connect(lambda: self.label_screen.setText(''))
        self.btns_layout.addWidget(self.btn_del, 0, 3, 1, 1)

        self.btn_percent = QtWidgets.QPushButton(self.central_widget)
        self.btn_percent.setMinimumSize(QtCore.QSize(0, 50))
        font = QtGui.QFont()
        font.setPointSize(15)
        self.btn_percent.setFont(font)
        self.btn_percent.setObjectName("btn_percent")
        self.btn_percent.clicked.connect(lambda:
                                         self.label_screen.setText(Percent(self.label_screen.text(), '%').calculate()))
        self.btns_layout.addWidget(self.btn_percent, 0, 0, 1, 1)

        self.btn_pm = QtWidgets.QPushButton(self.central_widget)
        self.btn_pm.setMinimumSize(QtCore.QSize(0, 50))
        font = QtGui.QFont()
        font.setPointSize(15)
        self.btn_pm.setFont(font)
        self.btn_pm.setObjectName("btn_pm")
        self.btn_pm.clicked.connect(lambda:
                                    self.label_screen.setText(PlusMinus(self.label_screen.text(), '+-').calculate()))
        self.btns_layout.addWidget(self.btn_pm, 4, 0, 1, 1)

        self.btn_dot = QtWidgets.QPushButton(self.central_widget)
        self.btn_dot.setMinimumSize(QtCore.QSize(0, 50))
        font = QtGui.QFont()
        font.setPointSize(15)
        self.btn_dot.setFont(font)
        self.btn_dot.setObjectName("btn_dot")
        self.btn_dot.clicked.connect(lambda: self.show_equation('.'))
        self.btns_layout.addWidget(self.btn_dot, 4, 3, 1, 1)

        self.btn_equal = QtWidgets.QPushButton(self.central_widget)
        self.btn_equal.setMinimumSize(QtCore.QSize(0, 50))
        font = QtGui.QFont()
        font.setPointSize(15)
        self.btn_equal.setFont(font)
        self.btn_equal.setObjectName("btn_equal")
        self.btn_equal.clicked.connect(lambda:
                                       self.label_screen.setText(Equal(self.label_screen.text(), '=').calculate()))
        self.btns_layout.addWidget(self.btn_equal, 4, 4, 1, 1)

        self.vertical_layout.addLayout(self.btns_layout)
        main_window.setCentralWidget(self.central_widget)

        self.menubar = QtWidgets.QMenuBar(main_window)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 450, 21))
        self.menubar.setObjectName("menubar")
        main_window.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(main_window)
        self.statusbar.setObjectName("statusbar")
        main_window.setStatusBar(self.statusbar)

        self.retranslate_ui(main_window)
        QtCore.QMetaObject.connectSlotsByName(main_window)

    def retranslate_ui(self, main_window) -> None:
        """Sets text onto different widgets

        Args:
            main_window: link onto what's called PyQt-MainWindow (instance of PyQt's window)"""

        _translate = QtCore.QCoreApplication.translate
        main_window.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label_screen.setText(_translate("MainWindow", ""))
        self.btn_4.setText(_translate("MainWindow", "4"))
        self.btn_5.setText(_translate("MainWindow", "5"))
        self.btn_6.setText(_translate("MainWindow", "6"))
        self.btn_2.setText(_translate("MainWindow", "2"))
        self.btn_1.setText(_translate("MainWindow", "1"))
        self.btn_plus.setText(_translate("MainWindow", "+"))
        self.btn_3.setText(_translate("MainWindow", "3"))
        self.btn_min.setText(_translate("MainWindow", "–"))
        self.btn_div.setText(_translate("MainWindow", "/"))
        self.btn_7.setText(_translate("MainWindow", "7"))
        self.btn_8.setText(_translate("MainWindow", "8"))
        self.btn_mult.setText(_translate("MainWindow", "*"))
        self.btn_9.setText(_translate("MainWindow", "9"))
        self.btn_square.setText(_translate("MainWindow", "x2"))
        self.btn_del.setText(_translate("MainWindow", "Del"))
        self.btn_percent.setText(_translate("MainWindow", "%"))
        self.btn_0.setText(_translate("MainWindow", "0"))
        self.btn_pm.setText(_translate("MainWindow", "+/–"))
        self.btn_dot.setText(_translate("MainWindow", "."))
        self.btn_equal.setText(_translate("MainWindow", "="))

    def show_equation(self, symbol: str) -> None:
        """Draws users input in label area (into 'calculator screen')

        Args:
            symbol: button, that was pressed"""

        text = self.label_screen.text()

        # We don't want to see numbers like '09' on the 'screen', so if text on the 'screen' is now 0 => remove 0
        if text == '0' and symbol != '.':
            self.label_screen.setText(symbol)
            return
        # We don't want to have more than 16 symbols, because it would extend calculator's window size
        if not len(text) == 16:
            if symbol == '.' and '.' in text:
                return
            text += symbol
            self.label_screen.setText(text)

