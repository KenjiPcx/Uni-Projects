package maze;

/**
 * This exception is thrown when there are too many
 * entrances to a maze.
 */
public class MultipleEntranceException extends InvalidMazeException {
    public MultipleEntranceException(String errorMsg) {
        super(errorMsg);
    }
}