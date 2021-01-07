import mysql.connector


class Queries:
    def __init__(self):
        self.connection = mysql.connector.connect(
            host="localhost",
            user="root",
            passwd="123456",
            database="testdb"
        )

        self.cursor = self.connection.cursor(prepared=True)
        self.insertSensorDataQuery = "INSERT INTO weather_station_data (temperature, humidity) VALUES (%s,%s)"

    def addMeasurement(self, parameters):
        self.cursor.execute(self.insertSensorDataQuery, (parameters, parameters))
        self.connection.commit()
