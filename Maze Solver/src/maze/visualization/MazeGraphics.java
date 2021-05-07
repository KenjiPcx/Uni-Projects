package maze.visualization;

import javafx.geometry.Pos;
import javafx.scene.layout.GridPane;
import javafx.scene.paint.Color;
import javafx.scene.shape.Rectangle;
import javafx.scene.text.TextAlignment;
import javafx.scene.control.Label;
import javafx.scene.text.Font;
import javafx.scene.text.FontWeight;

/**
 * Contains all the shapes and graphics that will be used to generate the maze
 */
public class MazeGraphics extends GridPane {
    private String maze;

    /**
     * Initializes an instance of graphics and apply them to the given layout
     */
    public MazeGraphics() {
        super();
        this.maze = "";
    }

    /**
     * Sets the maze that will use the graphics
     * @param s: String representation of Maze
     */
    public void setMaze(String s) {
        this.maze = s;
    }

    public String getMaze() {
        return this.maze;
    }

    /**
     * Generates a representation of the maze with graphics, shapes and labels
     */
    public void printMaze() {
        int x = 0;
        int y = 0;
        this.setAlignment(Pos.CENTER);
        String fontstyle = "Verdana";
        for (int i=0; i<this.maze.length(); i++) {

            if (this.maze.charAt(i) != '\n') {
                // Wall Tile
                if (this.maze.charAt(i) == '#') {
                    Rectangle r = new Rectangle();
                    r.setWidth(30);
                    r.setHeight(30);
                    r.setArcWidth(5);
                    r.setArcHeight(5);
                    r.setFill(Color.SADDLEBROWN);
                    GridPane.setConstraints(r, x, y);
                    this.getChildren().addAll(r);
                // Route Tile
                } else if (this.maze.charAt(i) == '-') {
                    Label l = new Label("*");
                    l.setMaxWidth(30);
                    l.setMaxHeight(30);
                    l.setAlignment(Pos.CENTER);
                    l.setFont(Font.font(fontstyle, FontWeight.BOLD, 20));
                    l.setTextFill(Color.BLUE);
                    l.setTextAlignment(TextAlignment.CENTER);
                    GridPane.setConstraints(l, x, y);
                    this.getChildren().addAll(l);
                // Visited Tile
                } else if (this.maze.charAt(i) == '=') {
                    Label l = new Label("*");
                    l.setMaxWidth(30);
                    l.setMaxHeight(30);
                    l.setAlignment(Pos.CENTER);
                    l.setFont(Font.font(fontstyle, FontWeight.BOLD, 20));
                    l.setTextFill(Color.ORCHID);
                    l.setTextAlignment(TextAlignment.CENTER);
                    GridPane.setConstraints(l, x, y);
                    this.getChildren().addAll(l);
                // Entrance Tile
                } else if (maze.charAt(i) == 'e') {
                    Label l = new Label("E");
                    l.setMaxWidth(30);
                    l.setMaxHeight(30);
                    l.setAlignment(Pos.CENTER);
                    l.setFont(Font.font(fontstyle, FontWeight.BOLD, 20));
                    l.setTextFill(Color.GREEN);
                    l.setTextAlignment(TextAlignment.CENTER);
                    GridPane.setConstraints(l, x, y);
                    this.getChildren().addAll(l);
                // Exit Tile
                } else if (maze.charAt(i) == 'x') {
                    Label l = new Label("X");
                    l.setMaxWidth(30);
                    l.setMaxHeight(30);
                    l.setAlignment(Pos.CENTER);
                    l.setFont(Font.font(fontstyle, FontWeight.BOLD, 20));
                    l.setTextFill(Color.RED);
                    l.setTextAlignment(TextAlignment.CENTER);
                    GridPane.setConstraints(l, x, y);
                    this.getChildren().addAll(l);
                }
                x += 1;
            } else if (this.maze.charAt(i) == '\n'){
                y += 1;
                x = 0;
            }
        }
    }

    /**
     * Clears the grid of the maze
     */
    public void clearGrid() {
        this.getChildren().clear();
    }
}
