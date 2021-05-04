package maze;

/**
 * This exception is thrown when there is
 * no entrance to a maze.
 */
public class NoEntranceException extends InvalidMazeException {
    public NoEntranceException(String errorMsg) {
        super(errorMsg);
    }
}