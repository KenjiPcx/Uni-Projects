package maze.visualization;

import javafx.scene.layout.VBox;
import javafx.scene.layout.HBox;
import javafx.scene.control.Label;
import javafx.geometry.Pos;
import javafx.scene.text.Font;
import javafx.scene.text.FontWeight;
import javafx.scene.text.TextAlignment;
import javafx.scene.paint.Color;
import javafx.scene.layout.Region;

import java.util.ArrayList;
import java.util.List;
import java.util.Arrays;
import maze.visualization.MazeGraphics;

/**
 * Contains the maze visuals and coordinates 
 */
public class MazeWithCoordinateGraphics extends VBox {

    private MazeGraphics mg;
    private int rows;
    private int columns;
    private HBox xCoordBar;
    private VBox yCoordBar;
    private HBox mazeWithYBar;

    /**
     * Initializes a VBox with maze and coordinates inside
     * @param n: VBox Spacing 
     */
    public MazeWithCoordinateGraphics(int n) {
        super(n);
        this.rows = -2;
        this.columns = 0;
        this.mg = new MazeGraphics();
        this.mg.setId("root");
        this.yCoordBar = new VBox(5);
        this.yCoordBar.setAlignment(Pos.CENTER);
        this.xCoordBar = new HBox(2);
        this.xCoordBar.setAlignment(Pos.BOTTOM_RIGHT);
        this.mazeWithYBar = new HBox(25);
    }

    /**
     * Sets up the maze and coordinates graphics
     */
    public void setupGraphics() {
        final String css = "-fx-border-color: black;\n -fx-border-width: 3;";
        this.mg.setStyle(css);
        
        this.calculateRowsAndColumns();
        for (int i=0; i<this.rows; i++) {
            Label l = new Label(" " + Integer.toString(this.rows-i-1) + " ");
            l.setMinWidth(Region.USE_PREF_SIZE);
            l.setMaxHeight(30);
            l.setAlignment(Pos.CENTER);
            l.setFont(Font.font("Verdana", FontWeight.BOLD, 20));
            l.setTextFill(Color.BLACK);
            l.setTextAlignment(TextAlignment.CENTER);
            this.yCoordBar.getChildren().addAll(l);
        }

        for (int i=0; i<this.columns; i++) {
            String text;
            if (i<10) {
                text = " " + Integer.toString(i) + " ";
            } else {
                text = "" + Integer.toString(i) + "";
            }
            Label l = new Label(text);
            l.setMinWidth(Region.USE_PREF_SIZE);
            l.setMaxHeight(30);
            l.setAlignment(Pos.CENTER);
            l.setFont(Font.font("Verdana", FontWeight.BOLD, 19.65));
            l.setTextFill(Color.BLACK);
            l.setTextAlignment(TextAlignment.CENTER);
            this.xCoordBar.getChildren().addAll(l);
        }

        this.mazeWithYBar.getChildren().addAll(this.yCoordBar, this.mg);
        this.getChildren().addAll(this.mazeWithYBar, this.xCoordBar);
    }

    /**
     * Updates the visuals of the maze and coordinates
     */
    public void updateGraphics() {
        this.rows = -2;
        this.xCoordBar.getChildren().clear();
        this.yCoordBar.getChildren().clear();
        this.mazeWithYBar.getChildren().clear();
        this.getChildren().clear();
        this.updateMaze();
        this.setupGraphics();
    }

    /**
     * Helper method to calculate rows and columns of a maze
     */
    public void calculateRowsAndColumns() {
        boolean firstZeroFound = false;
        String subStr = "";
        String s = this.mg.getMaze();
        for (int i=0; i<s.length(); i++) {
            if (s.charAt(i) == '\n') {
                this.rows += 1;
            } else if (s.charAt(i) == '0') {
                firstZeroFound = true;
            }
            if (firstZeroFound) {
                subStr += s.charAt(i);
            }
        }

        String strArr[] = s.split(" |\n");
        List<String> al = new ArrayList<String>();
	    al = Arrays.asList(strArr);
        String lastElem = al.get(al.size()-1);
        this.columns = Integer.parseInt(lastElem) + 1;
    }

    /**
     * Sets the maze using the string representation of the maze
     * @param s: String representation of maze
     */
    public void setMaze(String s) {
        this.mg.setMaze(s);
    }

    /**
     * Updates the maze only
     */
    public void updateMaze() {
        this.mg.clearGrid();
        this.mg.printMaze();
    }

}
