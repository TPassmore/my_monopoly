from PySide6 import QtWidgets, QtCore, QtGui
from pp_core.pp_system import pp_file

card_width = 80
card_height = card_width * 2
border = 2

class Board_piece(QtWidgets.QDialog):
    
    def __init__(self):
        super().__init__()
        self.setFixedSize(card_width, card_height)
        self.setObjectName("MasterPiece")
        self.setStyleSheet(f"#MasterPiece {{border: {border}px solid black; background-color: #b9e7f0}}")




class Property_piece(Board_piece):
    
    def __init__(self, family_color, name, price):
        super().__init__()
        self.init_ui(family_color, name, price)

    def init_ui(self, family_color, name, price):
        layout = QtWidgets.QVBoxLayout()
        self.setLayout(layout)
        layout.setAlignment(QtCore.Qt.AlignHCenter)
        layout.setContentsMargins(0, 0, 0, 0)
        layout.setSpacing(0)

        color_widget = QtWidgets.QWidget()
        color_widget.setObjectName("FamilyColor")
        color_widget.setStyleSheet(f"#FamilyColor {{background-color: {family_color}; margin: {border}px;}}")
        color_widget.setFixedSize(card_width, card_height*0.2)

        piece_name = QtWidgets.QLabel(name)
        price_desc = QtWidgets.QLabel(f"Price: ${price}")

        layout.addWidget(color_widget, alignment=QtCore.Qt.AlignTop)
        layout.addWidget(piece_name, alignment=QtCore.Qt.AlignTop | QtCore.Qt.AlignHCenter)
        layout.addWidget(price_desc, alignment=QtCore.Qt.AlignBottom | QtCore.Qt.AlignHCenter)


class Non_property_piece(Board_piece):
    
    def __init__(self, title, image_path, bottom_desc):
        super().__init__()
        self.init_ui(title, image_path, bottom_desc)

    def init_ui(self, title, image_path, bottom_desc):
        layout = QtWidgets.QVBoxLayout()
        self.setLayout(layout)
        layout.setAlignment(QtCore.Qt.AlignHCenter)

        self.title = QtWidgets.QLabel(title)
        self.image = QtWidgets.QLabel()
        pixmap = QtGui.QPixmap(pp_file.find_in_path(image_path)).scaledToWidth(card_width * 0.8)
        self.image.setPixmap(pixmap)

        self.bottom_desc = QtWidgets.QLabel(bottom_desc)

        layout.addWidget(self.title, stretch=1)
        layout.addWidget(self.image, stretch=3)
        layout.addWidget(self.bottom_desc, stretch=1, alignment=QtCore.Qt.AlignHCenter)

class Corner_piece(Board_piece):

    def __init__(self):
        super().__init__()
        self.setFixedWidth(card_width*2)

class Community_chest(Non_property_piece):
    
    icon_path = "Monopoly/mo_assets/mo_png/community_chest.png"
    
    def __init__(self):
        super().__init__("Community Chest", self.icon_path, "take a card")


    