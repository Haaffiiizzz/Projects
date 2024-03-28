import sys
from PyQt6.QtWidgets import *

app = QApplication([])
window = QWidget()
window.setWindowTitle("Calculator App")
window.setGeometry(0, 0, 300, 300)

layout = QHBoxLayout()
layout.addWidget(QPushButton("9"))
layout.addWidget(QPushButton("0"))
layout.addWidget(QPushButton("="))
window.setLayout(layout)


inputSpace = QLineEdit(parent = window)
inputSpace.setFixedSize(300,20)
window.show()
sys.exit(app.exec())