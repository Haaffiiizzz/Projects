import urllib3
import io
import sys
from PyQt6.QtWidgets import * 
from PyQt6.QtCore import QTimer

def getInput(website, name, window):
   
    url = website.text()
    name = name.text() + ".html" if name.text() else "index.html"
    try:
        web = urllib3.request("GET", url, preload_content= False)
        web.auto_close = False
    except Exception:
        label = QLabel("Sorry. Can't get the HTML file for that site.", parent = window)
        label.setGeometry(70, 30, 300, 60)
        label.show()
        QTimer.singleShot(5000, window.close)
    else:
        with open(name, "w") as file:
            for line in io.TextIOWrapper(web):
                file.write(line)
        label = QLabel("HTML file generated!", parent = window)
        label.setGeometry(70, 30, 300, 60)     
        label.show()
        QTimer.singleShot(5000, window.close)

def main():
    app = QApplication([])
    window = QWidget()
    window.setWindowTitle("HTML FILE GENERATOR")
    window.setGeometry(0, 0, 300, 300)

    websiteSpace = QLineEdit(parent = window,)
    websiteSpace.setFixedSize(300,20)
    websiteSpace.setPlaceholderText("Type in the website!")
    websiteSpace.setGeometry(0, 100, 300, 20)

    nameSpace = QLineEdit(parent = window,)
    nameSpace.setFixedSize(300,20)
    nameSpace.setPlaceholderText("Type in the name of the file!")
    nameSpace.setGeometry(0, 120, 300, 20)

    submit = QPushButton("Generate", parent = window)
    submit.setGeometry(110, 150, 60, 30)
    submit.clicked.connect(lambda: getInput(websiteSpace, nameSpace, window))
    
    window.show()
    sys.exit(app.exec())

if __name__ == "__main__":
    main()
