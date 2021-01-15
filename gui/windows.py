import sys
from PyQt5.QtWidgets import *

app = QApplication.instance()
if not app:
    app = QApplication(sys.argv)

    nbclick = 0


def namemethode():
    # GARDE LE RESULTAT DE 1
    # UNE SEULE FOIS
    print("Appuyer")


button_result1 = QPushButton("Un : click")
button_result1.clicked.connect(namemethode)

button_result2 = QPushButton("Deux : ")
button_result3 = QPushButton("Trois : ")
button_result4 = QPushButton("Quatre : ")
button_result5 = QPushButton("Cinq : ")
button_resultSum = QPushButton("Six : ")
button_resultBonus = QPushButton("Bonus : ")
button_resultX3 = QPushButton("X3 : ")
button_resultX4 = QPushButton("X4 : ")
button_resultFULL = QPushButton("Full : ")
button_resultSMALL = QPushButton("Small : ")
button_resultCHANCE = QPushButton("Chance : ")
text_score = QLabel("TOTAL NOM DU JOUEUR : VARIABLE TOTAL")

layout_top = QVBoxLayout()
layout_top.addWidget(button_result1)
layout_top.addWidget(button_result2)
layout_top.addWidget(button_result3)
layout_top.addWidget(button_result4)
layout_top.addWidget(button_result5)
layout_top.addWidget(button_resultSum)
layout_top.addWidget(button_resultBonus)
layout_top.addWidget(button_resultX3)
layout_top.addWidget(button_resultX4)
layout_top.addWidget(button_resultFULL)
layout_top.addWidget(button_resultSMALL)
layout_top.addWidget(button_resultCHANCE)
layout_top.addWidget(text_score)

button_keepD1 = QPushButton("D1")
button_keepD2 = QPushButton("D2")
button_keepD3 = QPushButton("D3")
button_keepD4 = QPushButton("D4")
button_keepD5 = QPushButton("D5")
button_rolls = QPushButton("ROLLS")

layout_bot = QHBoxLayout()
layout_bot.addWidget(button_keepD1)
layout_bot.addWidget(button_keepD2)
layout_bot.addWidget(button_keepD3)
layout_bot.addWidget(button_keepD4)
layout_bot.addWidget(button_keepD5)
layout_bot.addWidget(button_rolls)

main_layout = QVBoxLayout()
main_layout.addLayout(layout_bot)
main_layout.addLayout(layout_top)

windows = QWidget()
windows.setLayout(main_layout)
windows.show()
app.exec_()
