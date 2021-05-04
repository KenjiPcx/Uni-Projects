package maze;

/**
 * This exception is thrown when there is
 * no exit to a maze.
 */
public class NoExitException extends InvalidMazeException {
    public NoExitException(String errorMsg) {
        super(errorMsg);
    }
}