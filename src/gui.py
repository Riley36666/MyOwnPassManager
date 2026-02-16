from PyQt5.QtWidgets import (
    QWidget,
    QVBoxLayout,
    QFormLayout,
    QPushButton,
    QLineEdit,
    QLabel,
    QMessageBox,
)
from PyQt5.QtCore import Qt

from src.store_pass import storepass


class StorePasswordScreen(QWidget):
    def __init__(self, main_window):
        super().__init__()

        self.main_window = main_window

        layout = QVBoxLayout()
        form_layout = QFormLayout()

        self.website_input = QLineEdit()
        self.password_input = QLineEdit()

        # ✅ PyQt5 enum style
        self.password_input.setEchoMode(QLineEdit.Password)

        form_layout.addRow("Website:", self.website_input)
        form_layout.addRow("Password:", self.password_input)

        layout.addLayout(form_layout)

        save_button = QPushButton("Save Password")
        save_button.clicked.connect(self.store_pass)

        back_button = QPushButton("Back")
        back_button.clicked.connect(self.go_back)

        layout.addWidget(save_button)
        layout.addWidget(back_button)

        self.setLayout(layout)

    def store_pass(self):
        website = self.website_input.text()
        password = self.password_input.text()

        if storepass(website, password):
            QMessageBox.information(self, "Success", "Successfully stored password!")
            self.website_input.clear()
            self.password_input.clear()
        else:
            QMessageBox.warning(self, "Error", "Please enter both website and password.")

    def go_back(self):
        self.main_window.show_start_screen()


class StartScreen(QWidget):
    def __init__(self, main_window):
        super().__init__()

        self.main_window = main_window

        layout = QVBoxLayout()
        layout.setSpacing(15)

        store_btn = QPushButton("Store a New Password")
        store_btn.clicked.connect(self.main_window.show_store_screen)

        all_pass_btn = QPushButton("Display All Passwords")
        all_pass_btn.clicked.connect(lambda: print("Not implemented yet"))

        gen_pass_btn = QPushButton("Generate New Password")
        gen_pass_btn.clicked.connect(lambda: print("Not implemented yet"))

        delete_pass_btn = QPushButton("Delete Saved Password")
        delete_pass_btn.clicked.connect(lambda: print("Not implemented yet"))

        exit_btn = QPushButton("Exit")
        exit_btn.clicked.connect(self.main_window.close)

        for btn in [
            store_btn,
            all_pass_btn,
            gen_pass_btn,
            delete_pass_btn,
            exit_btn,
        ]:
            btn.setMinimumHeight(45)
            layout.addWidget(btn)

        self.setLayout(layout)
