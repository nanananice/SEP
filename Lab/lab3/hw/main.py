import sys
from PySide6.QtWidgets import *
from PySide6.QtCore import *
from PySide6.QtGui import QFont
from phone_main import Ui_Form as phone_main_ui
from phone_call import Ui_Form as phone_call_ui
from phone_calculator import Ui_Form as phone_calc_ui
from phone_exchanger import Ui_Form as phone_ex_ui
from phone_game import Ui_Form as phone_game_ui
from phone_contact import Ui_Form as phone_cont_ui
import random

class phone_main(QMainWindow):
    def __init__(self):
        QMainWindow.__init__(self, None)
        self.ui = phone_main_ui()
        self.ui.setupUi(self)
        self.ui.calculator_app.clicked.connect(self.open_calculator)
        self.ui.phone_app.clicked.connect(self.open_phone)   
        self.ui.exchanger_app.clicked.connect(self.open_exchanger)   
        self.ui.game_app.clicked.connect(self.open_game)   
        self.ui.contact_app.clicked.connect(self.open_contact)      

    def open_calculator(self):
        self.phone_calculator_window = phone_calculator()
        self.phone_calculator_window.show()
        self.close()

    def open_phone(self):
        self.phone_call_window = phone_call()
        self.phone_call_window.show()
        self.close()

    def open_exchanger(self):
        self.phone_exchanger_window = phone_exchanger()
        self.phone_exchanger_window.show()
        self.close()

    def open_game(self):
        self.phone_game_window = phone_game()
        self.phone_game_window.show()
        self.close()
    
    def open_contact(self):
        self.phone_contact_window = phone_contact()
        self.phone_contact_window.show()
        self.close()


class phone_call(QMainWindow):
    def __init__(self):
        QMainWindow.__init__(self, None)
        self.ui = phone_call_ui()
        self.ui.setupUi(self)
        self.ui.button_1.clicked.connect(self.edit)
        self.ui.button_2.clicked.connect(self.edit)
        self.ui.button_3.clicked.connect(self.edit)
        self.ui.button_4.clicked.connect(self.edit)
        self.ui.button_5.clicked.connect(self.edit)
        self.ui.button_6.clicked.connect(self.edit)
        self.ui.button_7.clicked.connect(self.edit)
        self.ui.button_8.clicked.connect(self.edit)
        self.ui.button_9.clicked.connect(self.edit)
        self.ui.button_0.clicked.connect(self.edit)
        self.ui.button_mul.clicked.connect(self.edit)
        self.ui.button_hash.clicked.connect(self.edit)
        self.ui.button_del.clicked.connect(self.delete_last)
        self.ui.button_talk.clicked.connect(self.dial)
        self.ui.home_app.clicked.connect(self.go_phone_main)

    def edit(self):
        add = self.sender().text()
        self.ui.phone_number.setText(self.ui.phone_number.text() + add) 
    
    def delete_last(self):
        self.ui.phone_number.setText((self.ui.phone_number.text())[:-1]) 

    def dial(self):
        dialog = QDialog(self)
        layout = QVBoxLayout()
        label = QLabel(self)
        label.setText("Dialing << " + self.ui.phone_number.text() + " >>")
        layout.addWidget(label)
        close_button = QPushButton("Close", self)
        close_button.clicked.connect(dialog.close)
        layout.addWidget(close_button)
        dialog.setLayout(layout)
        dialog.show()

    def go_phone_main(self):
        self.phone_call_window = phone_main()
        self.phone_call_window.show()
        self.close()

