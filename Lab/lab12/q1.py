import sys
from PySide6.QtCore import *
from PySide6.QtWidgets import *
from PySide6.QtGui import *
from datetime import date as Date


class BookingSystemObject:
    def __init__(self):
        self.observers = []
        self.bookings = {}

    def addObserver(self, o):
        self.observers.append(o)

    def notifyObservers(self, data):
        for o in self.observers:
            o.update(data)

    def addBooking(self, date, booking):
        if date in self.bookings:
            self.bookings[date].append(booking)
        else:
            self.bookings[date] = [booking]

    def getBookings(self, date):
        bookings = []
        for k, v in self.bookings.items():
            if k == date:
                bookings.append((k, v))
        
        self.notifyObservers(bookings)
        return bookings

    def display(self, date):
        self.getBookings(date)

class BookingObserverObject:
    def update(self, data):
        pass

class StaffUI(BookingObserverObject):
    def __init__(self, s, name,textEdit):
        self.name = name
        self.system = s
        self.textEdit = textEdit

    def update(self, bookings):
        print(self.name + " - StaffUI.update():")
        print("--- Booking Data ---")
        info = ""
        for data in bookings:
            items = data[1]
            for item in items:
                info += str(data[0]) + " - " + item + "\n"
                print(str(data[0]) + " - " + item)

        self.textEdit.setPlainText(info)            

    def submit(self, date,):
        self.system.display(date)
        


class BookingList(QWidget):
    def __init__(self, system, staffUI):
        super().__init__()
        self.system = system
        self.staffUI = staffUI

        self.setWindowTitle("Booking List")
        layout = QVBoxLayout()
        self.textEdit = QTextEdit()
        layout.addWidget(self.textEdit)
        self.setLayout(layout)

        self.btnPress = QPushButton("Select Bookings ...")
        layout.addWidget(self.btnPress)
        self.btnPress.clicked.connect(self.select)

    def select(self):
        self.w = SelectBooking(self.system, self.staffUI)  # Pass the system and staffUI references
        self.w.show()



class SelectBooking(QWidget):
    def __init__(self, system, staffUI):
        super().__init__()
        self.system = system  # Reference to the BookingSystemObject
        self.staffUI = staffUI  # Reference to the StaffUI

        self.setMinimumSize(300, 300)
        self.setWindowTitle("Select Booking")
        layout = QVBoxLayout()

        self.d = QLabel(self)
        self.d.setText('Day')
        layout.addWidget(self.d)
        self.dline = QLineEdit(self)
        layout.addWidget(self.dline)

        self.m = QLabel(self)
        self.m.setText('Month')
        layout.addWidget(self.m)
        self.mline = QLineEdit(self)
        layout.addWidget(self.mline)

        self.ye = QLabel(self)
        self.ye.setText('Year')
        layout.addWidget(self.ye)
        self.yline = QLineEdit(self)
        layout.addWidget(self.yline)

        self.setLayout(layout)

        self.btnPress = QPushButton("Submit")
        layout.addWidget(self.btnPress)
        self.btnPress.clicked.connect(self.selectbooking)

    def selectbooking(self):
        y = int(self.yline.text())
        m = int(self.mline.text())
        d = int(self.dline.text())

        selectedDate = Date(y, m, d)
        self.staffUI.submit(selectedDate)  # Use the submit method from StaffUI


def main():
    app = QApplication(sys.argv)

    s = BookingSystemObject()
    s.addBooking(Date(2011, 9, 1), "Booking#1")
    s.addBooking(Date(2011, 10, 1), "Booking#2")
    s.addBooking(Date(2011, 10, 1), "Booking#3")
    s.addBooking(Date(2011, 11, 1), "Booking#4")
    s.addBooking(Date(2011, 12, 1), "Booking#5")
    w = BookingList(s, None) 
    ui1 = StaffUI(s, "UI#1", w.textEdit)
    w.staffUI = ui1 

    s.addObserver(ui1)
    ui1.submit(Date(2011, 10, 1))

    w.show()
    return app.exec_()


if __name__ == "__main__":
    sys.exit(main())