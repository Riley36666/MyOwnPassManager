import sys
from PyQt5.QtWidgets import (
    QApplication,
    QMainWindow,
    QWidget,
    QVBoxLayout,
    QPushButton,
    QStackedWidget,
)
from PyQt5.QtGui import QIcon
from PyQt5.QtCore import Qt

from src.gui import StartScreen, StorePasswordScreen
from src.logic import startup
from src.buttonFunctions import (
    storeButton,
    allPassButton,
    genPass,
    deletePass,
)


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        startup()

        self.setWindowTitle("Password Manager")
        self.setWindowIcon(QIcon(r"C:\Users\riley\Desktop\Python project\images\icon.png"))
        self.showMaximized()

        central_widget = QWidget()
        self.setCentralWidget(central_widget)

        layout = QVBoxLayout()
        layout.setSpacing(15)
        central_widget.setLayout(layout)

        self.store_btn = QPushButton("Store a New Password")
        self.store_btn.clicked.connect(lambda: storeButton(self))

        self.all_pass_btn = QPushButton("Display All Passwords")
        self.all_pass_btn.clicked.connect(lambda: allPassButton(self))

        self.gen_pass_btn = QPushButton("Generate New Password")
        self.gen_pass_btn.clicked.connect(lambda: genPass(self))

        self.delete_pass_btn = QPushButton("Delete Saved Password")
        self.delete_pass_btn.clicked.connect(lambda: deletePass(self))

        self.exit_btn = QPushButton("Exit")
        self.exit_btn.clicked.connect(self.close)

        for btn in [
            self.store_btn,
            self.all_pass_btn,
            self.gen_pass_btn,
            self.delete_pass_btn,
            self.exit_btn,
        ]:
            btn.setMinimumHeight(50)
            layout.addWidget(btn)

    def show_start_screen(self):
        self.setWindowTitle("Password Manager")
        self.stack.setCurrentWidget(self.start_screen)

    def show_store_screen(self):
        self.setWindowTitle("Store a Password")
        self.stack.setCurrentWidget(self.store_screen)


if __name__ == "__main__":
    app = QApplication(sys.argv)

    window = MainWindow()
    window.show()

    sys.exit(app.exec_())