class phone_calculator(QMainWindow):
    def __init__(self):
        QMainWindow.__init__(self, None)
        self.ui = phone_calc_ui()
        self.ui.setupUi(self)
        self.ui.button_0.clicked.connect(self.edit)
        self.ui.button_1.clicked.connect(self.edit)
        self.ui.button_2.clicked.connect(self.edit)
        self.ui.button_3.clicked.connect(self.edit)
        self.ui.button_4.clicked.connect(self.edit)
        self.ui.button_5.clicked.connect(self.edit)
        self.ui.button_6.clicked.connect(self.edit)
        self.ui.button_7.clicked.connect(self.edit)
        self.ui.button_8.clicked.connect(self.edit)
        self.ui.button_9.clicked.connect(self.edit)
        self.ui.button_decimal.clicked.connect(self.edit)
        self.ui.button_plus.clicked.connect(self.edit)
        self.ui.button_minus.clicked.connect(self.edit)
        self.ui.button_multiply.clicked.connect(self.edit)
        self.ui.button_divide.clicked.connect(self.edit)
        self.ui.button_equal.clicked.connect(self.total)
        self.ui.button_clear.clicked.connect(self.clear)
        self.ui.button_delete.clicked.connect(self.delete_last)
        self.ui.button_plusminus.clicked.connect(self.plusminus)
        self.ui.home_app.clicked.connect(self.go_phone_main)
    
    def plusminus(self):
        self.ui.number.setText(str(float(eval(self.ui.number.text()))*(-1)))

    def delete_last(self):
        self.ui.number.setText((self.ui.number.text())[:-1]) 

    def edit(self):
        add = self.sender().text()
        self.ui.number.setText(self.ui.number.text() + add) 
    
    def total(self):
        self.ui.number.setText(str(eval(self.ui.number.text()))) 

    def clear(self):
        self.ui.number.setText('') 

    def go_phone_main(self):
        self.phone_call_window = phone_main()
        self.phone_call_window.show()
        self.close()

class phone_exchanger(QMainWindow):
    def __init__(self):
        QMainWindow.__init__(self, None)
        self.ui = phone_ex_ui()
        self.ui.setupUi(self)
        # this is average currency value 
        # the value might change a bit to a lot
        self.conversion_rates = {
            'THB': [30, '฿', 'Thai Baht'],
            'USD': [1, '$', 'US Dollar'],
            'CNY': [7, '¥', 'Chinese Yuan'],
            'JPY': [140, '¥', 'Japanese Yen'],
            'KRW': [1300, '₩', 'South Korean Won'],
            'EUR': [0.9, '€', 'Euro'],
            'CHF': [0.9, 'CHF', 'Swiss Franc'],
            'HKD': [8, 'HK$', 'Hong Kong Dollar'],
            'SGD': [1.3, 'S$', 'Singapore Dollar'],
            'MYR': [4.7, 'RM', 'Malaysian Ringgit'],
            'IDR': [15490, 'Rp', 'Indonesian Rupiah'],
            'BND': [1.3, 'B$', 'Brunei Dollar'],
            'INR': [83, '₹', 'Indian Rupee']
        }
        self.populate_comboboxes()
        self.ui.home_app.clicked.connect(self.go_phone_main)
        self.ui.confirm.clicked.connect(self.convert_currency)

    def populate_comboboxes(self):
        for currency in self.conversion_rates.keys():
            self.ui.from_currency_combo.addItem(currency)
            self.ui.to_currency_combo.addItem(currency)

    def convert_currency(self):
        try:
            from_currency = self.ui.from_currency_combo.currentText()
            to_currency = self.ui.to_currency_combo.currentText()
            amount = float(self.ui.from_currency_input.text())
            converted_amount = (amount / self.conversion_rates[from_currency][0]) * self.conversion_rates[to_currency][0]
            self.ui.to_currency_total.setText(str(round(converted_amount,5)))
            self.ui.from_currency_name.setText(self.conversion_rates[from_currency][2])
            self.ui.to_currency_name.setText(self.conversion_rates[to_currency][2])
            self.ui.from_currency_symbol.setText(self.conversion_rates[from_currency][1])
            self.ui.to_currency_symbol.setText(self.conversion_rates[to_currency][1])
        except ValueError:
            QMessageBox.warning(self, "Input Error", "Please enter a valid number.")

    def go_phone_main(self):
        self.phone_main_window = phone_main()
        self.phone_main_window.show()
        self.close()

