import os

from PySide2 import QtWidgets, QtCore, QtUiTools


class LoadUiFile(QtWidgets.QWidget):

    def __init__(self):
        super(LoadUiFile, self).__init__()

        self.setup_ui()
        self.fill_combo_box()
        self.set_up_signals()

    def setup_ui(self):
        loader = QtUiTools.QUiLoader()
        ui_dir = os.path.dirname(os.path.realpath(__file__))
        ui_filepath = os.path.join(ui_dir, "example.ui")
        ui_file = QtCore.QFile(ui_filepath)
        ui_file.open(QtCore.QFile.ReadOnly)
        self.ui = loader.load(ui_file, self)
        ui_file.close()

    def fill_combo_box(self):
        self.ui.combo_box.addItems(['alpha', 'bravo', 'charlie'])

    def set_up_signals(self):
        self.ui.push_button.clicked.connect(self.print_dropdown_item)

    def print_dropdown_item(self):
        print self.ui.combo_box.currentText()


def start():
    """Start up function."""
    global interface
    interface = LoadUiFile()
    interface.show()


def start_from_main():
    app = QtWidgets.QApplication()
    global interface
    interface = LoadUiFile()
    interface.show()
    app.exec_()


if __name__ == '__main__':
    start_from_main()
