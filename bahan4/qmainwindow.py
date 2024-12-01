# Menggunakan QmainWindow
from PyQt5.QtWidgets import QApplication, QPushButton, QLabel, QMainWindow

app = QApplication([])

window = QMainWindow()

# label = QLabel("Label1", window) # cara1
label = QLabel(window)             # cara2
label.setText("Label1")
label.move(200,0)

# label = QPushButton("Button1", window) # cara1
button = QPushButton(window)             # cara2
button.setText("Button1")

window.show()
app.exec_()