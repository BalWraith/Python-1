##Initial Code Setup:
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QApplication, QWidget,QLabel,QPushButton,QVBoxLayout,QHBoxLayout

##App Settings
app = QApplication([]) ## This takes an empty list 
main_window = QWidget() ## 
main_window.setWindowTitle("🐍Random Word Maker") ## title of the webpage
main_window.resize(300,200) ## window size

##Create all Object/Widgets below here

main_window.show() ## shows the window
app.exec_() ## starts the app
    


















