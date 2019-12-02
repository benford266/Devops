import sys
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *


class Gui(QWidget):

    def __init__(self):
        super().__init__()

        self.initUI()

    def initUI(self):

        # Window
        self.setGeometry(300, 300, 300, 220)
        self.setWindowTitle('Capture Port')
        self.center()

        # Widgets
        capture = QPushButton('Capture Ports')
        exitapp = QPushButton('Exit')

        hbox = QHBoxLayout()
        hbox.addStretch(1)
        hbox.addWidget(capture)
        hbox.addWidget(exitapp)

        vbox = QVBoxLayout()
        vbox.addStretch(1)
        vbox.addLayout(hbox)

        self.setLayout(vbox)


        # Run GUI
        self.show()

    # Function to center application on screen.
    def center(self):
        qr = self.frameGeometry()
        cp = QDesktopWidget().availableGeometry().center()
        qr.moveCenter(cp)
        self.move(qr.topLeft())



if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Gui()
    sys.exit(app.exec_())