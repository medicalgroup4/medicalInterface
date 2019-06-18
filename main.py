from PyQt5.QtWidgets import QAction, QMenu, QApplication, QLabel, QWidget, QPushButton, QGridLayout, QLineEdit, QMessageBox, QLayoutItem, QComboBox
from PyQt5 import QtCore
from dbConnector import *

app = QApplication([])
btnAddPatient = QPushButton('Add patient')
tbPatientName = QLineEdit('Patient name')
tbPatientRoom = QLineEdit('Room')
btnRefresh = QPushButton('Refresh')
cbPatients = QComboBox()
table = QTableWidget()
seltable = QTableWidget()
window = QWidget()
layout = QGridLayout()


def init(pname):
    print('Initializing')
    conn = dbConnector()

    global seltable

    # Add patient section
    layout.addWidget(tbPatientName, 0, 0)
    layout.addWidget(tbPatientRoom, 0, 1)
    layout.addWidget(btnAddPatient, 1, 0, 1, 2)

    # Refresh button
    layout.addWidget(btnRefresh, 0, 2)

    # Get patients section
    if pname is None:
        patients = conn.getPatients()
        cbPatients.clear()
        cbPatients.addItems(patients)
        layout.addWidget(cbPatients, 2, 0)

    # Get messages section
    table1 = conn.getMessages(pname)
    layout.addWidget(table1, 2, 1, 3, 1)

    window.setLayout(layout)

    print("Init Done")


def clear():
    for i in reversed(range(layout.count())):
        layout.itemAt(i).widget().setParent(None)


def on_addpatient_clicked():
    conn = dbConnector()
    conn.addPatient(tbPatientName.text(), tbPatientRoom.text())
    alert = QMessageBox()
    alert.setText('Patient added')
    clear()
    init(None)
    alert.exec_()


def on_refresh_clicked():
    init(None)


def on_patient_clicked(action):
    conn = dbConnector()
    patient = cbPatients.itemText(action)
    init(patient)


init(None)
window.setLayout(layout)
window.show()

btnAddPatient.clicked.connect(on_addpatient_clicked)
btnRefresh.clicked.connect(on_refresh_clicked)
cbPatients.currentIndexChanged.connect(on_patient_clicked)

app.exec()

