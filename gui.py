from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from core import Core


class MainWindow(QMainWindow):
    def __init__(self, parent = None):
        super().__init__(parent)
        self.init_gui()

    def init_gui(self):
        self.window = QWidget()
        self.layout = QGridLayout()
        #self.layout.setHorizontalSpacing(0)
        #self.layout.setVerticalSpacing(0)
        self.setCentralWidget(self.window)
        self.window.setLayout(self.layout)

def game_page(win, game):
    btn1.hide(), btn2.hide()
    win.resize(1000, 500)
    label.setText("Guess the word!")
    word_label(win, game)
    guessed_letters(win, game)
    lives_setup(win, game)
    center(win)
    win.setWindowTitle('Hangman')

def lives_setup(win, game):
    lives = QLabel()
    lives.setText(f"Lives remaining: {game.lives}")
    lives.setFont(QFont("Arial font", 15))
    win.layout.addWidget(lives, 3, 0, 1, 2)
    lives.show()

def word_label(win, game):
    wrd = QLabel()
    sp = int((15 - len(game.progress))/2)
    print (sp)
    str = ("  " * sp) + game.progress
    wrd.setText(str)
    wrd.setFont(QFont("Arial font", 30))
    win.layout.addWidget(wrd, 2, 1, 1, 2)
    wrd.show()

def guessed_letters(win, game):
    gsd = QLabel()
    gsd.setText("Guessed:")
    gsd.setFont(QFont("Arial font", 15))
    win.layout.addWidget(gsd, 3, 2, 1, 1)
    gsd.show()

def center(win):
    frameGm = win.frameGeometry()
    screen = QApplication.desktop().screenNumber(QApplication.desktop().cursor().pos())
    centerPoint = QApplication.desktop().screenGeometry(screen).center()
    frameGm.moveCenter(centerPoint)
    win.move(frameGm.topLeft())

if __name__== '__main__':
    app = QApplication([])
    game = Core()
    win = MainWindow()
    win.resize(300, 180)
    win.setWindowTitle('Hangman')

    label = QLabel()
    label.setText("Hangman")
    label.setFont(QFont('Arial font', 30))
    win.layout.addWidget(label, 1, 1, 1, 2)
    label.show()

    btn1 = QPushButton()
    btn1.setText("Play")
    btn1.setFont(QFont('Arial font', 18))
    win.layout.addWidget(btn1)
    btn1.show()
    btn1.clicked.connect(lambda: game_page(win, game))

    btn2 = QPushButton()
    btn2.setText("Exit")
    btn2.setFont(QFont('Arial font', 18))
    win.layout.addWidget(btn2)
    btn2.show()
    btn2.clicked.connect(win.close)

    win.show()

    app.exec_()
