package maze;

/**
 * This exception is thrown when the size of the maze is 
 * not consistent.
 */
public class RaggedMazeException extends InvalidMazeException {
    public RaggedMazeException(String errorMsg) {
        super(errorMsg);
    }
}
