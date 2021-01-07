package weatherstation;

import java.sql.Connection;
import java.sql.DriverManager;
import java.sql.PreparedStatement;
import java.sql.SQLException;

public class WStationQueries {
    
    private Connection connection = null;
    private PreparedStatement insertSensorData = null;

    public WStationQueries() throws SQLException{
        
        
        connection = DriverManager.getConnection(
                "jdbc:mysql://localhost:3306/testdb",
                "root",
                "123456");
        
        insertSensorData = connection.prepareStatement(
                "INSERT INTO `testdb`.`weather_station_data` " +
                "(`temperature`, `humidity`) " +
                "VALUES (?, ?)");
        
    }
    
    public int addMeasurement(String temperature, String humidity) throws SQLException{
        
        insertSensorData.setString(1, temperature);
        insertSensorData.setString(2, humidity);
        return insertSensorData.executeUpdate();
    }
}
