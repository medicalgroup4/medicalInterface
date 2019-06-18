import mysql.connector
from PyQt5.QtWidgets import QAction, QMenu, QTableWidget, QTableWidgetItem


class dbConnector:
    def __init__(self):

        self.menu = QMenu()
        self.db = mysql.connector.connect(
            host="51.83.42.157",
            user="remote",
            passwd="1234Hoedjevan!",
            database="medicaldb"
)

    def addPatient(self, name, room):
        cursor = self.db.cursor()
        sql = "INSERT INTO Patients (name, room) VALUES (%s, %s)"
        val = (name, room)
        cursor.execute(sql, val)
        self.db.commit()
        print("Patient inserted")

    def getPatients(self):
        cursor = self.db.cursor()
        cursor.execute("SELECT Name FROM Patients")
        myresult = cursor.fetchall()

        patient_list = []

        print(myresult)
        for patient in myresult:
            patient_list.append(''.join(patient))

        return patient_list

    def getPatient(self, p):
        cursor = self.db.cursor()
        cursor.execute("SELECT id FROM Patients WHERE name = " + "'" + p + "'")
        id = cursor.fetchone()

        cursor.execute("SELECT room FROM Patients WHERE name = " + "'" + p + "'")
        room = cursor.fetchone()

        data = [id[0], room[0]]
        return data

    def getMessages(self, pname):
        table = QTableWidget()
        table.setColumnCount(6)
        table.setHorizontalHeaderLabels(['id', 'patient_id', 'severity', 'message', 'location', 'confirmed'])
        table.setColumnWidth(0, 30)
        table.setColumnWidth(1, 80)
        table.setColumnWidth(2, 60)
        table.setColumnWidth(3, 240)
        table.setColumnWidth(4, 60)
        table.setColumnWidth(5, 80)

        cursor = self.db.cursor()

        if pname is None:
            cursor.execute("SELECT * FROM Messages")

        else:
            cursor.execute("SELECT id FROM Patients WHERE name = " + "'" + pname + "'")
            p_id = cursor.fetchone()
            string_id = str(p_id)
            string_id = string_id.replace('(', '')
            string_id = string_id.replace(')', '')
            string_id = string_id.replace(',', '')

            cursor.execute("SELECT * FROM Messages WHERE patient_id = " + "'" + string_id + "'")

        myresult = cursor.fetchall()

        for message in myresult:
            rowPosition = table.rowCount()
            table.insertRow(rowPosition)
            table.setItem(rowPosition, 0, QTableWidgetItem(str(message[0])))
            table.setItem(rowPosition, 1, QTableWidgetItem(str(message[1])))
            table.setItem(rowPosition, 2, QTableWidgetItem(str(message[2])))
            table.setItem(rowPosition, 3, QTableWidgetItem(message[3]))
            table.setItem(rowPosition, 4, QTableWidgetItem(message[4]))
            table.setItem(rowPosition, 5, QTableWidgetItem(str(message[5])))

        return table

