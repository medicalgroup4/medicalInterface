from PyQt5.QtWidgets import QMenu, QApplication, QLabel, QWidget, QPushButton, QGridLayout, QLineEdit, QMessageBox, QLayoutItem
from dbConnector import *

app = QApplication([])
btnAddPatient = QPushButton('Add patient')
tbPatientName = QLineEdit('Patient name')
tbPatientRoom = QLineEdit('Room')
btnRefresh = QPushButton('Refresh')

window = QWidget()
layout = QGridLayout()


def init():

    conn = dbConnector()

    # Add patient section
    layout.addWidget(tbPatientName, 0, 0)
    layout.addWidget(tbPatientRoom, 0, 1)
    layout.addWidget(btnAddPatient, 1, 0, 1, 2)

    # Refresh button
    layout.addWidget(btnRefresh, 0, 2)

    # Get patients section
    patientsMenu = conn.getPatients()
    layout.addWidget(patientsMenu, 2, 0)

    # Get Messages section
    table = conn.getMessages()
    layout.addWidget(table, 2, 1)

    window.setLayout(layout)


def update():
    for i in reversed(range(layout.count())):
        layout.itemAt(i).widget().setParent(None)
    init()


def on_addpatient_clicked():
    conn = dbConnector()
    conn.addPatient(tbPatientName.text(), tbPatientRoom.text())
    alert = QMessageBox()
    alert.setText('Patient added')
    update()
    alert.exec_()


def on_refresh_clicked():
    update()


init()
window.showFullScreen()
btnAddPatient.clicked.connect(on_addpatient_clicked)
btnRefresh.clicked.connect(on_refresh_clicked)

app.exec()

