from PySide6 import QtWidgets, QtGui
from my_monopoly.mo_ui import mo_board_pieces, mo_properties


card_height = mo_board_pieces.card_height
card_width = mo_board_pieces.card_width
cards_in_a_row = 13
total_width = cards_in_a_row*card_width

properties_dict = mo_properties.properties_dict

# TODO: implement a queue system to take the board information from a json/list of tuples
# TODO: Add a dictionary (id: object) system to link the model and gui

class Board(QtWidgets.QWidget):

    def __init__(self):
        super().__init__()
        self.init_ui()

    def init_ui(self):
        self.graphicsview = QtWidgets.QGraphicsView()
        self.scene = QtWidgets.QGraphicsScene(self.graphicsview)
        self.graphicsview.setScene(self.scene)
        self.scene.setSceneRect(0, 0, total_width, total_width)

        layout = QtWidgets.QVBoxLayout(self)
        layout.setContentsMargins(0, 0, 0, 0)
        layout.setSpacing(0)

        h_layout = QtWidgets.QHBoxLayout()
        h_layout.setContentsMargins(0, 0, 0, 0)
        h_layout.setSpacing(0)

        pos = (0, 0) #(total_width, card_height)
        self.row_1 = Board_row(properties_dict[2], rotate=180, pos=pos)
        
        pos = ((card_width * 7.5) - 11 * card_width, card_width * 5.5)
        self.row_2 = Board_row(properties_dict[4], has_corners=False, rotate=90, pos=pos)
        
        pos = (card_width*7.5, card_width * 5.5)
        self.row_3 = Board_row(properties_dict[3], has_corners=False, rotate=270, pos=pos)
        
        pos = (0, 11 * card_width)
        self.row_4 = Board_row(properties_dict[1], pos=pos)

        self.add_rows()

        layout.addWidget(self.graphicsview)

    def add_rows(self):
        self.scene.clear()
        
        self.scene.addItem(self.create_row(self.row_1))
        self.scene.addItem(self.create_row(self.row_2))
        self.scene.addItem(self.create_row(self.row_3))
        self.scene.addItem(self.create_row(self.row_4))

    def create_row(self, row_widget):
        proxy = QtWidgets.QGraphicsProxyWidget()
        proxy.setWidget(row_widget)
        proxy.setTransformOriginPoint(proxy.boundingRect().center())
        proxy.setPos(*row_widget.get_pos())
        rotation = row_widget.get_rotation()
        if not rotation is None:
            print(row_widget, rotation)
            proxy.setRotation(rotation)

        return proxy
    
    def rotate_board(self, angle=90):
        self.graphicsview.rotate(angle)

class Board_row(QtWidgets.QWidget):

    def __init__(self, row_properties, has_corners=True, rotate=None, pos=(0, 0)):
        super().__init__()
        self.rotate = rotate
        self._pos = pos
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
                self._layout.addWidget(self.get_next_property())
            else:
                # TODO: Change this to include the other pieces, such as tax and the trains
                self._layout.addWidget(mo_board_pieces.Community_chest())
        
        if has_corners: self._layout.addWidget(mo_board_pieces.Corner_piece())

    def get_rotation(self): return self.rotate
    def get_pos(self): return self._pos
        
