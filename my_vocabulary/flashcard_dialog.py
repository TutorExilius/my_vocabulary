from pathlib import Path
from enum import IntEnum
from functools import partial

from PyQt5 import uic
from PyQt5.QtWidgets import QDialog
from PyQt5.QtWidgets import QApplication

class DirectionState(IntEnum):
    LEFT = 0  # value will be used as index
    RIGHT = 1  # value will be used as index
    BIDIRECTIONAL = 2  # value will be used as index

class FlashCardDialog(QDialog):
    def __init__(self) -> None:
        """Initialise the MainWindow widget."""

        super().__init__()
        uic.loadUi(Path(__file__).parent / "ui" / "flashcard_dialog.ui", self)
        self.clearFocus()

        self.frame_continuebuttons.setVisible(False)
        self.pushButton_play_right.setVisible(False)

        # connections
        self.pushButton_show_language_right.clicked.connect(self.show_button_clicked)
        self.pushButton_correct_language_right.clicked.connect(self.correct_button_clicked)
        self.pushButton_wrong_language_right.clicked.connect(self.wrong_button_clicked)
        #self.pushButton_play_left.clicked.connect(partial(self.update_buttonstate, with_state_change=True))

        self.pushButton_play_left.direction = DirectionState.BIDIRECTIONAL
        #self.update_buttonstate(with_state_change=False)


    def update_buttonstate(self, _=False, with_state_change=True):
        if with_state_change:
            states = list(DirectionState)
            self.pushButton_play_left.direction = states[self.pushButton_play_left.direction.value - 1]

        if self.pushButton_play_left.direction == DirectionState.LEFT:
            self.pushButton_play_left.setText("←")
        elif self.pushButton_play_left.direction == DirectionState.RIGHT:
            self.pushButton_play_left.setText("→")
        else:
            self.pushButton_play_left.setText("↔")


    def show_button_clicked(self):
        self.frame_continuebuttons.setVisible(True)
        self.pushButton_show_language_right.setVisible(False)
        self.pushButton_play_right.setVisible(True)
        self.pushButton_correct_language_right.clearFocus()

    def correct_button_clicked(self):
        self.close()

    def wrong_button_clicked(self):
        self.close()


