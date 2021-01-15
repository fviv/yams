import sys
from PyQt5.QtWidgets import *
# from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QVBoxLayout


app = QApplication.instance()
if not app:
    app = QApplication(sys.argv)


def rolls_dice():
    print("Appui sur le bouton rolls dice")


def keep_dice():
    print("Appui sur le bouton rolls dice")


def note_result():
    print("Appui sur le bouton rolls dice")


text_who_play = QLabel()
text_score = QLabel()
text_who_play.setText("Variable Nom du joueur")
text_score.setText("Total score")

windows_yams = QWidget()
windows_yams.setWindowTitle("Yams")
windows_yams.resize(700, 750)


button_rolls = QPushButton("ROLLS DICES")
button_result = QPushButton("NOTE THIS RESULT")

button_keepD1 = QPushButton("D1")
button_keepD2 = QPushButton("D2")
button_keepD3 = QPushButton("D3")
button_keepD4 = QPushButton("D4")
button_keepD5 = QPushButton("D5")

button_rolls.clicked.connect(rolls_dice)
button_result.clicked.connect(note_result)

button_keepD1.clicked.connect(keep_dice)
button_keepD2.clicked.connect(keep_dice)
button_keepD3.clicked.connect(keep_dice)
button_keepD4.clicked.connect(keep_dice)
button_keepD5.clicked.connect(keep_dice)


layout_D = QHBoxLayout()
layout_D.addWidget(button_keepD1)
layout_D.addWidget(button_keepD2)
layout_D.addWidget(button_keepD3)
layout_D.addWidget(button_keepD4)
layout_D.addWidget(button_keepD5)

layout_windows = QVBoxLayout()
layout_windows.addWidget(text_score)
layout_windows.addWidget(button_result)
layout_windows.addWidget(button_rolls)

Style = """
QPushButton{
    background-color:red;
    width:50;
    height:10;
}
"""
layout_grille = QGridLayout()
# layout_grille.addChildLayout(layout_windows)
layout_grille.addWidget(button_keepD3)
layout_grille.addWidget(button_keepD2)
layout_grille.addWidget(button_keepD4)
layout_grille.addWidget(button_keepD5)
# layout_grille.setGeometry(300, 300, 500, 250)


windows_yams.setLayout(layout_grille)
windows_yams.show()

app.setStyleSheet(Style)
app.exec_()
