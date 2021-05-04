package maze;

import java.io.Serializable;

/**
 * Contains the details of a tile
 */
public class Tile implements Serializable {
    private Tile.Type type;

    /**
     * Inner class of Tile to enumerate the type of a tile.
     */
    public enum Type {
        CORRIDOR,
        ENTRANCE,
        EXIT,
        WALL,
    }

    /**
     * Initializes an instance of a tile and sets its type.
     * @param t: Type
     */
    private Tile(Tile.Type t) {
        this.type = t;
    }

    /**
     * Creates a tile from a character.
     * @param c: Character
     * @return Returns an instance of a tile of the corresponding type given, 
       returns null if character is invalid
     */
    protected static Tile fromChar(char c) throws InvalidMazeException {
        switch (c) {
            case '.':
                return new Tile(Tile.Type.CORRIDOR);
            case 'e':
                return new Tile(Tile.Type.ENTRANCE);
            case 'x':
                return new Tile(Tile.Type.EXIT);
            case '#':
                return new Tile(Tile.Type.WALL);
            default:
                throw new InvalidMazeException("Invalid Character");
        }
    }

    /**
     * Gets the type of a tile.
     * @return Returns the type of the tile
     */
    public Tile.Type getType() {
        return this.type;
    }

    /**
     * Checks if the tile is navigable.
     * @return Returns true if tile is navigable, false otherwise
     */
    public boolean isNavigable() {
        if (this.type == Tile.Type.WALL) {
            return false;
        }
        return true;
    }

    /**
     * Returns the string representation of the tile.
     * @return Returns the string representation of the tile
     */
    public String toString() {
        if (this.type == Tile.Type.CORRIDOR) {
            return ".";
        } else if (this.type == Tile.Type.ENTRANCE) {
            return "e";
        } else if (this.type == Tile.Type.EXIT) {
            return "x";
        } else {
            return "#";
        }
    }
}
