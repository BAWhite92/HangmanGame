from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
import core


class MainWindow(QMainWindow):
    def __init__(self, parent = None):
        super().__init__(parent)
        self.init_gui()

    def init_gui(self):
        self.window = QWidget()
        self.layout = QGridLayout()
        self.layout.setHorizontalSpacing(1)
        self.layout.setVerticalSpacing(1)
        self.layout.setColumnMinimumWidth(1, 0)
        self.layout.setColumnMinimumWidth(3, 0)
        self.setCentralWidget(self.window)
        self.window.setLayout(self.layout)

class Game():

    def game_page(self, win, game):
        btn1.hide(), btn2.hide(), label.hide()
        win.resize(1000, 500)
        gameLabel = QLabel()
        gameLabel.setText("Guess the word!")
        gameLabel.setFont(QFont('Arial font', 14))
        win.layout.addWidget(gameLabel, 0, 2)
        txt = QLineEdit("Your Letter")
        win.layout.addWidget(txt, 1, 2, 1, 1)
        btn = QPushButton()
        btn.setText("Enter")
        btn.setFont(QFont('Arial font', 14))
        btn.show()
        btn.clicked.connect(lambda: self.make_guess(win, game, txt.text()))
        win.layout.addWidget(btn, 2, 2, 1 ,1)
        self.word_label(win, game)
        self.guessed_letters(win, game)
        self.lives_setup(win, game)
        self.center(win)
        win.setWindowTitle('Hangman')

    def lives_setup(self, win, game):
        self.lives = QLabel()
        self.lives.setText(f"Lives remaining: {game.lives}")
        self.lives.setFont(QFont("Arial font", 15))
        win.layout.addWidget(self.lives, 4, 0, 1, 2)
        self.lives.show()

    def word_label(self, win, game):
        self.wrd = QLabel()
        sp = int((15 - len(game.progress))/2)
        print (sp)
        str = ("  " * sp) + game.progress
        self.wrd.setText(str)
        self.wrd.setFont(QFont("Arial font", 30))
        win.layout.addWidget(self.wrd, 3, 2, 1, 2)
        self.wrd.show()

    def guessed_letters(self, win, game):
        self.gsd = QLabel()
        self.gsd.setText("Guessed:")
        self.gsd.setFont(QFont("Arial font", 15))
        win.layout.addWidget(self.gsd, 4, 4, 1, 1)
        self.gsd.show()

    def make_guess(self, win, game, letter):
        self.update_progress(letter, game, win)
        self.update_guessed(letter, game, win)
        if game.won():
            self.success_screen()

    def update_guessed(self, letter, game, win):
        self.gsd.setText(f"Guessed: {game.guessed}")

    def update_progress(self, letter, game, win):
        if game.letter_guess(letter):
            sp = int((15 - len(game.progress))/2)
            str = ("  " * sp) + game.progress
            self.wrd.setText(str)
            self.lives.setText(f"Lives remaining: {game.lives}")
        else:
            self.loss_screen()

    def center(self, win):
        frameGm = win.frameGeometry()
        screen = QApplication.desktop().screenNumber(QApplication.desktop().cursor().pos())
        centerPoint = QApplication.desktop().screenGeometry(screen).center()
        frameGm.moveCenter(centerPoint)
        win.move(frameGm.topLeft())

    def success_screen(self):
        msg = QMessageBox()
        msg.setWindowTitle("Winner")
        msg.setText("You Won!")
        msg.exec_()

    def loss_screen(self):
        msg = QMessageBox()
        msg.setWindowTitle("Loser")
        msg.setText("You Lose :( ")
        msg.exec_()


if __name__== '__main__':
    app = QApplication([])
    gamescreen = Game()
    game = core.Core()
    win = MainWindow()
    win.resize(300, 180)
    win.setWindowTitle('Hangman')

    menulayout = QVBoxLayout()
    label = QLabel()
    label.setText("Hangman")
    label.setFont(QFont('Arial font', 30))
    menulayout.addWidget(label)
    label.show()

    btn1 = QPushButton()
    btn1.setText("Play")
    btn1.setFont(QFont('Arial font', 18))
    menulayout.addWidget(btn1)
    btn1.show()
    btn1.clicked.connect(lambda: gamescreen.game_page(win, game))

    btn2 = QPushButton()
    btn2.setText("Exit")
    btn2.setFont(QFont('Arial font', 18))
    menulayout.addWidget(btn2)
    btn2.show()
    btn2.clicked.connect(win.close)

    win.layout.addLayout(menulayout, 1, 1, 1, 2)

    win.show()

    app.exec_()
