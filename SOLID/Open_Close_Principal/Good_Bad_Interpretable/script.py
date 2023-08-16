import sys
from PyQt5 import QtWidgets
from Open_Close_Principal.Good_Bad_Interpretable.calc_template import CalcTemplate


class CalculatorApplicationStarter(QtWidgets.QApplication):

    def __init__(self, *args):
        super().__init__(*args)
        self.main_window = CalcWindow()
        self.main_window.show()

    def run(self):
        self.exec_()


class CalcWindow(QtWidgets.QMainWindow):
    def __init__(self, *args, parent=None, **kwargs):
        QtWidgets.QMainWindow.__init__(self, *args, parent, **kwargs)
        self.template = CalcTemplate()
        self.template.setup_ui(self)


if __name__ == '__main__':
    calc = CalculatorApplicationStarter(sys.argv)
    calc.run()
