import sys

import PyQt6.QtCore as QtCore
from PyQt6.QtCore import QSize, Qt
from PyQt6.QtWidgets import (QWidget, QApplication, QMainWindow, QLabel, QPushButton, QVBoxLayout, QHBoxLayout, QSpinBox, QDoubleSpinBox, QCheckBox)

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

        # Checkboxes
        in_battle_checkbox = QCheckBox("Are they in the battle?")
        evolution_checkbox = QCheckBox("Are they a higher level than it takes to evolve?")
        lucky_egg_checkbox = QCheckBox("Are they holding a lucky egg?")

        # Spinboxes
        base_XP_spinbox = QSpinBox()
        victorious_level_spinbox = QSpinBox()
        defeated_level_spinbox = QSpinBox()
        ally_number_spinbox = QSpinBox()
        enemy_number_spinbox = QSpinBox()
        xp_multiplier_spinbox = QDoubleSpinBox()

        # Results button
        button_results = QPushButton("Calculate results!")

        # Set the font
        h1_font = title_label.font()
        h1_font.setPointSize(30)
        title_label.setFont(h1_font)

        # Results Label
        results_label = QLabel("Results")
        h2_font = results_label.font()
        h2_font.setPointSize(26)
        results_label.setFont(h2_font)

        # Align the label
        title_label.setAlignment(Qt.AlignmentFlag.AlignHCenter |
                                 Qt.AlignmentFlag.AlignTop)
        
        results_label.setAlignment(Qt.AlignmentFlag.AlignHCenter |
                                 Qt.AlignmentFlag.AlignTop)
        
        # Add out left pane widgets
        left_pane.addWidget(title_label)
        
        # Add our right pane widgets
        right_pane.addWidget(results_label)

        # Add the two panes to the layout
        main_layout.addLayout(left_pane)
        main_layout.addLayout(right_pane)

        widget = QWidget()
        widget.setLayout(main_layout)
        self.setCentralWidget(widget)

app = QApplication(sys.argv)

window = MainWindow()
window.show()

app.exec()