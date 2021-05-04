package maze.visualization;

import javafx.scene.layout.VBox;
import javafx.geometry.Pos;
import javafx.scene.control.Label;
import javafx.scene.text.Font;
import javafx.scene.paint.Color;
import javafx.scene.text.FontWeight;

/**
 * Contains the VBox pane that has the legend for the tiles
 */
public class TileLegend extends VBox {

    /**
     * Initializes an instance of tile legend
     * @param i: Spacing between nodes
     */
    public TileLegend(int i) {
        super(i);
        String fontstyle = "Verdana";
        Label legend = new Label("Tiles");
        legend.setFont(Font.font(fontstyle, FontWeight.BOLD, 15));
        Label greenTile = new Label("Entrance(E)");
        greenTile.setFont(Font.font(fontstyle, FontWeight.BOLD, 15));
        greenTile.setTextFill(Color.GREEN);
        Label redTile = new Label("Exit(X)");
        redTile.setTextFill(Color.RED);
        redTile.setFont(Font.font(fontstyle, FontWeight.BOLD, 15));
        Label blueTile = new Label("Route(*)");
        blueTile.setFont(Font.font(fontstyle, FontWeight.BOLD, 15));
        blueTile.setTextFill(Color.BLUE);
        Label purpleTile = new Label("Visited(*)");
        purpleTile.setFont(Font.font(fontstyle, FontWeight.BOLD, 15));
        purpleTile.setTextFill(Color.ORCHID);
        this.getChildren().addAll(legend, greenTile, redTile, blueTile, purpleTile);
        this.setAlignment(Pos.CENTER);
    }
}
