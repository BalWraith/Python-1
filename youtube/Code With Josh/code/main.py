##Initial Code Setup:
from random import choice
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QApplication, QWidget,QLabel,QPushButton,QVBoxLayout,QHBoxLayout

from random import choice 

##App Settings
app = QApplication([]) ## This takes an empty list 
main_window = QWidget() ## 
main_window.setWindowTitle("🐍Random Word Maker") ## title of the webpage
main_window.resize(700,500) ## window size


## Create all App Objects
title = QLabel("Random Keywords")

text1 = QLabel("?")
text2 = QLabel("?")
text3 = QLabel("?")
text4 = QLabel() ## row 4
  
button1 = QPushButton("Click me")
button2 = QPushButton("Click me")
button3 = QPushButton("Click me")

## RANDOM WORD CHOICE 
my_words = ['anime','manga','coding','c++','python','javascript','css','html']

##Design our app
##Assigns QVBoxLayout() to the variable master_layout
master_layout = QVBoxLayout()

row1 = QHBoxLayout()
row2 = QHBoxLayout()
row3 = QHBoxLayout()
row4 = QHBoxLayout()

## Adds the title to the center
row1.addWidget(title, alignment=Qt.AlignCenter)

## adds text 1-3 to row 2 and aligns it 
row2.addWidget(text1, alignment=Qt.AlignCenter)
row2.addWidget(text2, alignment=Qt.AlignCenter)
row2.addWidget(text3, alignment=Qt.AlignCenter)

## adds the buttons to row 3
row3.addWidget(button1)
row3.addWidget(button2)
row3.addWidget(button3)

## row 4 bottom spacers
row4.addWidget(text4)
row4.addWidget(text4)
row4.addWidget(text4)


master_layout.addLayout(row1)
master_layout.addLayout(row2)
master_layout.addLayout(row3)

main_window.setLayout(master_layout)

## CREATE FUNCTION
def random_word1():
    word = choice(my_words)
    text1.setText(word)

def random_word2():
    word = choice(my_words)
    text2.setText(word)

def random_word3():
    word = choice(my_words)
    text3.setText(word)

## EVENTS
## gives the buttons functionality when clicked 
button1.clicked.connect(random_word1)
button2.clicked.connect(random_word2)
button3.clicked.connect(random_word3)



## Show/Run our App
main_window.show() ## shows the window
app.exec_() ## starts the app































