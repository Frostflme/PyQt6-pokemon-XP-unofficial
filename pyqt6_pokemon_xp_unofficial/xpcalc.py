import sys
import controller

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
        self.in_battle_checkbox = QCheckBox("Are they in the battle?")
        self.in_battle_checkbox.setCheckState(Qt.CheckState.Checked)
        self.evolution_checkbox = QCheckBox("Are they a higher level than it takes to evolve?")
        self.lucky_egg_checkbox = QCheckBox("Are they holding a lucky egg?")

        # Spinboxes
        self.base_XP_spinbox = QSpinBox()
        self.base_XP_spinbox.setMinimum(0)
        self.base_XP_spinbox.setMaximum(1023)
        self.base_XP_spinbox.setValue(70)
        self.victorious_level_spinbox = QSpinBox()
        self.victorious_level_spinbox.setMinimum(1)
        self.victorious_level_spinbox.setMaximum(100)
        self.victorious_level_spinbox.setValue(50)
        self.defeated_level_spinbox = QSpinBox()
        self.defeated_level_spinbox.setMinimum(1)
        self.defeated_level_spinbox.setMaximum(100)
        self.defeated_level_spinbox.setValue(50)
        self.ally_number_spinbox = QSpinBox()
        self.ally_number_spinbox.setMinimum(1)
        self.ally_number_spinbox.setMaximum(2147483647)
        self.enemy_number_spinbox = QSpinBox()
        self.enemy_number_spinbox.setMinimum(1)
        self.enemy_number_spinbox.setMaximum(2147483647)
        self.xp_multiplier_spinbox = QDoubleSpinBox()
        self.xp_multiplier_spinbox.setMinimum(0)
        self.xp_multiplier_spinbox.setMaximum(float(10**308))
        self.xp_multiplier_spinbox.setSingleStep(0.05)
        self.xp_multiplier_spinbox.setValue(1)

        # Results button
        self.button_results = QPushButton("Calculate results!")
        self.button_results.clicked.connect(self.calculate_XP)

        # Widget labels
        base_XP_label = QLabel("How much base XP does the defeated Pokémon give?")
        victorious_level_label = QLabel("What's the level of the Pokémon being given XP?")
        defeated_level_label = QLabel("What's the level of the defeated Pokémon?")
        ally_number_label = QLabel("How many Pokémon are on the team being given XP?")
        enemy_number_label = QLabel("How many Pokémon are on the same team as the defeated Pokémon?")
        xp_multiplier_label = QLabel("What are you multiplying the total XP by?")

        # Results labels
        base_XP_results_label = QLabel("Base XP")
        self.base_XP_results = QLabel("N/A")
        victorious_level_results_label = QLabel("Level (Self)")
        self.victorious_level_results = QLabel("N/A")
        defeated_level_results_label = QLabel("Level (Enemy)")
        self.defeated_level_results = QLabel("N/A")
        ally_number_results_label = QLabel("Ally Number")
        self.ally_number_results = QLabel("N/A")
        enemy_number_results_label = QLabel("Enemy Number")
        self.enemy_number_results = QLabel("N/A")
        xp_multiplier_results_label = QLabel("XP Multiplier")
        self.xp_multiplier_results = QLabel("N/A")
        in_battle_results_label = QLabel("Battling")
        self.in_battle_results_checkbox_label = QLabel("N/A")
        evolution_results_label = QLabel("Post-evolution")
        self.evolution_results_checkbox_label = QLabel("N/A")
        lucky_egg_results_label = QLabel("Lucky Egg")
        self.lucky_egg_results_checkbox_label = QLabel("N/A")
        final_results_label = QLabel("Final Results")
        self.final_results = QLabel("")

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
        
        self.base_XP_results.setAlignment(Qt.AlignmentFlag.AlignHCenter)
        base_XP_results_label.setAlignment(Qt.AlignmentFlag.AlignHCenter)
        self.victorious_level_results.setAlignment(Qt.AlignmentFlag.AlignHCenter)
        victorious_level_results_label.setAlignment(Qt.AlignmentFlag.AlignHCenter)
        self.defeated_level_results.setAlignment(Qt.AlignmentFlag.AlignHCenter)
        defeated_level_results_label.setAlignment(Qt.AlignmentFlag.AlignHCenter)
        self.ally_number_results.setAlignment(Qt.AlignmentFlag.AlignHCenter)
        ally_number_results_label.setAlignment(Qt.AlignmentFlag.AlignHCenter)
        self.enemy_number_results.setAlignment(Qt.AlignmentFlag.AlignHCenter)
        enemy_number_results_label.setAlignment(Qt.AlignmentFlag.AlignHCenter)
        self.xp_multiplier_results.setAlignment(Qt.AlignmentFlag.AlignHCenter)
        xp_multiplier_results_label.setAlignment(Qt.AlignmentFlag.AlignHCenter)
        in_battle_results_label.setAlignment(Qt.AlignmentFlag.AlignHCenter)
        evolution_results_label.setAlignment(Qt.AlignmentFlag.AlignHCenter)
        lucky_egg_results_label.setAlignment(Qt.AlignmentFlag.AlignHCenter)
        final_results_label.setAlignment(Qt.AlignmentFlag.AlignHCenter)
        self.in_battle_results_checkbox_label.setAlignment(Qt.AlignmentFlag.AlignHCenter)
        self.evolution_results_checkbox_label.setAlignment(Qt.AlignmentFlag.AlignHCenter)
        self.lucky_egg_results_checkbox_label.setAlignment(Qt.AlignmentFlag.AlignHCenter)

        # TODO: Center checkboxes 

        # Add out left pane widgets
        left_pane.addWidget(title_label)
        
        left_pane.addWidget(xp_multiplier_label)
        left_pane.addWidget(self.xp_multiplier_spinbox)
        left_pane.addWidget(base_XP_label)
        left_pane.addWidget(self.base_XP_spinbox)
        left_pane.addWidget(victorious_level_label)
        left_pane.addWidget(self.victorious_level_spinbox)
        left_pane.addWidget(defeated_level_label)
        left_pane.addWidget(self.defeated_level_spinbox)
        left_pane.addWidget(ally_number_label)
        left_pane.addWidget(self.ally_number_spinbox)
        left_pane.addWidget(enemy_number_label)
        left_pane.addWidget(self.enemy_number_spinbox)
        left_pane.addWidget(self.in_battle_checkbox)
        left_pane.addWidget(self.evolution_checkbox)
        left_pane.addWidget(self.lucky_egg_checkbox)
        left_pane.addWidget(self.button_results)
        
        # Add our right pane widgets
        right_pane.addWidget(results_label)

        right_pane.addWidget(xp_multiplier_results_label)
        right_pane.addWidget(self.xp_multiplier_results)
        right_pane.addWidget(base_XP_results_label)
        right_pane.addWidget(self.base_XP_results)
        right_pane.addWidget(victorious_level_results_label)
        right_pane.addWidget(self.victorious_level_results)
        right_pane.addWidget(defeated_level_results_label)
        right_pane.addWidget(self.defeated_level_results)
        right_pane.addWidget(ally_number_results_label)
        right_pane.addWidget(self.ally_number_results)
        right_pane.addWidget(enemy_number_results_label)
        right_pane.addWidget(self.enemy_number_results)
        right_pane.addWidget(in_battle_results_label)
        right_pane.addWidget(self.in_battle_results_checkbox_label)
        right_pane.addWidget(evolution_results_label)
        right_pane.addWidget(self.evolution_results_checkbox_label)
        right_pane.addWidget(lucky_egg_results_label)
        right_pane.addWidget(self.lucky_egg_results_checkbox_label)
        right_pane.addWidget(final_results_label)
        right_pane.addWidget(self.final_results)

        # Add the two panes to the layout
        main_layout.addLayout(left_pane)
        main_layout.addLayout(right_pane)

        widget = QWidget()
        widget.setLayout(main_layout)
        self.setCentralWidget(widget)

    def calculate_XP(self):
        """Calculate final XP"""
        # get variables
        base_XP = self.base_XP_spinbox.value()
        victorious_level = self.victorious_level_spinbox.value()
        defeated_level = self.defeated_level_spinbox.value()
        ally_number = self.ally_number_spinbox.value()
        enemy_number = self.enemy_number_spinbox.value()
        xp_multiplier = self.xp_multiplier_spinbox.value()
        in_battle = self.in_battle_checkbox.isChecked()
        not_evolved_fully = self.evolution_checkbox.isChecked()
        has_lucky_egg = self.lucky_egg_checkbox.isChecked()

        # find results
        final_xp = controller.calculateXP(base_XP, victorious_level, defeated_level, ally_number, enemy_number, xp_multiplier, in_battle, not_evolved_fully, has_lucky_egg)

        # display results
        self.base_XP_results.setText(str(base_XP))
        self.victorious_level_results.setText(str(victorious_level))
        self.defeated_level_results.setText(str(defeated_level))
        self.ally_number_results.setText(str(ally_number))
        self.enemy_number_results.setText(str(enemy_number))
        self.xp_multiplier_results.setText(str(xp_multiplier))
        self.in_battle_results_checkbox_label.setText(str(in_battle))
        self.evolution_results_checkbox_label.setText(str(not_evolved_fully))
        self.lucky_egg_results_checkbox_label.setText(str(has_lucky_egg))
        self.final_results.setText(str(final_xp))

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
#     app.setStyleSheet("""
#     QWidget {
#         background-color: "green";
#         color: "white";
#     }
#     QPushButton {
#         font-size: 16px;
#         background-color: "darkgreen"
#     }
#     QLineEdit {
#         background-color: "white";
#         color: "black";
#     }
# """)
    app.exec()

    ### finished with video ###