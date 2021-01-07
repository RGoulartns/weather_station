
package weatherstation;

import java.net.URL;
import java.sql.SQLException;
import java.util.ResourceBundle;
import javafx.event.ActionEvent;
import javafx.fxml.FXML;
import javafx.fxml.Initializable;
import javafx.scene.control.Button;
import javafx.scene.control.Label;
import javafx.scene.control.TextField;
import javafx.scene.control.ToggleButton;
import jssc.SerialPortException;


public class WStationController implements Initializable {   
    private WStationMsgs msgs;
    private WStationQueries queries;
    public Label lbl_temperature;
    public ToggleButton tbtn_motor;
    public ToggleButton tbtn_led;
    public Button btn_upFreq;
    public TextField tf_upFreq;
    
    
    @Override
    public void initialize(URL url, ResourceBundle rb){
        try{
            msgs = new WStationMsgs(this);
            queries = new WStationQueries();
        } 
        catch (SerialPortException | SQLException ex){
            System.exit(1);
        }        
    }
    
    @FXML
    private void onMotorToggleBtnClicked(ActionEvent e){
        if(tbtn_motor.isSelected()){
            tbtn_motor.setText("ON");
            msgs.sendMessage("M1");
        }
        else{
            tbtn_motor.setText("OFF");
            msgs.sendMessage("M0");
        }
    }

    @FXML
    private void onLEDToggleBtnClicked(ActionEvent e){
        if(tbtn_led.isSelected()){
            tbtn_led.setText("ON");
            msgs.sendMessage("L1");
        }
        else{
            tbtn_led.setText("OFF");
            msgs.sendMessage("L0");
        }
    }
    
    @FXML
    public void onUpdateFreqBtnClicked(ActionEvent e){
        msgs.sendMessage("F" + tf_upFreq.getText() );
    }
    
    public void onNewMessage(String s){
        lbl_temperature.setText("Temperature: " + s);
        try {
            queries.addMeasurement(s, s);
        } catch (SQLException ex) {
            System.exit(1);
        }
    }
    
}