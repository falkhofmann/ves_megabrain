from PySide2 import QtWidgets, QtCore


class BasicWidget(QtWidgets.QWidget):

    def __init__(self):
        super(BasicWidget, self).__init__()

        self.build_widgets()
        self.build_layouts()
        self.set_window_properties()
        self.set_up_signals()

    def set_window_properties(self):
        self.setMinimumSize(400, 500)
        self.setWindowFlags(QtCore.Qt.WindowStaysOnTopHint)
        self.setWindowTitle('Basic widget example')

    def build_widgets(self):
        self.button_a = QtWidgets.QPushButton()
        self.button_a.setFixedSize(100, 20)
        self.button_a.setText('Blue')

        self.button_b = QtWidgets.QPushButton()
        self.button_b.setFixedSize(100, 20)
        self.button_b.setText('Clear')

    def build_layouts(self):
        layout = QtWidgets.QVBoxLayout()
        self.setLayout(layout)

        button_layout = QtWidgets.QHBoxLayout()
        button_layout.addWidget(self.button_a)
        button_layout.addWidget(self.button_b)

        layout.addLayout(button_layout)

    def set_up_signals(self):
        self.button_a.clicked.connect(self.set_stylesheet)
        self.button_b.clicked.connect(self.clear_stylesheet)

    def set_stylesheet(self):
        self.setStyleSheet('background: blue')

    def clear_stylesheet(self):
        self.setStyleSheet('')


def start():
    """Start up function from nuke."""
    global widget
    widget = BasicWidget()
    widget.show()


def start_from_main():
    """Start up function from within IDE."""
    app = QtWidgets.QApplication()
    global widget
    widget = BasicWidget()
    widget.show()
    app.exec_()


if __name__ == '__main__':
    start_from_main()
