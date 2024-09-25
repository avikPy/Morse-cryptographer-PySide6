from PySide6.QtWidgets import QMainWindow, QApplication
from PySide6.QtGui import QIcon
from win_morse_Eng import *

class Just(QMainWindow):
    def __init__(self):
        super(Just, self).__init__()
        self.ui = Ui_MorsePro()
        self.ui.setupUi(self)
    
if __name__ == '__main__':
    app = QApplication([])
    win = Just()
    win.setFixedSize(712, 315)
    win.setWindowIcon(QIcon('more_icon.png'))
    win.show()
    app.exec()