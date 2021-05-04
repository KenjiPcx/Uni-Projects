package maze;

/**
 * This exception is thrown when there are too many
 * exits to a maze.
 */
public class MultipleExitException extends InvalidMazeException {
    public MultipleExitException(String errorMsg) {
        super(errorMsg);
    }
}
