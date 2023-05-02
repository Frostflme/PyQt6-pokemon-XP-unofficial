import sys

import PyQt6.QtCore as QtCore
from PyQt6.QtCore import QSize, Qt
from PyQt6.QtWidgets import (QWidget, QApplication, QMainWindow, QLabel, QPushButton, QVBoxLayout, QHBoxLayout, QSpinBox, QDoubleSpinBox)

class MainWindow(QMainWindow):

    def __init__(self):
        super(MainWindow, self).__init__()

        self.setWindowTitle("Pokémon XP Calculator App")

        # Create our Layouts
        main_layout = QHBoxLayout()

        # Create 2 columns (each a VBox)
        left_pane = QVBoxLayout()
        right_pane = QVBoxLayout()

        # Title label
        title_label = QLabel("Pokémon XP Calculator")

        # Set the font
        h1_font = title_label.font()
        h1_font.setPointSize(30)
        title_label.setFont(h1_font)

        # Results Label
        results_label = QLabel("Results")
        h2_font = results_label.font()
        h2_font.setPointSize(26)
        results_label.setFont(h2_font)

        # Align the lavel
        title_label.setAlignment(Qt.AlignmentFlag.AlignHCenter |
                                 Qt.AlignmentFlag.AlignTop)
        
        # Add out left pane widgets
        left_pane.addWidget(title_label)
        
        # Add our right pane widgets
        right_pane.addWidget(results_label)

        # Add the two panes to the layout
        main_layout.addLayout(left_pane)
        main_layout.addLayout(right_pane)