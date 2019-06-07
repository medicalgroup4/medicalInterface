from PyQt5.QtWidgets import QApplication, QLabel, QWidget, QPushButton, QVBoxLayout, QLineEdit, QMessageBox
from dbConnector import *

app = QApplication([])
window = QWidget()
layout = QVBoxLayout()
btnAddPatient = QPushButton('Add patient')
tbPatientName = QLineEdit('Patient name')
tbPatientRoom = QLineEdit('Room')

layout.addWidget(QLabel('Add patient'))
layout.addWidget(tbPatientName)
layout.addWidget(tbPatientRoom)
layout.addWidget(btnAddPatient)
window.setLayout(layout)
window.show()

#TODO make database remotely accessable and uncomment line below
#conn = dbConnector()


def on_addpatient_clicked():
    conn.addPatient(tbPatientRoom.text(), tbPatientName.text())
    alert = QMessageBox()
    alert.setText('Patient added')
    alert.exec_()


btnAddPatient.clicked.connect(on_addpatient_clicked)
app.exec()

