import sys

import matplotlib.pyplot as plt
import numpy as np
import sympy as sp
import Validation
from PySide2.QtCore import QSize
from PySide2.QtGui import QIcon, QFont
from PySide2.QtWidgets import QApplication, QMainWindow, QWidget, QVBoxLayout, QLabel, QLineEdit, \
    QPushButton, QMessageBox
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas


class FunctionPlotter(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Function Plotter")
        self.set_icon()
        self.set_ui()

    def set_icon(self):
        app_icon = QIcon("favicon.png")
        self.setWindowIcon(app_icon)

    def set_ui(self):
        self.central_widget = QWidget()
        self.setCentralWidget(self.central_widget)

        self.layout = QVBoxLayout()
        self.setGeometry(750, 250, 600, 700)

        self.label_func = QLabel("Enter the function of x:")
        self.label_func.setFont(QFont("Sanserif", 10))
        self.edit_func = QLineEdit()
        self.layout.addWidget(self.label_func)
        self.layout.addWidget(self.edit_func)

        self.label_min = QLabel("Enter the minimum value of x:")
        self.edit_min = QLineEdit()
        self.layout.addWidget(self.label_min)
        self.layout.addWidget(self.edit_min)
        self.label_min.setFont(QFont("Sanserif", 10))

        self.label_max = QLabel("Enter the maximum value of x:")
        self.edit_max = QLineEdit()
        self.layout.addWidget(self.label_max)
        self.layout.addWidget(self.edit_max)
        self.label_max.setFont(QFont("Sanserif", 10))

        self.plot_button = QPushButton("Plot")
        self.plot_button.clicked.connect(self.draw_function)
        self.layout.addWidget(self.plot_button)
        self.plot_button.setFixedSize(QSize(200, 30))

        self.figure = plt.figure()
        self.canvas = FigureCanvas(self.figure)
        self.layout.addWidget(self.canvas)

        self.central_widget.setLayout(self.layout)

    def draw_function(self):
        try:
            function = self.edit_func.text()
            x_min = float(self.edit_min.text())
            x_max = float(self.edit_max.text())

            # Input validation: Check if the function contains invalid characters
            Validation.validate_function_characters(function)
            # Input validation: Check if the minimum > maximum
            Validation.validate_min_max(x_min, x_max)

            x = sp.Symbol('x')
            user_function = sp.sympify(function)

            # set the x and y values
            x_values = np.linspace(x_min, x_max)
            y_values = [user_function.subs(x, val) for val in x_values]

            # draw the function using Matplotlib
            self.figure.clear()
            self.figure.add_subplot(111).plot(x_values, y_values)
            self.canvas.draw()

        except ValueError as ve:
            QMessageBox.critical(self, "Error", f"Error: {str(ve)}", QMessageBox.Ok)
        except Exception as e:
            QMessageBox.critical(self, "Error", f"Error: {str(e)}", QMessageBox.Ok)


def main():
    app = QApplication(sys.argv)
    window = FunctionPlotter()
    window.show()
    sys.exit(app.exec_())


if __name__ == "__main__":
    main()
