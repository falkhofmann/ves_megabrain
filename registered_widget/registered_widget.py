from PySide2 import QtWidgets

import nuke

class RegisteredWidget(QtWidgets.QWidget):

    def __init__(self):
        super(RegisteredWidget, self).__init__()

        self.build_widgets()
        self.build_layouts()
        self.set_up_signals()

    def build_widgets(self):
        self.copy = QtWidgets.QPushButton('Copy nodes')
        self.paste = QtWidgets.QPushButton('Paste nodes')

    def build_layouts(self):
        layout = QtWidgets.QHBoxLayout()
        layout.addWidget(self.copy)
        layout.addWidget(self.paste)
        self.setLayout(layout)

    def set_up_signals(self):
        self.copy.clicked.connect(self.copy_nodes)
        self.paste.clicked.connect(self.paste_nodes)

    def copy_nodes(self):
        nuke.nodeCopy("%clipboard%")

    def paste_nodes(self):
        nuke.nodePaste("%clipboard%")


def start():
    """Start up function."""
    global interface  # pylint: disable=global-statement
    interface = RegisteredWidget()
    interface.show()


def start_from_main():
    app = QtWidgets.QApplication()
    global interface  # pylint: disable=global-statement
    interface = RegisteredWidget()
    interface.show()
    app.exec_()


if __name__ == '__main__':
    start_from_main()
