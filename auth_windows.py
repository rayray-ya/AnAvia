from PySide6.QtCore import Qt, QCoreApplication
from PySide6.QtWidgets import (QMainWindow, QWidget, QVBoxLayout, QHBoxLayout,
                              QLabel, QLineEdit, QPushButton, QMessageBox)
from PySide6.QtGui import QIcon
from database import Database

class LoginWindow(QMainWindow):
    def __init__(self, main_window=None):
        super().__init__()
        self.main_window = main_window
        self.db = Database()
        self.setWindowTitle("Авторизация")
        self.setFixedSize(400, 300)
        icon = QIcon("pineapple.ico")
        self.setWindowIcon(icon)

        
        # Создаем центральный виджет и главный layout
        central_widget = QWidget()
        self.setCentralWidget(central_widget)
        main_layout = QVBoxLayout(central_widget)
        main_layout.setAlignment(Qt.AlignCenter)
        
        # Создаем форму
        form_widget = QWidget()
        form_layout = QVBoxLayout(form_widget)
        form_layout.setSpacing(15)
        
        # Заголовок
        title_label = QLabel("Авторизация")
        title_label.setStyleSheet("font-size: 24px; font-weight: bold;")
        title_label.setAlignment(Qt.AlignCenter)
        form_layout.addWidget(title_label)
        
        # Поля для ввода
        self.login_edit = QLineEdit()
        self.login_edit.setPlaceholderText("Введите логин")
        form_layout.addWidget(self.login_edit)
        
        self.password_edit = QLineEdit()
        self.password_edit.setPlaceholderText("Введите пароль")
        self.password_edit.setEchoMode(QLineEdit.Password)
        form_layout.addWidget(self.password_edit)
        
        # Кнопки
        buttons_layout = QHBoxLayout()
        
        self.login_button = QPushButton("Войти")
        self.login_button.clicked.connect(self.login)
        buttons_layout.addWidget(self.login_button)
        
        self.register_button = QPushButton("Регистрация")
        self.register_button.clicked.connect(self.show_register_window)
        buttons_layout.addWidget(self.register_button)
        
        form_layout.addLayout(buttons_layout)
        
        # Добавляем форму в главный layout
        main_layout.addWidget(form_widget)
        
        # Стилизация
        self.setStyleSheet("""
            QMainWindow {
                background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:1, 
                    stop:0 rgba(0, 50, 150, 255), 
                    stop:0.5 rgba(0, 100, 200, 255), 
                    stop:1 rgba(100, 150, 255, 255));
            }
            QLabel {
                color: white;
            }
            QLineEdit {
                padding: 8px;
                border: 1px solid #ccc;
                border-radius: 4px;
                background-color: black;
            }
            QPushButton {
                padding: 8px 16px;
                background-color: #4a90e2;
                color: white;
                border: none;
                border-radius: 4px;
            }
            QPushButton:hover {
                background-color: #357abd;
            }
        """)

    def login(self):
        login = self.login_edit.text()
        password = self.password_edit.text()
        
        if not login or not password:
            QMessageBox.warning(self, "Ошибка", "Пожалуйста, заполните все поля")
            return
            
        if self.db.check_user_exists(login, password):
            if self.main_window:
                self.main_window.show()
            self.close()
        else:
            QMessageBox.warning(self, "Ошибка", "Неверный логин или пароль")

    def show_register_window(self):
        self.register_window = RegisterWindow(self.main_window)
        self.register_window.show()
        self.hide()


class RegisterWindow(QMainWindow):
    def __init__(self, main_window=None):
        super().__init__()
        self.main_window = main_window
        self.db = Database()
        self.setWindowTitle("Регистрация")
        self.setFixedSize(400, 400)
        icon = QIcon("pineapple.ico")
        self.setWindowIcon(icon)
        
        # Создаем центральный виджет и главный layout
        central_widget = QWidget()
        self.setCentralWidget(central_widget)
        main_layout = QVBoxLayout(central_widget)
        main_layout.setAlignment(Qt.AlignCenter)
        
        # Создаем форму
        form_widget = QWidget()
        form_layout = QVBoxLayout(form_widget)
        form_layout.setSpacing(15)
        
        # Заголовок
        title_label = QLabel("Регистрация")
        title_label.setStyleSheet("font-size: 24px; font-weight: bold;")
        title_label.setAlignment(Qt.AlignCenter)
        form_layout.addWidget(title_label)
        
        # Поля для ввода
        self.login_edit = QLineEdit()
        self.login_edit.setPlaceholderText("Придумайте логин")
        form_layout.addWidget(self.login_edit)
        
        self.email_edit = QLineEdit()
        self.email_edit.setPlaceholderText("Введите email")
        form_layout.addWidget(self.email_edit)
        
        self.password_edit = QLineEdit()
        self.password_edit.setPlaceholderText("Придумайте пароль")
        self.password_edit.setEchoMode(QLineEdit.Password)
        form_layout.addWidget(self.password_edit)
        
        self.confirm_password_edit = QLineEdit()
        self.confirm_password_edit.setPlaceholderText("Подтвердите пароль")
        self.confirm_password_edit.setEchoMode(QLineEdit.Password)
        form_layout.addWidget(self.confirm_password_edit)
        
        # Кнопки
        buttons_layout = QHBoxLayout()
        
        self.register_button = QPushButton("Зарегистрироваться")
        self.register_button.clicked.connect(self.register)
        buttons_layout.addWidget(self.register_button)
        
        self.back_button = QPushButton("Назад")
        self.back_button.clicked.connect(self.back_to_login)
        buttons_layout.addWidget(self.back_button)
        
        form_layout.addLayout(buttons_layout)
        
        # Добавляем форму в главный layout
        main_layout.addWidget(form_widget)
        
        # Стилизация
        self.setStyleSheet("""
            QMainWindow {
                background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:1, 
                    stop:0 rgba(0, 50, 150, 255), 
                    stop:0.5 rgba(0, 100, 200, 255), 
                    stop:1 rgba(100, 150, 255, 255));
            }
            QLabel {
                color: white;
            }
            QLineEdit {
                padding: 8px;
                border: 1px solid #ccc;
                border-radius: 4px;
                background-color: black;
            }
            QPushButton {
                padding: 8px 16px;
                background-color: #4a90e2;
                color: white;
                border: none;
                border-radius: 4px;
            }
            QPushButton:hover {
                background-color: #357abd;
            }
        """)

    def register(self):
        login = self.login_edit.text()
        email = self.email_edit.text()
        password = self.password_edit.text()
        confirm_password = self.confirm_password_edit.text()
        
        if not all([login, email, password, confirm_password]):
            QMessageBox.warning(self, "Ошибка", "Пожалуйста, заполните все поля")
            return
            
        if password != confirm_password:
            QMessageBox.warning(self, "Ошибка", "Пароли не совпадают")
            return
            
        if self.db.check_login_exists(login):
            QMessageBox.warning(self, "Ошибка", "Пользователь с таким логином уже существует")
            return
            
        if self.db.check_email_exists(email):
            QMessageBox.warning(self, "Ошибка", "Пользователь с таким email уже существует")
            return
            
        if self.db.register_user(login, email, password):
            QMessageBox.information(self, "Успех", "Регистрация успешно завершена")
            if self.main_window:
                self.main_window.show()
            self.close()
        else:
            QMessageBox.warning(self, "Ошибка", "Ошибка при регистрации")

    def back_to_login(self):
        self.login_window = LoginWindow(self.main_window)
        self.login_window.show()
        self.hide()
