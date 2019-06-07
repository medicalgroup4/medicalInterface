import mysql.connector


class dbConnector:
    def __init__(self):
        self.db = mysql.connector.connect(
            host="51.83.42.157",
            user="root",
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
