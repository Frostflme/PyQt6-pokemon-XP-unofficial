import sys
import controller

import PyQt6.QtCore as QtCore
from PyQt6.QtCore import QSize, Qt
from PyQt6.QtWidgets import (QWidget, QApplication, QMainWindow, QLabel, QPushButton, QVBoxLayout, QHBoxLayout, QSpinBox, QDoubleSpinBox, QCheckBox)

class AveragingWindow(QWidget):
    def __init__(self) -> None:
        super().__init__()

        # Layouts
        loop_layout = QVBoxLayout()
        final_iter_layout = QVBoxLayout()
        average_layout = QVBoxLayout()

        main_pane_loop = QVBoxLayout()
        main_pane_final = QVBoxLayout()
        main_pane_average = QVBoxLayout()

        button_pane_full = QHBoxLayout()
        button_pane_only_exit = QHBoxLayout()
        button_pane_no_average = QHBoxLayout()

        continue_button_pane = QHBoxLayout()
        different_section_button_pane = QHBoxLayout()
        exit_button_pane = QHBoxLayout()

        # Spinbox and DoubleSpinbox
        self.level_spinbox = QSpinBox()
        self.level_spinbox.setMinimum(1)
        self.level_spinbox.setMinimum(100)
        self.level_spinbox.setValue(50)

        self.average_double_spinbox = QDoubleSpinBox()
        self.average_double_spinbox.setMinimum(1)
        self.average_double_spinbox.setMaximum(100)
        self.average_double_spinbox.setValue(50.0)

        # Buttons
        self.continue_button = QPushButton("Continue")
        self.continue_button.clicked.connect(self.average_input_loop)
        self.diff_section_button = QPushButton("I already know the average")
        self.diff_section_button.clicked.connect(self.direct_input_menu)
        self.exit_button = QPushButton("Exit")
        self.exit_button.clicked.connect(self.exit_window)

        # Variables
        self.current_part = "Allies"
        self.loop_number = 1
        self.remaining = -1 # Placeholder value, it won't be that for the final.

        # Labels
        self.description_label = QLabel(f"Input the level of one of the {self.current_part} then hit continue to move on.")
        self.description_average_label = QLabel(f"Input the average level of the {self.current_part}.")
        self.spinbox_label = QLabel(f"Enter the level of {self.current_part} #{self.loop_number}")
        self.status_label = QLabel(f"{self.remaining} left.")
        self.status_label_final = QLabel("This is the final one.")

        # Align the labels
        self.description_label.setAlignment(Qt.AlignmentFlag.AlignHCenter)
        self.spinbox_label.setAlignment(Qt.AlignmentFlag.AlignHCenter)
        self.status_label.setAlignment(Qt.AlignmentFlag.AlignHCenter)
        self.status_label_final.setAlignment(Qt.AlignmentFlag.AlignHCenter)

        # Add buttons to the correct pane
        exit_button_pane.addWidget(self.exit_button)
        different_section_button_pane.addWidget(self.diff_section_button)
        continue_button_pane.addWidget(self.continue_button)

        # Add widgets to main loop
        main_pane_loop.addWidget(self.description_label)
        main_pane_loop.addWidget(self.spinbox_label)
        main_pane_loop.addWidget(self.level_spinbox)
        main_pane_loop.addWidget(self.status_label)

        # Add widgets to main final
        main_pane_final.addWidget(self.description_label)
        main_pane_final.addWidget(self.spinbox_label)
        main_pane_final.addWidget(self.level_spinbox)
        main_pane_final.addWidget(self.status_label_final)

        # Add widgets to main average
        main_pane_average.addWidget(self.description_average_label)
        main_pane_average.addWidget(self.average_double_spinbox)

        # Add layouts to button full
        button_pane_full.addLayout(continue_button_pane)
        button_pane_full.addLayout(different_section_button_pane)
        button_pane_full.addLayout(exit_button_pane)

        # Add layouts to button w/o average
        button_pane_no_average.addLayout(continue_button_pane)
        button_pane_no_average.addLayout(exit_button_pane)

        # Add layouts to button only exit
        button_pane_only_exit.addLayout(exit_button_pane)

        # Finalize three main layouts
        loop_layout.addLayout(main_pane_loop)
        loop_layout.addLayout(button_pane_full)
        
        final_iter_layout.addLayout(main_pane_final)
        final_iter_layout.addLayout(button_pane_full)

        average_layout.addLayout(main_pane_average)
        average_layout.addLayout(button_pane_no_average)

    
    def exit_window(self):
        pass

    def direct_input_menu(self):
        pass

    def average_input_loop(self):
        pass

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
        self.final_results.setAlignment(Qt.AlignmentFlag.AlignHCenter)
        self.in_battle_results_checkbox_label.setAlignment(Qt.AlignmentFlag.AlignHCenter)
        self.evolution_results_checkbox_label.setAlignment(Qt.AlignmentFlag.AlignHCenter)
        self.lucky_egg_results_checkbox_label.setAlignment(Qt.AlignmentFlag.AlignHCenter)

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

        # Add the secondary window as a variable
        average_window = AveragingWindow()


    def calculate_XP(self) -> None:
        """Calculate final XP"""
        # get variables
        input_dict = self.fetch_inputted_variables()
        xp_multiplier = input_dict["XP multiplier"]
        # find results
        final_xp = self.get_final_XP(input_dict["Base XP"], input_dict["Winner's level"], input_dict["Loser's level"], input_dict["Number of allies"], input_dict["Number of enemies"], xp_multiplier, input_dict["Is in battle?"], input_dict["Evolution possible?"], input_dict["Holding lucky egg?"])

        # remove the floating point error during the display of the XP multiplier
        xp_multiplier = round(xp_multiplier, 2)

        # display results
        self.base_XP_results.setText(str(input_dict["Base XP"]))
        self.victorious_level_results.setText(str(input_dict["Winner's level"]))
        self.defeated_level_results.setText(str(input_dict["Loser's level"]))
        self.ally_number_results.setText(str(input_dict["Number of allies"]))
        self.enemy_number_results.setText(str(input_dict["Number of enemies"]))
        self.xp_multiplier_results.setText(str(xp_multiplier))
        self.in_battle_results_checkbox_label.setText(str(input_dict["Is in battle?"]))
        self.evolution_results_checkbox_label.setText(str(input_dict["Evolution possible?"]))
        self.lucky_egg_results_checkbox_label.setText(str(input_dict["Holding lucky egg?"]))
        self.final_results.setText(str(final_xp))

    def fetch_inputted_variables(self) -> dict:
        """Grabs the current inputted variables"""
        input_dictionary = {
            "Base XP": self.base_XP_spinbox.value(),
            "Winner's level": self.victorious_level_spinbox.value(),
            "Loser's level": self.defeated_level_spinbox.value(),
            "Number of allies": self.ally_number_spinbox.value(),
            "Number of enemies": self.enemy_number_spinbox.value(),
            "XP multiplier": self.xp_multiplier_spinbox.value(),
            "Is in battle?": self.in_battle_checkbox.isChecked(),
            "Evolution possible?": self.evolution_checkbox.isChecked(),
            "Holding lucky egg?": self.lucky_egg_checkbox.isChecked()
            }

        return input_dictionary
    
    def get_final_XP(self, base_XP: int, victorious_level: int, defeated_level: int, ally_number: int, enemy_number: int, xp_multiplier: float, in_battle: bool, not_evolved_fully: bool, has_lucky_egg: bool) -> int:
        """Calculates the final XP using all the neccessary variables."""
        # Calculation Part 1
        final_xp = base_XP * defeated_level
        final_xp /= 5

        # Adjusting for being outside of battle
        if in_battle:
            temp1 = 1
        else:
            temp1 = 2
        final_xp *= (1/temp1)

        # Calculation Part 2
        temp1 = 2 * defeated_level
        temp1 += 10
        temp1 = temp1 ** 2.5
        temp2 = defeated_level + victorious_level + 10
        temp2 = temp2 ** 2.5
        temp1 /= temp2
        final_xp *= temp1
        
        final_xp += 1

        # Extra multipliers
        if has_lucky_egg:
            temp1 = 1.5
        else:
            temp1 = 1
        if not_evolved_fully:
            temp2 = 4915/4096
        else:
            temp2 = 1
        final_xp *= temp1 * temp2
        # Adjusting for the number of teammates and enemies
        temp1 = enemy_number ** 1.5
        temp2 = ally_number ** 0.5
        temp1 *= temp2
        temp2 = ally_number ** 2.5
        temp1 /= temp2

        final_xp *= temp1

        # Adjusting for the XP multiplier
        final_xp *= xp_multiplier

        return int(round(final_xp))

    def show_averaging_window(self):
        self.average_window.show()

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