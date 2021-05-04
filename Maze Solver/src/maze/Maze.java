package maze;

import java.io.BufferedReader;
import java.io.FileReader;
import java.io.IOException;
import java.io.Serializable;
import java.util.ArrayList;
import java.util.List;

/** 
 *  Contains the details of a maze
 */
public class Maze implements Serializable {
    private Tile entrance;
    private Tile exit;
    private List<List<Tile>> tiles;

    /** 
     * Inner class of Maze used to enumerate directions in the maze
     */
    public enum Direction{
        NORTH,
        SOUTH,
        EAST,
        WEST
    }

    /**
     * Inner class of Maze used to create coordinates in the maze
     */
    public class Coordinate {
        private int x;
        private int y;
    
        public Coordinate(int x, int y){
            this.x = x;
            this.y = y;
        }
    
        public int getX(){
            return this.x;
        }
    
        public int getY(){
            return this.y;
        }
    
        public String toString(){
            return "(" + Integer.toString(this.x) + ", " + Integer.toString(this.y) + ")";
        }
    }

    /**
     * Initializes an instance of a maze.
     */
    private Maze(){
        this.entrance = null;
        this.exit = null;
        this.tiles = new ArrayList<List<Tile>>();
    }

    /**
     * Loads a maze from a txt file.
     * @param fpath: File path
     * @return Returns maze object, returns null if file path does not exist
     * @throws RaggedMazeException if size of the maze is not consistent
     * @throws NoEntranceException if there is no entrance in the maze
     * @throws NoExitException if there is no exit in the maze
     * @throws InvalidMazeException if the file is invalid or contains unsuitable format for maze
     */
    public static Maze fromTxt(String fpath) throws 
        InvalidMazeException, RaggedMazeException, NoEntranceException, NoExitException {
        try (BufferedReader reader = new BufferedReader(new FileReader(fpath))) {
            String line = reader.readLine();
            Maze maze = new Maze();
            int width;
            while (line != null) {
                List<Tile> row = new ArrayList<Tile>();
                maze.tiles.add(row);
                width = line.length();
                for (int i=0; i<line.length(); i++) {
                    if (line.charAt(i) == 'e') {
                        Tile t = Tile.fromChar(line.charAt(i));
                        row.add(t);
                        maze.setEntrance(t);
                    }
                    else if (line.charAt(i) == 'x') {
                        Tile t = Tile.fromChar(line.charAt(i));
                        row.add(t);
                        maze.setExit(t);
                    }
                    else {
                        try {
                            row.add(Tile.fromChar(line.charAt(i)));
                        } catch (InvalidMazeException e) {
                            throw e;
                        }
                    }
                }
                line = reader.readLine();
                if (line != null && line.length() != width) {
                    throw new RaggedMazeException("Maze is ragged.");
                }
            }
            if (maze.entrance == null) {
                throw new NoEntranceException("The maze has no entrance.");
            }
            if (maze.exit == null) {
                throw new NoExitException("The maze has no exit");
            }
            return maze;
        } catch (IOException e) {
            throw new InvalidMazeException(fpath + "is an invalid File");
        }
    }

    /**
     * Gets a tile adjacent to the given tile.
     * @param t: Current Tile
     * @param d: Direction
     * @return Returns the adjacent tile, returns null if there is no adjacent tile in given direction
     */
    public Tile getAdjacentTile(Tile t, Maze.Direction d) {
        Maze.Coordinate c = this.getTileLocation(t);
        int x = c.getX();
        int y = c.getY();
        if (d == Maze.Direction.NORTH) {
            try {
                return getTileAtLocation(new Maze.Coordinate(x,y+1));
            } catch (IndexOutOfBoundsException e) {
                return null;
            }
        } else if (d == Maze.Direction.SOUTH) {
            try {
                return getTileAtLocation(new Maze.Coordinate(x,y-1));
            } catch (IndexOutOfBoundsException e) {
                return null;
            }
        } else if (d == Maze.Direction.EAST) {
            try {
                return getTileAtLocation(new Maze.Coordinate(x+1,y));
            } catch (IndexOutOfBoundsException e) {
                return null;
            }
        } else if (d == Maze.Direction.WEST) {
            try {
                return getTileAtLocation(new Maze.Coordinate(x-1,y));
            } catch (IndexOutOfBoundsException e) {
                return null;
            }
        }
        return null;
    }

    /**
     * Gets the entrance tile of the maze.
     * @return Returns the entrance tile
     */
    public Tile getEntrance() {
        return this.entrance;
    }

    /**
     * Gets the exit tile of the maze.
     * @return Returns the exit tile
     */
    public Tile getExit() {
        return this.exit;
    }

    /**
     * Gets the tile at the given coordinate.
     * @param c: Coordinate of tile
     * @return Returns the tile at the given coordinate
     */
    public Tile getTileAtLocation(Maze.Coordinate c) {
        return tiles.get(this.tiles.size()-c.getY()-1).get(c.getX());
    }

    /**
     * Gets the coordinate location of the given tile.
     * @param t: Tile
     * @return Returns the coordinate of the tile, returns null if tile is not in the maze
     */
    public Maze.Coordinate getTileLocation(Tile t) {
        for (List<Tile> row : this.tiles) {
            if (row.contains(t)) {
                int y = tiles.indexOf(row);
                int x = row.indexOf(t);
                return new Maze.Coordinate(x,this.tiles.size()-y-1);
            }
        }
        return null;
    }

    /**
     * Gets all the tiles of the maze.
     * @return Returns all the tiles of the maze
     */
    public List<List<Tile>> getTiles() {
        return this.tiles;
    }

    /**
     * Sets the entrance tile of the maze. Fails if the tile is not in the maze.
     * @param t: Tile
     * @throws MultipleEntranceException if an entrance is already set
     */
    private void setEntrance(Tile t) throws MultipleEntranceException {
        for (List<Tile> row : this.tiles) {
            if (row.contains(t)) {
                if (this.entrance == null) {
                    this.entrance = t;
                } else {
                    throw new MultipleEntranceException("This maze has too many entrances.");
                }
            }
        }
    }

    /**
     * Sets the exit tile of the maze. Fails if the tile is not in the maze.
     * @param t: Tile
     * @throws MultipleExitException if an exit is already set
     */
    private void setExit(Tile t) throws MultipleExitException {
        for (List<Tile> row : this.tiles) {
            if (row.contains(t)) {
                if (this.exit == null) {
                    this.exit = t;
                } else {
                    throw new MultipleExitException("This maze has too many exits.");
                }
            }
        }
    }

    /**
     * Returns the string representation of the maze.
     * @return Returns the string representation of the maze
     */
    public String toString() {
        String s = "";
        for (int i=0; i<this.tiles.size(); i++) {
            s += Integer.toString(this.tiles.size()-i-1) + "  ";
            for (Tile col : this.tiles.get(i)) {
                s += " " + col.toString();
            }
            s += "\n";
        }
        s += "\n   "; 
        for (int i=0; i<this.tiles.get(0).size(); i++) {
            s += " " + Integer.toString(i);
        }
        s += "\n";
        return s;
    }
}