package maze.visualization;

import javafx.scene.control.Alert;
import javafx.scene.control.Alert.AlertType;
import javafx.scene.control.ButtonType;
import javafx.scene.control.ButtonBar.ButtonData;

/**
 * Alert Box class to display exceptions on GUI
 */
public class AlertBox extends Alert {

    /**
     * Creates a pop up with error message
     * @param errType: Type of Exception
     * @param errMsg: Error Message
     */
    public AlertBox(String errType, String errMsg) {
        super(Alert.AlertType.ERROR);
        this.setTitle(errType);
        this.setContentText(errMsg);
    }
}
