import sys
from PySide6 import QtWidgets
from Monopoly.mo_ui import mo_gui


class App(QtWidgets.QApplication):

    def __init__(self):

        super().__init__()
        self.init_UI()

   # secondary methods

    def init_UI(self):
        gui = mo_gui.Gui(self)
        gui.show()
        sys.exit(self.exec_())