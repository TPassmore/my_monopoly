from PySide6 import QtWidgets, QtGui
from pp_core.pp_system import pp_file
from my_monopoly.mo_ui import mo_board, mo_board_pieces




class Gui(QtWidgets.QMainWindow):

    # icon_path = pp_file.find_in_path()

    def __init__(self, app):

        super(Gui, self).__init__()
        self.app = app
        
        self.init_UI()

    # secondary methods

    def init_UI(self):  

        self.dialog = mo_board.Board()
        self.setCentralWidget(self.dialog)
        self.setWindowTitle('Monopoly')
        # self.setWindowIcon(QtGui.QIcon(self.icon_path))
        # self.setFixedSize(1080, 720)