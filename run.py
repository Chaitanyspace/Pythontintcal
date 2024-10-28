from PyQt5 import QtWidgets, QtCore
import sys
from datetime import datetime

class TintCalculatorApp(QtWidgets.QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        # Window settings
        self.setWindowTitle("Window Tint Calculator")
        self.setGeometry(100, 100, 850, 600)
        self.setStyleSheet("background-color: #F5F7FA; font-family: Arial;")

        # Layouts
        main_layout = QtWidgets.QVBoxLayout()
        form_layout = QtWidgets.QFormLayout()
        button_layout = QtWidgets.QHBoxLayout()
        table_layout = QtWidgets.QVBoxLayout()

        # Project Name
        self.project_name = QtWidgets.QLineEdit()
        form_layout.addRow("Project Name:", self.project_name)

        # Unit Selector
        self.unit_selector = QtWidgets.QComboBox()
        self.unit_selector.addItems(["cm", "in"])
        form_layout.addRow("Unit:", self.unit_selector)

        # Window Dimensions and Quantity
        self.width_entry = QtWidgets.QLineEdit()
        form_layout.addRow("Window Width:", self.width_entry)

        self.height_entry = QtWidgets.QLineEdit()
        form_layout.addRow("Window Height:", self.height_entry)

        self.quantity_entry = QtWidgets.QLineEdit()
        form_layout.addRow("Quantity:", self.quantity_entry)

        self.rate_entry = QtWidgets.QLineEdit()
        form_layout.addRow("Rate per sqm ($):", self.rate_entry)

        # Add Window Button
        self.add_button = QtWidgets.QPushButton("Add Window")
        self.add_button.clicked.connect(self.add_window)
        self.add_button.setStyleSheet("background-color: #4CAF50; color: white; font-size: 14px; padding: 8px;")
        button_layout.addWidget(self.add_button)

        # Table
        self.window_table = QtWidgets.QTableWidget()
        self.window_table.setColumnCount(7)
        self.window_table.setHorizontalHeaderLabels(["Date", "Time", "Width", "Height", "Quantity", "Area (sqm)", "Cost ($)"])
        self.window_table.horizontalHeader().setStretchLastSection(True)
        self.window_table.setStyleSheet("font-size: 12px;")
        table_layout.addWidget(self.window_table)

        # Result Label
        self.result_label = QtWidgets.QLabel("")
        self.result_label.setStyleSheet("font-size: 14px; color: #4CAF50; font-weight: bold; padding: 10px;")
        table_layout.addWidget(self.result_label)

        # Assemble layout
        main_layout.addLayout(form_layout)
        main_layout.addLayout(button_layout)
        main_layout.addLayout(table_layout)
        self.setLayout(main_layout)

    def add_window(self):
        # Input validation and calculations
        try:
            width = float(self.width_entry.text())
            height = float(self.height_entry.text())
            quantity = int(self.quantity_entry.text())
            rate_per_sqm = float(self.rate_entry.text())
            unit = self.unit_selector.currentText()

            if width <= 0 or height <= 0 or quantity <= 0 or rate_per_sqm <= 0:
                raise ValueError("Dimensions, quantity, and rate must be positive numbers.")

            # Convert inches to centimeters if necessary
            if unit == "in":
                width *= 2.54
                height *= 2.54

            # Calculate area and cost
            area_sqm = (width * height) / 10000 * quantity
            cost = area_sqm * rate_per_sqm

            # Current date and time
            current_date = datetime.now().strftime("%b-%d-%Y")
            current_time = datetime.now().strftime("%I:%M %p")

            # Add data to table
            row_position = self.window_table.rowCount()
            self.window_table.insertRow(row_position)
            self.window_table.setItem(row_position, 0, QtWidgets.QTableWidgetItem(current_date))
            self.window_table.setItem(row_position, 1, QtWidgets.QTableWidgetItem(current_time))
            self.window_table.setItem(row_position, 2, QtWidgets.QTableWidgetItem(f"{width:.2f} {unit}"))
            self.window_table.setItem(row_position, 3, QtWidgets.QTableWidgetItem(f"{height:.2f} {unit}"))
            self.window_table.setItem(row_position, 4, QtWidgets.QTableWidgetItem(str(quantity)))
            self.window_table.setItem(row_position, 5, QtWidgets.QTableWidgetItem(f"{area_sqm:.2f}"))
            self.window_table.setItem(row_position, 6, QtWidgets.QTableWidgetItem(f"${cost:.2f}"))

            # Clear entries
            self.width_entry.clear()
            self.height_entry.clear()
            self.quantity_entry.clear()
            self.rate_entry.clear()
        except ValueError as e:
            error_dialog = QtWidgets.QErrorMessage()
            error_dialog.showMessage(f"Invalid input: {e}")

# Ensure that the QApplication instance is created and the window is shown
if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    window = TintCalculatorApp()
    window.show()
    sys.exit(app.exec_())
