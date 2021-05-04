package maze.visualization;

import javafx.scene.control.Label;
import javafx.scene.text.Font;
import javafx.scene.text.FontWeight;
import javafx.geometry.Pos;
import javafx.scene.text.TextAlignment;

/**
 * Upgraded Labels with specific settings
 */
public class AppLabel extends Label {
    
    public AppLabel(String text, int size) {
        super(text);
        this.setMaxWidth(Double.MAX_VALUE);
        this.setAlignment(Pos.CENTER);
        this.setTextAlignment(TextAlignment.CENTER);
        this.setFont(Font.font("Verdana", FontWeight.BOLD, size));
    }
}
