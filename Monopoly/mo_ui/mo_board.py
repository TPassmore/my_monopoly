from PySide6 import QtWidgets, QtGui
from Monopoly.mo_ui import mo_board_pieces

card_height = mo_board_pieces.card_height
card_width = mo_board_pieces.card_width
cards_in_a_row = 13
total_width = cards_in_a_row*card_width

# TODO: implement a queue system to take the board information from a json/list of tuples
# TODO: Add a dictionary (id: object) system to link the model and gui

class Board(QtWidgets.QWidget):

    def __init__(self):
        super().__init__()
        self.init_ui()

    def init_ui(self):
        graphicsview = QtWidgets.QGraphicsView()
        scene = QtWidgets.QGraphicsScene(graphicsview)
        graphicsview.setScene(scene)
        scene.setSceneRect(0, 0, total_width, total_width)

        layout = QtWidgets.QVBoxLayout(self)
        layout.setContentsMargins(0, 0, 0, 0)
        layout.setSpacing(0)

        h_layout = QtWidgets.QHBoxLayout()
        h_layout.setContentsMargins(0, 0, 0, 0)
        h_layout.setSpacing(0)

        row_1 = Board_row()
        self.row_2 = Board_row(corners=False, rotate=90)
        self.row_3 = Board_row(corners=False, rotate=270)
        row_4 = Board_row()

        proxy = QtWidgets.QGraphicsProxyWidget()
        proxy.setWidget(row_1)
        proxy.setPos(0, 0)
        scene.addItem(proxy)

        proxy = QtWidgets.QGraphicsProxyWidget()
        proxy.setWidget(self.row_2)
        proxy.setTransformOriginPoint(proxy.boundingRect().center())
        proxy.setPos((card_width * 7.5) - 11 * card_width, card_width * 5.5)
        proxy.setRotation(90)
        
        scene.addItem(proxy)

        proxy = QtWidgets.QGraphicsProxyWidget()
        proxy.setWidget(self.row_3)
        proxy.setTransformOriginPoint(proxy.boundingRect().center())
        proxy.setPos(card_width*7.5, card_width * 5.5)
        proxy.setRotation(270)
        
        scene.addItem(proxy)

        proxy = QtWidgets.QGraphicsProxyWidget()
        proxy.setWidget(row_4)
        proxy.setPos(0, 11 * card_width)
        scene.addItem(proxy)

        layout.addWidget(graphicsview)
        
        # graphicsview.fitInView(0, 0, 1500, 1500, aspectRadioMode=QtGui.Qt.IgnoreAspectRatio)

        # layout.addWidget(row_1)
        # h_layout.addWidget(self.row_2, stretch=1)
        # h_layout.addWidget(QtWidgets.QWidget(), stretch=3)
        # h_layout.addWidget(self.row_3, stretch=1)
        # layout.addLayout(h_layout)
        # layout.addWidget(row_4)
        # layout.addWidget(test)

        


class Board_row(QtWidgets.QWidget):

    def __init__(self, corners=True, rotate=None):
        super().__init__()
        self.rotate = rotate
        self.init_ui(corners)

    def init_ui(self, corners):

        layout = QtWidgets.QHBoxLayout(self)
        layout.setContentsMargins(0, 0, 0, 0)
        layout.setSpacing(0)

        corner_piece = mo_board_pieces.Corner_piece()
        family_color = "#222244"
        prop_1 = mo_board_pieces.Property_piece(family_color, "Burnside", 60)
        prop_2 = mo_board_pieces.Property_piece(family_color, "Major Taylor", 60)
        family_color = "#442244"
        prop_3 = mo_board_pieces.Property_piece(family_color, "Worcester", 100)
        prop_4 = mo_board_pieces.Property_piece(family_color, "Ecotarium", 100)
        prop_5 = mo_board_pieces.Property_piece(family_color, "Museum", 120)

        if corners: layout.addWidget(corner_piece)
        layout.addWidget(prop_1)
        layout.addWidget(mo_board_pieces.Community_chest())
        layout.addWidget(prop_2)
        layout.addWidget(mo_board_pieces.Community_chest())
        layout.addWidget(mo_board_pieces.Community_chest())
        layout.addWidget(prop_3)
        layout.addWidget(mo_board_pieces.Community_chest())
        layout.addWidget(prop_4)
        layout.addWidget(prop_5)
        if corners: layout.addWidget(mo_board_pieces.Corner_piece())

    # def paintEvent(self, event):
    #     if self.rotate is not None:
    #         print("here")
    #         painter = QtGui.QPainter(self)
            
    #         # Calculate the rotation angle in radians
    #         radians = self.rotate * (3.141592653589793 / 180.0)
            
    #         # Create a transformation matrix for rotation
    #         transform = QtGui.QTransform()
    #         transform.rotate(self.rotate)
            
    #         # Apply the transformation to the painter
    #         painter.setTransform(transform)
            
    #         # Draw whatever you want here, it will be rotated
    #         painter.drawText(0, 0, "Rotated Text")