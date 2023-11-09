from PySide6 import QtWidgets, QtGui
from my_monopoly.mo_ui import mo_board_pieces, mo_properties


card_height = mo_board_pieces.card_height
card_width = mo_board_pieces.card_width
cards_in_a_row = 13
total_width = cards_in_a_row*card_width

properties_dict = mo_properties.properties_dict
print("board")
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

        print(properties_dict[1])
        row_1 = Board_row(properties_dict[1])
        self.row_2 = Board_row(properties_dict[2], has_corners=False, rotate=90)
        self.row_3 = Board_row(properties_dict[3], has_corners=False, rotate=270)
        row_4 = Board_row(properties_dict[4])
        print(properties_dict[1])

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

    def __init__(self, row_properties, has_corners=True, rotate=None):
        super().__init__()
        self.rotate = rotate
        self.init_ui(row_properties, has_corners)

    def init_ui(self, row_properties, has_corners):

        self._layout = QtWidgets.QHBoxLayout(self)
        self._layout.setContentsMargins(0, 0, 0, 0)
        self._layout.setSpacing(0)

        self.properties_list = []
        for name, details in row_properties["properties"].items():
            self.generate_next_property(name, details)
        
        self.generate_layout(row_properties["layout"], has_corners)
        

    def generate_next_property(self, name, details):
        color = details["color"]
        value = details["purchase_price"]
        self.properties_list.append(mo_board_pieces.Property_piece(color, name, value)) 

    def get_next_property(self): return self.properties_list.pop(0)

    def generate_layout(self, row_layout, has_corners):
        corner_piece = mo_board_pieces.Corner_piece()

        if has_corners: self._layout.addWidget(corner_piece)
        for i in range(1, 10):
            if i in row_layout:
                print(i)
                self._layout.addWidget(self.get_next_property())
            else:
                # TODO: Change this to include the other pieces, such as tax and the trains
                self._layout.addWidget(mo_board_pieces.Community_chest())
        
        if has_corners: self._layout.addWidget(mo_board_pieces.Corner_piece())
        

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