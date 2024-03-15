import sys
from PySide2.QtWidgets import QApplication, QWidget, QVBoxLayout, QLabel, QLineEdit, QPushButton, QTextEdit

class ShapeMakerApp(QWidget):
    def __init__(self, parameters):
        super().__init__()
        self.parameters = parameters
        self.initUI()

    def initUI(self):
        self.layout = QVBoxLayout()

        self.param_labels = {}
        self.param_lineedits = {}
        self.result_text = QTextEdit()
        self.layout.addWidget(self.result_text)

        # Créer des champs de saisie pour chaque paramètre
        for param_name, param_type in self.parameters.items():
            label = QLabel(f'{param_name}:')
            line_edit = QLineEdit()
            self.param_labels[param_name] = label
            self.param_lineedits[param_name] = line_edit
            self.layout.addWidget(label)
            self.layout.addWidget(line_edit)

        submit_button = QPushButton("Create Shape")
        submit_button.clicked.connect(self.create_shape)
        self.layout.addWidget(submit_button)

        self.setLayout(self.layout)
        self.setWindowTitle('Shape Maker')

    def create_shape(self):
        # Récupérer les valeurs des paramètres depuis les QLineEdit
        input_line = {}
        for param_name, line_edit in self.param_lineedits.items():
            input_line[param_name] = line_edit.text()

        # Afficher le dictionnaire résultant dans le QTextEdit
        self.result_text.clear()
        for param_name, param_value in input_line.items():
            self.result_text.append(f'{param_name}: {param_value}')

if __name__ == '__main__':
    app = QApplication(sys.argv)
            # Définir les paramètres de la forme
    parameters = {
        'name': 'str',
        'point': 'gp_Pnt',
        'sizeX': 'float',
        'sizeY': 'float',
        'sizeZ': 'float',
    }

    ex = ShapeMakerApp(parameters)
    ex.show()
    sys.exit(app.exec_())
