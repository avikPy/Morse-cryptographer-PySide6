from PySide6.QtWidgets import QMainWindow, QApplication
from PySide6.QtGui import QIcon
from win_morze_Ru import *

class Just(QMainWindow):
    def __init__(self):
        super(Just, self).__init__()
        self.ui = Ui_MorsePro()
        self.ui.setupUi(self)
    
if __name__ == '__main__':
    app = QApplication([])
    win = Just()
    win.setFixedSize(712, 315)
    win.setWindowIcon(QIcon('icon_lock.png'))
    win.show()
    app.exec()