package maze;

/**
 * This class is the superclass of those exceptions that 
 * can be thrown if there is an error with the maze.
 */
public class InvalidMazeException extends RuntimeException {
    public InvalidMazeException(String errorMsg) {
        super(errorMsg);
    }
}
