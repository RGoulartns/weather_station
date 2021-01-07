package weatherstation;

import javafx.application.Platform;
import jssc.SerialPort;
import jssc.SerialPortEvent;
import jssc.SerialPortException;

public class WStationMsgs{
    
    private WStationController controller;
    public SerialPort port;
    public StringBuilder messageBuffer;
    private String message;
    
    public WStationMsgs(WStationController c) throws SerialPortException{
        controller = c; //bad design?
        message = null;
        messageBuffer = new StringBuilder();
        port = new SerialPort("COM2");
        
        port.openPort();
        port.setParams(
                SerialPort.BAUDRATE_9600,
                SerialPort.DATABITS_8,
                SerialPort.STOPBITS_1,
                SerialPort.PARITY_NONE);
        port.setFlowControlMode(SerialPort.FLOWCONTROL_RTSCTS_IN | SerialPort.FLOWCONTROL_RTSCTS_OUT);
        port.setEventsMask(SerialPort.MASK_RXCHAR);
        
		//append characters until '\n'. Send the message to the controller once the endline is received
        port.addEventListener((SerialPortEvent e) -> {
            if(e.isRXCHAR()){
                try{
                    String s = port.readString(e.getEventValue());
                    if(s.equals("\n")){
                        message = messageBuffer.toString();
                        messageBuffer.setLength(0);
                        Platform.runLater(() -> controller.onNewMessage(message) );
                    }
                    else
                        messageBuffer.append(s);
                }
                catch (SerialPortException ex){
                    System.exit(1);
                }
            }
        });
            
    }

    public boolean sendMessage(String x){
        try{
            port.writeString(x);
            return true;
        }
        catch (SerialPortException ex){
            return false;
        }    
    }
    
    public void closeConnection() throws SerialPortException{
        port.closePort();
    }
    
}