class phone_game(QMainWindow):
    def __init__(self):
        QMainWindow.__init__(self, None)
        self.ui = phone_game_ui()
        self.ui.setupUi(self)
        self.number_now = 0
        self.life = 0
        self.ui.home_app.clicked.connect(self.go_phone_main)
        self.ui.button_start.clicked.connect(self.game_start)
        self.ui.button_restart.clicked.connect(self.game_start)
        self.ui.button_guess.clicked.connect(self.guess_press)

    def game_start(self):
        number_range = self.ui.level_combo.currentText()
        self.number_now = random.randint(1, int(number_range))
        mode_diff = self.ui.mode_combo.currentText()
        if mode_diff == 'EASY':
            self.life  = 10
        elif mode_diff == 'NORMAL':
            self.life  = 7
        elif mode_diff == 'HARD':
            self.life  = 5
        elif mode_diff == 'LEGENDARY':
            self.life  = 3
        elif mode_diff == 'IMPOSSIBLE':
            self.life  = 1 
        self.ui.life_amount.setText(str(self.life))

    def guess_press(self):
        try:
            player_guess = int(self.ui.number_input.text())
            if player_guess == self.number_now and self.life > 0:
                QMessageBox.information(self, "YAY!", "You've won!")
                self.ui.message_now.setText("Please restart the game!")
            elif self.life == 0:
                QMessageBox.information(self, "Noo!", "You've lost!")
                self.ui.message_now.setText("Please restart the game!")
            elif player_guess < self.number_now and self.life > 0:
                self.ui.message_now.setText(f"The number is HIGHER than {player_guess}")
                self.life -= 1
                self.ui.life_amount.setText(str(self.life))
            elif player_guess > self.number_now and self.life > 0:
                self.ui.message_now.setText(f"The number is LOWER than {player_guess}")
                self.life -= 1
                self.ui.life_amount.setText(str(self.life))
        except ValueError:
            QMessageBox.warning(self, "Error", "Please enter a valid number.")


    def go_phone_main(self):
        self.phone_main_window = phone_main()
        self.phone_main_window.show()
        self.close()

class phone_contact(QMainWindow):
    def __init__(self):
        QMainWindow.__init__(self, None)
        self.ui = phone_cont_ui()
        self.ui.setupUi(self)
        self.ui.add_contact.clicked.connect(self.add_contact_to_list)
        self.ui.home_app.clicked.connect(self.go_phone_main)
        self.contacts_layout = QVBoxLayout()
        self.contacts_layout.setAlignment(Qt.AlignTop)
        self.contacts_layout.setSpacing(10)
        self.ui.scrollAreaWidgetContents.setLayout(self.contacts_layout)
        self.ui.scrollAreaWidgetContents.setFixedWidth(350)
        self.contacts = {} 
        
    def add_contact_to_list(self):
        name = self.ui.name.text()
        phone = self.ui.phone.text()
        if (name, phone) in self.contacts:
            QMessageBox.warning(self, "Error", "Contact already exist!")
            self.ui.name.clear()
            self.ui.phone.clear()
            return
        self.contacts[(name, phone)] = None 
        contact_widget = QWidget()
        contact_layout = QHBoxLayout(contact_widget)
        contact_label = QLabel(f"{name}: {phone}")
        contact_label.setFont(QFont("Verdana", 14))
        contact_label.setStyleSheet("background-color: white; border-radius: 10px;")
        contact_layout.addWidget(contact_label)
        contact_widget.setFixedHeight(60)
        self.contacts_layout.addWidget(contact_widget)
        self.ui.name.clear()
        self.ui.phone.clear()

    def go_phone_main(self):
        self.phone_main_window = phone_main()
        self.phone_main_window.show()
        self.close()



if __name__ == "__main__":
    app = QApplication(sys.argv)
    w = phone_main()
    w.show()
    sys.exit(app.exec())
