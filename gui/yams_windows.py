import sys
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QVBoxLayout


app = QApplication.instance()
if not app:
    app = QApplication(sys.argv)

w = QWidget()
b1 = QPushButton("mon 1 bouton dans un QVBoxLayout")
b2 = QPushButton("mon 2 bouton dans un QVBoxLayout")
layout = QVBoxLayout()
# ajout du premier bouton au gestionnaire de mise en forme
layout.addWidget(b1)
layout.addWidget(b2)
w.setLayout(layout)


w.setWindowTitle("Yams")
w.resize(700, 750)
w.show()

app.exec_()
