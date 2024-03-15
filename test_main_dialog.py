import sys
from PySide2.QtWidgets import QApplication, QMainWindow, QVBoxLayout, QLabel, QLineEdit, QPushButton, QTextEdit, QDialog, QVBoxLayout

class ShapeMakerDialog(QDialog):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.setWindowTitle('Shape Maker Dialog')
        layout = QVBoxLayout()

        self.name_input = QLineEdit()
        layout.addWidget(QLabel('Name:'))
        layout.addWidget(self.name_input)

        self.create_button = QPushButton('Create Shape')
        layout.addWidget(self.create_button)

        self.setLayout(layout)

    def get_name(self):
        return self.name_input.text()

class MyMainWindow(QMainWindow):
    def __init__(self):
        super().__init()

        self.initUI()

    def initUI(self):
        self.setGeometry(100, 100, 800, 600)
        self.setWindowTitle('My Main Window')

        button = QPushButton('Open Shape Maker Dialog')
        button.clicked.connect(self.open_shape_maker_dialog)
        self.setCentralWidget(button)

    def open_shape_maker_dialog(self):
        dialog = ShapeMakerDialog()
        result = dialog.exec_()

        if result == QDialog.Accepted:
            name = dialog.get_name()
            print(f'Name entered: {name}')

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = MyMainWindow()
    ex.show()
    sys.exit(app.exec_())
