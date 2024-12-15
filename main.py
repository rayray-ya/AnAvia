import sys
from PySide6.QtWidgets import QApplication, QMainWindow
from auth_windows import LoginWindow
from aaa import Ui_MainWindow


class MainWindow(QMainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    
    # Создаем главное окно, но не показываем его
    main_window = MainWindow()
    
    # Показываем окно авторизации
    login_window = LoginWindow(main_window)
    login_window.show()
    
    sys.exit(app.exec())
